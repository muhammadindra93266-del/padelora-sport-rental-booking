# PADELORA — Sport Rental & Court Booking

**Rent. Book. Play.**  
Website konsep bisnis penyewaan perlengkapan padel dan pengajuan booking lapangan. Proyek ini dibuat sebagai starter project untuk tugas Lab Pemrograman.

## Fitur
- Landing page responsif.
- Katalog sewa raket dan bola dengan pencarian.
- Form pengajuan booking lapangan/peralatan.
- CTA WhatsApp dengan pesan otomatis.
- Halaman jadwal komunitas (data contoh).
- Halaman tentang bisnis.
- MCP server dengan tools katalog, jadwal, booking request, dan caption iklan.

## Teknologi
- HTML5, CSS3, JavaScript vanilla.
- Python dan MCP Python SDK untuk MCP server.
- Git/GitHub untuk version control.

## Menjalankan website
Tidak perlu build step atau framework.

**Opsi 1 — Python**
```bash
python -m http.server 8000
```
Buka `http://localhost:8000`.

**Opsi 2 — VS Code**
Install ekstensi Live Server, klik kanan `index.html`, lalu pilih **Open with Live Server**.

## Konfigurasi WhatsApp
Edit file `js/main.js`:
```js
window.PADELORA_WHATSAPP = "6281234567890";
```
Ganti dengan nomor WhatsApp bisnis dalam format internasional tanpa `+`, spasi, atau tanda baca. Nomor saat ini adalah placeholder.

## Data demo yang wajib diperbarui
Harga rental, foto, jadwal, nama venue, dan nomor WhatsApp adalah contoh awal. Perbarui berdasarkan hasil validasi dan kerja sama nyata sebelum website dipublikasikan sebagai layanan komersial. Booking dari website membuka WhatsApp dan belum memeriksa ketersediaan lapangan secara otomatis.

## Menjalankan MCP server
Lihat [`mcp-server/README.md`](mcp-server/README.md). MCP server berjalan terpisah dari website statis.

## Struktur repository
```text
padelora-sport-rental-booking/
├── index.html
├── rental.html
├── booking.html
├── schedule.html
├── about.html
├── css/style.css
├── js/
│   ├── main.js
│   ├── rental.js
│   └── booking.js
├── mcp-server/
│   ├── server.py
│   ├── requirements.txt
│   └── README.md
├── .github/workflows/
│   └── pages.yml
├── .gitignore
└── LICENSE
```

## Upload ke GitHub
1. Buat repository baru bernama `padelora-sport-rental-booking`.
2. Extract ZIP project ini.
3. Buka terminal di folder hasil extract.
4. Jalankan:
```bash
git init
git add .
git commit -m "Initial commit: PADELORA website and MCP server"
git branch -M main
git remote add origin https://github.com/USERNAME/padelora-sport-rental-booking.git
git push -u origin main
```
Ganti `USERNAME` dengan username GitHub milikmu.

## GitHub Pages
Repository sudah dilengkapi workflow deploy otomatis. Di GitHub, buka **Settings → Pages**, pilih **GitHub Actions** sebagai Build and deployment source. Setelah push ke branch `main`, website akan dideploy oleh workflow.

## Kolaborasi tim
Buka **Settings → Collaborators** pada repository, lalu undang email GitHub anggota tim/dosen yang diminta. Gunakan branch dan pull request agar kontribusi setiap orang tercatat. Jangan membagikan token atau password GitHub.

## Ide pengembangan berikutnya
- Backend API dan database.
- Dashboard admin untuk mengelola inventaris.
- Integrasi kalender/ketersediaan venue.
- Login pengguna dan riwayat transaksi.
- Payment gateway.
- Integrasi WhatsApp Business API.
- MCP dengan penyimpanan database dan otorisasi.

## Catatan akademik
PADELORA pada repository ini adalah prototipe akademik. Data katalog, harga, jadwal, dan venue bersifat dummy/contoh, bukan penawaran komersial atau konfirmasi booking yang sesungguhnya.
