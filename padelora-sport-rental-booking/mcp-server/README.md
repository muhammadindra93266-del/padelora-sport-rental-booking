# PADELORA MCP Server

MCP server demo untuk menghubungkan AI assistant dengan data katalog, contoh jadwal, permintaan booking, dan pembuatan caption.

## Persiapan
Disarankan menggunakan Python 3.10+.

```bash
cd mcp-server
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
```

## Menjalankan
```bash
python server.py
```

Server berjalan melalui transport STDIO. Untuk menghubungkannya ke MCP host/client, daftarkan command Python dan path absolut ke `server.py` sesuai konfigurasi host yang digunakan.

Contoh konfigurasi konseptual:
```json
{
  "mcpServers": {
    "padelora": {
      "command": "python",
      "args": ["/absolute/path/to/padelora/mcp-server/server.py"]
    }
  }
}
```

## Tools
- `get_rental_catalog(category?)`
- `get_booking_schedule(venue?, booking_date?)`
- `create_booking_request(name, phone, service, booking_date, time_slot, players?, venue?, notes?)`
- `generate_ad_caption(product_or_service, audience?, platform?, tone?)`

Permintaan booking disimpan ke `data/booking_requests.json`. Ini hanya demo lokal; belum ada autentikasi, database produksi, notifikasi, pembayaran, atau integrasi ketersediaan lapangan real-time.
