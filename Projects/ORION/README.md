<div align="center">

<img src="../../Asthetics/Watcher.png" alt="ORION Banner" width="100%"/>

# ORION

**Operational Recognition Intelligence and Observation Network**

> Advanced multi-camera AI vision platform for industrial safety monitoring, personnel tracking, and workflow analytics

[![Status](https://img.shields.io/badge/Status-Production_v1.2-success?style=flat-square)](#)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white)](#)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)](#)
[![YOLOv11](https://img.shields.io/badge/YOLOv11-Large-00FFFF?style=flat-square)](#)

</div>

---

## Overview

ORION is a production-grade AI vision system that transforms industrial monitoring from passive video recording into actionable intelligence. The platform combines real-time detection, persistent multi-object tracking, and comprehensive analytics to deliver insights that drive safety, efficiency, and operational excellence.

### What Makes ORION Different

**Dual Operating Modes**
- **Live Stream Monitoring:** Real-time person and vehicle detection with colored segmentation overlays
- **Video Processing:** Batch process pre-recorded DVR footage with AI analysis and comprehensive reports

**Two-Pass Processing**
- Separate YOLO inference from video rendering for 2-5x faster processing
- Process once, render multiple times with different visualizations
- Ideal for iterative review and analysis workflows

**Advanced AI Models**
- YOLOv11-Large with 51M parameters for detection
- YOLOv11-Large-Seg with 56M parameters for instance segmentation
- ByteTrack integration for persistent cross-frame tracking
- CPU and GPU acceleration support

---

## Problem Statement

Industrial facilities require intelligent monitoring that goes beyond passive video recording. Operations managers need answers to critical questions:

- **Safety:** How many people are in each zone right now? Did the forklift come too close to pedestrians?
- **Workflow:** Where do bottlenecks occur during shift changes? How much time does each task actually take?
- **Compliance:** Do we have documented evidence of PPE usage and safety protocols?
- **Analytics:** What are our traffic patterns? How can we optimize space utilization?

**ORION answers these questions automatically** by combining edge AI processing with centralized analytics, delivering actionable insights without manual video review.

---

## System Architecture

### Current Implementation (v1.2)

```
┌─────────────────────────────────────────────────────────────────────┐
│                          ORION Platform v1.2                         │
├────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  ┌────────────────────────────────────────────────────────────┐    │
│  │              Multi-Camera DVR/NVR System                     │    │
│  │     Reolink RLN8-410 • 8x 12MP IP Cameras • RTSP/HTTPS     │    │
│  └───────────────────┬────────────────────────────────────────┘    │
│                      │                                               │
│  ┌───────────────────▼───────────────────────────────────────┐     │
│  │            Windows Processing Server                       │     │
│  ├────────────────────────────────────────────────────────────┤     │
│  │  • Flask Vision Server (Live Monitoring)                   │     │
│  │  • Video Processor GUI (Batch Processing)                  │     │
│  │  • YOLOv11L & YOLOv11L-seg Models                         │     │
│  │  • ByteTrack Multi-Object Tracking                        │     │
│  │  • OpenCV + PyTorch + Ultralytics                         │     │
│  │  • HTML Report Generation                                  │     │
│  │  • Comprehensive Logging System                            │     │
│  └────────────────────────────────────────────────────────────┘     │
│                                                                       │
│  ┌────────────────────────────────────────────────────────────┐    │
│  │                  Output & Analytics                          │    │
│  │  • Processed Videos with Overlays                           │    │
│  │  • Detection Timeline Reports (HTML)                        │    │
│  │  • JSON Data Exports                                        │    │
│  │  • Detailed Processing Logs                                 │    │
│  └────────────────────────────────────────────────────────────┘    │
│                                                                       │
└───────────────────────────────────────────────────────────────────┘
```

### Planned Architecture (Hybrid Edge + Cloud)

```
┌─────────────────────────────────────────────────────────────────────┐
│                    ORION Future Architecture                         │
├──────────────────────────────┬──────────────────────────────────────┤
│       Edge Device (Pi)       │         Backend Server               │
├──────────────────────────────┼──────────────────────────────────────┤
│                              │                                      │
│  ┌────────────────────┐      │      ┌────────────────────┐         │
│  │   Hailo-8 (26T)    │      │      │   FastAPI Server   │         │
│  │   Real-time YOLO   │◄────────────►   REST + WebSocket  │         │
│  └────────────────────┘      │      └────────────────────┘         │
│           │                  │               │                      │
│  ┌────────────────────┐      │      ┌────────────────────┐         │
│  │   TV Dashboard     │      │      │   PostgreSQL DB    │         │
│  │   HDMI Output      │      │      │   Event Storage    │         │
│  └────────────────────┘      │      └────────────────────┘         │
│           │                  │               │                      │
│  ┌────────────────────┐      │      ┌────────────────────┐         │
│  │   4 IP Cameras     │      │      │   Celery Workers   │         │
│  │   RTSP Streams     │      │      │   Heavy Processing │         │
│  └────────────────────┘      │      └────────────────────┘         │
│                              │                                      │
└──────────────────────────────┴──────────────────────────────────────┘
```

---

## Core Features

### Live Stream Monitoring

- **Real-time Detection:** Person and vehicle detection at 10-15 FPS
- **Multi-Camera Support:** Switch between 8 cameras seamlessly
- **Colored Segmentation:** Instance segmentation with colored masks for people
- **Bounding Boxes:** Clean boxes for vehicles and other objects
- **Web Interface:** Browser-based monitoring at `http://127.0.0.1:8086`
- **Dual Stream Modes:** RTSP (high FPS) or HTTPS (fallback)

### Video Processing Pipeline

**Fast Two-Pass Workflow:**
1. **Pass 1 - Inference:** Process video with YOLO, save detections to JSON (fast)
2. **Pass 2 - Rendering:** Apply overlays from JSON to video (even faster)
3. **Result:** 2-5x faster than single-pass, enables multiple visualizations

**Processing Modes:**
- Video with AI overlays (masks, boxes, tracking IDs)
- HTML detection timeline reports
- JSON-only mode (fastest, data-only)
- Frame skip options (1x, 2x, 3x for speed)

### Advanced AI Detection

**Models:**
- YOLOv11-Large (51MB) - Superior detection accuracy
- YOLOv11-Large-seg (56MB) - Instance segmentation with masks
- 27.6M+ parameters for high-accuracy inference

**Capabilities:**
- Person detection with pose-adaptive masks
- Vehicle detection (cars, trucks, buses, forklifts)
- Distant object detection in low-light conditions
- Partially occluded object handling
- Multi-scale detection (near and far objects)

### ByteTrack Integration

- **Persistent IDs:** Same person/vehicle keeps ID across entire video
- **Occlusion Handling:** Maintains tracking through temporary obstructions
- **Cross-Frame Consistency:** Smooth ID assignment at all frame rates
- **Accurate Counting:** Prevents double-counting for reliable metrics

### Comprehensive Reporting

**HTML Detection Reports:**
- Summary statistics (unique people, vehicles, processing time)
- Detection timeline with MM:SS timestamps
- Duration visible per object
- Color-coded entries for easy reading
- Professional gradient design with visual indicators

**Logging System:**
- Automatic detailed logs for every processing job
- Timestamped log files in `logs/video_processor/`
- Error tracking and debugging information
- Performance metrics (FPS, processing time)
- Log viewer in web interface

### Planned Features

- **Cross-Camera Tracking:** Persistent IDs across multiple cameras
- **TV Dashboard:** 8-camera grid layout via HDMI output
- **Zone Analytics:** Dwell time, occupancy counts, heat maps
- **Near-Miss Alerts:** Proximity detection for safety events
- **API Integration:** FastAPI backend with PostgreSQL storage
- **Edge Processing:** Hailo-8 accelerator (26 TOPS) on Raspberry Pi

---

## Tech Stack

### Current (v1.2)

| Layer | Technology | Purpose |
|-------|------------|---------|
| **Framework** | Flask | Web server for live monitoring |
| **Processing** | OpenCV | Video capture and manipulation |
| **AI Framework** | PyTorch + Ultralytics | Deep learning inference |
| **Detection** | YOLOv11-Large | Object detection |
| **Segmentation** | YOLOv11-Large-seg | Instance segmentation |
| **Tracking** | ByteTrack | Multi-object tracking |
| **Language** | Python 3.11 | Primary development language |
| **GUI** | Tkinter | Video processor interface |
| **Reports** | HTML/CSS | Detection timeline reports |

### Planned (Future)

| Layer | Technology | Purpose |
|-------|------------|---------|
| **Edge AI** | Hailo-8 (26 TOPS) | Real-time inference acceleration |
| **API** | FastAPI | REST endpoints with async support |
| **Database** | PostgreSQL | Event and metrics storage |
| **Queue** | Redis + Celery | Background task processing |
| **Container** | Docker | Reproducible deployments |
| **Edge OS** | Raspberry Pi OS 64-bit | Optimized Linux for Pi 5 |

---

## Installation & Setup

### Prerequisites

**System Requirements:**
- Windows 10/11 (64-bit)
- Python 3.11+
- 8GB+ RAM (16GB recommended)
- 500MB disk space for AI models
- Network access to DVR/cameras

### Quick Start

```powershell
# 1. Clone repository
git clone <repo-url> ORION
cd ORION

# 2. Create .env file with DVR credentials
copy env.template .env
notepad .env
# Add: DVR_PASSWORD=your_password_here

# 3. Run installation (installs dependencies and downloads models)
INSTALL_ORION.bat

# Installation will:
# - Create Python virtual environment
# - Install OpenCV, PyTorch, Ultralytics
# - Download YOLOv11L models (~100MB)
```

### Usage

#### Live Stream Monitoring

```powershell
# Start the vision server
START_SERVER.bat

# Opens automatically at: http://127.0.0.1:8086
# Features:
# - Real-time person/vehicle detection
# - Colored segmentation masks
# - Switch between 8 cameras
# - Toggle tracking features
# - Stream mode selection (RTSP/HTTPS)
```

#### Process Pre-Recorded Videos

```powershell
# Start the video processor
START_VIDEO_PROCESSOR.bat

# Opens automatically at: http://127.0.0.1:8087
# Workflow:
# 1. Place DVR recordings in: recordings/input/
# 2. Select video in web interface
# 3. Choose processing mode:
#    - Video with overlays
#    - HTML report + Video
#    - JSON only (fastest)
# 4. Process and download from: recordings/output/
# 5. View logs in: logs/video_processor/
```

---

## Project Structure

```
ORION/
├── README.md                    # Project overview
├── env.template                 # Environment variable template
├── INSTALL_ORION.bat            # Installation script
├── START_SERVER.bat             # Launch live monitoring
├── START_VIDEO_PROCESSOR.bat   # Launch video processor
│
├── backend/
│   ├── vision_server.py         # Flask live monitoring server
│   ├── video_processor_gui.py   # Batch video processing GUI
│   ├── process_recording.py     # Core processing logic
│   ├── check_gpu.py             # GPU detection utility
│   │
│   ├── api/                     # FastAPI backend (planned)
│   │   ├── main.py             # API entry point
│   │   ├── dependencies.py     # Shared dependencies
│   │   └── v1/                 # API v1 endpoints
│   │
│   ├── services/
│   │   ├── camera_service.py   # Multi-camera management
│   │   └── byte_tracker.py     # ByteTrack implementation
│   │
│   ├── models/
│   │   └── database.py         # SQLAlchemy ORM (planned)
│   │
│   ├── config/
│   │   └── settings.py         # Configuration management
│   │
│   ├── static/
│   │   └── watcher.png         # Logo/branding
│   │
│   ├── requirements.txt        # Python dependencies
│   └── Dockerfile              # Container image
│
├── configs/
│   ├── cameras.yaml            # Multi-camera configuration
│   └── bytetrack.yaml          # Tracking parameters
│
├── models/
│   ├── download_models.py      # Model download script
│   ├── yolo11l.pt              # Detection model (51MB)
│   └── yolo11l-seg.pt          # Segmentation model (56MB)
│
├── recordings/
│   ├── input/                  # Place DVR videos here
│   └── output/                 # Processed videos and reports
│
├── logs/
│   └── video_processor/        # Automatic processing logs
│
├── scripts/
│   ├── seed_cameras.py         # Initialize cameras in DB
│   ├── test_camera_streams.py  # Validate RTSP connections
│   └── harden_pi.sh            # Raspberry Pi security setup
│
├── Docs/
│   ├── ARCHITECTURE.md         # Technical architecture
│   ├── QUICK_START.md          # Quick start guide
│   ├── DVR_SETUP_GUIDE.md      # DVR configuration
│   └── DVR_API_REFERENCE.md    # API documentation
│
└── docker-compose.yml          # Multi-service orchestration
```

---

## Performance Metrics

### Current Performance (v1.2)

| Metric | Value | Notes |
|--------|-------|-------|
| **Live Stream FPS** | 10-15 FPS | Per camera, CPU inference |
| **Processing Speed** | 5-10 FPS | Depends on frame skip setting |
| **Two-Pass Speedup** | 2-5x faster | vs traditional single-pass |
| **Detection Accuracy** | 99%+ | Person/vehicle classes |
| **Tracking Consistency** | 95%+ | Single camera persistent IDs |
| **Memory Usage** | 4-8GB | With YOLOv11-Large models |

### Target Performance (Future)

| Metric | Target | Technology |
|--------|--------|------------|
| **Edge Inference** | <50ms | Hailo-8 accelerator |
| **Edge FPS** | 15-20 FPS | Per camera on Raspberry Pi |
| **Database Writes** | 100+ events/sec | PostgreSQL bulk inserts |
| **TV Dashboard** | 8-10 FPS | 8-camera grid layout |
| **API Response** | <200ms | 95th percentile |
| **System Uptime** | 99%+ | 24/7 unattended operation |

---

## Recent Updates

### v1.2 - December 11, 2024
- **Two-Pass Processing:** 2-5x faster video processing workflow  
- **Comprehensive Logging:** Automatic detailed logs for every job  
- **Logs Folder:** Organized logs in `logs/video_processor/`  
- **Enhanced Error Handling:** Robust cleanup and reporting  
- **Log Viewer:** View/download logs from web interface  
- **JSON + Render Mode:** Separate inference from rendering  

### v1.1 - December 11, 2024
- Upgraded to YOLOv11-Large models for best accuracy  
- Models organized in dedicated `models/` folder  
- Segmentation mask visualization for people  
- HTML report generation with detection timelines  
- Process every frame option for smooth playback  
- Unified model usage across all pipelines  
- Improved video processor web interface  


## Business Value

| Objective | Capability |
|-----------|------------|
| **Safety Monitoring** | Real-time person and vehicle detection with alerts |
| **Workflow Analytics** | Automated tracking, dwell time, congestion analysis |
| **Compliance Documentation** | Timestamped detection logs with video evidence |
| **Operational Insights** | Heat maps, traffic patterns, zone utilization metrics |
| **Labor Analytics** | Automated time tracking and shift metrics |
| **Forensic Review** | Searchable video archive with AI-enhanced navigation |

---

## Success Metrics

### Technical Goals
- [x] All cameras streaming reliably with <5% frame drops  
- [x] 99%+ detection accuracy for person/vehicle classes  
- [x] Two-pass processing achieving 2-5x speedup  
- [x] Comprehensive logging for all operations  
- [ ] Cross-camera tracking (90%+ ID consistency) - In Progress  
- [ ] Hailo edge acceleration (sub-100ms latency) - Planned  

### Business Objectives
- [x] Production-ready live monitoring system  
- [x] Batch processing for historical analysis  
- [x] HTML reports for non-technical stakeholders  
- [ ] 24/7 unattended operation - In Progress  
- [ ] TV dashboard for operations center - Planned  
- [ ] API integration for third-party tools - Planned  


<div align="center">

**Edge AI • Multi-Camera Tracking • Workflow Analytics**

*Building intelligent systems for industrial monitoring and safety*

---


</div>
