# ASTRA Deployment Architecture

## 1. Multi-Container Orchestration
ASTRA utilizes containerized modular architecture managed via Docker Compose.

```
┌────────────────────────────────────────────────────────────────────────┐
│                        Docker Compose Network                          │
│                                                                        │
│  ┌───────────────┐     ┌───────────────┐     ┌──────────────────────┐  │
│  │   frontend    │     │    backend    │     │       postgres       │  │
│  │ (Vite / React)│────>│   (FastAPI)   │────>│   (Database 5432)    │  │
│  └───────────────┘     └───────┬───────┘     └──────────────────────┘  │
│                                │                                       │
│                                ▼                                       │
│                        ┌───────────────┐                               │
│                        │     astra     │                               │
│                        │ (ROS 2 Core)  │                               │
│                        └───────────────┘                               │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Service Separation
- **`astra` Container**: Contains ROS 2 Humble, OpenCV, PyTorch CPU wheels, colcon workspace, and core autonomy node processing.
- **`postgres` Container**: Runs PostgreSQL 15 for mission history and telemetry storage.
- **`backend` Container**: FastAPI service providing REST endpoints and WebSocket channels.
- **`frontend` Container**: Serves React dashboard UI for mission control.
- **Simulation / Hardware Host**: Gazebo simulation or physical rover GPU acceleration is bound per host environment.
