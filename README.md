# Yashasvi Singh Rathore

Backend engineer. I work mostly in Go — REST and WebSocket services on PostgreSQL and Redis, and systems where state has to stay correct under concurrency.

Prayagraj, India · [Portfolio](https://yashasvidev.netlify.app/) · [LinkedIn](https://www.linkedin.com/in/yashasvi-rathore-412861190/)

---

### Backend work

| Project | What it does | Stack |
| --- | --- | --- |
| [GameVault](https://github.com/yashasvi16/gamevault) | Competitive gaming stats API. JWT (JSON Web Token) auth, transactional match recording, Redis cache-aside leaderboards pushed live over WebSocket, and graceful degradation when the cache is down. One-command Docker setup. | Go, PostgreSQL, Redis, Docker |
| [Jetstrike Arena — Server](https://github.com/yashasvi16/Jetstrike-Arena-Golang) | Authoritative game server for a 2D multiplayer shooter: matchmaking, room state, and authoritative client sync. <!-- TODO: name the transport once you confirm it — "…client sync over WebSocket" reads much stronger than "authoritative client sync". --> | Go |

**Building now** — `mini-sidekiq`, a Redis-backed background job queue in Go: enqueue, worker pool, retries with exponential backoff, dead-letter handling.
<!-- TODO: rewrite the line above to match what you actually shipped, then move it into the table with a link. -->

### Also

Real-time multiplayer clients in Unity — [Jetstrike Arena](https://github.com/yashasvi16/Jetstrike-Arena) on Photon Fusion 2, [Egg Bounce](https://github.com/yashasvi16/Egg-Bounce-Multiplayer) on Netcode for GameObjects.

Computer vision in Python — [crowd density estimation](https://github.com/yashasvi16/Crowd-Density-Estimation-and-Crowd-Behavior-Analysis) using M-CNN (multi-column convolutional neural network) and C3D (3D convolutional network), and [abandoned object detection](https://github.com/yashasvi16/Real-Time-Surveillance-abandoned-object-detection-) with OpenCV.

Competitive programming in C++ on [Codeforces](https://codeforces.com/profile/yashasvi_xvi) — Specialist, max rating 1408.

### Stack

- **Languages** — Go · C++ · C# · Python
- **Data** — PostgreSQL · Redis
- **Infra** — Docker · Docker Compose
<!-- TODO: add "GitHub Actions" to Infra once GameVault has a CI workflow. -->

---

### 🎮 Stay a minute and play

GitHub strips JavaScript out of READMEs, so these are built from plain `<details>` toggles. No install, no tab switch — just click.

<details>
<summary><b>🔔 The 3 A.M. Page</b> — a 60-second incident, one wrong turn ends it</summary>

<br>

Your phone buzzes. The API is throwing 500s. Latency graph looks like a cliff face. Pick one:

<details>
<summary>👉 Roll back the deploy that went out at midnight</summary>

<br>

Errors stop. You start typing "resolved" into the channel — and 20 minutes later the pager goes off again. The deploy wasn't it.

<details>
<summary>👉 Fine. Actually read the logs this time</summary>

<br>

`dial tcp 10.0.1.7:6379: connection refused`, roughly nine thousand times. Redis is gone and every request is falling straight through to Postgres.

<details>
<summary>👉 Flip on graceful degradation and serve stale leaderboards</summary>

<br>

**🏆 YOU WIN.** Postgres stops drowning, p99 drops back under 200 ms, and you bring Redis up warm at a civilized hour. You wrote that fallback path six months ago and nobody noticed. That's the job.

</details>

<details>
<summary>👉 Restart Redis right now, cold</summary>

<br>

**💀 GAME OVER.** Empty cache, every client retries at once, thundering herd, Postgres tips over for real. Now you have two outages. Scroll up, take the other door.

</details>

</details>

</details>

<details>
<summary>👉 Restart all the app servers, it usually works</summary>

<br>

It works! For ninety glorious seconds. Then it doesn't.

**💀 GAME OVER** — you rebooted the symptom. Scroll up and read the logs instead.

</details>

</details>

<br>

<details>
<summary><b>🧠 Guess the Output</b> — three Go snippets, no compiler allowed</summary>

<br>

**1.**

```go
var m map[string]int
fmt.Println(m["hello"])
m["hello"] = 1
```

<details>
<summary>Answer</summary>

Prints `0`, then panics: `assignment to entry in nil map`. Reading a nil map is fine and hands back the zero value. Writing to one is not.

</details>

**2.**

```go
a := []int{1, 2, 3}
b := a[:2]
b = append(b, 99)
fmt.Println(a)
```

<details>
<summary>Answer</summary>

`[1 2 99]`. `b` has length 2 but capacity 3, so `append` reuses the backing array and quietly overwrites `a[2]`. This one has eaten real production data.

</details>

**3.**

```go
func f() (result int) {
    defer func() { result *= 2 }()
    return 5
}
```

<details>
<summary>Answer</summary>

`10`. `return 5` assigns to the named return value first, *then* runs the deferred function, which gets to edit it on the way out.

</details>

</details>
