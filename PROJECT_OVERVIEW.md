# SafeHer - Women Safety Platform

## 🌟 Project Overview

SafeHer is a comprehensive women safety web application designed to provide real-time emergency assistance, incident reporting, and community safety features. The platform enables women to record video evidence, send automatic location-based alerts, and connect with safety networks.

## 🎯 Core Mission
**"Empowering women with technology for instant safety and protection"**

---

## 🛠️ Technology Stack

### Backend
- **Framework**: Django 4.2.7 (Python)
- **Database**: SQLite (Development) / PostgreSQL (Production)
- **API**: Django REST Framework 3.14.0
- **Authentication**: Django Auth System
- **File Storage**: Django File Handling
- **Location Services**: Geopy 2.4.0

### Frontend
- **Framework**: HTML5, CSS3, JavaScript (ES6+)
- **Styling**: Tailwind CSS (CDN)
- **Icons**: Font Awesome 6.0
- **Responsive Design**: Mobile-first approach
- **PWA Ready**: Service Worker compatible

### APIs & Services
- **Geolocation**: HTML5 Geolocation API
- **Media**: MediaRecorder API, getUserMedia API
- **SMS Integration**: SMS URL Scheme
- **WhatsApp**: WhatsApp Business API
- **Speech**: Web Speech API
- **Notifications**: Web Notifications API

### Security & Privacy
- **HTTPS**: SSL/TLS encryption
- **CORS**: Cross-Origin Resource Sharing
- **CSRF**: Cross-Site Request Forgery protection
- **Data Privacy**: Local storage for sensitive data

---

## 🏗️ Project Architecture

```
SafeHer/
├── women_safety_platform/     # Main Django project
│   ├── settings.py           # Configuration
│   ├── urls.py              # URL routing
│   └── wsgi.py              # WSGI application
├── users/                   # User management
│   ├── models.py           # User, PoliceStation, Officer
│   └── views.py            # Authentication views
├── reports/                 # Incident reporting
│   ├── models.py           # IncidentReport
│   ├── views.py            # Video upload, SMS alerts
│   └── urls.py             # Report endpoints
├── emergency/               # SOS functionality
│   ├── models.py           # SOSAlert, LiveTracking
│   ├── views.py            # Emergency triggers
│   └── urls.py             # Emergency endpoints
├── safety/                  # Community features
│   ├── models.py           # SafetyZone, SafetyBuddy
│   └── views.py            # Community functions
├── templates/               # HTML templates
│   ├── base/               # Base template
│   ├── reports/            # Incident pages
│   ├── emergency/          # SOS pages
│   └── safety/             # Community pages
└── media/                   # Uploaded files
```

---

## ⚡ Key Features

### 1. 📹 **Incident Reporting System**
- **Real-time video recording** using device camera
- **Automatic location capture** via GPS
- **Evidence storage** on device
- **Police station detection** (nearest station)
- **SMS alerts** with Google Maps links
- **WhatsApp sharing** for evidence distribution

### 2. 🚨 **Emergency SOS System**
- **One-tap SOS button** for instant alerts
- **Loud siren sounds** + voice alerts
- **Phone vibration** patterns
- **Live location tracking** (updates every 5 seconds)
- **Automatic SMS** to emergency contacts
- **Volume maximization** for emergency sounds

### 3. 👥 **Safety Community Features**
- **Safety buddy finder** - Connect with nearby women
- **Real-time location sharing** with trusted contacts
- **Safety groups** for regular routes
- **Emergency contact network** management
- **Anonymous tip reporting** system

### 4. 🎨 **Modern UI/UX**
- **Mobile-first responsive design**
- **Pink/white feminine color scheme**
- **Gradient animations** and hover effects
- **Empowering quotes** and messaging
- **Intuitive navigation** with large touch targets

### 5. 🔧 **Customization Options**
- **Custom emergency numbers** (3-15 digits)
- **Personal safety contacts** management
- **Notification preferences**
- **Privacy settings**

---

## 📱 Core Functionality Workflow

### Incident Reporting Flow:
1. User opens `/report/` page
2. Browser requests camera + location permissions
3. User records video evidence
4. Video automatically downloads to device
5. Location captured via GPS
6. SMS app opens with pre-filled emergency message
7. User taps "Send" to alert emergency contact
8. Report stored in database with police station info

### SOS Emergency Flow:
1. User taps SOS button on `/sos/` page
2. Loud siren + voice alert plays
3. Phone vibrates in emergency pattern
4. GPS location captured
5. SMS app opens with emergency message
6. Live tracking starts (5-second updates)
7. Emergency contacts receive location link

### Safety Community Flow:
1. User accesses `/safety/` page
2. Find nearby safety buddies
3. Join or create safety groups
4. Share live location with trusted contacts
5. Submit anonymous tips about unsafe areas

---

## 🔐 Security Features

### Data Protection:
- **Local storage** for emergency contacts
- **No server storage** of personal videos
- **HTTPS encryption** for all communications
- **CSRF protection** on all forms

### Privacy Controls:
- **Anonymous reporting** options
- **No tracking** without explicit consent
- **Local data storage** (not cloud-based)
- **User-controlled** data sharing

---

## 📊 Database Schema

### Users App:
```python
User (Custom):
- username, email, phone
- emergency_contact1, emergency_contact2
- address, is_police

PoliceStation:
- name, phone, latitude, longitude
- address, is_online, response_time, safety_rating

Officer:
- name, badge_number, station
- photo, is_available
```

### Reports App:
```python
IncidentReport:
- reporter (User), video_file
- latitude, longitude, description
- timestamp, status, police_station
```

### Emergency App:
```python
SOSAlert:
- user, latitude, longitude
- timestamp, is_active, audio_file

LiveTracking:
- sos_alert, latitude, longitude, timestamp
```

### Safety App:
```python
SafetyZone:
- name, latitude, longitude, radius
- safety_level, incident_count

SafetyBuddy:
- user, buddy, is_active, created_at

AnonymousTip:
- location_lat, location_lng
- description, tip_type, verified
```

---

## 🚀 Installation & Setup

### Prerequisites:
```bash
- Python 3.8+
- pip (Python package manager)
- Modern web browser (Chrome/Safari recommended)
```

### Step 1: Clone & Setup
```bash
cd c:\Users\ASUS\Desktop\safety
pip install -r requirements.txt
```

### Step 2: Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### Step 3: Add Sample Data
```bash
python add_sample_data.py
```

### Step 4: Run Development Server
```bash
python manage.py runserver 0.0.0.0:8000
```

### Step 5: Access Application
- **Local**: http://127.0.0.1:8000/
- **Mobile**: Use ngrok for HTTPS (required for camera access)

---

## 📱 Mobile Setup (HTTPS Required)

### Option 1: Ngrok (Recommended)
```bash
# Download ngrok from https://ngrok.com/
# Add auth token:
.\ngrok config add-authtoken YOUR_TOKEN

# Run tunnel:
.\ngrok http 8000

# Use the https://xxx.ngrok.io URL on mobile
```

### Option 2: Localtunnel
```bash
npm install -g localtunnel
lt --port 8000 --local-host 127.0.0.1

# Use the https://xxx.loca.lt URL on mobile
```

---

## 🌐 URL Structure

```
/ (Home)                    - Landing page with main features
/report/                    - Incident reporting with video
/sos/                       - Emergency SOS system
/safety/                    - Community safety features
/admin/                     - Django admin panel

API Endpoints:
/api/upload-incident/       - Video upload & SMS trigger
/api/trigger-sos/           - SOS activation
/api/update-location/       - Live tracking updates
/api/police-map/            - Nearby police stations
/api/find-buddy/            - Safety buddy finder
/api/submit-tip/            - Anonymous tip submission
```

---

## 📋 Features Checklist

### ✅ Implemented Features:
- [x] Video recording with back camera
- [x] Automatic location capture
- [x] SMS alerts with location links
- [x] WhatsApp evidence sharing
- [x] SOS button with siren + voice alerts
- [x] Live location tracking
- [x] Custom emergency numbers (3-15 digits)
- [x] Police station detection
- [x] Safety buddy system
- [x] Anonymous tip reporting
- [x] Responsive mobile design
- [x] Modern UI with animations

### 🔄 Future Enhancements:
- [ ] AI harassment detection
- [ ] Face recognition for repeat offenders
- [ ] Push notifications
- [ ] Offline mode support
- [ ] Multi-language support
- [ ] Advanced analytics dashboard
- [ ] Integration with local police systems

---

## 🎯 Target Users

### Primary Users:
- **Women of all ages** seeking personal safety
- **Students** commuting to colleges/universities
- **Working professionals** traveling alone
- **Tourists** in unfamiliar areas

### Secondary Users:
- **Police departments** for incident management
- **Safety organizations** for community building
- **Family members** for peace of mind

---

## 📈 Impact & Benefits

### For Women:
- **Instant emergency response** capability
- **Evidence collection** for legal proceedings
- **Community support** network
- **Confidence boost** in daily activities

### For Society:
- **Crime deterrent** effect
- **Faster police response** times
- **Community awareness** of unsafe areas
- **Data-driven safety** improvements

---

## 🔧 Troubleshooting

### Common Issues:

**Camera not working:**
- Ensure HTTPS connection
- Allow camera permissions in browser
- Use Chrome or Safari browser
- Check if camera is being used by another app

**Location not detected:**
- Enable location services on device
- Allow location permissions in browser
- Ensure GPS is enabled
- Try refreshing the page

**SMS not sending:**
- Check if SMS app is installed
- Verify phone number format
- Ensure device has SMS capability
- Try different browser

---

## 📞 Support & Contact

### Technical Support:
- Check browser console for errors
- Ensure all permissions are granted
- Verify HTTPS connection for mobile
- Clear browser cache if issues persist

### Emergency Contacts:
- **Police**: 100 (India), 911 (USA)
- **Ambulance**: 108 (India), 911 (USA)
- **Women Helpline**: 1091 (India)

---

## 📄 License & Legal

### Privacy Policy:
- No personal data stored on servers
- Videos stored locally on user device
- Location data used only for emergency alerts
- User controls all data sharing

### Terms of Use:
- Platform for emergency assistance only
- Users responsible for appropriate usage
- No guarantee of response times
- Compliance with local laws required

---

## 🎉 Conclusion

SafeHer represents a comprehensive approach to women's safety using modern web technologies. The platform combines real-time emergency response, evidence collection, and community support to create a powerful safety ecosystem.

**Key Strengths:**
- **Immediate response** capability
- **Evidence preservation** for legal use
- **Community-driven** safety network
- **Privacy-focused** design
- **Mobile-optimized** experience

**Ready for deployment** with proper HTTPS setup and can scale to serve thousands of users while maintaining privacy and security standards.

---

*Built with ❤️ for women's safety and empowerment*