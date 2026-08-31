<img src="./assets/header.svg" alt="Yashasvi Singh Rathore — Backend Engineer · Go · PostgreSQL · Redis" width="100%" />

<div align="center">

<a href="https://yashasvidev.netlify.app/"><img src="https://img.shields.io/badge/Portfolio-0A0A0A?style=for-the-badge&logo=netlify&logoColor=00C7B7" alt="Portfolio" /></a>
<a href="https://www.linkedin.com/in/yashasvi-rathore-412861190/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
<a href="https://codeforces.com/profile/yashasvi_xvi"><img src="https://img.shields.io/badge/Codeforces-Specialist%201408-1F8ACB?style=for-the-badge&logo=codeforces&logoColor=white" alt="Codeforces — Specialist, max rating 1408" /></a>
<a href="https://github.com/yashasvi16"><img src="https://img.shields.io/github/followers/yashasvi16?style=for-the-badge&logo=github&label=Follow&labelColor=0A0A0A&color=00ADD8" alt="GitHub followers" /></a>

</div>

---

## 🧭 About

<table>
<tr>
<td width="56%" valign="top">

```go
package main

type Engineer struct {
    Name  string
    Stack []string
    Likes string
}

func (e Engineer) Ship(ctx context.Context) error {
    // the interesting part is never the handler.
    // it's what happens when two of them run at once.
    return e.KeepStateCorrect(ctx)
}

var me = Engineer{
    Name:  "Yashasvi Singh Rathore",
    Stack: []string{"Go", "PostgreSQL", "Redis", "Docker"},
    Likes: "concurrency, caches, and things that fail loudly",
}
```

</td>
<td width="44%" valign="top">

<table>
<tr><td>⚡</td><td><b>Focus</b></td><td>Concurrency · caching · real-time</td></tr>
<tr><td>🔨</td><td><b>Daily</b></td><td>Go · PostgreSQL · Redis · Docker</td></tr>
<tr><td>🚧</td><td><b>Building</b></td><td><code>mini-sidekiq</code>, a job queue</td></tr>
<tr><td>🎮</td><td><b>Came from</b></td><td>Unity multiplayer game dev</td></tr>
<tr><td>🏅</td><td><b>Codeforces</b></td><td>Specialist · max 1408</td></tr>
<tr><td>📍</td><td><b>Based in</b></td><td>Prayagraj, India</td></tr>
</table>

<div align="center">
<img src="https://img.shields.io/badge/open%20to-backend%20roles-00ADD8?style=flat-square&labelColor=0d1117" alt="Open to backend roles" />
</div>

</td>
</tr>
</table>

---

## 🚀 Backend work

<table>
<tr>
<td width="50%" valign="top">

### [GameVault](https://github.com/yashasvi16/gamevault)

<a href="https://github.com/yashasvi16/gamevault/stargazers"><img src="https://img.shields.io/github/stars/yashasvi16/gamevault?style=flat-square&logo=github&labelColor=0d1117&color=00ADD8" alt="Stars" /></a>
<img src="https://img.shields.io/github/last-commit/yashasvi16/gamevault?style=flat-square&labelColor=0d1117&color=8b949e" alt="Last commit" />
<img src="https://img.shields.io/github/languages/top/yashasvi16/gamevault?style=flat-square&labelColor=0d1117&color=00ADD8" alt="Top language" />

Competitive gaming stats API. JWT (JSON Web Token) auth, transactional match recording, Redis cache-aside leaderboards pushed live over WebSocket, and graceful degradation when the cache is down. One-command Docker setup.

<img src="https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white" alt="Go" />
<img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL" />
<img src="https://img.shields.io/badge/Redis-FF4438?style=flat-square&logo=redis&logoColor=white" alt="Redis" />
<img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker" />

</td>
<td width="50%" valign="top">

### [Jetstrike Arena — Server](https://github.com/yashasvi16/Jetstrike-Arena-Golang)

<a href="https://github.com/yashasvi16/Jetstrike-Arena-Golang/stargazers"><img src="https://img.shields.io/github/stars/yashasvi16/Jetstrike-Arena-Golang?style=flat-square&logo=github&labelColor=0d1117&color=00ADD8" alt="Stars" /></a>
<img src="https://img.shields.io/github/last-commit/yashasvi16/Jetstrike-Arena-Golang?style=flat-square&labelColor=0d1117&color=8b949e" alt="Last commit" />
<img src="https://img.shields.io/github/languages/top/yashasvi16/Jetstrike-Arena-Golang?style=flat-square&labelColor=0d1117&color=00ADD8" alt="Top language" />

Authoritative game server for a 2D multiplayer shooter: matchmaking, room state, and authoritative client sync. <!-- TODO: name the transport once you confirm it, and fix the badge below if it isn't WebSocket. -->

<img src="https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white" alt="Go" />
<img src="https://img.shields.io/badge/WebSocket-010101?style=flat-square&logo=socketdotio&logoColor=white" alt="WebSocket" />

</td>
</tr>
</table>

> **🚧 Building now — `mini-sidekiq`** &nbsp;·&nbsp; a Redis-backed background job queue in Go: enqueue, worker pool, retries with exponential backoff, dead-letter handling.
> <!-- TODO: rewrite to match what you actually shipped, then promote it into the grid above. -->

---

## 🎮 Also built

<table>
<tr>
<td width="55%" valign="top">

**Real-time multiplayer, Unity**

- [Jetstrike Arena](https://github.com/yashasvi16/Jetstrike-Arena) — 2D shooter client on Photon Fusion 2
- [Egg Bounce](https://github.com/yashasvi16/Egg-Bounce-Multiplayer) — multiplayer party game on Netcode for GameObjects

<img src="https://img.shields.io/badge/Unity-000000?style=flat-square&logo=unity&logoColor=white" alt="Unity" />
<img src="https://img.shields.io/badge/C%23-512BD4?style=flat-square&logo=csharp&logoColor=white" alt="C#" />

</td>
<td width="45%" valign="top">

**Computer vision, Python**

- [Crowd density estimation](https://github.com/yashasvi16/Crowd-Density-Estimation-and-Crowd-Behavior-Analysis) — M-CNN (multi-column convolutional neural network) and C3D (3D convolutional network)
- [Abandoned object detection](https://github.com/yashasvi16/Real-Time-Surveillance-abandoned-object-detection-) — real-time surveillance with OpenCV

<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white" alt="OpenCV" />

</td>
</tr>
</table>

---

## 🧰 Stack

<table>
<tr>
<td align="right"><b>Languages</b></td>
<td>
<img src="https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white" alt="Go" />
<img src="https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++" />
<img src="https://img.shields.io/badge/C%23-512BD4?style=for-the-badge&logo=csharp&logoColor=white" alt="C#" />
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
</td>
</tr>
<tr>
<td align="right"><b>Data</b></td>
<td>
<img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" />
<img src="https://img.shields.io/badge/Redis-FF4438?style=for-the-badge&logo=redis&logoColor=white" alt="Redis" />
</td>
</tr>
<tr>
<td align="right"><b>Infra &amp; tools</b></td>
<td>
<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" />
<img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git" />
<img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" alt="Linux" />
</td>
</tr>
<tr>
<td align="right"><b>Game dev</b></td>
<td>
<img src="https://img.shields.io/badge/Unity-000000?style=for-the-badge&logo=unity&logoColor=white" alt="Unity" />
<img src="https://img.shields.io/badge/Photon%20Fusion%202-1B1B1B?style=for-the-badge&logoColor=white" alt="Photon Fusion 2" />
</td>
</tr>
</table>

<!-- TODO: add a GitHub Actions badge to the Infra row once GameVault has a CI (continuous integration) workflow. -->

---

## 🐍 Contribution snake

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/yashasvi16/yashasvi16/output/snake-dark.svg" />
  <img src="https://raw.githubusercontent.com/yashasvi16/yashasvi16/output/snake.svg" alt="Snake eating my contribution graph" width="98%" />
</picture>

</div>

<!-- 404s until .github/workflows/snake.yml runs once. Push it, then trigger it from the Actions tab. -->

<!-- ─────────────────────────────────────────────────────────────
     OPTIONAL: stats cards from community services on Vercel.
     Uncomment only if these load for you in a browser first.
     They were removed because they were rendering as broken images.

<div align="center">
<img src="https://github-readme-stats.vercel.app/api?username=yashasvi16&show_icons=true&hide_border=true&include_all_commits=true&count_private=true&theme=transparent&title_color=00ADD8&icon_color=00ADD8&text_color=8b949e" alt="GitHub stats" height="170" />
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=yashasvi16&layout=compact&hide_border=true&langs_count=6&hide=shaderlab,hlsl,jupyter%20notebook,html,css&theme=transparent&title_color=00ADD8&text_color=8b949e" alt="Most used languages" height="170" />
</div>
     ───────────────────────────────────────────────────────────── -->

---

<div align="center">

### 💬 Reach me

<a href="https://www.linkedin.com/in/yashasvi-rathore-412861190/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
<a href="https://yashasvidev.netlify.app/"><img src="https://img.shields.io/badge/Portfolio-0A0A0A?style=for-the-badge&logo=netlify&logoColor=00C7B7" alt="Portfolio" /></a>
<!-- TODO: add a mail badge once you pick a public address:
<a href="mailto:you@example.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" /></a> -->

<br><br>

<sub><i>Thanks for scrolling all the way down.</i></sub>

</div>
