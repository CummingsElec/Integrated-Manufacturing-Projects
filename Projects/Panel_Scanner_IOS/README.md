<div align="center">

<img src="../../Asthetics/Panel_scanner_IOS.png" alt="Panel Scanner iOS Banner" width="300"/>

# Panel Scanner iOS

**Real-Time Electrical Panel Detection & Inventory**

> Professional iOS application for electrical contractors with on-device ML, AR visualization, and smart data capture

[![Status](https://img.shields.io/badge/Status-Production-success?style=flat-square)](#)
[![Swift](https://img.shields.io/badge/Swift-5.9-F05138?style=flat-square&logo=swift&logoColor=white)](#)
[![iOS](https://img.shields.io/badge/iOS-17.0+-007AFF?style=flat-square&logo=apple&logoColor=white)](#)
[![CoreML](https://img.shields.io/badge/CoreML-Neural_Engine-00C7B7?style=flat-square)](#)

</div>

---

## Problem Statement

Electrical contractors spend significant time manually documenting panel inventories during service calls, inspections, and installations. This process involves:

- Visually identifying each breaker
- Recording part numbers and amperage ratings
- Taking photos for documentation
- Entering data into spreadsheets or work orders

**Panel Scanner automates this entire workflow** using on-device machine learning to detect, identify, and catalog electrical components in real-time—turning hours of manual work into minutes of guided capture.

---

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                      Panel Scanner iOS                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐         │
│  │   Camera    │───►│   CoreML    │───►│   Vision    │         │
│  │   Feed      │    │   YOLO      │    │   OCR       │         │
│  └─────────────┘    └─────────────┘    └─────────────┘         │
│         │                  │                  │                 │
│         ▼                  ▼                  ▼                 │
│  ┌─────────────────────────────────────────────────────┐       │
│  │              Tracking & Deduplication                │       │
│  │         Spatial • Temporal • Confidence              │       │
│  └─────────────────────────────────────────────────────┘       │
│                           │                                     │
│         ┌─────────────────┼─────────────────┐                  │
│         ▼                 ▼                 ▼                  │
│  ┌─────────────┐   ┌─────────────┐   ┌─────────────┐          │
│  │  AR Mode    │   │   Export    │   │   Cloud     │          │
│  │  ARKit      │   │  JSON/CSV   │   │   Sync      │          │
│  └─────────────┘   └─────────────┘   └─────────────┘          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Tech Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Framework** | SwiftUI + Combine | Reactive UI architecture |
| **Pattern** | MVVM | Clean separation of concerns |
| **ML Inference** | CoreML + Neural Engine | 30 FPS on-device detection |
| **Object Detection** | YOLOv8-Large | Panel and breaker localization |
| **OCR** | Vision Framework | Part number extraction |
| **AR** | ARKit + RealityKit | 3D label visualization |
| **Auth** | Enterprise SSO | Secure workforce access |
| **Storage** | Core Data + FileManager | Local session persistence |
| **Cloud** | OneDrive SDK | Optional team sync |

---

## Core Features

### 🎥 Scanning Modes

| Mode | Description | Best For |
|------|-------------|----------|
| **Panel Mode** | Detects panel labels only | Quick identification |
| **Full Mode** | Detects panels + all breakers | Complete inventory |
| **AR Mode** | Floating 3D labels in space | Hands-free inspection |

### 🎯 Detection Intelligence

- **Real-time tracking** — Spatial deduplication prevents duplicate entries
- **Dwell-time validation** — Only captures stable detections (configurable)
- **Cooldown system** — Prevents re-detecting same items
- **OCR confirmation** — Review and verify labels before saving

### 📊 Export Options

| Format | Content |
|--------|---------|
| **JSON** | Structured data with timestamps and confidence |
| **CSV** | Spreadsheet-ready breaker inventory |
| **MP4** | Video recording of scan session |
| **ZIP** | All files bundled for sharing |
| **Cloud** | Direct upload (optional) |

### 🤖 AI Assistant

- **Electrical Guru** — In-app AI chat for NEC codes and electrical questions
- **Context-aware** — Understands panel scanning workflow
- **Offline capable** — Works without network (with limitations)

---

## ML Model Performance

### YOLOv8-Large CoreML

| Metric | Value |
|--------|-------|
| **Inference Time** | ~30ms on iPhone 13+ |
| **FPS** | 30+ (capped at 10 for battery) |
| **Input Resolution** | 640×640 |
| **Output** | Bounding boxes + confidence |

### Detection Classes

| Class | Description |
|-------|-------------|
| `panel` | Electrical panel enclosure |
| `panel_label` | Manufacturer part number label |
| `breaker_face` | Individual circuit breaker |
| `text_roi` | Text regions for OCR |

---

## App Structure

### 5-Tab Navigation

| Tab | Purpose |
|-----|---------|
| **Scan** | Camera preview, detection, recording |
| **History** | Past sessions, export, sharing |
| **Settings** | Thresholds, FPS, data management |
| **Play** | Easter egg game (Circuit Breaker) |
| **Help** | Guides, tips, walkthrough |

### Architecture Overview

```
PanelScanner/
├── Services/               # Business logic
│   ├── CameraService       # AVFoundation capture
│   ├── DetectionService    # CoreML inference
│   ├── OCRService          # Text extraction
│   ├── TrackingService     # Deduplication
│   └── AROverlayService    # 3D rendering
├── ViewModels/             # Presentation logic
│   └── ScannerViewModel    # Main app state
├── Views/                  # UI components
│   ├── CameraView          # Live preview
│   ├── AROverlayView       # AR mode
│   └── MainView            # Tab navigation
└── Models/                 # Data structures
    └── Detection           # Detection results
```

---

## Current Status

**✅ Production**

- ✅ On-device YOLOv8 inference at 30 FPS
- ✅ All three scanning modes operational
- ✅ Smart OCR with user confirmation
- ✅ Video + JSON/CSV synchronized export
- ✅ Enterprise SSO integration
- 🔄 iPad optimization planned
- 📋 Multi-language OCR in roadmap


## Business Value

| Metric | Impact |
|--------|--------|
| **Documentation speed** | Hours → Minutes per panel |
| **Data accuracy** | ML validation reduces errors |
| **Training required** | Minimal—intuitive mobile UX |
| **Hardware cost** | Uses existing iPhones |
| **Data portability** | JSON/CSV exports integrate with any system |

---

## Device Requirements

| Requirement | Specification |
|-------------|---------------|
| **Device** | iPhone 11 or newer |
| **iOS** | 17.0+ |
| **Storage** | ~200MB for app + models |
| **Network** | Optional (for cloud sync) |

---

## Easter Egg 🎮

Hidden in the **Play** tab: a fully functional **Circuit Breaker** game!

- Tetris-style gameplay with electrical component theming
- Ghost piece preview, wall kick rotation
- Combo scoring with haptic feedback
- High score persistence

*A fun surprise for users during downtime on job sites.*

---

<div align="center">

**On-Device ML • Augmented Reality • Professional Field Tool**

*Built with Swift • Powered by CoreML • Made for Electricians*

</div>

