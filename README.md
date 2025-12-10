# 🛡️ SAFEHER - Women Safety Platform (DEMO VERSION)

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Django](https://img.shields.io/badge/Django-4.2.7-green.svg)
![License](https://img.shields.io/badge/License-Proprietary-red.svg)
![Status](https://img.shields.io/badge/Status-Demo-yellow.svg)

</div>

## ⚠️ IMPORTANT NOTICE

**THIS IS A DEMONSTRATION VERSION WITH LIMITED FUNCTIONALITY**

Core backend features including SMS alerts, real-time tracking, and database operations have been intentionally removed. This version is for **evaluation and portfolio purposes only**.

### 📧 Contact for Full Project

**Developer:** Vivek P S  
**Email:** viveksubhash4@gmail.com  
**GitHub:** [@VivekOrginal](https://github.com/VivekOrginal)

💼 **Interested in the complete working project?** Contact me to purchase the full version with all features fully implemented and production-ready.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [System Architecture](#system-architecture)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Database Schema](#database-schema)
- [Demo Limitations](#demo-limitations)
- [Full Version Features](#full-version-features)
- [License](#license)
- [Contact](#contact)

---

## 🌟 Overview

SafeHer is a comprehensive Django-based web application designed to empower women's safety through cutting-edge technology. This platform combines real-time emergency response, incident reporting, community-driven safety features, and location-based services to create a secure digital ecosystem.

**⚠️ Note:** This demo version showcases the UI/UX and frontend functionality. Backend features like SMS alerts and real-time tracking are not functional in this version.

### Mission Statement
**"Empowering women with technology for instant safety and protection"**

### Key Objectives
- Provide instant emergency response capabilities
- Enable evidence collection for legal proceedings
- Build community-driven safety networks
- Offer real-time location-based safety information
- Create awareness about unsafe areas

---

## ✨ Features

**⚠️ DEMO VERSION NOTICE:** The features listed below represent the full project design. In this demo version, only frontend UI/UX is functional. Backend operations (SMS, real-time tracking) are not implemented.

### 🚨 Emergency SOS System
- **One-Tap Emergency Alerts** - Instant SOS activation with single button press *(UI only in demo)*
- **Live Location Tracking** - Real-time GPS tracking with 5-second updates *(Not functional in demo)*
- **Loud Siren & Voice Alerts** - Automatic audio warnings to deter threats *(Frontend only)*
- **Phone Vibration Patterns** - Emergency vibration alerts *(Frontend only)*
- **SMS Integration** - Automatic emergency messages to contacts *(Not functional in demo)*
- **Volume Maximization** - Auto-increase device volume for alerts *(Frontend only)*
- **Shake Detection** - Advanced accelerometer-based emergency trigger *(Frontend only)*
- **Emergency Contact Management** - Store and manage multiple emergency contacts *(UI only)*

### 📹 Incident Reporting System
- **Video Recording** - Record incidents using device camera (front/back) *(Frontend only)*
- **Automatic Location Capture** - GPS coordinates with timestamp *(Frontend only)*
- **Evidence Storage** - Secure local storage of video evidence *(Local only, no server)*
- **Police Station Detection** - Find nearest police station automatically *(Not functional in demo)*
- **SMS Alerts** - Send incident reports via SMS with location links *(Not functional in demo)*
- **WhatsApp Integration** - Share evidence through WhatsApp *(Not functional in demo)*
- **Anonymous Reporting** - Report incidents without login *(UI only)*
- **Incident History** - Track all reported incidents *(Limited in demo)*

### 🗺️ Smart Location Services
- **Police Station Locator** - Find nearby police stations with contact info *(Requires Google Maps API)*
- **Hospital Finder** - Locate nearest hospitals and emergency services *(Requires Google Maps API)*
- **Safe Places** - Discover safe public places (malls, stores, etc.) *(Requires Google Maps API)*
- **Petrol Stations** - Find fuel stations along your route *(Requires Google Maps API)*
- **Real-time Navigation** - Google Maps integration for directions *(Frontend only)*
- **Distance Calculation** - Show distance from current location *(Frontend only)*
- **24/7 Availability Info** - Check if services are open *(Static data in demo)*

### 👥 Community Safety Network
- **User Chat System** - Connect with other users for safety *(Not functional in demo)*
- **Safety Reviews** - Rate and review locations for safety *(UI only)*
- **Community Ratings** - Crowd-sourced safety information *(UI only)*
- **Safety Tips** - Share and learn safety best practices *(Static content)*
- **User Profiles** - Manage personal safety information *(Basic functionality)*

### 🔐 User Authentication & Security
- **Secure Registration** - Email-based user registration *(Functional)*
- **OTP Verification** - Two-factor authentication via email *(Requires email config)*
- **Password Management** - Change and reset password functionality *(Functional)*
- **Session Management** - Secure session handling *(Functional)*
- **Profile Management** - Update personal information *(Functional)*
- **Privacy Controls** - Manage data sharing preferences *(UI only)*

### 📱 Mobile-First Design
- **Responsive Layout** - Optimized for all screen sizes *(Fully functional)*
- **Modern UI** - Pink gradient theme with smooth animations *(Fully functional)*
- **Touch-Optimized** - Large buttons for easy mobile interaction *(Fully functional)*
- **Smooth Animations** - Gradient effects and hover transitions *(Fully functional)*
- **Mobile Navigation** - Responsive navigation for mobile devices *(Fully functional)*
- **PWA Ready** - Progressive Web App capabilities *(Frontend ready)*

---

## 🛠️ Technology Stack

### Backend Technologies
```
- Python 3.8+
- Django 4.2.7 (Web Framework)
- Django REST Framework 3.14.0 (API)
- SQLite (Development Database)
- Geopy 2.4.0 (Location Services)
```

### Frontend Technologies
```
- HTML5 (Semantic Markup)
- CSS3 (Styling)
- JavaScript ES6+ (Interactivity)
- Tailwind CSS (Utility-First CSS)
- Font Awesome 6.0 (Icons)
```

### APIs & Services
```
- HTML5 Geolocation API
- MediaRecorder API (Video Recording)
- getUserMedia API (Camera Access)
- Web Speech API (Voice Alerts)
- Web Notifications API
- DeviceMotion API (Accelerometer)
- Google Maps API (Location Services)
```

---

## 📦 Installation

### Quick Demo Setup

#### Option 1: Simple Demo Server (Recommended)
```bash
# Clone repository
git clone https://github.com/VivekOrginal/SafeHer-Web-Django.git
cd SafeHer-Web-Django

# Run demo server
python demo_server.py
```

#### Option 2: Windows Batch File
```bash
# Double-click to run
START_DEMO.bat
```

#### Option 3: Static Files
Navigate to `templates` folder and open `loading.html` in your browser.

---

## ⚠️ Demo Limitations

### Removed Features (Demo Version)

❌ **Backend Features:**
- SMS alert system integration
- Real-time location tracking infrastructure
- Database operations for anonymous users
- Email notification system
- WhatsApp API integration
- Push notifications
- Advanced analytics

❌ **Security Features:**
- Production-grade encryption
- Advanced authentication
- Rate limiting
- DDoS protection

❌ **Integration Features:**
- Twilio SMS API
- Police department integration
- Hospital network integration
- Payment gateway

### Available Features (Demo Version)

✅ **Frontend Features:**
- Complete UI/UX design
- Responsive layouts
- Interactive elements
- Camera access interface
- Location services interface
- Shake detection interface
- Audio alerts interface

✅ **Basic Functionality:**
- Template rendering
- Static file serving
- URL routing
- Basic navigation

---

## 🎯 Full Version Features

### Complete Backend Implementation
- ✅ Fully functional SMS alert system
- ✅ Real-time location tracking with WebSockets
- ✅ Complete database operations
- ✅ Email notification system
- ✅ WhatsApp Business API integration
- ✅ Push notifications (FCM)
- ✅ Advanced analytics dashboard

### Production-Ready Features
- ✅ PostgreSQL database
- ✅ Redis caching
- ✅ Celery task queue
- ✅ AWS S3 storage
- ✅ CDN integration
- ✅ Load balancing
- ✅ Auto-scaling

### Security Enhancements
- ✅ SSL/TLS certificates
- ✅ Advanced encryption
- ✅ Rate limiting
- ✅ DDoS protection
- ✅ Security auditing
- ✅ Penetration testing

### Additional Features
- ✅ Multi-language support
- ✅ Offline mode
- ✅ Voice commands
- ✅ Geofencing
- ✅ Route planning
- ✅ Safety score algorithm
- ✅ Community moderation

---

## 📄 License

**Proprietary License**

© 2025 Vivek P S. All Rights Reserved.

This is a demonstration version with restricted usage:
- ❌ No commercial use
- ❌ No redistribution
- ❌ No modification
- ✅ Evaluation purposes only

See [LICENSE.md](LICENSE.md) for full terms.

---

## 📞 Contact

### Developer Information

**Vivek P S**

📧 **Email:** viveksubhash4@gmail.com  
🐙 **GitHub:** [@VivekOrginal](https://github.com/VivekOrginal)

### Purchase Full Version

Interested in the complete working project?

**What You Get:**
- ✅ Complete source code with all features
- ✅ Full backend implementation
- ✅ Production-ready deployment
- ✅ Documentation & guides
- ✅ Technical support
- ✅ Future updates
- ✅ Customization options

**Contact:** viveksubhash4@gmail.com

---

## 🙏 Acknowledgments

- Django Framework Team
- Python Community
- Open Source Contributors
- Women Safety Advocates

---

<div align="center">

**Made with 💙 for women's safety and empowerment**

© 2025 Vivek P S. All Rights Reserved.

[⬆ Back to Top](#-safeher---women-safety-platform-demo-version)

</div>