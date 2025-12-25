<div align="center">

<img src="../../Asthetics/Thundercats_Cummings_CV.jpg" alt="Cummings CV Banner" width="100%"/>

# Cummings CV

**Enterprise Computer Vision System for Industrial Safety & Monitoring**

> Production-grade video analytics platform with real-time AI inference across multi-channel camera feeds

[![Status](https://img.shields.io/badge/Status-Production-success?style=flat-square)](#)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](#)
[![YOLO](https://img.shields.io/badge/YOLO-v11--Large-00FFFF?style=flat-square)](#)
[![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)](#)

</div>

---

## Problem Statement

Industrial facilities need continuous monitoring for safety compliance, personnel tracking, and incident documentation. Traditional CCTV systems provide passive recording but offer no real-time intelligence or automated alerting.

**Cummings CV transforms existing camera infrastructure** into an active AI-powered monitoring system that detects people, tracks movement, and provides privacy-preserving analytics—all processed locally with no cloud dependencies.

---

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         Web Interface (Flask)                            │
├─────────────────────────────────────────────────────────────────────────┤
│  Camera Selector │ Live Stream │ Detection Toggles │ Analysis Queue    │
└────────┬────────────────┬────────────────┬────────────────┬─────────────┘
         │                │                │                │
         ▼                ▼                ▼                ▼
┌─────────────────┐ ┌───────────────┐ ┌───────────────┐ ┌────────────────┐
│  DVR/NVR Layer  │ │ YOLO Inference│ │ ByteTrack     │ │ LM Studio      │
│  Multi-Channel  │ │ GPU/CPU       │ │ MOT Engine    │ │ Vision LLM     │
│  8 Cameras      │ │ CUDA/CPU      │ │ ID Persistence│ │ Text Analysis  │
├─────────────────┤ ├───────────────┤ ├───────────────┤ ├────────────────┤
│ • HTTPS/RTSP    │ │ • yolo11l-seg │ │ • track_buffer│ │ • Local only   │
│ • 12MP streams  │ │ • yolo11l-pose│ │ • IoU matching│ │ • OCR capable  │
│ • Adaptive FPS  │ │ • 640px input │ │ • 120 frames  │ │ • No cloud     │
└─────────────────┘ └───────────────┘ └───────────────┘ └────────────────┘
                                    │
                                    ▼
                        ┌────────────────────┐
                        │   Data Export      │
                        │  JPEG • JSON • CSV │
                        └────────────────────┘
```

---

## Tech Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Web Framework** | Flask | REST API and web dashboard |
| **Object Detection** | YOLOv11-Large | Person/vehicle detection |
| **Segmentation** | YOLOv11-Seg | Pixel-accurate instance masks |
| **Pose Estimation** | YOLOv11-Pose | 17-keypoint skeleton tracking |
| **Tracking** | ByteTrack | Multi-object tracking with persistent IDs |
| **Video Processing** | OpenCV | Frame capture and manipulation |
| **Camera Integration** | HTTPS/RTSP | Multi-protocol DVR communication |

---

## Core Features

### 📹 Multi-Camera Monitoring
- **8 simultaneous channels** from NVR/DVR systems
- **Adaptive streaming** with automatic protocol fallback (HTTPS → HTTP → RTSP)
- **Web-based camera selector** for live channel switching
- **DVR throttling** to prevent overload during high-frequency requests

### 🎯 AI Detection Capabilities
- **Person detection** with YOLOv11-Large (27.6M parameters)
- **Instance segmentation** for pixel-accurate person boundaries
- **Pose estimation** with 17-keypoint skeleton overlay
- **Configurable detection classes** and confidence thresholds

### 🔒 Privacy-Preserving Features
- **Anonymization mode** — Solid color overlays obscure identifying features
- **Local processing only** — No data leaves the network
- **No telemetry** — Zero external data transmission
- **Configurable retention** — Control what gets stored and for how long

### 📊 Tracking & Analytics
- **ByteTrack integration** optimized for low-FPS DVR streams (1-3 FPS)
- **Persistent ID assignment** across frames
- **Track buffer** maintains identity through brief occlusions
- **JSON/CSV export** for downstream analysis

---

## Detection Models

### YOLOv11-Large Specifications

| Metric | Value |
|--------|-------|
| **Parameters** | 27,678,368 |
| **GFLOPs** | 132.9 |
| **Input Resolution** | 640×640 |
| **mAP@0.5** | 0.53 |
| **Supported Classes** | 80 (COCO) |

### Available Detection Modes

| Mode | Model | Output |
|------|-------|--------|
| **Detection** | yolo11l | Bounding boxes |
| **Segmentation** | yolo11l-seg | Pixel masks |
| **Pose** | yolo11l-pose | Skeleton keypoints |

---

## Web Interface

The Flask-powered dashboard provides:

| Component | Function |
|-----------|----------|
| **Camera Selector** | Switch between 8 DVR channels |
| **Live Stream** | Real-time video with AI overlays |
| **Detection Toggles** | Enable/disable Person, Pose, Segmentation |
| **Analysis Queue** | Submit frames to vision LLM |
| **Capture History** | Recent snapshots with thumbnails |

### API Endpoints

```
GET  /                    → Web dashboard
GET  /frame.jpg           → Current processed frame
GET  /stream              → MJPEG video stream
POST /api/snapshot        → Capture image
POST /api/analyze         → Queue AI analysis
GET  /api/cameras         → List available cameras
POST /api/switch_camera   → Change active camera
GET  /api/status          → System status
```

---

## Current Status

**✅ Production**

- ✅ Multi-camera DVR integration (8 channels)
- ✅ YOLOv11-Large model support
- ✅ Instance segmentation with anonymization
- ✅ ByteTrack optimization for low FPS
- ✅ Web-based camera selector
- 🔄 Direct camera RTSP bypass planned
- 📋 Custom detection models (forklift, PPE) in roadmap



## Business Value

| Capability | Impact |
|------------|--------|
| **Real-time monitoring** | Immediate awareness of personnel and activity |
| **Safety compliance** | Automated detection supports safety audits |
| **Privacy preservation** | Anonymization enables monitoring without identity exposure |
| **Incident documentation** | Timestamped captures with detection metadata |
| **Local processing** | No cloud costs, no data sovereignty concerns |

---

## Hardware Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| **OS** | Windows 10 64-bit | Windows 11 |
| **CPU** | Intel i5 / Ryzen 5 | Intel i7 / Ryzen 7 |
| **RAM** | 8 GB | 16+ GB |
| **GPU** | Integrated | NVIDIA RTX (8+ GB VRAM) |
| **Network** | 100 Mbps | 1 Gbps |

---

<div align="center">

**Industrial Computer Vision • Real-Time AI • Privacy-Preserving Analytics**

</div>

