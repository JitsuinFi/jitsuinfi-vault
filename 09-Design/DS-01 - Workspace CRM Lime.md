---
tags: [design-ref, "DS-01"]
type: design-ref
id: DS-01
source_file: 20c32c7a4a04e0a26a0ea26ae1a6b8e0.jpg
kind: dashboard-app
mode: operate
updated: 2026-10-20
---

# DS-01 - Workspace CRM Lime

> **Peta link:** [[DS-00 - Peta Visual Design|Peta visual]] · [[09 - Design|Hub modul]] · [[DS-PAL - Palet Utama JitsuinFi|Palet utama]]

![DS-01](20c32c7a4a04e0a26a0ea26ae1a6b8e0.jpg)

## 1. Identitas
| | |
|---|---|
| File | `09-Design/20c32c7a4a04e0a26a0ea26ae1a6b8e0.jpg`, 1024×768 |
| Jenis | Shot konsep dashboard CRM penjualan (gaya Dribbble), di atas latar abu-abu presentasi; bukan produk yang bisa dicek |
| Sumber atau pembuat | Tidak tercantum di file |
| Mode (istilah impeccable) | **Operate**: pengguna menyelesaikan tugas harian |

## 2. Yang terlihat (apa adanya)
- **Bar jadwal** pill hitam di atas: "Your Schedule", chip tanggal "28 March", garis waktu dengan segmen lime dan jarum "2:15 pm", avatar peserta, tombol panah.
- **Judul** "WORKSPACE" kapital besar; huruf O diganti lingkaran lime. Tombol pill hitam "+ New Task". KPI: **34** Deals (lencana hijau +3), **20** won (lencana merah), **3** lost (lencana merah).
- **New Leads (7 Leads)**: chip filter (search, pengaturan, All aktif putih, Hot Client dengan ikon api, Great, Medium, Low, Non interest), lalu baris kartu orang: foto, nama, jabatan, chip sumber (LinkedIn, Email, Facebook, Typeform), titik warna minat, tombol panah di sudut kanan atas yang "menggigit" kartu.
- **Rel ikon kiri**: tombol lingkaran vertikal.
- **Jendela video call** mengambang (Google Meet): wajah pria, tombol kamera, mikrofon, speaker, tutup merah.
- **Panel gelap "Summary"** di kanan: timeline vertikal (3:15, 2:46), "Documents" dengan dua thumbnail (Brief, Requirements), "Goal:" dengan kata tebal "incidents by 50%".
- **Your Days Tasks (16 Tasks)**: filter All, Hot, Due Today, Overdue, Completed. Kartu tugas: satu lime (aktif: Google Meet Call, 28.03.2023 at 2 pm, status "Call scheduled"), sisanya putih ("Send Proposal", $20.000, "Waiting Proposal").
- Baris kartu terpotong di tepi kanan: tersirat **gulir horizontal**.

## 3. Style
- **Monokrom abu-abu + satu aksen neon lime + hitam sebagai warna perintah.** Pola SaaS Dribbble 2023 – 2024.
- **Semua serba pill dan radius besar** (±20 – 28 px pada kartu, 999 px pada chip dan tombol).
- **Kartu bertakik** (inverted corner): sudut kanan atas dipotong untuk tombol lingkaran. Ini ciri paling khas gambar ini.
- Hampir tanpa bayangan; kedalaman datang dari **tumpukan** (video dan panel gelap menimpa grid) dan kontras terang-gelap.

## 4. POV dan komposisi
- **Kamera:** tampak depan, datar (orthografis), tanpa mockup perangkat. Penonton = pengguna yang duduk di depan layar.
- **Urutan baca:** pola Z dari bar jadwal → judul dan KPI → baris leads → baris tugas; panel kanan = konteks kedua.
- **Hierarki:** angka KPI dan judul paling besar; lime hanya di "sekarang" (jarum waktu, tugas aktif).
- **Lapisan:** grid dasar terang, lalu overlay (video, panel gelap) yang keluar dari grid di sisi kanan.

## 5. Makna
- **Hari kerja sebagai garis waktu.** Jarum "sekarang" di atas dan tugas aktif lime menyatakan "ini yang harus dikerjakan sekarang".
- **Lime = hidup, aktif, jalan. Hitam = perintah dan kendali. Abu-abu = data yang menunggu.**
- **Berpusat pada orang**: foto di setiap kartu, video call di tengah alur. Pesannya: penjualan adalah hubungan.

## 6. Warna terukur (sampel piksel, area UI)
| Hex | Porsi | Peran yang terlihat | Calon token (3 tingkat) |
|---|---|---|---|
| `#E3E4E3` / `#D9D9D8` | ±48% | Latar halaman | `--raw-color-neutral-200` → `--background` |
| `#FBFBFB` / `#ECECEC` | ±24% | Kartu, chip aktif | `--raw-color-neutral-50` → `--surface-raised` |
| `#000000` / `#1E1E1E` | panel | Bar jadwal, tombol utama, panel Summary | `--raw-color-neutral-950` → `--action-primary`, `--surface-inverse` |
| `#B6FF65` | ±10% | Sekarang, aktif, fokus | `--raw-color-lime-300` → `--state-active` |
| `#524E49` | teks | Teks utama dan ikon | `--raw-color-neutral-700` → `--foreground` |
| Merah, oranye, kuning, hijau kecil | titik dan lencana | Skala minat, delta KPI | `--status-hot` … `--status-cold`, `--delta-up`, `--delta-down` |

Kontras: hitam di atas lime ±17:1 (sangat baik). Label abu-abu kecil di atas `#E3E4E3` terlihat lemah; perlu diukur bila ditiru.

## 7. Tipografi
- Sans geometris berhuruf O bulat (mirip Urbanist atau Outfit; tidak terverifikasi). Judul kapital, berat sedang.
- Angka KPI besar dengan label kecil di samping (pola "angka + satuan").
- Ukuran tersirat: judul ±32 px, angka KPI ±28 px, nama kartu ±16 px, label ±10 px.

## 8. Komponen terdeteksi
| Komponen | Fungsi | Catatan |
|---|---|---|
| Bar jadwal dengan jarum waktu | Posisi "sekarang" di hari ini | Bisa digulir; segmen lime = rentang aktif |
| Kartu KPI inline | Ringkasan angka + delta | Tanpa kotak, hanya angka |
| Grup chip filter | Menyaring daftar | Satu chip aktif putih, ikon api untuk "Hot" |
| Kartu bertakik | Satu entitas (lead, tugas) | Tombol panah di takikan sudut |
| Rel ikon | Navigasi utama | Lingkaran 40 px |
| Overlay video | Komunikasi tanpa keluar alur | Mengambang, bisa digeser |
| Panel ringkasan gelap | Konteks dokumen dan tujuan | Timeline vertikal |

## 9. Gerak yang tersirat (tidak terlihat di gambar statis)
Dipetakan ke kontrak gerak panduan ai-design-vault:
- `Inview`: kartu masuk berurutan saat baris terlihat.
- `Hover`: tombol panah di takikan bergeser, kartu sedikit naik.
- `Handle` (drag): baris kartu digulir horizontal; jendela video digeser.
- `SpringTrigger`: jarum waktu bergerak, kartu tugas berpindah status.

## 10. Relevansi untuk JitsuinFi
| Bisa diambil | Ke mana |
|---|---|
| Bar waktu dengan jarum "sekarang" | Timeline jatuh tempo dan pelunasan di layar buyer atau financier |
| KPI inline (angka + delta, tanpa kotak) | Pipeline financier: terdaftar, dibiayai, lunas, ditolak |
| Chip filter dengan satu status aktif | Daftar deal supplier (semua, perlu tindakan, menunggu, selesai) |
| Satu warna aksen hanya untuk "sekarang" | Disiplin aksen yang sama dengan `--seal` di `MASTER.md` |

| Bertentangan | Alasan |
|---|---|
| Foto wajah dan nama di setiap kartu | JitsuinFi menyembunyikan pihak; identitas = key, sidik jari, segel |
| Kartu sebagai wadah utama | `MASTER.md` melarang kartu di landing; HNK-21 meminta "adegan, bukan kartu" di app |
| Lime `#B6FF65` | Tidak ada di [[DS-PAL - Palet Utama JitsuinFi]] |
| Logo merek pihak lain (sprocket ala HubSpot, Google Meet) | Tidak boleh dipakai |

## 11. Pertanyaan terbuka
- Gambar ini acuan untuk **app internal** (HNK-21) atau hanya inspirasi pola?
- Kartu bertakik boleh dipakai di app walaupun landing melarang kartu?
