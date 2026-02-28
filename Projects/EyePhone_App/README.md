<div align="center">

<img src="./EyePhone_App.png" alt="EyePhone App Banner" width="300"/>

# EyePhone App

**Animated Robot Eyes for Android — Remotely Controllable**

> Full-screen expressive eye animations for robots, kiosks, and installations with face tracking, remote control, and kiosk lockdown

[![Status](https://img.shields.io/badge/Status-Production-success?style=flat-square)](#)
[![Android](https://img.shields.io/badge/Android-API_24+-3DDC84?style=flat-square&logo=android&logoColor=white)](#)
[![Java](https://img.shields.io/badge/Java-17-ED8B00?style=flat-square&logo=openjdk&logoColor=white)](#)
[![WebSocket](https://img.shields.io/badge/WebSocket-Remote_Control-4353FF?style=flat-square)](#)

</div>

---

## Problem Statement

Interactive robotics and kiosk deployments need expressive, human-readable interfaces that feel alive—but building custom display firmware is expensive and rigid. Off-the-shelf solutions lack the expressiveness, remote controllability, and industrial durability needed for field-deployed hardware.

**EyePhone turns any low-power Android phone into an animated robot face** with 10 mood presets, real-time face tracking, remote WebSocket control, and kiosk lockdown—all running in a single lightweight app.

---

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        EyePhone App                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐          │
│  │   WebView   │◄──►│    GSAP     │◄──►│   Mood      │          │
│  │   Renderer  │    │   Animate   │    │   Engine    │          │
│  └─────────────┘    └─────────────┘    └─────────────┘          │
│         ▲                                     ▲                  │
│         │           ┌─────────────┐           │                  │
│         └──────────►│   Gaze      │◄──────────┘                  │
│                     │   Manager   │                              │
│                     └─────────────┘                              │
│                           ▲                                      │
│         ┌─────────────────┼─────────────────┐                   │
│         ▼                 ▼                 ▼                   │
│  ┌─────────────┐   ┌─────────────┐   ┌─────────────┐          │
│  │  ML Kit     │   │    IMU      │   │  WebSocket  │          │
│  │  Face Det.  │   │  Gyro/Accel │   │   Remote    │          │
│  └─────────────┘   └─────────────┘   └─────────────┘          │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

Three gaze input sources feed the animation engine:
1. **Face Tracking** — ML Kit detects faces and drives gaze following, blink mirroring, and reactive expressions
2. **IMU Sensors** — Accelerometer and gyroscope tilt the eyes when the phone moves
3. **WebSocket** — Remote commands for mood, gaze, and theme from any machine on the network

---

## Tech Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Rendering** | WebView + GSAP | Smooth eye animation at 60fps |
| **Face Detection** | ML Kit (Google) | On-device face tracking and expression recognition |
| **Camera** | CameraX (AndroidX) | Front camera feed for face detection |
| **Remote Control** | WebSocket Server | Network-accessible mood/gaze/theme commands |
| **Kiosk Mode** | Device Owner API | Lock Task Mode with passcode protection |
| **Snapshots** | CameraX ImageCapture | Periodic JPEG captures with auto-recycling |
| **Controller** | Python + websockets | Desktop remote control interface |

---

## Core Features

### 👁️ Expressive Eye Animation
- Realistic eyeballs with iris fibers, dynamic pupils, curved eyebrows, and 3D depth effects
- GSAP-powered smooth transitions between states
- Persistent hold states with periodic emphasis animations

### 🎭 10 Mood Presets
| Mood | Trigger |
|------|---------|
| Happy, Sad, Angry | Manual or face-reactive |
| Surprise, Fear, Disgust | Manual or face-reactive |
| Confused, Love, Sleepy, Excited | Manual or remote command |

### 📷 Face Tracking Intelligence
- ML Kit on-device face detection drives gaze direction
- Blink mirroring from detected faces
- Reactive expressions (smile → joy, head turn → surprise)
- Auto-snapshot captures during detection with 200MB recycling

### 🎨 7 Color Themes
OD Green (default), Cyan, Amber, Green, Red, White, Purple — plus custom hex color picker

### 🔒 Kiosk Mode
- Android Device Owner / Lock Task Mode
- Passcode-protected unlock
- Auto-launch on device boot
- Adaptive screen brightness based on battery level

### 📡 WebSocket Remote Control
| Command | Example |
|---------|---------|
| `emotion <mood>` | `emotion joy` |
| `eye <x> <y>` | `eye 0.8 0.3` (normalized 0-1) |
| `theme <name>` | `theme odgreen` |
| `neutral` | Reset to idle |

---

## App Structure

```
app/src/main/
├── assets/
│   ├── index.html              # WebView entry point
│   ├── web-eye-animation.js    # Eye rendering, animation, UI, state
│   └── gsap.min.js             # GSAP animation library
├── java/com/ceim/roboteyes/
│   ├── MainActivity.java       # WebView host, CameraX, ML Kit, IMU, kiosk
│   ├── AdminReceiver.java      # Device admin for kiosk lock task
│   └── BootReceiver.java       # Auto-start on boot
controller/
└── eye_controller.py           # Python WebSocket server for remote control
```

---

## Current Status

**✅ Production**

- ✅ Full eye animation system with 10 moods
- ✅ ML Kit face tracking with reactive expressions
- ✅ WebSocket remote control operational
- ✅ Kiosk mode with boot auto-start
- ✅ 7 color themes + custom hex picker
- ✅ Auto-snapshot system with storage management

## Business Value

| Metric | Impact |
|--------|--------|
| **Hardware cost** | Repurposes any Android phone (API 24+) |
| **Deployment** | Single APK install, no custom firmware |
| **Remote management** | WebSocket control from any networked device |
| **Durability** | Kiosk lockdown prevents tampering |
| **Customization** | Themes, moods, and gaze all configurable |

---

<div align="center">

**Android • Face Tracking • WebSocket Control • Kiosk Mode**

*Built with Java • Powered by ML Kit & GSAP • Made for Robots*

</div>
