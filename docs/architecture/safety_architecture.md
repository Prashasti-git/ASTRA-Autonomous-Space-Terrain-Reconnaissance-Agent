# ASTRA Safety Architecture

## 1. Safety Controller Design
The Safety Controller acts as a deterministic barrier between high-level mission planning/AI directives and low-level motor actuation.

---

## 2. Core Safety Parameters
- **Maximum Linear Velocity**: `0.5 m/s` (hard ceiling on drive speed).
- **Maximum Angular Velocity**: `1.0 rad/s` (hard ceiling on turn rate).
- **Maximum Incline / Slope Threshold**: `20.0 degrees` (prevents rollover hazards).
- **Minimum Obstacle Distance Clearance**: `0.5 meters` (triggers immediate stop/reroute).
- **Minimum Battery Threshold**: `15.0%` (forces return to base or safe-hold state).
- **Emergency Stop (E-Stop)**: High-priority hardware/software latch over-riding all active actions.
- **Geofence / Restricted Zones**: Polygon boundaries forbidding entry.
- **Mission Timeout**: Maximum duration per action step before triggering safe-hold mode.

---

## 3. Enforcement Hierarchy
```
Mission Command / Action Step
            │
            ▼
[ Geofence & Range Check ] ──(Fail)──> [ Halt & Alert ]
            │ (Pass)
            ▼
[ Obstacle & Slope Check ] ──(Fail)──> [ Emergency Stop ]
            │ (Pass)
            ▼
[ Battery & Health Check ] ──(Fail)──> [ Return to Base ]
            │ (Pass)
            ▼
  Approved Action Signal
```
