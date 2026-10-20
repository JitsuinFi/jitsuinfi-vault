---
tags: [design-ref, "DS-08"]
type: design-ref
id: DS-08
source_file: bf2cdcf11501d4fa54d3300489442c25.jpg
kind: mobile-app
mode: persuade-operate
updated: 2026-10-20
---

# DS-08 - Paytin Finance Mobile

> **Peta link:** [[DS-00 - Peta Visual Design|Peta visual]] · [[09 - Design|Hub modul]] · [[DS-PAL - Palet Utama JitsuinFi|Palet utama]]

![DS-08](bf2cdcf11501d4fa54d3300489442c25.jpg)

## 1. Identitas
| | |
|---|---|
| File | `09-Design/bf2cdcf11501d4fa54d3300489442c25.jpg`, 1200×900 |
| Jenis | Shot presentasi konsep aplikasi bank mobile "Paytin" (tiga iPhone: onboarding, beranda, statistik) |
| Sumber atau pembuat | Tidak tercantum; kepala gambar: logo "Paytin", "Finance Mobile App", "www.paytin.com" |
| Mode | Onboarding: **Persuade**; beranda dan statistik: **Operate** |

## 2. Yang terlihat (apa adanya)
- **Panggung:** latar abu terang dengan lantai grid berperspektif dan kata raksasa pudar di belakang ponsel ("Secure", "Trusted", sebagian kata lain).
- **Ponsel kiri (onboarding), layar lime penuh:**
  - Ilustrasi garis hitam dengan isian krem: orang keluar dari dompet sambil memegang kartu; ikon koin, QR, kartu, struk melayang; lingkaran hijau tua di belakang.
  - Judul "Degital Banking Made for [pill hitam →] Digital Users" (tertulis "Degital"), sub "Spend, earn and track financial activity", "Skip", "Let's Start" + tombol panah bulat hitam.
- **Ponsel tengah (beranda):**
  - "William Current, Welcome Back 👋", foto, lonceng.
  - **Kartu hitam bertekstur dengan tab di sudut kanan atas** ("+ Set Budget", lime) seperti tab map; VISA, Balance `$ 25,453.00`, `**** 7281`, Exp `07/26`, panel kontak nirsentuh lime di kanan, kilau bintang.
  - Empat aksi bulat: Send, Bill, Mobile, More (lime).
  - "Quick Send": deret avatar bernama.
  - "Recent Activity": Food Store `-$15.00`, House Rent `-$290.00` …; bar bawah mengambang hitam dengan tombol pindai lime di tengah.
- **Ponsel kanan (statistik):**
  - Chip bulat Today, Weekly, **Monthly** (lime), Yearly.
  - Kartu lime "Earning 24%" dengan teks penjelasan dan **progres titik** Goal `$2567 / $5000`.
  - Kartu hitam "Spending `$3,250.80`" dengan grafik radar (Debit Card, Credit Card).
  - "Overview": Total Balance `$25,453.00`, grafik batang bertumpuk Jan – Jun (lime + hitam), tooltip `$2,410.00`.

## 3. Style
- **Fintech ramah:** lime + hitam + putih kehijauan; lingkaran di semua aksi.
- **Ilustrasi garis tangan** (outline hitam tebal, isian datar) untuk onboarding.
- **Tipografi persegi agak teknis** pada judul.
- **Kata nilai merek raksasa** sebagai lapisan latar (watermark tipografi).

## 4. POV dan komposisi
- **Kamera:** tiga ponsel tegak tampak depan; yang tengah lebih tinggi (hero), dua di sisi lebih rendah, ditopang lantai grid perspektif yang memberi kedalaman.
- **Narasi kiri → kanan:** sambutan (kenapa) → pakai (apa) → pahami (hasil).
- Tiap layar punya satu permukaan dominan: lime penuh, kartu hitam, kartu lime+hitam.

## 5. Makna
- **"Uang keluar dari dompet dan kembali ke tangan pengguna"**: ilustrasi adalah janji kebebasan.
- Kata "Secure", "Trusted" di latar = klaim kepercayaan sebagai suasana, bukan teks yang dibaca.
- Progres titik = tujuan yang bisa dicapai selangkah demi selangkah.

## 6. Warna terukur
| Hex | Peran yang terlihat | Calon token |
|---|---|---|
| `#C4E860` | Layar onboarding, aksi aktif, kartu earning | `--raw-color-lime-300` → `--surface-brand`, `--state-active` |
| `#EDFDDF` | Latar layar aplikasi | `--raw-color-lime-50` → `--background` |
| `#1C2222` | Kartu saldo, bar bawah, tombol | `--raw-color-ink-950` → `--surface-inverse`, `--action-primary` |
| `#EEEEEE` | Latar presentasi | — |
| `#5F6454` (campuran) | Teks redup | `--foreground-muted` |

Kontras: hitam di atas `#C4E860` ±14:1; teks kecil abu di atas `#EDFDDF` perlu dicek.

## 7. Tipografi
- Judul: sans persegi semi-teknis (mirip "Saira" atau "Lexend"; tidak terverifikasi), ±28 px di onboarding.
- Angka uang sans tebal ±24 px; label ±11 px.

## 8. Komponen terdeteksi
| Komponen | Fungsi | Catatan |
|---|---|---|
| Layar onboarding ilustratif | Menyambut + satu CTA | Skip di kiri, CTA bulat di kanan |
| Judul dengan pill ikon di tengah kalimat | Menyambung kata dengan simbol aksi | "Made for [→] Digital Users" |
| **Kartu dengan tab sudut** | Saldo + aksi tambahan di tab | Bentuk tab map |
| Deret aksi bulat | Aksi utama | Empat lingkaran 56 px, satu lime |
| Daftar aktivitas | Riwayat | Ikon dalam lingkaran hitam |
| Bar bawah mengambang | Navigasi + aksi pusat | Tombol tengah lime |
| Chip periode | Pilih rentang waktu | Lingkaran, satu lime |
| **Progres titik** | Kemajuan ke tujuan | Titik terisi dan kosong |
| Grafik radar, batang bertumpuk | Komposisi pengeluaran | Lime + hitam |

## 9. Gerak yang tersirat
- `Inview`: ilustrasi masuk bertahap (orang naik dari dompet, koin melayang).
- `SpringTrigger`: titik progres terisi satu per satu; batang naik.
- `Hover`/tekan: tombol bulat memadat; tab kartu terbuka.
- `Handle`: deret Quick Send digulir.

## 10. Relevansi untuk JitsuinFi
| Bisa diambil | Ke mana |
|---|---|
| Ilustrasi garis untuk onboarding | Cocok dengan **hairline** (figur garis isometrik) yang sudah terpasang tapi belum dipakai ([[FE-11 - hairline]]); layar Sign in atau Account (HNK-22) |
| Judul dengan pill ikon di tengah kalimat | Mirip "tanda segel di dalam judul" di hero landing (`MASTER.md` Amendment 2) |
| Kartu dengan tab sudut | Metafora map dokumen, sama dengan [[DS-07 - Cardiology Timeline Tree]] |
| Progres titik | Jumlah konfirmasi blok (`min_confirmations`) sebelum advance; tiga segel yang sudah terkumpul |
| Deret aksi bulat | Buyer: Tanda tangani, Segel, Bayar, Riwayat |
| Kata nilai raksasa di latar | Landing: "private", "once" sebagai lapisan tipografi |

| Bertentangan | Alasan |
|---|---|
| Foto dan nama orang, Quick Send ke kontak bernama | Identitas pihak harus tersembunyi |
| Nomor kartu, VISA | Merek pihak lain; JitsuinFi memakai ZEC shielded |
| Lime `#C4E860` | Tidak ada di [[DS-PAL - Palet Utama JitsuinFi]] |
| Salah eja "Degital" | Contoh copy yang harus dicek sebelum rilis |

## 11. Pertanyaan terbuka
- Gaya ilustrasi garis seperti ini (atau hairline) diinginkan untuk layar Sign in dan onboarding?
