# Yashasvi Singh Rathore

Backend engineer. I work mostly in Go — REST and WebSocket services on PostgreSQL and Redis, and systems where state has to stay correct under concurrency.

Prayagraj, India · [Portfolio](https://yashasvidev.netlify.app/) · [LinkedIn](https://www.linkedin.com/in/yashasvi-rathore-412861190/)

---

### Backend work

| Project | What it does | Stack |
| --- | --- | --- |
| [GameVault](https://github.com/yashasvi16/gamevault) | Competitive gaming stats API. JWT (JSON Web Token) auth, transactional match recording, Redis cache-aside leaderboards pushed live over WebSocket, and graceful degradation when the cache is down. One-command Docker setup. | Go, PostgreSQL, Redis, Docker |
| [mini-sidekiq](#) | Background job queue: Redis-backed enqueue, worker pool, retries with exponential backoff, and dead-letter handling <!-- CONFIRM — rewrite to match what you actually built. Link once it runs. --> | Go, Redis |
| [Jetstrike Arena — Server](https://github.com/yashasvi16/Jetstrike-Arena-Golang) | Authoritative game server for a 2D multiplayer shooter: matchmaking, room state, and client sync over <!-- WebSockets? UDP? --> | Go |

### Also

Real-time multiplayer clients in Unity — [Jetstrike Arena](https://github.com/yashasvi16/Jetstrike-Arena) on Photon Fusion 2, [Egg Bounce](https://github.com/yashasvi16/Egg-Bounce-Multiplayer) on Netcode for GameObjects. Computer vision in Python: [crowd density estimation](https://github.com/yashasvi16/Crowd-Density-Estimation-and-Crowd-Behavior-Analysis) using M-CNN (multi-column convolutional neural network) and C3D (3D convolutional network), and [abandoned object detection](https://github.com/yashasvi16/Real-Time-Surveillance-abandoned-object-detection-) with OpenCV.

Competitive programming in C++ on [Codeforces](https://codeforces.com/profile/<handle>) — Specialist, max rating 1408.

### Stack

**Languages** Go · C++ · C# · Python
**Data** PostgreSQL · Redis
**Infra** Docker · Docker Compose · <!-- add CI once GameVault has a GitHub Actions workflow -->
