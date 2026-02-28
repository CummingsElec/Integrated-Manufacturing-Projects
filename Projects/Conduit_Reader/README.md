<div align="center">

<img src="./Conduit_Reader.png" alt="Conduit Reader Banner" width="300"/>

# Conduit Reader

**Conduit Bend Verification via Computer Vision**

> Tablet-based vision tool for verifying conduit bend angles, offsets, and saddles against tolerances on the shop floor

[![Status](https://img.shields.io/badge/Status-Active_Development-blue?style=flat-square)](#)
[![Kotlin](https://img.shields.io/badge/Kotlin-Compose-7F52FF?style=flat-square&logo=kotlin&logoColor=white)](#)
[![Android](https://img.shields.io/badge/Android-API_28+-3DDC84?style=flat-square&logo=android&logoColor=white)](#)
[![CameraX](https://img.shields.io/badge/CameraX-Vision-00C7B7?style=flat-square)](#)

</div>

---

## Problem Statement

Electricians bend conduit by hand or with mechanical benders, then rely on visual inspection and physical protractors to verify angles. Offsets, saddles, and kicks require multiple bends at precise angles with specific segment lengths between them. Verification is slow, subjective, and error-prone—bad bends mean rework, wasted material, and schedule delays.

**Conduit Reader automates bend verification** using the tablet camera to detect conduit geometry, measure bend angles and segment lengths, and provide instant pass/fail results against configurable tolerances.

---

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                       Conduit Reader                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐          │
│  │  Template   │───►│   CameraX   │───►│   Capture   │          │
│  │  Selector   │    │   Preview   │    │   + Upload  │          │
│  └─────────────┘    └─────────────┘    └─────────────┘          │
│                                               │                  │
│                    ┌──────────────────────────┘                  │
│                    ▼                                              │
│         ┌──────────────────────┐                                │
│         │  Inference Server    │                                │
│         │  Segmentation →      │                                │
│         │  Centerline →        │                                │
│         │  Curvature →         │                                │
│         │  Angles + Lengths    │                                │
│         └──────────────────────┘                                │
│                    │                                              │
│         ┌──────────┼──────────┐                                 │
│         ▼          ▼          ▼                                 │
│  ┌───────────┐ ┌────────┐ ┌──────────┐                         │
│  │ Pass/Fail │ │ Overlay│ │  Save    │                         │
│  │ Results   │ │ Render │ │ + Export │                         │
│  └───────────┘ └────────┘ └──────────┘                         │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

The workflow:
1. **Select** — Technician picks a bend template (90°, offset, saddle, kick, custom)
2. **Frame** — Live camera with guide overlay, optional calibration tag in view
3. **Capture** — Single frame sent to inference server for analysis
4. **Result** — Bend angles, segment lengths, and pass/fail displayed with overlay
5. **Save** — Stamped with operator, building, unit, station, and timestamp

---

## Tech Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **UI Framework** | Jetpack Compose | Modern declarative tablet UI |
| **Language** | Kotlin | Full app codebase |
| **Camera** | CameraX | Preview, capture, exposure/flash control |
| **ML (on-device)** | ML Kit | Object detection, barcode scanning (calibration tags) |
| **Measurement** | ARCore (optional) | Plane/depth for pixel-to-inch scaling |
| **Networking** | OkHttp | Multipart image upload to inference server |
| **State** | DataStore Preferences | Device config, tolerances, settings |
| **Kiosk** | Launched by CEIM Field Display | Runs within tablet kiosk pipeline |

---

## Core Features

### 📏 Bend Template System
| Template | Bends | Description |
|----------|-------|-------------|
| Single (90/60/45/30/22.5°) | 1 | Standard single-angle verification |
| Offset | 2 | Two equal bends, opposite directions |
| 3-Bend Saddle | 3 | Center peak with symmetric outer bends |
| 4-Bend Saddle | 4 | Full symmetric saddle profile |
| Kick | 1 | Single offset kick |
| Custom | Any | User-defined parameters |

### 🎯 Tolerance Engine
- Per-bend angle tolerance (default ±2°)
- Segment length tolerance (default ±1/4")
- Green/red pass/fail with drill-down details
- Confidence meter — only reports when confidence is high

### 📐 Scale / Measurement
| Method | Reliability | Setup |
|--------|-------------|-------|
| AprilTag / ArUco calibration target | Best | Printed tag on inspection board |
| ARCore plane + depth | Good | Device must support ARCore |
| Known EMT diameter | Acceptable | User selects conduit size (1/2" – 4") |

### 📋 Traceability
- Auto-stamped: project, building, unit, station, operator, timestamp
- Snapshot with overlay saved as proof
- JSON/CSV export for QA systems

### 🔌 Integration
- Launched from CEIM Field Display kiosk pipeline
- Shares CEIM brand theming across tablet apps
- Inference server handles heavy compute off-device

---

## App Structure

```
com.ceim.conduitreader/
├── MainActivity.kt              # App host, navigation
├── ConduitReaderApp.kt          # Application class
├── AdminReceiver.kt             # Device admin (kiosk support)
├── BootReceiver.kt              # Auto-start on boot
├── data/
│   ├── AppSettings.kt           # DataStore, device config, tolerances
│   ├── BendModels.kt            # Templates, EMT sizes, analysis results
│   └── InspectionRecord.kt      # Saved inspection with traceability
├── services/
│   ├── CameraService.kt         # CameraX lifecycle + capture
│   └── InferenceApiService.kt   # Server communication + result parsing
└── ui/
    ├── screens/                  # Home, TemplateSelect, Capture, Results, History, Admin
    └── theme/
        └── Theme.kt             # CEIM brand colors + pass/fail/warn
```

---

## Current Status

**🔄 Active Development — Scaffold Complete**

- ✅ Project structure and Gradle build system
- ✅ CameraX service with capture pipeline
- ✅ Inference API client (multipart upload + result parsing)
- ✅ Bend template system (10 types + EMT sizes)
- ✅ Tolerance engine data models
- ✅ Traceability / inspection record models
- ✅ CEIM Field Display kiosk integration
- 🔄 Screen UI composables in progress
- 📋 Inference server implementation planned
- 📋 AprilTag / calibration detection planned

## Business Value

| Metric | Impact |
|--------|--------|
| **Bend verification speed** | Minutes of manual checking → seconds |
| **Rework reduction** | Catch bad bends before installation |
| **Consistency** | Objective CV measurement vs subjective eye |
| **Traceability** | Every inspection stamped and saved |
| **Hardware cost** | Uses existing job-site tablet |

---

## Device Requirements

| Requirement | Specification |
|-------------|---------------|
| **Device** | Android tablet (sw ≥ 600dp) |
| **Android** | API 28+ (Android 9.0) |
| **Camera** | Rear-facing, autofocus preferred |
| **ARCore** | Optional (improves measurement accuracy) |
| **Network** | Required for inference server communication |

---

<div align="center">

**Computer Vision • Conduit Verification • Tolerance Engine • Field Tool**

*Built with Kotlin Compose • Powered by CameraX & ML Kit • Made for the Shop Floor*

</div>
