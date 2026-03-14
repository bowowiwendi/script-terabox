# 🚀 Deploy to Vercel - Static HTML

## Cara Termudah Deploy ke Vercel

### Metode 1: Drag & Drop (Paling Mudah!)

1. **Buka** [vercel.com/new](https://vercel.com/new)
2. **Login** dengan GitHub
3. **Klik** "Continue with Email" atau GitHub
4. **Drag folder** project kamu ke area deploy
5. **Done!** Website online dalam hitungan detik

URL: `https://your-project.vercel.app`

---

### Metode 2: Vercel CLI

```bash
# 1. Install Vercel CLI
npm install -g vercel

# 2. Login
vercel login

# 3. Deploy (di folder project)
vercel

# 4. Production
vercel --prod
```

---

### Metode 3: GitHub Integration (Auto Deploy)

```bash
# 1. Push ke GitHub
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/script-terabox.git
git push -u origin main
```

2. **Buka** [vercel.com/new](https://vercel.com/new)
3. **Import** dari GitHub
4. **Deploy!**

Setiap kali push ke GitHub, otomatis deploy! 🎉

---

## 📁 Struktur File

```
script-terabox/
├── index.html          # Main page ✅
├── favicon.svg         # Favicon ✅
├── vercel.json         # Vercel config ✅
└── README.md           # Documentation ✅
```

---

## ⚙️ vercel.json untuk Static HTML

File `vercel.json` sudah dikonfigurasi untuk:
- ✅ Serve file `index.html` sebagai homepage
- ✅ Cache favicon.svg (1 tahun)
- ✅ Security headers (XSS protection, clickjacking)

---

## 🌐 Custom Domain (Optional)

1. **Vercel Dashboard** → Project → Settings → Domains
2. **Add Domain**
3. **Update DNS**:
   ```
   Type: A
   Name: @
   Value: 76.76.21.21
   
   Type: CNAME
   Name: www
   Value: cname.vercel-dns.com
   ```

---

## ⚠️ CORS Note

Karena ini static HTML, API calls langsung dari browser ke Sonzaix API.

**Jika ada CORS error:**

1. **Gunakan CORS Proxy** (edit `index.html`):
   ```javascript
   const CORS_PROXY = 'https://corsproxy.io/?';
   const apiUrl = CORS_PROXY + encodeURIComponent(url);
   ```

2. **Atau deploy backend** (Flask) ke Render/Railway

---

## 📊 Vercel Free Tier

| Feature | Limit |
|---------|-------|
| Bandwidth | 100 GB/month |
| Build Minutes | 6,000 minutes |
| Domains | Unlimited |
| HTTPS | ✅ Auto SSL |
| Serverless Functions | 100 GB-hours |

---

## 🎨 Preview & Share

Setiap push ke GitHub:
- **Preview URL** untuk testing
- **Production URL** setelah merge ke main

Share link: `https://your-project.vercel.app`

---

## 🔧 Troubleshooting

### 404 Error
- Pastikan `index.html` ada di root folder
- Cek file names (case-sensitive!)

### API tidak jalan
- Cek CORS policy
- Gunakan CORS proxy jika perlu

### Favicon tidak muncul
- Clear browser cache
- Hard refresh: `Ctrl+Shift+R` / `Cmd+Shift+R`

---

## 📞 Links

- Vercel Dashboard: [vercel.com](https://vercel.com)
- Vercel Docs: [vercel.com/docs](https://vercel.com/docs)
- API by: [Sonzai X シ](https://t.me/November2k)
