#!/usr/bin/env python3
"""
Renders public GitHub activity as a backend service dashboard (SVG).

No third-party services, no pip installs — stdlib only.
Run by .github/workflows/dashboard.yml; writes assets/activity.svg.

Local preview:  python scripts/dashboard.py --demo
"""

import json
import os
import sys
import urllib.request
import urllib.error
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone

USER = os.environ.get("GH_USER", "yashasvi16")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
OUT = os.environ.get("OUT_PATH", "assets/activity.svg")
DAYS = 30

BG = "#0d1117"
PANEL = "#11161d"
BORDER = "#21262d"
ACCENT = "#00ADD8"
ACCENT_DIM = "#0d5c73"
TEXT = "#c9d1d9"
MUTED = "#6e7681"

LEVEL_COLORS = {
    "push": "#00ADD8",
    "pr": "#a371f7",
    "star": "#e3b341",
    "create": "#3fb950",
    "issue": "#db6d28",
    "fork": "#8b949e",
}

EVENT_LABELS = {
    "PushEvent": "push",
    "PullRequestEvent": "pr",
    "WatchEvent": "star",
    "CreateEvent": "create",
    "IssuesEvent": "issue",
    "IssueCommentEvent": "issue",
    "ForkEvent": "fork",
    "ReleaseEvent": "create",
    "PullRequestReviewEvent": "pr",
}


def esc(s):
    return (
        str(s)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def fetch_events():
    events = []
    for page in range(1, 4):  # 300 events max, ~90 days of public history
        url = f"https://api.github.com/users/{USER}/events/public?per_page=100&page={page}"
        req = urllib.request.Request(url, headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": f"{USER}-dashboard",
            **({"Authorization": f"Bearer {TOKEN}"} if TOKEN else {}),
        })
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                batch = json.load(r)
        except urllib.error.HTTPError as e:
            print(f"warning: page {page} failed with {e.code}", file=sys.stderr)
            break
        if not isinstance(batch, list) or not batch:
            break
        events.extend(batch)
        if len(batch) < 100:
            break
    return events


def demo_events():
    """Deterministic sample data so the layout can be checked offline."""
    import random
    random.seed(7)
    now = datetime.now(timezone.utc)
    repos = ["yashasvi16/gamevault", "yashasvi16/mini-sidekiq",
             "yashasvi16/Jetstrike-Arena-Golang", "yashasvi16/yashasvi16"]
    msgs = ["feat: cache-aside leaderboard with TTL refresh",
            "fix: release the lock before returning on error path",
            "refactor: move match recording into a single tx",
            "perf: drop N+1 on the player stats query",
            "chore: bump go 1.24, tidy modules",
            "feat: dead-letter queue for failed jobs",
            "test: race detector on the room state mutator"]
    out = []
    for d in range(DAYS):
        if random.random() < 0.28:
            continue
        for _ in range(random.randint(1, 2)):
            ts = now - timedelta(days=d, hours=random.randint(0, 20))
            out.append({
                "type": random.choices(
                    ["PushEvent", "PullRequestEvent", "WatchEvent", "CreateEvent"],
                    weights=[80, 8, 6, 6])[0],
                "repo": {"name": random.choice(repos)},
                "created_at": ts.strftime("%Y-%m-%dT%H:%M:%SZ"),
                "payload": {"commits": [{"message": random.choice(msgs)}
                                        for _ in range(random.randint(1, 4))]},
            })
    return sorted(out, key=lambda e: e["created_at"], reverse=True)


def parse(events):
    today = datetime.now(timezone.utc).date()
    start = today - timedelta(days=DAYS - 1)

    per_day = {start + timedelta(days=i): 0 for i in range(DAYS)}
    per_repo = Counter()
    total_commits = 0
    active_days = set()
    log = []

    for e in events:
        try:
            ts = datetime.strptime(e["created_at"], "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=timezone.utc)
        except (KeyError, ValueError):
            continue
        day = ts.date()
        kind = EVENT_LABELS.get(e.get("type", ""), "create")
        repo = e.get("repo", {}).get("name", "").split("/")[-1]
        commits = e.get("payload", {}).get("commits") or []
        n = len(commits) if kind == "push" else 0

        if day >= start:
            per_day[day] = per_day.get(day, 0) + max(n, 1 if kind != "push" else 0)
            if n or kind != "push":
                active_days.add(day)
            if kind == "push":
                per_repo[repo] += n or 1
        if n:
            total_commits += n

        if len(log) < 5:
            msg = commits[-1]["message"].split("\n")[0] if commits else kind
            log.append({
                "time": ts.strftime("%m-%d %H:%M"),
                "kind": kind,
                "repo": repo or "—",
                "n": n,
                "msg": msg[:58],
            })

    # longest run of consecutive active days inside the window
    streak = best = 0
    for i in range(DAYS):
        if per_day.get(start + timedelta(days=i), 0) > 0:
            streak += 1
            best = max(best, streak)
        else:
            streak = 0

    return {
        "days": [per_day[start + timedelta(days=i)] for i in range(DAYS)],
        "labels": [(start + timedelta(days=i)) for i in range(DAYS)],
        "repos": per_repo.most_common(4),
        "repo_total": len(per_repo),
        "commits": total_commits,
        "active": len(active_days),
        "streak": best,
        "log": log,
    }


def build_svg(d):
    W, H = 1200, 452
    p = []
    add = p.append

    add(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" '
        f'height="{H}" role="img" aria-label="GitHub activity dashboard for {esc(USER)}: '
        f'{d["commits"]} commits, {d["active"]} active days in the last {DAYS} days">')

    add('<defs>')
    add(f'<linearGradient id="bar" x1="0" y1="0" x2="0" y2="1">'
        f'<stop offset="0%" stop-color="#7CE3FF"/><stop offset="100%" stop-color="{ACCENT_DIM}"/>'
        f'</linearGradient>')
    add('</defs>')

    add('<style>'
        '.m{font-family:"SFMono-Regular","Fira Code",Consolas,monospace}'
        '.s{font-family:"Segoe UI",Helvetica,Arial,sans-serif}'
        '.led{animation:led 2.4s ease-in-out infinite}'
        '@keyframes led{0%,100%{opacity:.45}50%{opacity:1}}'
        '</style>')

    add(f'<rect width="{W}" height="{H}" rx="14" fill="{BG}" stroke="{BORDER}"/>')

    # ── header ──────────────────────────────────────────────────────────
    add(f'<rect x="1" y="1" width="{W-2}" height="52" rx="13" fill="{PANEL}"/>')
    add(f'<rect x="1" y="38" width="{W-2}" height="15" fill="{PANEL}"/>')
    add(f'<line x1="0" y1="53" x2="{W}" y2="53" stroke="{BORDER}"/>')
    add(f'<circle class="led" cx="30" cy="27" r="5" fill="#3fb950"/>')
    add(f'<text class="m" x="46" y="32" font-size="14" fill="{TEXT}">'
        f'{esc(USER)}<tspan fill="{MUTED}"> / activity</tspan></text>')
    add(f'<text class="m" x="{W-24}" y="32" font-size="12" fill="{MUTED}" '
        f'text-anchor="end">window: last {DAYS}d &#183; refreshed daily</text>')

    # ── metric tiles ────────────────────────────────────────────────────
    tiles = [
        ("COMMITS", str(d["commits"]), "pushed, 90d public"),
        ("ACTIVE DAYS", f'{d["active"]}/{DAYS}', "days with a push"),
        ("BEST STREAK", f'{d["streak"]}d', "consecutive"),
        ("REPOS TOUCHED", str(d["repo_total"]), "in this window"),
    ]
    tw, gap, x0, ty = 279, 12, 24, 70
    for i, (label, value, sub) in enumerate(tiles):
        x = x0 + i * (tw + gap)
        add(f'<rect x="{x}" y="{ty}" width="{tw}" height="76" rx="10" fill="{PANEL}" stroke="{BORDER}"/>')
        add(f'<rect x="{x}" y="{ty}" width="3" height="76" rx="1.5" fill="{ACCENT}"/>')
        add(f'<text class="m" x="{x+18}" y="{ty+24}" font-size="10.5" fill="{MUTED}" '
            f'letter-spacing="1.1">{label}</text>')
        add(f'<text class="s" x="{x+18}" y="{ty+54}" font-size="26" font-weight="700" '
            f'fill="{ACCENT}">{esc(value)}</text>')
        add(f'<text class="m" x="{x+18}" y="{ty+68}" font-size="10" fill="{MUTED}">{esc(sub)}</text>')

    # ── throughput chart ────────────────────────────────────────────────
    cx, cy, cw, ch = 24, 162, 740, 130
    add(f'<rect x="{cx}" y="{cy}" width="{cw}" height="{ch}" rx="10" fill="{PANEL}" stroke="{BORDER}"/>')
    add(f'<text class="m" x="{cx+18}" y="{cy+22}" font-size="10.5" fill="{MUTED}" '
        f'letter-spacing="1.1">COMMIT THROUGHPUT</text>')

    peak = max(d["days"]) or 1
    add(f'<text class="m" x="{cx+cw-18}" y="{cy+22}" font-size="10.5" fill="{MUTED}" '
        f'text-anchor="end">peak {peak}/day</text>')

    base = cy + ch - 26
    span = cw - 44
    step = span / DAYS
    bw = max(6, step - 6)
    for i, v in enumerate(d["days"]):
        bx = cx + 22 + i * step
        bh = max(2, (v / peak) * 66)
        fill = "url(#bar)" if v else BORDER
        add(f'<rect x="{bx:.1f}" y="{base-bh:.1f}" width="{bw:.1f}" height="{bh:.1f}" rx="2" fill="{fill}">'
            f'<animate attributeName="height" from="0" to="{bh:.1f}" dur="0.7s" '
            f'begin="{i*0.022:.2f}s" fill="freeze"/>'
            f'<animate attributeName="y" from="{base}" to="{base-bh:.1f}" dur="0.7s" '
            f'begin="{i*0.022:.2f}s" fill="freeze"/></rect>')

    add(f'<line x1="{cx+20}" y1="{base+4}" x2="{cx+cw-20}" y2="{base+4}" stroke="{BORDER}"/>')
    add(f'<text class="m" x="{cx+22}" y="{base+18}" font-size="9.5" fill="{MUTED}">'
        f'{d["labels"][0].strftime("%b %d")}</text>')
    add(f'<text class="m" x="{cx+cw-22}" y="{base+18}" font-size="9.5" fill="{MUTED}" '
        f'text-anchor="end">today</text>')

    # ── top repos ───────────────────────────────────────────────────────
    rx_, ry, rw, rh = 776, 162, 400, 130
    add(f'<rect x="{rx_}" y="{ry}" width="{rw}" height="{rh}" rx="10" fill="{PANEL}" stroke="{BORDER}"/>')
    add(f'<text class="m" x="{rx_+18}" y="{ry+22}" font-size="10.5" fill="{MUTED}" '
        f'letter-spacing="1.1">TOP SERVICES</text>')

    if d["repos"]:
        top = d["repos"][0][1] or 1
        for i, (name, n) in enumerate(d["repos"]):
            yy = ry + 42 + i * 21
            width = max(4, (n / top) * 168)
            add(f'<text class="m" x="{rx_+18}" y="{yy+4}" font-size="11" fill="{TEXT}">'
                f'{esc(name if len(name) <= 19 else name[:18] + chr(8230))}</text>')
            add(f'<rect x="{rx_+196}" y="{yy-7}" width="168" height="10" rx="5" fill="{BG}"/>')
            add(f'<rect x="{rx_+196}" y="{yy-7}" width="{width:.1f}" height="10" rx="5" fill="{ACCENT}" opacity="0.85">'
                f'<animate attributeName="width" from="0" to="{width:.1f}" dur="0.8s" '
                f'begin="{0.3+i*0.1:.2f}s" fill="freeze"/></rect>')
            add(f'<text class="m" x="{rx_+rw-18}" y="{yy+4}" font-size="10.5" fill="{MUTED}" '
                f'text-anchor="end">{n}</text>')
    else:
        add(f'<text class="m" x="{rx_+18}" y="{ry+62}" font-size="11" fill="{MUTED}">no public pushes in window</text>')

    # ── log tail ────────────────────────────────────────────────────────
    lx, ly, lw, lh = 24, 306, 1152, 130
    add(f'<rect x="{lx}" y="{ly}" width="{lw}" height="{lh}" rx="10" fill="{PANEL}" stroke="{BORDER}"/>')
    add(f'<text class="m" x="{lx+18}" y="{ly+22}" font-size="10.5" fill="{MUTED}" '
        f'letter-spacing="1.1">$ tail -f ~/activity.log</text>')

    if d["log"]:
        for i, row in enumerate(d["log"]):
            yy = ly + 44 + i * 17
            color = LEVEL_COLORS.get(row["kind"], MUTED)
            add('<g>')
            add(f'<text class="m" x="{lx+18}" y="{yy}" font-size="11.5" fill="{MUTED}">{esc(row["time"])}</text>')
            add(f'<text class="m" x="{lx+112}" y="{yy}" font-size="11.5" fill="{color}" '
                f'font-weight="600">{esc(row["kind"].upper())}</text>')
            add(f'<text class="m" x="{lx+172}" y="{yy}" font-size="11.5" fill="{TEXT}">'
                f'repo=<tspan fill="{ACCENT}">{esc(row["repo"][:22])}</tspan></text>')
            add(f'<text class="m" x="{lx+400}" y="{yy}" font-size="11.5" fill="{MUTED}">'
                f'{("commits=" + str(row["n"])) if row["n"] else ""}</text>')
            add(f'<text class="m" x="{lx+500}" y="{yy}" font-size="11.5" fill="{TEXT}" '
                f'opacity="0.75">msg="{esc(row["msg"])}"</text>')
            add('</g>')
    else:
        add(f'<text class="m" x="{lx+18}" y="{ly+62}" font-size="11.5" fill="{MUTED}">waiting for events…</text>')

    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    add(f'<text class="m" x="{W-24}" y="{H-12}" font-size="9.5" fill="{MUTED}" '
        f'text-anchor="end">generated {stamp}</text>')

    add('</svg>')
    return "\n".join(p)


def main():
    events = demo_events() if "--demo" in sys.argv else fetch_events()
    if not events:
        print("no events returned; keeping the existing SVG", file=sys.stderr)
        return 0
    svg = build_svg(parse(events))
    os.makedirs(os.path.dirname(OUT) or ".", exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"wrote {OUT} ({len(svg)} bytes) from {len(events)} events")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
