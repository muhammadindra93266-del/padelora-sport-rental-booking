"""PADELORA MCP server — demo tools for rental, booking and marketing."""
import json
from pathlib import Path
from datetime import date
from mcp.server.fastmcp import FastMCP

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
DATA.mkdir(exist_ok=True)
mcp = FastMCP("padelora")

CATALOG = [
    {"id":"racket-basic","name":"Racket — Starter","category":"Raket padel","price_idr":50000,"unit":"hari","description":"Untuk pemain pemula."},
    {"id":"racket-pro","name":"Racket — Performance","category":"Raket padel","price_idr":85000,"unit":"hari","description":"Untuk latihan dan permainan reguler."},
    {"id":"padel-balls","name":"Padel Ball Set","category":"Bola padel","price_idr":25000,"unit":"set","description":"Satu set bola padel."}
]

@mcp.tool()
def get_rental_catalog(category: str = "") -> list[dict]:
    """Ambil katalog perlengkapan rental. Filter opsional berdasarkan kategori."""
    if not category:
        return CATALOG
    return [item for item in CATALOG if category.lower() in item["category"].lower()]

@mcp.tool()
def get_booking_schedule(venue: str = "", booking_date: str = "") -> dict:
    """Berikan contoh slot waktu untuk membantu pertanyaan pelanggan. Bukan data ketersediaan live."""
    slots = ["08.00–10.00","10.00–12.00","13.00–15.00","15.00–17.00","18.00–20.00","20.00–22.00"]
    return {"venue_query": venue or "Belum ditentukan", "date_query": booking_date or "Belum ditentukan",
            "example_time_slots": slots, "availability_status": "Perlu konfirmasi pengelola lapangan",
            "notice": "Slot contoh, bukan ketersediaan real-time."}

@mcp.tool()
def create_booking_request(name: str, phone: str, service: str, booking_date: str,
                           time_slot: str, players: int = 4, venue: str = "",
                           notes: str = "") -> dict:
    """Simpan permintaan booking ke file JSON lokal. Tidak mengonfirmasi reservasi."""
    if not name.strip() or not phone.strip():
        raise ValueError("Nama dan nomor WhatsApp wajib diisi.")
    try:
        date.fromisoformat(booking_date)
    except ValueError as exc:
        raise ValueError("Tanggal harus menggunakan format YYYY-MM-DD.") from exc
    if players < 1 or players > 20:
        raise ValueError("Jumlah pemain harus antara 1 dan 20.")
    DATA.mkdir(exist_ok=True)
    path = DATA / "booking_requests.json"
    records = json.loads(path.read_text(encoding="utf-8")) if path.exists() else []
    record = {"request_id": f"PAD-{len(records)+1:04d}", "name": name.strip(),
              "phone": phone.strip(), "service": service, "booking_date": booking_date,
              "time_slot": time_slot, "players": players, "venue": venue, "notes": notes,
              "status": "pending_confirmation"}
    records.append(record)
    path.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
    return {"success": True, "request": record,
            "message": "Permintaan tersimpan. Pengelola tetap harus mengonfirmasi ketersediaan."}

@mcp.tool()
def generate_ad_caption(product_or_service: str, audience: str = "pemula",
                        platform: str = "Instagram", tone: str = "friendly") -> str:
    """Buat draf caption promosi sederhana untuk media sosial."""
    return (f"Siap coba padel? 🎾 {product_or_service} dari PADELORA bikin persiapan main "
            f"lebih praktis, terutama untuk kamu yang {audience}. Yuk, mulai sesi bermainmu! "
            f"Rent. Book. Play. #PADELORA #PadelSemarang #PadelIndonesia "
            f"(Draf untuk {platform}; sesuaikan detail harga dan ketersediaan sebelum dipublikasikan.)")

if __name__ == "__main__":
    mcp.run()
