const products = [
  {id:"racket-basic",name:"Racket — Starter",category:"Raket padel",price:50000,unit:"hari",emoji:"🎾",image:"https://images.unsplash.com/photo-1622279457486-62dcc4a431d6?auto=format&fit=crop&w=700&q=80",description:"Pilihan untuk pemain yang baru mulai mencoba padel."},
  {id:"racket-pro",name:"Racket — Performance",category:"Raket padel",price:85000,unit:"hari",emoji:"🏓",image:"https://images.unsplash.com/photo-1554068865-24cecd4e34b8?auto=format&fit=crop&w=700&q=80",description:"Opsi raket untuk sesi latihan dan permainan reguler."},
  {id:"padel-balls",name:"Padel Ball Set",category:"Bola padel",price:25000,unit:"set",emoji:"🟡",image:"",description:"Satu set bola untuk melengkapi sesi bermain."}
];
const grid = document.getElementById("product-grid");
const search = document.getElementById("rental-search");
const rupiah = n => new Intl.NumberFormat("id-ID",{style:"currency",currency:"IDR",maximumFractionDigits:0}).format(n);
function renderProducts(term=""){
  if(!grid) return;
  const filtered = products.filter(p => (p.name+" "+p.category+" "+p.description).toLowerCase().includes(term.toLowerCase()));
  grid.innerHTML = filtered.length ? filtered.map(p => `<article class="product-card"><div class="product-image">${p.image ? `<img src="${p.image}" alt="${p.name}" loading="lazy">` : `<span class="product-emoji">${p.emoji}</span>`}</div><div class="product-info"><span class="eyebrow">${p.category}</span><h3>${p.name}</h3><p>${p.description}</p><div class="product-bottom"><span class="price">${rupiah(p.price)} <small>/ ${p.unit}</small></span><button class="mini-btn" data-rent="${p.id}">Sewa ↗</button></div></div></article>`).join("") : "<p>Perlengkapan tidak ditemukan.</p>";
  grid.querySelectorAll("[data-rent]").forEach(btn => btn.addEventListener("click", () => {
    const p = products.find(x => x.id === btn.dataset.rent);
    const message = `Halo PADELORA, saya tertarik menyewa ${p.name}. Mohon informasi ketersediaan dan cara pemesanannya.`;
    window.open(`https://wa.me/${window.PADELORA_WHATSAPP}?text=${encodeURIComponent(message)}`,"_blank","noopener");
  }));
}
if(search) search.addEventListener("input", e => renderProducts(e.target.value));
renderProducts();
