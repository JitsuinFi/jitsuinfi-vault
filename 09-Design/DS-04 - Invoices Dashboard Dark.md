---
tags: [design-ref, "DS-04"]
type: design-ref
id: DS-04
source_file: 6483e2cb739e4f9ac22b4310a6d0bdf7.jpg
kind: dashboard-app
mode: operate
updated: 2026-10-20
---

# DS-04 - Invoices Dashboard Dark

> **Peta link:** [[DS-00 - Peta Visual Design|Peta visual]] · [[09 - Design|Hub modul]] · [[DS-PAL - Palet Utama JitsuinFi|Palet utama]]

![DS-04](6483e2cb739e4f9ac22b4310a6d0bdf7.jpg)

## 1. Identitas
| | |
|---|---|
| File | `09-Design/6483e2cb739e4f9ac22b4310a6d0bdf7.jpg`, 736×736 |
| Jenis | Shot konsep dashboard invoice dan pembayaran di dalam bingkai tablet, latar abu-abu lavender |
| Sumber atau pembuat | Tidak tercantum di file; memakai logo Salesforce dan nama perusahaan "BlueRock" |
| Mode | **Operate** (menagih, memantau, mencairkan dana) |
| Relevansi domain | **Tinggi**: satu-satunya referensi yang membahas invoice dan pembayaran |

## 2. Yang terlihat (apa adanya)
- **Nav:** logo Salesforce, tab pill di dalam bar putih (Estimates, **+ Invoices** aktif lime, Payments, Recurring Invoices, Checkouts), deret ikon, notifikasi, foto profil.
- **Judul** "Invoices" dengan tombol kembali; aksi kanan: ikon filter dan "Create an invoice".
- **Panel ringkasan gelap:** Overdue `$31,211.00`, Due within next month `$172,560.00`, Average time to get paid `12 days`. Di bawahnya **garis waktu bulan** (Sep, Oct, Nov, Dec) dengan bar progres lime dan deret avatar pelanggan per periode.
- **Panel payout:** "Available for Instant Payout" `$214,390.00` dengan pill "Expects"; tumpukan kartu metode (Visa `*4443`, **Stripe `#177210` lime menonjol ke atas**, PayPal `#711221`); tombol putih "Pay out now".
- **Active filters (2):** dropdown pelanggan, status, rentang tanggal "November 2023 – December 2023", pencarian "Enter invoice #".
- **Tab bersegmen menempel di atas panel putih:** All Invoices, Draft (3), **Unpaid (5)** aktif lime.
- **Daftar "Unpaid Invoices"** (panel putih): baris dengan avatar, nomor `# 404-002` … `# 417-020`, "in 2 days", status "Unsent"/"Viewed", jumlah. Baris terpilih `# 427-012` berlatar hitam.
- **Panel detail invoice gelap:** "Invoice details # 427-012" (Unsent), Company "BlueRock", Customer "Maria Jones, CEO BlueRock Pvt Ltd"; tiga sel item (Concept Development `$10,630.80`, CRM Development `$31,892.40`, CRM Integration `$10,630.80`) dan sel "+" berarsir; baris total (Sub Total, Total, Balance Due `$53,154.00`) dengan ikon dan tombol lime "Pay out now".

## 3. Style
- **Dark UI biru-arang** (bukan hitam murni) + panel putih kontras + **lime neon** untuk "aktif dan uang siap".
- **Master–detail:** daftar putih di kiri, detail gelap di kanan, baris terpilih "tersambung" dengan detail lewat warna hitam yang sama.
- **Tumpukan kartu pembayaran** dengan satu kartu terangkat: metafora dompet.
- Radius besar, pill di tab dan tombol, angka uang dengan simbol `$` kecil di depan.

## 4. POV dan komposisi
- **Kamera:** tablet tampak depan lurus, layar penuh; bingkai perangkat memberi konteks "alat kerja".
- **Urutan baca:** ringkasan uang (atas) → saring → daftar → detail → bayar. Alur dari gambaran besar ke satu invoice ke satu tombol.
- **Hierarki:** angka uang terbesar; lime hanya di tab aktif, progres, kartu pilihan, tombol bayar.

## 5. Makna
- **Uang yang tertunda dibuat terlihat dan bisa ditindaklanjuti**: overdue, jatuh tempo, rata-rata hari dibayar, lalu satu tombol "Pay out now".
- **Instant payout = mengubah piutang jadi kas sekarang**, inti yang sama dengan pembiayaan invoice (factoring).
- Avatar per periode: siapa yang berutang kapan.

## 6. Warna terukur
| Hex | Peran yang terlihat | Calon token |
|---|---|---|
| `#1E212B` / `#222833` / `#11151E` | Latar layar gelap biru-arang | `--raw-color-slate-950` → `--background` (tema gelap) |
| `#2A2D35` / `#3E4249` | Panel dan sel di atas latar | `--surface-raised` |
| `#FFFFFF` | Panel daftar, bar nav, tombol payout | `--surface-inverse` |
| `#94FF04` | Aktif, progres, uang siap | `--raw-color-lime-400` → `--state-positive`, `--action-primary` |
| `#687564` (sampel campuran) | Teks redup | `--foreground-muted` |
| Bingkai `#C7C4CB` | Latar presentasi | — |

Kontras: lime di atas `#1E212B` ±13:1; teks abu redup kecil di atas panel gelap terlihat lemah.

## 7. Tipografi
- Sans geometris ringan (mirip "Outfit" atau "Manrope"; tidak terverifikasi). Judul "Invoices" ±28 px regular, angka uang ±16 – 20 px, label ±9 – 10 px.
- Nomor invoice `#427-012` tampil besar di detail: nomor = identitas dokumen.

## 8. Komponen terdeteksi
| Komponen | Fungsi | Catatan |
|---|---|---|
| Tiga metrik uang | Overdue, due soon, rata-rata hari | Angka besar, label kecil di atas |
| Garis waktu bulan + progres + avatar | Siapa jatuh tempo kapan | Bar lime per periode |
| Tumpukan metode payout | Pilih sumber pencairan | Kartu terpilih terangkat |
| Bar filter aktif | Penyaring dengan jumlah filter | Badge angka |
| Tab bersegmen dengan hitungan | Draft (3), Unpaid (5) | Menempel ke panel di bawahnya |
| Daftar invoice | Nomor, jatuh tempo relatif, status, jumlah | Baris terpilih hitam |
| Detail invoice | Item, total, balance due, aksi | Sel "+" berarsir untuk item baru |

## 9. Gerak yang tersirat
- `Inview`: angka uang menghitung naik; bar progres terisi.
- `SpringTrigger`: memilih baris menggeser panel detail; kartu metode terangkat.
- `Hover`: tombol panah di sel item, baris daftar.
- `Handle`: gulir garis waktu bulan.

## 10. Relevansi untuk JitsuinFi
| Bisa diambil | Ke mana |
|---|---|
| Master–detail daftar invoice | Daftar deal supplier (HNK-24.T9) dan detail per N |
| Status per invoice (Unsent, Viewed) | Status deal: belum ditandatangani, ditawarkan, terdaftar, disegel, advance diterima, lunas |
| Garis waktu bulan dengan jatuh tempo | Layar buyer: tagihan per jatuh tempo; financier: jadwal pelunasan |
| "Available for Instant Payout" + "Pay out now" | Supplier: advance yang bisa dicairkan; financier: tombol bayar advance (Sign-to-Pay) |
| Tab bersegmen dengan hitungan | Filter deal per tahap |
| Nomor dokumen besar di detail | Tampilkan sidik jari N atau `TES-INV-…` sebagai identitas utama |

| Bertentangan | Alasan |
|---|---|
| Nama pelanggan, foto, nama perusahaan | Data pihak harus tersembunyi; tampilkan key, sidik jari, segel |
| Logo Salesforce, Visa, Stripe, PayPal | Merek pihak lain; JitsuinFi memakai ZEC shielded |
| Lime `#94FF04`, slate gelap | Tidak ada di [[DS-PAL - Palet Utama JitsuinFi]]; padanan peran: Dark Raspberry untuk aksi, Cetacean/Catalina untuk tema gelap |
| Kartu panel di mana-mana | Landing melarang kartu; untuk app perlu keputusan (lihat pertanyaan) |

## 11. Pertanyaan terbuka
- Gambar ini acuan utama untuk layar app (HNK-21)? Struktur master–detail-nya paling dekat dengan alur deal JitsuinFi.
- Tema gelap app boleh memakai Cetacean dan Catalina sebagai permukaan?
