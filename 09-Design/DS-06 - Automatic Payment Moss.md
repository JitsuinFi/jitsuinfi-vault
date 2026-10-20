---
tags: [design-ref, "DS-06"]
type: design-ref
id: DS-06
source_file: 8628ae96fff4184f7b7588fbcf81ca95.jpg
kind: dashboard-app
mode: operate
creator: RonDesignLab
updated: 2026-10-20
---

# DS-06 - Automatic Payment Moss

> **Peta link:** [[DS-00 - Peta Visual Design|Peta visual]] · [[09 - Design|Hub modul]] · [[DS-PAL - Palet Utama JitsuinFi|Palet utama]]

![DS-06](8628ae96fff4184f7b7588fbcf81ca95.jpg)

## 1. Identitas
| | |
|---|---|
| File | `09-Design/8628ae96fff4184f7b7588fbcf81ca95.jpg`, 1200×900 |
| Jenis | Shot konsep dashboard pembayaran otomatis (langganan perangkat lunak tim) |
| Pembuat | **RonDesignLab** (tertulis "Original creator: RonDesignLab"); seri "09/90" |
| Mode | **Operate** (mengatur dan menyetujui pembayaran berulang) |

## 2. Yang terlihat (apa adanya)
- **Latar:** tekstur kertas atau dinding hijau lumut yang tergores; panel aplikasi hijau transparan di atasnya.
- **Nav:** logo "ob", pill navigasi (Dashboard, Taxes, Invoicing, Reports, **Payment** aktif hitam, Cash Flow, Projects), profil "Anshika Khola, Product Designer", ikon pengaturan.
- **Judul** besar "Automatic Payment", cincin progres "11%", tiga angka: Overall balance `256,612 $`, Monthly profits `167,612 $`, Monthly payments `25,612 $`.
- **Pill kategori besar bergaris:** All, Salary, Taxes, **Software** (hitam), Promotion, Rent, Cleaning, "+"; tombol bagikan dan pengaturan.
- **Kartu hitam utama** "Figma, Collective use" dengan deret avatar dan "+", tombol hapus dan perbesar.
  - **Garis penghubung tiga langkah** dengan simpul centang hijau di atas tiga sel:
    1. "Date of payment": kalender bulan, tanggal **18** dipilih.
    2. "Payment plan": pill Professional, Organisation, Enterprise (terpilih), `75 $ / personal user`.
    3. "Pay from" (sel hijau): batang perbandingan Venmo `39,902`, **Wise `45,876` hitam**, PayPal `78,890`.
  - Ringkasan bawah: Payment details `18th`, No. of users `08`, Payment amount `375 $`, Payment method `Wise`, tombol centang hijau bulat.
- **Kartu krem kanan:** "Unsplash images, Monthly, every 17th, `375 $`" dan "Dropbox storage, Annually, Jan 27, `2566 $`"; masing-masing ikon edit dan **sakelar tolak/setuju** (× / ✓ hijau).

## 3. Style
- **Organik-gelap:** monokrom hijau lumut + hitam + krem, di atas **tekstur kertas tergores**. Jauh dari SaaS steril.
- **Angka raksasa** sebagai elemen visual utama (lebih besar dari judul bagian).
- **Pill bergaris tipis besar** untuk kategori; satu pill hitam terisi = aktif.
- **Alur bertahap terlihat**: garis horizontal dengan simpul centang menghubungkan tiga sel.

## 4. POV dan komposisi
- **Kamera:** layar datar tampak depan, panel aplikasi melayang di atas permukaan bertekstur, ada margin lebar di sekeliling.
- **Grid:** atas = judul + metrik (baris), tengah = filter, bawah = kartu kerja besar (kiri 2/3) + dua kartu tindakan kecil (kanan 1/3).
- **Urutan baca:** judul → angka besar → kategori → alur tiga langkah → ringkasan → centang.

## 5. Makna
- **Pembayaran sebagai proses yang dipastikan langkah demi langkah**: tanggal, rencana, sumber dana, lalu satu centang.
- **Tekstur kertas = dokumen nyata**, bukan sekadar layar. Hijau = uang dan "lanjut".
- Sakelar × / ✓ = persetujuan manusia sebelum uang keluar.

## 6. Warna terukur
| Hex | Peran yang terlihat | Calon token |
|---|---|---|
| `#313C34` / `#152117` | Latar bertekstur gelap | `--raw-color-moss-950` → `--background` |
| `#597745` / `#4F6A3D` | Panel hijau, sel "Pay from" | `--raw-color-moss-600` → `--surface-tint` |
| `#0D0D0D` | Kartu kerja utama, pill aktif | `--raw-color-neutral-950` → `--surface-inverse`, `--state-selected` |
| `#F3F7E9` | Kartu tindakan krem | `--raw-color-cream-50` → `--surface-raised` |
| `#93C870` | Centang, simpul langkah, batang PayPal | `--raw-color-leaf-400` → `--state-positive`, `--action-confirm` |
| `#DDE6D2` | Teks dan garis terang di atas hijau | `--foreground-on-tint` |

Kontras: teks putih di atas `#597745` ±4.9:1 (cukup untuk teks besar); hitam di atas `#93C870` ±10:1.

## 7. Tipografi
- Sans geometris dengan x-height tinggi (mirip "Satoshi" atau "Gilroy"; tidak terverifikasi). Judul ±48 px, angka metrik ±40 px, angka ringkasan ±40 px, label ±12 px.
- Satuan `$` dan sufiks `th` kecil superskrip.

## 8. Komponen terdeteksi
| Komponen | Fungsi | Catatan |
|---|---|---|
| Metrik raksasa berderet | Tiga angka uang | Label kecil di atas |
| Cincin progres kecil | Persentase target | Di samping judul |
| Pill kategori bergaris | Filter besar mudah disentuh | Satu terisi hitam |
| **Stepper horizontal dengan simpul centang** | Menunjukkan langkah yang sudah selesai | Menghubungkan tiga sel kerja |
| Kalender kompak | Pilih tanggal bayar | Tanggal terpilih lingkaran putih |
| Grup pill pilihan | Pilih rencana | Pill terpilih terisi |
| Batang perbandingan sumber dana | Pilih sumber | Batang terpilih hitam |
| Kartu tagihan berulang + sakelar setuju/tolak | Persetujuan cepat | Sakelar dua posisi × / ✓ |

## 9. Gerak yang tersirat
- `Inview`: angka besar menghitung naik; garis stepper tergambar dari kiri dan simpul berubah jadi centang satu per satu.
- `SpringTrigger`: sakelar meluncur ke ✓; tombol centang memantul sekali.
- `Hover`: pill kategori terisi; batang sumber dana naik.

## 10. Relevansi untuk JitsuinFi
| Bisa diambil | Ke mana |
|---|---|
| **Stepper tiga simpul centang** | **Rantai tiga segel Sign-to-Pay** (supplier, buyer, financier); timeline deal di layar supplier (HNK-24.T9) |
| Tekstur kertas sebagai latar | Sejalan dengan "washi" dan serat kertas di `MASTER.md` (`--fiber`, tepi kertas) |
| Sakelar setuju/tolak per tagihan | Financier: terima atau tolak penawaran; buyer: segel atau tolak surat |
| Angka raksasa tanpa kotak | Nilai invoice, advance, sisa tagihan |
| Satu tombol konfirmasi besar di akhir ringkasan | "Segel" atau "Bayar" sebagai aksi tunggal setelah semua langkah hijau |

| Bertentangan | Alasan |
|---|---|
| Hijau lumut dan krem | Tidak ada di [[DS-PAL - Palet Utama JitsuinFi]]; padanan: kertas `--paper` dan tinta plum, centang = Dark Raspberry |
| Avatar, nama, logo merek (Figma, Unsplash, Dropbox, Venmo, Wise, PayPal) | Identitas dan merek pihak lain |
| Kartu hitam besar sebagai wadah | Landing melarang kartu |

## 11. Pertanyaan terbuka
- Stepper simpul centang ini dijadikan pola resmi untuk rantai segel di app?
