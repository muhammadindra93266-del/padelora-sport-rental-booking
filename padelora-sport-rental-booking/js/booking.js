const form = document.getElementById("booking-form");
const dateInput = form?.querySelector('input[name="date"]');
if(dateInput){
  const today = new Date();
  const localDate = new Date(today.getTime() - today.getTimezoneOffset()*60000).toISOString().slice(0,10);
  dateInput.min = localDate;
}
form?.addEventListener("submit", event => {
  event.preventDefault();
  if(!form.reportValidity()) return;
  const data = Object.fromEntries(new FormData(form).entries());
  const message = [
    "Halo PADELORA, saya ingin mengajukan permintaan booking.",
    `Nama: ${data.name}`,`WhatsApp: ${data.phone}`,`Kebutuhan: ${data.service}`,
    `Jumlah pemain: ${data.players}`,`Tanggal: ${data.date}`,`Waktu: ${data.time}`,
    `Lapangan/area: ${data.venue || "-"}`,`Catatan: ${data.notes || "-"}`
  ].join("\n");
  document.getElementById("form-feedback").textContent = "Permintaan disiapkan. WhatsApp akan terbuka untuk mengirim pesan. Booking belum terkonfirmasi sampai ada balasan dari pengelola.";
  window.open(`https://wa.me/${window.PADELORA_WHATSAPP}?text=${encodeURIComponent(message)}`,"_blank","noopener");
});
