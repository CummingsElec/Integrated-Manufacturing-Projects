# Integrated Manufacturing Projects

<div align="center">

**A portfolio showcasing internal software engineering projects for industrial automation, computer vision, and mobile tooling.**

<br/>

[![Projects](https://img.shields.io/badge/Projects-6-0A66C2?style=for-the-badge)](Projects/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Swift](https://img.shields.io/badge/Swift-5.9-F05138?style=for-the-badge&logo=swift&logoColor=white)](https://swift.org)
[![Java](https://img.shields.io/badge/Java-17-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)](https://openjdk.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

<br/>

![Computer Vision](https://img.shields.io/badge/Computer_Vision-RF--DETR_|_SAM3-00FFFF?style=flat-square)
![Edge AI](https://img.shields.io/badge/Edge_AI-Hailo_|_CoreML-FF6F00?style=flat-square)
![Robotics](https://img.shields.io/badge/Robotics-6--DOF_Arm-9C27B0?style=flat-square)
![iOS](https://img.shields.io/badge/iOS-ARKit_|_SwiftUI-007AFF?style=flat-square)
![Android](https://img.shields.io/badge/Android-ML_Kit_|_WebSocket-3DDC84?style=flat-square)

</div>

---

## What Is This Repository?

This is a **public-facing portfolio** showcasing software systems I've architected and developed for industrial automation and computer vision applications. The actual source code resides in private repositories—this repository serves as a curated technical presentation of:

- **System Architecture & Design** — Technology decisions, data flow, and scalability patterns
- **Technical Implementation** — Full-stack development across Python, Swift, embedded systems
- **Business Impact** — Measurable outcomes, efficiency gains, and potential ROI
- **Development Progress** — Internal systems under active development and testing

**Portfolio Philosophy:** This showcase balances technical depth for engineering reviewers with clear business outcomes for leadership and stakeholders. Each project includes architecture diagrams, technology justifications, and development status.

---

## Project Showcase

<table>
<tr>
<td width="50%" align="center">

<a href="Projects/CERBERUS/">
<img src="Projects/CERBERUS/Cerberus.png" alt="CERBERUS" width="100%"/>
</a>

**[CERBERUS](Projects/CERBERUS/)**<br/>
*Robotic Panel Documentation*

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![RF-DETR](https://img.shields.io/badge/RF--DETR-00FFFF?style=flat-square)
![Robotics](https://img.shields.io/badge/Robotics-9C27B0?style=flat-square)

</td>
<td width="50%" align="center">

<a href="Projects/Cummings_CV/">
<img src="Projects/Cummings_CV/Thundercats_Cummings_CV.jpg" alt="Cummings CV" width="100%"/>
</a>

**[Cummings CV](Projects/Cummings_CV/)**<br/>
*Industrial Video Analytics*

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![SAM3](https://img.shields.io/badge/SAM3-00FFFF?style=flat-square)
![Flask](https://img.shields.io/badge/Flask-000?style=flat-square&logo=flask)

</td>
</tr>
<tr>
<td width="50%" align="center">

<a href="Projects/ORION/">
<img src="Projects/ORION/Watcher.png" alt="ORION" width="100%"/>
</a>

**[ORION](Projects/ORION/)**<br/>
*Multi-Camera AI Platform*

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Hailo](https://img.shields.io/badge/Hailo_AI-FF6F00?style=flat-square)

</td>
<td width="50%" align="center">

<a href="Projects/Panel_Scanner_IOS/">
<img src="Projects/Panel_Scanner_IOS/Panel_scanner_IOS.png" alt="Panel Scanner iOS" width="200"/>
</a>

**[Panel Scanner iOS](Projects/Panel_Scanner_IOS/)**<br/>
*Mobile Panel Detection App*

![Swift](https://img.shields.io/badge/Swift-F05138?style=flat-square&logo=swift&logoColor=white)
![CoreML](https://img.shields.io/badge/CoreML-00C7B7?style=flat-square)
![ARKit](https://img.shields.io/badge/ARKit-007AFF?style=flat-square)

</td>
</tr>
<tr>
<td width="50%" align="center">

<a href="Projects/EyePhone_App/">
<img src="Projects/EyePhone_App/EyePhone_App.png" alt="EyePhone App" width="200"/>
</a>

**[EyePhone App](Projects/EyePhone_App/)**<br/>
*Animated Robot Eyes for Android*

![Java](https://img.shields.io/badge/Java-ED8B00?style=flat-square&logo=openjdk&logoColor=white)
![ML Kit](https://img.shields.io/badge/ML_Kit-4285F4?style=flat-square)
![WebSocket](https://img.shields.io/badge/WebSocket-4353FF?style=flat-square)

</td>
<td width="50%" align="center">

<a href="Projects/Project_Recorder/">
<img src="Projects/Project_Recorder/Project_Recorder.png" alt="Project Recorder" width="200"/>
</a>

**[Project Recorder](Projects/Project_Recorder/)**<br/>
*Job Site Video with OCR Naming*

![Swift](https://img.shields.io/badge/Swift-F05138?style=flat-square&logo=swift&logoColor=white)
![CoreML](https://img.shields.io/badge/CoreML-00C7B7?style=flat-square)
![OneDrive](https://img.shields.io/badge/OneDrive-0078D4?style=flat-square)

</td>
</tr>
</table>

---

## Project Summaries

### CERBERUS
**Cummings Electrical Robotic Breaker & Equipment Recognition Unified System**

An automated robotic system that captures high-resolution images of electrical panels using a 6-DOF robotic arm and linear gantry, then applies RF-DETR object detection and OCR to identify breaker part numbers and phases. Features a multi-model AI pipeline with local LLM inference and cloud fallback. Computer vision model training pipelines help expedite inference systems to match exact needs for vision processing.

**Key Outcomes:**
- Eliminates manual image documentation and annotation (hours → minutes)
- Custom RF-DETR models trained for 15+ breaker classes, trainable for any CV task
- Edge processing via Raspberry Pi for portable use

📁 [View Project Details →](Projects/CERBERUS/)

---

### Cummings CV
**Enterprise Computer Vision for Industrial Safety & Monitoring**

A video analytics platform integrating with multi-channel NVR systems for real-time AI inference. Supports person detection, instance segmentation, pose estimation, and persistent object tracking across 8 simultaneous camera feeds.

**Key Outcomes:**
- 8-channel live monitoring with privacy-preserving anonymization
- RF-DETR-Large with transformer architecture for high-accuracy detection
- Web-based dashboard with real-time streaming and analysis queuing

📁 [View Project Details →](Projects/Cummings_CV/)

---

### ORION
**Operational Recognition Intelligence and Observation Network**

An AI vision platform delivering live stream monitoring and intelligent batch video processing. Features RF-DETR-Large models with SAM3 instance segmentation, ByteTrack multi-object tracking, and innovative two-pass processing for 2-5x speed improvements. Planned expansion includes edge computing with Hailo AI accelerators and cross-camera tracking.

**Key Outcomes:**
- Dual operating modes: Real-time monitoring + batch processing
- Two-pass workflow: Separate inference from rendering for massive speedup
- RF-DETR-Large with SAM3 for colored segmentation masks
- HTML detection reports with comprehensive timelines and metrics
- 8-camera DVR integration via RTSP/HTTPS streams
- **Planned:** Hybrid edge/cloud with Raspberry Pi + Hailo-8 (26 TOPS)

📁 [View Project Details →](Projects/ORION/)

---

### Panel Scanner iOS
**Mobile Electrical Panel Detection & Inventory App**

A professional iOS application for electrical contractors featuring 30 FPS on-device ML inference, AR visualization mode, and smart OCR for panel identification. Exports synchronized video recordings with structured JSON/CSV data.

**Key Outcomes:**
- RF-DETR CoreML model running entirely on-device
- AR mode with floating 3D labels for hands-free inspection
- Complete panel inventory captured in minutes, not hours

📁 [View Project Details →](Projects/Panel_Scanner_IOS/)

---

### EyePhone App
**Animated Robot Eyes for Android — Remotely Controllable**

A full-screen expressive eye animation system for Android devices, designed to run on low-power phones as an interactive face for robots, kiosks, or installations. Features ML Kit face tracking that drives gaze following and reactive expressions, IMU-based tilt gaze, 10 mood presets, and a WebSocket remote control interface. Includes kiosk lockdown mode with boot auto-start for unattended deployments.

**Key Outcomes:**
- Repurposes any Android phone (API 24+) as a robot face display
- ML Kit face detection drives realistic gaze and expression mirroring
- WebSocket control enables remote mood, theme, and gaze commands
- Kiosk mode with passcode lock and boot auto-start for field deployments

📁 [View Project Details →](Projects/EyePhone_App/)

---

### Project Recorder
**Job Site Video Recorder with Panel Label Detection & OCR**

An iOS app for recording walkthrough videos on job sites with automatic electrical panel label detection and OCR. A YOLO CoreML model detects panel label stickers in real-time, and tap-to-scan OCR reads the label text. Optional AI verification via xAI Grok catches misreads. The scanned label becomes the video filename automatically, and recordings can auto-upload to a configurable OneDrive folder.

**Key Outcomes:**
- Automatic video file naming from scanned panel labels—no manual entry
- YOLO on-device detection + Apple Vision OCR + Grok AI verification pipeline
- OneDrive auto-upload eliminates cable transfer and manual organization
- Eliminates hours of post-job file renaming and upload admin

📁 [View Project Details →](Projects/Project_Recorder/)

---

## Technical Highlights

### Computer Vision & Machine Learning
- **Open Source CV Models** — RF-DETR and SAM3 with Apache 2.0 licensing for unrestricted commercial use
- **Instance Segmentation** — Pixel-accurate masks for privacy-preserving person detection and tracking
- **Multi-Object Tracking** — ByteTrack integration for persistent ID assignment across frames
- **On-Device Inference** — CoreML (iOS Neural Engine) and Hailo AI accelerator (26 TOPS) optimization
- **Transfer Learning** — Custom training pipelines for specialized industrial detection tasks

### Edge AI & Embedded Systems
- **Raspberry Pi 5 Edge Computing** — 16GB RAM with dedicated Hailo-8 AI accelerator
- **Real-Time Performance** — 10-30 FPS inference depending on model complexity and hardware
- **Hybrid Architecture** — Edge inference for latency-critical tasks + cloud for heavy processing
- **Industrial Integration** — PLCs, robotic arms, motorized gantries, and IP camera systems
- **30TB Local Storage** — On-site data retention for edge devices

### iOS & Mobile Development
- **Modern Swift Architecture** — SwiftUI + Combine for reactive, maintainable codebases
- **Neural Engine Optimization** — CoreML models running at 30 FPS on-device
- **Augmented Reality** — ARKit integration with floating 3D labels and spatial tracking
- **Enterprise SSO** — Microsoft Entra ID / Okta authentication for secure access
- **Offline-First Design** — Full functionality without network connectivity

### Android Development
- **WebView + GSAP Animation** — 60fps expressive eye animations with 3D depth effects
- **ML Kit Face Detection** — On-device face tracking with gaze following and expression mirroring
- **WebSocket Remote Control** — Network-accessible command interface for mood, gaze, and theme
- **Kiosk Mode** — Device Owner / Lock Task Mode with passcode protection and boot auto-start
- **Sensor Integration** — IMU (accelerometer + gyroscope) for tilt-based gaze control

### Backend & Infrastructure
- **Modern API Frameworks** — FastAPI (async) and Flask for different workload types
- **Database Systems** — PostgreSQL with SQLAlchemy ORM for relational data
- **Containerization** — Docker and docker-compose for reproducible environments
- **Background Processing** — Redis + Celery for distributed task queues
- **Multi-Camera Streaming** — RTSP/HTTP stream management with 8+ simultaneous cameras
- **Video Analytics** — Two-pass processing for 2-5x speed improvements

### Robotics & Automation
- **6-DOF Robotic Arms** — Serial protocol control with inverse kinematics
- **Linear Gantry Systems** — PLC communication for precise positioning
- **Multi-Waypoint Planning** — Collision avoidance and safety interlocks
- **Computer Vision Integration** — Real-time feedback loops for adaptive behavior
- **Custom Training Pipelines** — End-to-end annotation, training, and deployment workflows

---

## Repository Structure

```
├── README.md                 ← You are here
├── LICENSE                   ← MIT + third-party notices
└── Projects/
    ├── CERBERUS/             ← Robotic panel documentation
    ├── Cummings_CV/          ← Industrial computer vision
    ├── EyePhone_App/         ← Animated robot eyes (Android)
    ├── ORION/                ← Multi-camera AI platform
    ├── Panel_Scanner_IOS/    ← iOS panel scanner app
    └── Project_Recorder/     ← Job site video recorder (iOS)
```

---

## My Role & Contributions

As the **principal engineer and sole developer** across these systems, I maintain the complete software lifecycle:

### Architecture & System Design
- Technology stack selection and architectural pattern decisions
- Hybrid edge/cloud architectures for optimal performance
- Database schema design and data modeling
- API design with REST, WebSocket, and async patterns
- Scalability planning for multi-device deployments

### Full-Stack Implementation
- **Backend:** Python (FastAPI, Flask), async/await patterns, ORM design
- **Frontend:** Web interfaces (HTML/CSS/JS), real-time dashboards
- **iOS:** Swift + SwiftUI, ARKit, CoreML on-device inference
- **Android:** Java, WebView + GSAP, ML Kit, CameraX, WebSocket
- **Embedded:** Raspberry Pi, Arduino, PLC integration

### ML/AI Engineering
- Computer vision pipeline development with RF-DETR and SAM3
- Custom dataset creation, annotation, and augmentation
- Model training, optimization, and hyperparameter tuning
- Model conversion for edge deployment (CoreML, Hailo HEF)
- Performance optimization and inference benchmarking

### Hardware & Systems Integration
- 6-DOF robotic arm control and motion planning
- PLC communication protocols and industrial automation
- Multi-camera IP camera systems and RTSP streaming
- AI accelerator integration (Hailo-8, Apple Neural Engine)
- Sensor fusion and real-time feedback systems

### DevOps & Deployment
- Docker containerization and docker-compose orchestration
- Deployment automation scripts and batch files
- Environment configuration and secrets management
- Logging, monitoring, and error tracking systems
- Database migrations and backup strategies

### Documentation & Knowledge Transfer
- Technical architecture documentation with diagrams
- API reference documentation and integration guides
- User manuals and training materials
- Troubleshooting guides and FAQ resources
- Code documentation and inline comments

---

## Contact

For questions about these projects or collaboration opportunities:

**Jacob Yount**  
*R&D Engineer — Industrial Automation & AI*

---

<div align="center">

**Industrial AI • Computer Vision • Mobile Development • Robotics**

*Building intelligent systems for manufacturing and electrical industries*

<br/>


</div>
