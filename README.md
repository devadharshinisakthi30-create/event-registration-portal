# 🎓 Event Registration Portal

A modern, responsive Flask web application for managing student event registrations with QR code mobile access.

## ✨ Features

- 📝 **Student Registration** - Easy-to-use form for event registration
- 🎫 **Auto Enroll Numbers** - Generates unique IDs (HME001, HME002, etc.)
- 📱 **QR Code Access** - Scan QR code to access on mobile
- 👥 **Student Directory** - View all registered students in horizontal table
- 🔐 **Admin Dashboard** - Secure admin panel with statistics
- 📊 **10 IT Events** - Pre-configured events with timing and venue
- 🎨 **Modern UI** - Beautiful gradient design with animations
- 📱 **Mobile Responsive** - Works perfectly on all devices

## 🚀 Quick Start

### Local Development

```bash
# Clone repository
git clone https://github.com/yourusername/event-registration-portal.git
cd event-registration-portal

# Install dependencies
pip install -r requirements.txt

# Run application
python app.py
```

Visit: `http://127.0.0.1:5000`

### Production Deployment

See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for detailed instructions.

## 🔐 Admin Access

**Default Credentials:**
- Username: `admin`
- Password: `admin123`

⚠️ **Change these in production via environment variables!**

## 📦 Tech Stack

- **Backend:** Flask 3.0.0
- **Server:** Gunicorn (production)
- **Frontend:** HTML5, CSS3, JavaScript
- **QR Generation:** QRCode.js (CDN)

## 🌐 Deploy to Render (Recommended)

1. Push to GitHub
2. Go to [render.com](https://render.com)
3. Create new Web Service
4. Connect your GitHub repo
5. Add environment variables:
   - `SECRET_KEY`
   - `DEPLOYED_URL`
   - `ADMIN_PASSWORD`
6. Deploy!

## 🎯 Events Included

1. Web Development Workshop
2. AI & Machine Learning Seminar
3. Cybersecurity Awareness
4. Cloud Computing Basics
5. Data Science Bootcamp
6. Mobile App Development
7. Blockchain Technology
8. IoT Innovations
9. Python Programming Contest
10. UI/UX Design Workshop

## 📝 License

MIT License

---

**Made with ❤️ for event management**
