#!/usr/bin/env bash
# ASTRA Service Startup Script (Phase 1 Skeleton)
# Standardized startup sequence for ASTRA ecosystem services.

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

echo "======================================================="
echo " ASTRA Autonomous Space Terrain & Reconnaissance Agent "
echo "======================================================="
echo "Phase 1 Service Orchestration Initialization..."
echo ""

echo "[1/6] Database Service (PostgreSQL)..."
echo "      Command: docker compose -f docker/docker-compose.yml up -d postgres"

echo "[2/6] Backend API Service (FastAPI)..."
echo "      Command: uvicorn app.main:app --host 0.0.0.0 --port 8000 (Cwd: backend/)"

echo "[3/6] Frontend Dashboard (React/Vite)..."
echo "      Command: npm run dev (Cwd: frontend/)"

echo "[4/6] ROS 2 Core Autonomy Node Stack..."
echo "      Command: ros2 launch astra_bringup astra_demo.launch.py"

echo "[5/6] Gazebo Simulation Environment..."
echo "      Command: ros2 launch astra_simulation simulation.launch.py (Phase 2)"

echo "[6/6] LLM & Voice Agent Services..."
echo "      Command: python3 -m agent.services.mission_agent (Phase 2)"

echo ""
echo "[ASTRA Phase 1] Environment and skeletons are ready."
