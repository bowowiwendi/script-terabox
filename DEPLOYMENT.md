# Deployment Guide

## 🌐 Deploy to Cloud (Free Options)

### Option 1: Render (Recommended)

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

2. **Deploy on Render**
   - Go to [render.com](https://render.com)
   - Sign up / Login
   - Click **New +** → **Web Service**
   - Connect your GitHub repository
   - Configure:
     - **Name**: `terabox-downloader`
     - **Environment**: `Python 3`
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn app:app`
   - Click **Create Web Service**

3. **Free Tier Limits**
   - 512 MB RAM
   - 0.1 CPU
   - 100 GB bandwidth/month
   - Auto-sleep after 15 min inactivity

---

### Option 2: Railway

1. Go to [railway.app](https://railway.app)
2. Click **New Project** → **Deploy from GitHub**
3. Select your repository
4. Add environment variable: `PORT=5000`
5. Deploy!

---

### Option 3: Replit

1. Go to [replit.com](https://replit.com)
2. Click **Create Repl** → **Import from GitHub**
3. Select your repository
4. Click **Run**

---

### Option 4: GitHub Codespaces (For Testing)

1. Open your repository on GitHub
2. Click **Code** → **Codespaces** → **Create codespace**
3. Wait for setup
4. Run in terminal:
   ```bash
   pip install -r requirements.txt
   python app.py
   ```
5. Click the forwarded port link

---

## 🖥️ Local Development

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run Development Server
```bash
python app.py
```

Access at: `http://localhost:5000`

### Run Production Server
```bash
gunicorn app:app --bind 0.0.0.0:5000
```

---

## 📁 Project Structure

```
script-terabox/
├── app.py                 # Flask web application
├── templates/
│   └── index.html         # Web UI
├── requirements.txt       # Python dependencies
├── Procfile              # Deployment config
├── terabox_downloader.py # CLI version
└── README.md             # Documentation
```

---

## ⚙️ Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `PORT`   | `5000`  | Server port |

---

## 🔒 Security Notes

- This is a proxy downloader - files pass through the server
- For production, consider adding rate limiting
- Add authentication if deploying publicly
- Be aware of copyright laws in your region

---

## 🐛 Troubleshooting

### "Module not found" error
```bash
pip install -r requirements.txt
```

### Port already in use
```bash
# Change port
export PORT=8080
python app.py
```

### API not responding
- Check your internet connection
- The Sonzaix API might be temporarily down
- Try again later

---

## 📞 Support

API by: [Sonzai X シ](https://t.me/November2k)
