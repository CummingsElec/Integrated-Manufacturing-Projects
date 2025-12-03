<div align="center">

<img src="../../Asthetics/Watcher.png" alt="ORION Banner" width="100%"/>

# ORION

**Operational Recognition Intelligence and Observation Network**

> Multi-camera AI vision platform for safety monitoring, personnel tracking, and workflow analytics

[![Status](https://img.shields.io/badge/Status-Active_Development-blue?style=flat-square)](#)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](#)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)](#)
[![Hailo](https://img.shields.io/badge/Hailo-26_TOPS-FF6F00?style=flat-square)](#)

</div>

---

## Problem Statement

Industrial facilities require intelligent monitoring that goes beyond passive video recording. Operations managers need answers to questions like:

- How many people are in each zone right now?
- Where do bottlenecks occur during shift changes?
- Did the forklift come too close to pedestrians?
- How much time does each task actually take?

**ORION answers these questions in real-time** by combining edge AI processing with centralized analytics, delivering actionable insights without manual video review.

---

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                           ORION Platform                             │
├──────────────────────────────┬──────────────────────────────────────┤
│       Edge Device (Pi)       │         Backend Server               │
├──────────────────────────────┼──────────────────────────────────────┤
│                              │                                      │
│  ┌────────────────────┐      │      ┌────────────────────┐         │
│  │   Hailo AI (26T)   │      │      │   FastAPI Server   │         │
│  │   Real-time YOLO   │◄────────────►   REST + WebSocket  │         │
│  └────────────────────┘      │      └────────────────────┘         │
│           │                  │               │                      │
│  ┌────────────────────┐      │      ┌────────────────────┐         │
│  │   TV Dashboard     │      │      │   PostgreSQL DB    │         │
│  │   HDMI Output      │      │      │   Event Storage    │         │
│  └────────────────────┘      │      └────────────────────┘         │
│           │                  │               │                      │
│  ┌────────────────────┐      │      ┌────────────────────┐         │
│  │   8 IP Cameras     │      │      │   Celery Workers   │         │
│  │   RTSP Streams     │      │      │   Heavy Processing │         │
│  └────────────────────┘      │      └────────────────────┘         │
│                              │                                      │
└──────────────────────────────┴──────────────────────────────────────┘
```

### Hybrid Processing Model

| Device | Role | Handles |
|--------|------|---------|
| **Raspberry Pi 5** | Edge Inference | Real-time detection, TV output, 4 camera streams |
| **Backend Server** | Heavy Compute | Database, analytics, batch processing, remaining cameras |

---

## Tech Stack

| Layer | Technology | Purpose |
|-------|------------|---------|
| **Edge AI** | Hailo-8 (26 TOPS) | Real-time inference acceleration |
| **Detection** | YOLOv8 | Person and vehicle detection |
| **Tracking** | ByteTrack | Cross-camera ID persistence |
| **API** | FastAPI | REST endpoints with async support |
| **Database** | PostgreSQL | Event and metrics storage |
| **Queue** | Redis + Celery | Background task processing |
| **Container** | Docker | Reproducible deployments |
| **Edge OS** | Raspberry Pi OS 64-bit | Optimized Linux for Pi 5 |

---

## Core Features

### 🛡️ Safety & Hazard Awareness
- **Real-time person and vehicle detection** across all cameras
- **Near-miss alerting** when pedestrians and vehicles converge
- **Zone-based monitoring** with configurable detection areas
- **Instant notifications** via webhooks or dashboard alerts

### 📊 Workflow & Congestion Analytics
- **Personnel movement tracking** with persistent IDs
- **Zone occupancy counts** updated in real-time
- **Bottleneck identification** through dwell time analysis
- **Heat map generation** for traffic pattern visualization

### ⏱️ Time & Labor Metrics
- **Automated labor hour estimation** based on zone presence
- **Task duration tracking** from zone entry to exit
- **Shift analytics** for workforce planning
- **Historical reporting** with CSV/JSON export

### 📺 Real-Time Dashboard
- **8-camera grid layout** rendered on TV via HDMI
- **Live detection overlays** with bounding boxes and IDs
- **Status indicators** for camera health and system state
- **Management web UI** for configuration and metrics

### 🔗 Cross-Camera Tracking
- **Persistent ID assignment** maintained across camera handoffs
- **Re-identification logic** reconnects tracks after gaps
- **Track history storage** for trajectory analysis
- **Multi-zone journey reconstruction**

---

## Performance Targets

| Metric | Target | Notes |
|--------|--------|-------|
| **Inference Latency** | <100ms | Per camera on Hailo |
| **Tracking FPS** | 10-15 | Per camera stream |
| **Database Writes** | 100+ events/sec | Bulk inserts |
| **TV Dashboard** | 8-10 FPS | 8-camera grid |
| **API Response** | <200ms | 95th percentile |
| **Memory (Pi)** | <12GB | With 4GB headroom |

---

## Project Structure

```
orion/
├── backend/                 # FastAPI server (Windows/Linux)
│   ├── api/                # REST endpoints
│   ├── services/           # Business logic
│   ├── models/             # Database ORM
│   ├── workers/            # Celery tasks
│   └── migrations/         # Alembic schemas
├── edge/                   # Raspberry Pi components
│   ├── inference/          # Hailo detection
│   ├── display/            # TV dashboard
│   └── api/                # Edge REST server
├── frontend/               # Web management UI (optional)
├── configs/                # YAML configurations
├── scripts/                # Deployment utilities
└── docs/                   # Technical documentation
```

---

## Current Status

**🔄 Active Development**

- ✅ Project structure and Docker environment
- ✅ PostgreSQL database schema with multi-camera support
- ✅ Camera service with RTSP stream management
- ✅ YOLOv8 detection integration
- 🔄 Raspberry Pi + Hailo deployment in progress
- 🔄 Cross-camera tracking implementation
- 📋 TV dashboard layout planned
- 📋 Web management UI planned

---

## My Contributions

As the sole developer, I am responsible for:

- **System design** — Hybrid edge/cloud architecture, device selection, data flow
- **Backend development** — FastAPI, PostgreSQL, Celery workers
- **Edge deployment** — Raspberry Pi setup, Hailo integration, dashboard rendering
- **ML pipeline** — Model conversion for Hailo, tracking optimization
- **DevOps** — Docker containerization, deployment scripts
- **Documentation** — Architecture docs, API reference, troubleshooting guides

---

## Business Value

| Objective | Capability |
|-----------|------------|
| **Safety monitoring** | Real-time detection and near-miss alerting |
| **Workflow visibility** | Zone occupancy, bottleneck identification |
| **Labor analytics** | Automated time tracking, shift metrics |
| **Compliance documentation** | Event logs with timestamps and evidence |
| **Operational insights** | Heat maps, traffic patterns, utilization data |

---

## Success Metrics

| Category | Target |
|----------|--------|
| **Uptime** | 24/7 unattended operation |
| **Detection accuracy** | 99%+ for person/vehicle classes |
| **Cross-camera tracking** | 90%+ ID consistency |
| **Frame drops** | <5% across all streams |

---

<div align="center">

**Edge AI • Cross-Camera Tracking • Workflow Analytics**

</div>

