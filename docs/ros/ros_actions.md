# ASTRA ROS 2 Action Reservations

## Reserved ROS 2 Actions (Future Phases)

The following ROS 2 Action interfaces are reserved for high-level mission execution:

### 1. `NavigateToWaypoint`
- **Goal**: Target coordinates `(x, y, theta)` and max velocity limit.
- **Feedback**: Current distance remaining, estimated time remaining, current speed.
- **Result**: Final pose reached status, total time elapsed.

### 2. `SearchForRock`
- **Goal**: Search region bounds and target rock properties (size, color, min confidence).
- **Feedback**: Area coverage percentage, candidates detected count.
- **Result**: Highest confidence detected rock location coordinates.

### 3. `CollectSample`
- **Goal**: Target object ID / coordinates and collection tool profile.
- **Feedback**: Arm/actuator status, load sensor force feedback.
- **Result**: Sample collection success confirmation, storage bay slot ID.

### 4. `ReturnToBase`
- **Goal**: Base station ID and battery conservation mode flag.
- **Feedback**: Progress along return trajectory, battery level remaining.
- **Result**: Docking confirmation status.

### 5. `ExploreRegion`
- **Goal**: Bounding polygon perimeter, search pattern strategy.
- **Feedback**: Grid cells visited percentage, hazard map updates.
- **Result**: Completed hazard map overlay data summary.
