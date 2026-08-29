# ASTRA System Architecture

## 1. Project Objective
**ASTRA (Autonomous Space Terrain & Reconnaissance Agent)** is an end-to-end, AI-powered autonomous space rover software platform. Designed for extraterrestrial exploration (Lunar and Martian analog missions), ASTRA integrates real-time robotic control (ROS 2), deep learning vision models, LLM-based intelligent mission planning, natural voice interface, telemetry web API, and real-time frontend visualization.

---

## 2. Final Feature Set
- **Autonomous Navigation & Hazard Avoidance**: Real-time camera & sensor processing with obstacle detection, path planning, and reactive safety stops.
- **Computer Vision & Classification**: Real-time rock, crater, and terrain feature detection with fallback logic (`UNKNOWN` classification when below confidence thresholds).
- **LLM Mission Intelligence**: High-level natural language prompt processing into validated structured mission execution plans.
- **Safety Supervision**: Deterministic safety controller acting as an emergency interlock between high-level AI directives and motor execution.
- **Full-Stack Operations & Telemetry**: FastAPI backend REST/WebSocket interface backed by PostgreSQL and React monitoring dashboard.
- **Voice Operations**: Speech-to-Text (STT) and voice intent parsing for hands-free rover commanding.

---

## 3. System Architecture Overview
The ASTRA platform operates across decoupled operational layers:
```
[ User / Voice / Dashboard ]
           │
           ▼
[ FastAPI Backend + Postgres ]
           │
           ▼
[ Agent (LLM + Mission Schema) ]
           │ (Structured Plan Validation)
           ▼
[ Safety Controller Interlock ]
           │ (Approved ROS 2 Actions/Topics)
           ▼
[ ROS 2 Autonomous Core ]
┌───────────────────────────────┐
│ camera_publisher -> /image_raw │
│ perception_node  -> /class    │
│ navigation_node  -> /cmd_vel  │
└───────────────────────────────┘
```

---

## 4. ROS 2 Architecture (Built Baseline)
ASTRA's robotic baseline is built on **ROS 2 Humble**.
- **Active Packages**:
  - `astra_interfaces`: Custom ROS messages (`Classification.msg`, `RoverState.msg`, etc.)
  - `astra_sensors`: Simulates camera output (`camera_publisher` publishing `/astra/camera/image_raw`).
  - `astra_perception`: OpenCV & vision inference (`perception_node` classifying `ROCK`, `CRATER`, `UNKNOWN`).
  - `astra_navigation`: Reactive controller (`navigation_node` responding to classifications).
  - `astra_bringup`: Launch orchestration (`astra_demo.launch.py`).
- **Reserved Packages**:
  - `astra_simulation`, `astra_classification`, `astra_mission`.

---

## 5. AI, ML & CV Architecture
- **Perception Pipeline**: Ingests `/astra/camera/image_raw`, performs image processing & object detection (YOLO/PyTorch), outputs bounding boxes, hazard scores, and classifications.
- **Confidence Interlock**: Any classification below confidence threshold defaults to `UNKNOWN` to avoid hallucinated navigation decisions.
- **Agent Intelligence**: Translates high-level mission goals into deterministic JSON mission plans.

---

## 6. Navigation & Safety Architecture
- **Navigation Node**: Listens to perception output and translates terrain state into velocity commands (`/cmd_vel`).
- **Safety Interlock**: Evaluates maximum allowed linear/angular velocity, slope limits, minimum obstacle clearance, battery threshold, e-stop flag, and mission timeout before sending motor commands.

---

## 7. Backend, Database & Frontend Architecture
- **Backend**: FastAPI app serving JSON APIs (`/`, `/health`) and WebSocket telemetry stream.
- **Database**: PostgreSQL (`astra_db`) storing rover telemetry logs, mission histories, and user audit trails.
- **Frontend**: Vite + React + TypeScript web application presenting real-time rover state and camera feeds.

---

## 8. Deployment Architecture
- **Containerization**: Microservice container layout using Docker Compose:
  - `astra` container (ROS 2 Humble, PyTorch, OpenCV, colcon build env)
  - `postgres` container (PostgreSQL 15 database)
  - `backend` container (FastAPI server)
  - `frontend` container (React production build or dev web server)

---

## 9. Evaluation & Verification Architecture
- Unit testing (`pytest` for Python components)
- Integration testing (`ros2 launch` smoke tests)
- Telemetry evaluation benchmarks for perception accuracy, mission completion rates, and safety boundary compliance.
