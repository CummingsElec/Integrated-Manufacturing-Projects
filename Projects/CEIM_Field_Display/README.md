<div align="center">

<img src="./CEIM_Field_Display.png" alt="CEIM Field Display Banner" width="300"/>

# CEIM Field Display

**Digital Signage, Kiosk Management & AI Field Assistant for Android**

> Full-screen configurable signage with kiosk lockdown, multi-app launching, and an AI-powered electrical field assistant

[![Status](https://img.shields.io/badge/Status-Active_Development-blue?style=flat-square)](#)
[![Kotlin](https://img.shields.io/badge/Kotlin-Compose-7F52FF?style=flat-square&logo=kotlin&logoColor=white)](#)
[![Android](https://img.shields.io/badge/Android-API_24+-3DDC84?style=flat-square&logo=android&logoColor=white)](#)
[![xAI](https://img.shields.io/badge/xAI-Grok_4-FF6F00?style=flat-square)](#)

</div>

---

## Problem Statement

Industrial facilities and job sites need a way to display company branding, safety messages, and rotating announcements on dedicated Android devices—while also locking those devices to prevent misuse. Teams also need quick access to field reference tools (Autodesk Vault, Bluebeam, PlanGrid) and NEC code lookups without switching between apps or pulling out a laptop.

**CEIM Field Display combines digital signage, kiosk management, and an AI field assistant** into a single Android app that runs on any tablet or phone, with passcode-protected admin controls and Device Owner kiosk lockdown.

---

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     CEIM Field Display                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────────────────────────────────────────┐            │
│  │              Signage Engine                       │            │
│  │  Dual-slide crossfade • Clock • Custom themes     │            │
│  └──────────────────────────────────────────────────┘            │
│                           │                                      │
│         ┌─────────────────┼─────────────────┐                   │
│         ▼                 ▼                 ▼                   │
│  ┌─────────────┐   ┌─────────────┐   ┌─────────────┐          │
│  │  Kiosk Mgr  │   │  AI Chat    │   │   Admin     │          │
│  │  Lock Task  │   │  Grok xAI   │   │   Panel     │          │
│  └─────────────┘   └─────────────┘   └─────────────┘          │
│         │                                     │                  │
│         ▼                                     ▼                  │
│  ┌─────────────────────────────────────────────────┐            │
│  │           External App Pipeline                  │            │
│  │  Vault • ACC/PlanGrid • Bluebeam • Overlay Nav   │            │
│  └─────────────────────────────────────────────────┘            │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

The app operates as a hub:
1. **Signage** — Full-screen configurable slides with crossfade transitions and live clock
2. **Kiosk** — Device Owner lock task mode pins the device to this app or a whitelisted external app
3. **AI Assistant** — xAI Grok-powered chat for NEC codes, wiring specs, and construction questions
4. **App Launcher** — One-tap launch to Autodesk Vault, PlanGrid/ACC, or Bluebeam with floating overlay to return

---

## Tech Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **UI Framework** | Jetpack Compose | Modern declarative Android UI |
| **Language** | Kotlin | Full app codebase |
| **State** | DataStore Preferences | Persistent settings and configuration |
| **AI** | xAI Grok (grok-4-1-fast) | Field assistant chat for NEC/electrical queries |
| **Kiosk** | Device Owner / Lock Task API | Full device lockdown with app whitelisting |
| **Overlay** | WindowManager + System Alert | Floating nav button over external apps |
| **Boot** | BroadcastReceiver | Auto-launch on device startup |

---

## Core Features

### 📺 Digital Signage
- **Dual-slide system** with configurable crossfade transitions
- Per-slide customization: text, subtitle, background color, text color, font size, weight, letter spacing
- 8 background color presets + 6 text color presets
- Configurable transition speed (3–30s) and fade duration (0.5–5s)
- Optional live clock display

### 🔒 Kiosk Management
- Android Device Owner / Lock Task Mode
- **Multi-app kiosk pipeline** — lock to signage or any whitelisted app:

| Target | App |
|--------|-----|
| CEIM Signage | Built-in signage display |
| Autodesk Vault | Drawing and document management |
| Autodesk ACC / PlanGrid | Construction management |
| Bluebeam Cloud | PDF markup and review |

- Floating overlay button for returning to CEIM from external apps
- Passcode-protected admin access
- Boot auto-start for unattended deployments

### 🤖 AI Field Assistant
- **xAI Grok** (grok-4-1-fast) powered chat
- NEC 2023 code lookups and interpretations
- Wire sizing, conduit fill, voltage drop calculations
- E-House fabrication and assembly guidance
- Switchgear, MCC, VFD, PLC specifications
- Safety and OSHA compliance questions

### ⚙️ Admin Panel
- Split-pane layout: slide editor (left) + system settings (right)
- Slide 1 / Slide 2 / Transitions tab navigation
- Kiosk target selector with one-tap app launch
- API key management (password-masked)
- Passcode security configuration

---

## App Structure

```
com.ceim.fielddisplay/
├── MainActivity.kt              # App host, kiosk control, external app launching
├── CEIMApplication.kt           # Application class
├── AdminReceiver.kt             # Device admin for kiosk lock task
├── BootReceiver.kt              # Auto-start on boot
├── FloatingOverlayService.kt    # Draggable overlay button for external apps
├── data/
│   ├── AppSettings.kt           # DataStore, config models, KioskTarget enum
│   └── ChatRepository.kt        # xAI Grok API integration
└── ui/
    ├── screens/
    │   ├── SignageScreen.kt      # Dual-slide signage with crossfade
    │   ├── ChatScreen.kt        # AI field assistant chat UI
    │   ├── AdminScreen.kt       # Settings panel (slides, kiosk, AI, security)
    │   ├── PasscodeScreen.kt    # Passcode gate for admin access
    │   └── NavOverlay.kt        # Navigation overlay menu
    └── theme/
        └── Theme.kt             # CEIM brand colors and theming
```

---

## Current Status

**🔄 Active Development**

- ✅ Dual-slide signage with crossfade transitions
- ✅ Full admin panel with slide/kiosk/AI configuration
- ✅ Device Owner kiosk mode with multi-app whitelisting
- ✅ Floating overlay for external app navigation
- ✅ xAI Grok AI field assistant
- ✅ Boot auto-start and passcode security
- 🔄 Additional kiosk target apps planned
- 📋 Remote configuration management in roadmap

## Business Value

| Metric | Impact |
|--------|--------|
| **Device management** | Single app controls signage + kiosk + field tools |
| **Hardware cost** | Any Android tablet or phone (API 24+) |
| **Field reference** | AI assistant for instant NEC code and spec lookups |
| **Security** | Device Owner lockdown prevents tampering |
| **Deployment** | Boot auto-start, no manual intervention after power-on |
| **Branding** | Customizable signage for any facility or job site |

---

<div align="center">

**Digital Signage • Kiosk Management • AI Assistant • Field Tools**

*Built with Kotlin Compose • Powered by xAI Grok • Made for Job Sites*

</div>
