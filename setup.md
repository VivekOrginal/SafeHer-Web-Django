# Women Safety Platform Setup

## 🚀 Quick Start

1. **Install Dependencies**
```bash
pip install -r requirements.txt
```

2. **Run Migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

3. **Create Superuser**
```bash
python manage.py createsuperuser
```

4. **Add Police Stations (Admin Panel)**
- Go to http://localhost:8000/admin/
- Add police stations with coordinates

5. **Run Server**
```bash
python manage.py runserver
```

## 📱 Features Implemented

✅ **Video Recording & Upload**
- Real-time video recording
- Automatic location capture
- Nearest police station detection

✅ **SOS Emergency System**
- One-tap SOS button
- Live location tracking
- Shareable tracking URL

✅ **Safety Features**
- Fake call simulation
- Voice command detection ("help me", "save me")

## 🔧 Next Steps to Add

1. **SMS/Email Alerts** - Integrate Twilio
2. **Face Detection** - Add OpenCV processing
3. **Police Dashboard** - Create admin interface
4. **Mobile App** - Convert to PWA or React Native
5. **Route Safety Scoring** - Add Google Maps integration

## 🌐 URLs

- Home/Report: http://localhost:8000/
- SOS Emergency: http://localhost:8000/sos/
- Admin Panel: http://localhost:8000/admin/