---
tags: [design-ref, "DS-02"]
type: design-ref
id: DS-02
source_file: 52f185f73317db7945878f469d4cbabc.jpg
kind: mobile-app
mode: operate
updated: 2026-10-20
---

# DS-02 - Sports Score App Mustard

> **Peta link:** [[DS-00 - Peta Visual Design|Peta visual]] · [[09 - Design|Hub modul]] · [[DS-PAL - Palet Utama JitsuinFi|Palet utama]]

![DS-02](52f185f73317db7945878f469d4cbabc.jpg)

## 1. Identitas
| | |
|---|---|
| File | `09-Design/52f185f73317db7945878f469d4cbabc.jpg`, 720×720 |
| Jenis | Shot konsep aplikasi mobile skor dan taruhan olahraga; dua iPhone dalam render 3D studio |
| Sumber atau pembuat | Tidak tercantum di file |
| Mode | **Operate** (cek skor, setor, tarik dana) |

## 2. Yang terlihat (apa adanya)
- **Layar kiri (beranda):** sapaan "Hey, Markus" dengan foto, lonceng; kartu saldo putih "Current Balance $500.00" dan "Bonus Balance $50.00" dengan ikon uang di tengah atas; dua tombol hitam besar "Deposit" (ikon kuning) dan "Withdraw" (ikon putih); "Top Events" + "See All"; tab cabang olahraga (Football aktif dalam pill putih, ikon lain dalam lingkaran); panel kuning "Premier League" lencana hijau "Ongoing", Liverpool 2 : 1 Arsenal FT, odds 1x 1.8, x 2.0, 2x 6.0; panel kedua "Credit Suisse Super League" lencana "Upcoming"; tab bar mengambang hitam dengan ikon.
- **Layar kanan (detail laga):** "Back", tombol "Live Match" dengan ikon siaran merah; "Matchday 2", logo klub, 2 : 1 FT; pita kuning berisi pencetak gol (Esther 15', Enzo 65', Saka 25', G. Jesus 41'); odds; tab Match, Odds, H2H, Standings; grid **Statistics** (Goal attempts 8 – 4, Possession 55% – 45% dalam sel hitam, Fouls, Saves, Shot on goal, Corner kicks).
- **Panggung 3D:** balok krem bertingkat, dua bola kuning mengilap, cahaya studio lembut.

## 3. Style
- **Krem hangat + kuning mustard + hitam pekat.** Netral dan ramah, bukan neon.
- **Panel kuning sebagai "lembar" konten** dengan sudut membulat besar dan tab yang menyambung ke panel (tab aktif menyatu dengan permukaan di bawahnya).
- **Bento statistik:** grid sel dengan satu sel hitam sebagai sorotan (Possession).
- **Presentasi produk 3D** (claymorphism ringan pada latar): bentuk geometris dan bola senada.

## 4. POV dan komposisi
- **Kamera:** sedikit dari depan atas, dua ponsel tegak berdiri di panggung bertingkat; ponsel kanan lebih rendah dan lebih dekat, menciptakan diagonal kiri-atas ke kanan-bawah.
- **Urutan baca:** saldo → aksi (Deposit/Withdraw) → acara → detail laga. Alur dari "uang saya" ke "apa yang terjadi".
- **Hierarki:** skor 2 : 1 dan saldo dolar paling tebal; kuning menandai konten yang bisa ditindaklanjuti.

## 5. Makna
- **Hangat dan percaya diri**: kuning mustard memberi energi tanpa agresif; hitam memberi bobot pada aksi uang.
- **Uang dan permainan dalam satu layar**: saldo di atas, odds di setiap laga. Desainnya mendorong aksi cepat.
- Bola dan panggung 3D: produk diperlakukan seperti objek fisik yang bisa disentuh.

## 6. Warna terukur
| Hex | Peran yang terlihat | Calon token |
|---|---|---|
| `#EAE7E0` | Latar layar krem | `--raw-color-sand-100` → `--background` |
| `#FFFFFE` | Kartu saldo, chip | `--raw-color-neutral-0` → `--surface-raised` |
| `#FACE6E` | Panel konten, pita pencetak gol | `--raw-color-mustard-300` → `--surface-accent` |
| `#212121` | Tombol uang, tab bar, sel sorotan | `--raw-color-neutral-900` → `--action-primary`, `--surface-inverse` |
| `#66593F` | Teks di atas krem dan kuning | `--raw-color-umber-700` → `--foreground` |
| `#3F9E53` | Lencana "Ongoing" | `--raw-color-green-600` → `--status-live` |

Kontras: teks gelap `#212121` di atas `#FACE6E` ±11:1 (baik). Teks putih di atas kuning tidak dipakai, dan memang tidak boleh.

## 7. Tipografi
- Sans grotesk tebal untuk angka (saldo, skor), regular untuk label. Angka tabular pada odds.
- Ukuran tersirat: saldo ±16 px tebal, skor ±20 px, label ±10 – 11 px.

## 8. Komponen terdeteksi
| Komponen | Fungsi | Catatan |
|---|---|---|
| Kartu saldo dua kolom | Dua angka uang berdampingan | Ikon bulat di tepi atas sebagai "jepit" |
| Pasangan tombol aksi uang | Setor dan tarik | Hitam, ikon dalam kotak kecil, ukuran sentuh besar |
| Tab menyatu dengan panel | Ganti kategori | Tab aktif putih, lainnya lingkaran |
| Panel laga | Satu acara + status + odds | Lencana status berwarna |
| Grid statistik bento | Perbandingan dua pihak | Satu sel disorot hitam |
| Tab bar mengambang | Navigasi utama | Pill hitam di atas konten |

## 9. Gerak yang tersirat
- `Inview`: panel laga muncul berurutan.
- `SpringTrigger`: skor berganti saat gol; lencana "Ongoing" berdenyut.
- `Hover`/tekan: tombol uang memadat saat ditekan.
- `Handle`: tab kategori digulir horizontal.

## 10. Relevansi untuk JitsuinFi
| Bisa diambil | Ke mana |
|---|---|
| Kartu dua angka (saldo dan bonus) | Ringkasan buyer: jumlah yang harus dibayar dan jatuh tempo; atau supplier: nilai invoice dan advance |
| Pasangan aksi uang besar dan jelas | "Bayar" (QR) di layar buyer, "Terima advance" di supplier |
| Lencana status berwarna pada setiap item | Status deal: menunggu tanda tangan, terdaftar, lunas, ditolak |
| Grid statistik dua sisi | Perbandingan invoice: nilai vs advance, jatuh tempo vs hari ini |
| Tab yang menyatu dengan panel | Pergantian tahap deal tanpa kotak terpisah |

| Bertentangan | Alasan |
|---|---|
| Domain taruhan | Arah proyek: proses bisnis privat yang terverifikasi, **bukan** perjudian |
| Foto pengguna, logo klub | Merek pihak lain; JitsuinFi tidak menampilkan identitas |
| Mustard `#FACE6E` | Tidak ada di [[DS-PAL - Palet Utama JitsuinFi]] |
| Panggung 3D dekoratif | Hanya untuk shot presentasi, bukan UI |

## 11. Pertanyaan terbuka
- Yang menarik dari gambar ini palet hangatnya, pola kartu uang, atau grid statistiknya?
