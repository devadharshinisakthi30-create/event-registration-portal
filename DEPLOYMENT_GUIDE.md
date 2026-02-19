# 🚀 Deployment Guide - Event Registration Portal

## ✅ Production Ready Features

This version is ready for deployment on GitHub and hosting platforms:
- ✅ No ngrok dependency
- ✅ Gunicorn WSGI server
- ✅ Environment variables support
- ✅ Production configuration
- ✅ GitHub push ready

---

## 📦 What's Included

### Core Files:
- `app.py` - Clean Flask application (no ngrok)
- `requirements.txt` - Production dependencies (Flask, gunicorn)
- `Procfile` - For Heroku/Render deployment
- `runtime.txt` - Python version specification
- `.gitignore` - Git ignore rules

### Configuration:
- Environment variable support
- Production secret key handling
- Dynamic port binding
- Debug mode control

---

## 🌐 Deployment Options

### Option 1: Render (Recommended - Free Tier)

**Steps:**
1. Push code to GitHub
2. Go to [render.com](https://render.com)
3. Create new "Web Service"
4. Connect your GitHub repo
5. Set:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
6. Add environment variables:
   ```
   SECRET_KEY=your-random-secret-key-here
   DEPLOYED_URL=https://your-app.onrender.com
   ADMIN_USERNAME=admin
   ADMIN_PASSWORD=your-secure-password
   ```
7. Deploy!

**Your app will be at:** `https://your-app.onrender.com`

---

### Option 2: Railway

**Steps:**
1. Push code to GitHub
2. Go to [railway.app](https://railway.app)
3. Click "New Project"
4. Select "Deploy from GitHub repo"
5. Choose your repository
6. Railway auto-detects Flask and deploys
7. Add environment variables in Settings:
   ```
   SECRET_KEY=your-random-secret-key
   DEPLOYED_URL=https://your-app.up.railway.app
   ```

**Your app will be at:** `https://your-app.up.railway.app`

---

### Option 3: Heroku

**Steps:**
1. Install Heroku CLI
2. Login: `heroku login`
3. Create app: `heroku create your-app-name`
4. Push: `git push heroku main`
5. Set environment variables:
   ```bash
   heroku config:set SECRET_KEY=your-secret-key
   heroku config:set DEPLOYED_URL=https://your-app.herokuapp.com
   heroku config:set ADMIN_USERNAME=admin
   heroku config:set ADMIN_PASSWORD=your-password
   ```

**Your app will be at:** `https://your-app.herokuapp.com`

---

### Option 4: Vercel (Serverless)

**Steps:**
1. Install Vercel CLI: `npm i -g vercel`
2. Run: `vercel`
3. Follow prompts
4. Add environment variables in Vercel dashboard

---

## 📁 GitHub Setup

### 1. Create Repository

```bash
# Initialize git (if not already)
git init

# Add files
git add .

# Commit
git commit -m "Initial commit: Event Registration Portal"

# Create repo on GitHub, then:
git remote add origin https://github.com/yourusername/event-registration.git

# Push
git push -u origin main
```

### 2. Repository Structure

```
event-registration-portal/
├── app.py                  ← Main application
├── requirements.txt        ← Dependencies
├── Procfile               ← Deployment config
├── runtime.txt            ← Python version
├── .gitignore             ← Git ignore rules
├── README.md              ← Documentation
├── templates/             ← HTML templates
│   ├── index.html
│   ├── success.html
│   ├── registered_students.html
│   ├── admin_login.html
│   ├── admin_dashboard.html
│   └── test.html
└── static/                ← Static files
    ├── css/
    │   └── style.css
    └── js/
        └── script.js
```

---

## 🔐 Environment Variables

### Required Variables:

```bash
# Production secret key (generate with: python -c "import secrets; print(secrets.token_hex(32))")
SECRET_KEY=your-64-character-random-string

# Your deployed URL (for QR code generation)
DEPLOYED_URL=https://your-app.render.com

# Admin credentials (change defaults!)
ADMIN_USERNAME=admin
ADMIN_PASSWORD=your-secure-password-here
```

### How to Set:

**Render:**
- Dashboard → Environment → Add Variable

**Railway:**
- Project → Variables → New Variable

**Heroku:**
```bash
heroku config:set SECRET_KEY=xxx
heroku config:set DEPLOYED_URL=https://xxx.herokuapp.com
```

---

## 🧪 Testing Deployed App

1. **Visit your URL:** `https://your-app.render.com`
2. **Register a student**
3. **Check success page** → Shows name + HME001
4. **View registered students** → Shows horizontal table
5. **Login to admin** → Use your credentials
6. **Test QR code** → Should show your deployed URL

---

## 📱 QR Code Behavior

### Local Development:
- QR shows: `http://127.0.0.1:5000` or local IP
- Works on same WiFi only

### Production Deployment:
- QR shows: `https://your-app.render.com`
- **Works on ANY network** (mobile data, any WiFi)
- **Globally accessible**

---

## 🔧 Local Development

### Setup:
```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
python app.py
```

### Access:
- Local: `http://127.0.0.1:5000`
- Network: `http://192.168.x.x:5000`

---

## ⚡ Quick Start Commands

### For GitHub:
```bash
git init
git add .
git commit -m "Event Registration Portal"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

### For Render (after GitHub push):
1. Go to render.com
2. New Web Service
3. Connect repo
4. Deploy automatically

### For Railway:
```bash
# Install Railway CLI (optional)
npm i -g @railway/cli

# Or just use web interface:
# railway.app → New Project → Deploy from GitHub
```

---

## 🎯 Production Checklist

Before deploying:

- [ ] Change `SECRET_KEY` to random value
- [ ] Change `ADMIN_PASSWORD` from default
- [ ] Set `DEPLOYED_URL` environment variable
- [ ] Test locally first
- [ ] Review `.gitignore` file
- [ ] Update README with your info
- [ ] Add repository description on GitHub
- [ ] Test deployed app thoroughly

---

## 🐛 Troubleshooting

### App won't start on Render:
- Check build logs
- Verify `requirements.txt` is correct
- Ensure `Procfile` exists: `web: gunicorn app:app`

### QR code shows wrong URL:
- Set `DEPLOYED_URL` environment variable
- Format: `https://your-app.render.com` (no trailing slash)

### Admin login not working:
- Check `ADMIN_USERNAME` and `ADMIN_PASSWORD` env vars
- Default is admin/admin123 if not set

### Static files not loading:
- Ensure `static/` folder structure is correct
- Check Flask is serving static files properly

---

## 📊 Comparison

| Feature | Local (ngrok) | Production Deployment |
|---------|--------------|----------------------|
| Setup | Quick | One-time setup |
| Cost | Free | Free tier available |
| Uptime | While running | 24/7 |
| URL | Changes each run | Permanent |
| Mobile data | ✅ (with ngrok) | ✅ Always |
| GitHub | Not needed | Required |
| Scalability | Limited | Auto-scaling |

---

## 🎓 Recommended: Render

**Why Render?**
- ✅ Free tier (750 hours/month)
- ✅ Easy GitHub integration
- ✅ Auto-deploy on push
- ✅ Built-in SSL (HTTPS)
- ✅ No credit card required
- ✅ Simple environment variables
- ✅ Logs and monitoring included

**Setup Time:** 5 minutes  
**Cost:** Free  
**Result:** Permanent, globally accessible URL

---

## 🚀 Next Steps

1. **Push to GitHub** (see commands above)
2. **Deploy on Render** (easiest option)
3. **Set environment variables**
4. **Test your deployed app**
5. **Share your QR code!**

Your event registration portal will be live and accessible from anywhere! 🌍

---

**Questions?**
- Check deployment platform documentation
- Review Flask deployment guides
- Test locally before deploying

**Status:** ✅ Ready for Production Deployment!
