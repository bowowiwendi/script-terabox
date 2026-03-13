# Universal Media Downloader

Download from **TeraBox**, **YouTube**, **TikTok**, **Facebook** & **Instagram** using Sonzaix API. Available in **CLI** and **Web** versions.

## 🚀 Features

| Platform | Video | Audio | Quality Options |
|----------|-------|-------|-----------------|
| **TeraBox** | ✅ | ✅ | Original |
| **YouTube** | ✅ | ✅ | 144p - 1080p / 128-320kbps |
| **TikTok** | ✅ | ✅ | HD/SD (No Watermark) |
| **Facebook** | ✅ | ❌ | HD/SD |
| **Instagram** | ✅ | ❌ | Original |

### General Features
- 🎯 CLI & Web interface
- 🔐 Password-protected link support (TeraBox)
- 📊 Download progress indicator
- 📥 Single or batch download
- 🌐 Browser-based UI (static HTML)
- ☁️ Deploy to GitHub Pages (FREE!)

---

## 🌐 Web Version - GitHub Pages (No Server Needed!)

### Deploy in 3 Steps:

1. **Push ke GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

2. **Aktifkan GitHub Pages**
   - Buka repository di GitHub
   - **Settings** → **Pages**
   - Source: **GitHub Actions**

3. **Done!** Akses di `https://<username>.github.io/<repo>/`

### File: `index.html`
- ✅ Pure HTML + CSS + JavaScript
- ✅ No backend server
- ✅ Gratis selamanya
- ✅ Auto-deploy dengan GitHub Actions

---

## 💻 Web Version (Flask - Local/Cloud)

```bash
pip install -r requirements.txt
python app.py
```

Access at: `http://localhost:5000`

---

## 🖥️ CLI Version

```bash
python terabox_downloader.py
```

### Menu Options

1. **Download from TeraBox URL** - Enter a TeraBox sharing link
2. **Exit** - Close the application

### URL Format

You can paste the URL in these formats:

- With password: `https://www.terabox.app/indonesian/sharing/init?surl=xxx&pwd=xxx`
- Without password: `https://www.terabox.app/indonesian/sharing/init?surl=xxx`

The script will automatically detect and extract the password if included in the URL.

## Example

```
╔════════════════════════════════════════╗
║       TeraBox Downloader CLI           ║
║       Powered by Sonzaix API           ║
╚════════════════════════════════════════╝

  Main Menu
  ----------------------------------------
  1. Download from TeraBox URL
  2. Exit
  ----------------------------------------

  Select option (1-2): 1

  Enter TeraBox URL (with optional &pwd=xxx):
  > https://www.terabox.app/indonesian/sharing/init?surl=9prdldSgkoo6rOrwnPYgVA&pwd=j04k

  ⏳ Fetching download information...

  ==================================================
  📁 FILE INFORMATION
  ==================================================
    Source       : TeraBox
    Status       : success
    Total Files  : 1
    Is Private   : True
  ==================================================

  📋 AVAILABLE FILES:
  --------------------------------------------------
    [1] Grok_1.1.38-release.31_Mod_Premium√[Rolling Hunters].apk
        Size: 82.99 MB

  📥 Downloading: Grok_1.1.38-release.31_Mod_Premium√[Rolling Hunters].apk
     Size: 82.99 MB
     Progress: [██████████████████████████████████████████████████] 100.0%
     ✅ Download complete!
```

## API Credit

- API Provider: [Sonzai X シ](https://t.me/November2k)
- API Endpoint: `https://api.sonzaix.indevs.in/terabox`

## License

This script is for educational purposes only.
