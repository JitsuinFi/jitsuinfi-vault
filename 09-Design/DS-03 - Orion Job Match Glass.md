---
tags: [design-ref, "DS-03"]
type: design-ref
id: DS-03
source_file: 5b6667b68b28d730c53727099c0348b3.jpg
kind: dashboard-hero
mode: operate
updated: 2026-10-20
---

# DS-03 - Orion Job Match Glass

> **Peta link:** [[DS-00 - Peta Visual Design|Peta visual]] · [[09 - Design|Hub modul]] · [[DS-PAL - Palet Utama JitsuinFi|Palet utama]]

![DS-03](5b6667b68b28d730c53727099c0348b3.jpg)

## 1. Identitas
| | |
|---|---|
| File | `09-Design/5b6667b68b28d730c53727099c0348b3.jpg`, 1024×768 |
| Jenis | Shot konsep dashboard pencocokan kerja berbasis AI bernama "ORION" (gaya Dribbble), latar abu-abu presentasi |
| Sumber atau pembuat | Tidak tercantum di file |
| Mode | Atas: **Persuade** (hero); bawah: **Operate** (memilah lowongan) |

## 2. Yang terlihat (apa adanya)
- **Nav:** logo "ORION", pill pencarian ("Web Designer, UX/UI", "Los Angeles", tombol putih "Search"), ikon headset dan pengaturan, foto profil.
- **Hero (setengah atas, latar sage abu-abu):**
  - Judul kapital "YOUR JOB MATCH" dengan pill garis "AI - Powered".
  - **Objek 3D di tengah**: bangunan kaca bertingkat yang ditumbuhi lumut dan tanaman, melayang miring.
  - Panel kaca buram kiri "Salary expectations": dua garis (Senior, Middle) dengan pita **arsir diagonal** di antaranya, penanda lime "48%" di bulan Jun, sumbu Mar – Aug.
  - Panel kaca kanan: "Candidates Online" (2 574 32%, 4 131 54%, 998 14%) dengan kontrol tersegmentasi Junior (hitam), Middle (putih), Senior (lime, sebagian berarsir); "Orion Index 0.27 +6" dengan slider Offers – Responses; "Vacancies 8,574 +37" dengan grafik batang, satu batang lime.
- **Zona bawah (hitam):**
  - Filter pill: This week, Remote, $100k – $130k, Full time, Senior, Middle; tombol filter dengan titik merah.
  - Paginasi "03 / 153" dengan panah.
  - Kartu lowongan gelap: logo perusahaan (Amazon, BeReal, Wise), jabatan, waktu, chip gaji, jenis, level, lokasi, "More than 60 applicants".
  - **Cincin kecocokan** lime "79% Strong Match", "86% Strong Match", dikelilingi tombol lingkaran: tolak (X), ikon coret, suka (hati lime), terima (centang).

## 3. Style
- **Dua dunia dalam satu layar**: atas terang, kabur, organik (kaca + tanaman); bawah hitam, rapat, transaksional.
- **Glassmorphism** pada panel data di atas render 3D.
- **Lime neon** sebagai satu-satunya warna "positif": cocok, aktif, puncak.
- **Arsir diagonal** sebagai tekstur untuk rentang dan nilai yang belum pasti.
- Radius besar, pill di semua kontrol, angka besar dengan persen kecil di superskrip.

## 4. POV dan komposisi
- **UI:** tampak depan datar.
- **Objek 3D:** sudut pandang 3/4 dari atas (oblique), melayang tanpa bayangan tanah; menjadi **jangkar visual** di antara judul (kiri) dan statistik (kanan).
- **Simetri seimbang:** judul + grafik di kiri, tiga panel data di kanan, objek di tengah. Bawah: grid kartu horizontal yang terpotong di kanan (gulir).
- **Garis horizon tegas** antara zona terang dan hitam membagi "melihat" dan "memutuskan".

## 5. Makna
- **Kaca = transparansi data AI; tanaman = pertumbuhan karier.** Struktur buatan yang hidup.
- **Cincin persen = keyakinan mesin**; tombol di sekelilingnya = keputusan manusia (setuju, tolak, simpan).
- Arsir = "perkiraan", bukan angka pasti.

## 6. Warna terukur
| Hex | Peran yang terlihat | Calon token |
|---|---|---|
| `#8D938A` / `#9EA597` / `#70766B` | Latar hero sage | `--raw-color-sage-400` → `--surface-hero` |
| `#8B8E8B` (panel) | Kaca buram di atas render | `--surface-glass` (dengan blur) |
| `#121212` / `#000000` | Zona keputusan, kartu | `--raw-color-neutral-950` → `--surface-inverse` |
| `#BFFD01` | Cocok, aktif, puncak | `--raw-color-lime-400` → `--state-positive` |
| Putih | Teks di atas gelap, tombol Search | `--foreground-on-inverse` |
| Merah kecil | Titik notifikasi filter | `--status-attention` |

Kontras: lime `#BFFD01` di atas hitam ±17:1; teks putih di atas kaca sage ±3:1 (lemah untuk teks kecil).

## 7. Tipografi
- Sans geometris lebar (mirip "Unbounded" atau "Outfit"; tidak terverifikasi) untuk judul kapital; angka besar tipis dengan persen superskrip.
- Ukuran tersirat: judul ±40 px, angka panel ±20 px, label ±10 px.

## 8. Komponen terdeteksi
| Komponen | Fungsi | Catatan |
|---|---|---|
| Pill pencarian ganda | Kata kunci + lokasi | Tombol aksi putih di dalam pill |
| Panel kaca dengan tombol panah | Ringkasan metrik, buka detail | Panah di sudut kanan atas |
| Grafik pita berarsir | Rentang dua seri | Penanda nilai lime |
| Kontrol tersegmentasi tiga | Pilih level | Segmen terpilih berwarna |
| Mini bar chart | Tren volume | Satu batang disorot |
| Paginasi angka besar | Posisi dalam daftar panjang | "03 / 153" |
| Cincin kecocokan + gugus aksi | Skor + keputusan cepat | Pola mirip swipe |

## 9. Gerak yang tersirat
- `Inview`: cincin persen terisi dari 0; batang grafik tumbuh.
- `SpringTrigger`: objek 3D berputar pelan atau mengambang; kontrol tersegmentasi bergeser.
- `Hover`: panel kaca menebal blur-nya, tombol panah berputar 45°.
- `Handle`: kartu lowongan digeser (swipe) untuk setuju atau tolak.

## 10. Relevansi untuk JitsuinFi
| Bisa diambil | Ke mana |
|---|---|
| Objek 3D sebagai jangkar di antara copy dan data | Sudah dipakai: diorama "Kota Piutang" di hero landing (`MASTER.md` Amendment 3) |
| Cincin skor + gugus keputusan | Layar financier: skor riwayat buyer (tepat waktu, terlambat, gagal bayar) lalu terima atau tolak penawaran (HNK-26.T5 – T6) |
| Pita berarsir untuk rentang | Indeks bunga per kelas diskon dan tenor (HNK-08), nilai yang disamarkan per bucket |
| Paginasi besar "03 / 153" | Menelusuri deal atau entri papan |
| Pemisahan zona "melihat" vs "memutuskan" | Verify (melihat bukti) vs aksi segel |

| Bertentangan | Alasan |
|---|---|
| Panel kaca sebagai kartu data | `MASTER.md`: kaca hanya untuk pill di atas adegan; kartu dilarang di landing |
| Lime `#BFFD01`, sage | Tidak ada di [[DS-PAL - Palet Utama JitsuinFi]] |
| Logo Amazon, BeReal, Wise; foto orang | Merek dan identitas pihak lain |
| Teks putih tipis di atas kaca | Kontras lemah |

## 11. Pertanyaan terbuka
- Pola "cincin skor + tombol keputusan" layak jadi pola layar financier?
