# 🚀 Setup GitHub Pages

## Cara Deploy ke GitHub Pages (GRATIS!)

### Langkah 1: Push ke GitHub

```bash
# Inisialisasi git
git init

# Tambahkan semua file
git add .

# Commit pertama
git commit -m "Initial commit - Universal Media Downloader"

# Buat branch main
git branch -M main

# Tambahkan remote repository (ganti dengan URL GitHub kamu)
git remote add origin https://github.com/YOUR_USERNAME/script-terabox.git

# Push ke GitHub
git push -u origin main
```

---

### Langkah 2: Konfigurasi GitHub Pages

1. **Buka repository** di GitHub
2. Klik tab **Settings**
3. Scroll ke **Pages** (di sidebar kiri)
4. Di bagian **Build and deployment**:
   - **Source**: Pilih `GitHub Actions`
5. Klik **Save** (jika perlu)

---

### Langkah 3: Tunggu Deployment

1. Klik tab **Actions** di repository
2. Workflow "Deploy to GitHub Pages" akan berjalan otomatis
3. Tunggu sampai statusnya ✅ (hijau)
4. URL website kamu akan muncul di bagian Pages

**URL format:**
```
https://YOUR_USERNAME.github.io/script-terabox/
```

---

### Langkah 4: Update Website

Setiap kali kamu update `index.html`:

```bash
git add index.html
git commit -m "Update UI"
git push
```

GitHub Actions akan auto-deploy! 🎉

---

## ⚠️ Catatan Penting

### CORS Issue

API Sonzaix mungkin memblokir request langsung dari browser karena CORS. Jika terjadi error:

**Solusi 1: Gunakan Flask Version**
```bash
python app.py
```

**Solusi 2: Deploy Flask ke Cloud**
- Render: [render.com](https://render.com)
- Railway: [railway.app](https://railway.app)

**Solusi 3: Gunakan CORS Proxy** (untuk development)
Edit `index.html`, tambahkan CORS proxy di awal script:
```javascript
const CORS_PROXY = 'https://corsproxy.io/?';
// Lalu gunakan untuk setiap fetch
const apiUrl = CORS_PROXY + encodeURIComponent(`${API_URL}?url=...`);
```

---

## 📁 Struktur File

```
script-terabox/
├── index.html              # Static web (GitHub Pages) - ALL IN ONE
├── .github/
│   └── workflows/
│       ├── pages.yml       # Auto-deploy GitHub Pages
│       └── deploy.yml      # Deploy ke Render
├── app.py                  # Flask server (opsional)
├── templates/
│   └── index.html          # Flask UI (backup)
├── requirements.txt        # Python dependencies
├── terabox_downloader.py   # CLI version (TeraBox only)
├── README.md               # Dokumentasi utama
└── GITHUB_PAGES_SETUP.md   # Panduan deploy GitHub Pages
```

---

## 🎨 Fitur Web UI

### Platform yang Didukung:
- ✅ **TeraBox** - Download files dengan password support
- ✅ **YouTube** - Video (144p-1080p) & Audio (128-320kbps)
- ✅ **TikTok** - HD/SD tanpa watermark + audio
- ✅ **Facebook** - HD/SD quality
- ✅ **Instagram** - Reels & videos

### Features:
- ✅ Modern dark theme
- ✅ Responsive (mobile friendly)
- ✅ Tab navigation untuk setiap platform
- ✅ Auto-detect password dari URL (TeraBox)
- ✅ Download langsung atau direct link
- ✅ Quality selection (YouTube, Facebook)
- ✅ Stats display (TikTok, Instagram)
- ✅ Thumbnail preview
- ✅ Loading indicator
- ✅ Error handling

---

## 🔧 Troubleshooting

### "Failed to fetch files"

**Penyebab:** CORS restriction dari API

**Solusi:**
1. Gunakan Flask version (`app.py`)
2. Deploy Flask ke Render/Railway
3. Atau gunakan CORS proxy

### GitHub Pages 404

**Solusi:**
1. Pastikan file `index.html` ada di root
2. Cek Actions tab untuk error
3. Tunggu 1-2 menit setelah push

### Website tidak update

**Solusi:**
```bash
# Force refresh browser
Ctrl + Shift + R (Windows)
Cmd + Shift + R (Mac)

# Atau clear cache
```

---

## 📺 Platform Endpoints

| Platform | Endpoint | Response |
|----------|----------|----------|
| TeraBox | `/terabox?url=xxx&pwd=xxx` | Files list dengan download link |
| YouTube Video | `/youtube/video?url=xxx` | Qualities: 144p-1080p |
| YouTube Music | `/youtube/music?url=xxx` | Qualities: 128kbps, 320kbps |
| TikTok | `/sosmed/tiktok?url=xxx` | HD, SD, WM play + audio |
| Facebook | `/sosmed/facebook?url=xxx` | HD, SD video |
| Instagram | `/sosmed/instagram?url=xxx` | Video URL |

---

## 📞 Support

API by: [Sonzai X シ](https://t.me/November2k)

Untuk pertanyaan deployment, lihat [DEPLOYMENT.md](DEPLOYMENT.md)
