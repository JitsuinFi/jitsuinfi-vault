---
tags: [design-ref, "DS-05"]
type: design-ref
id: DS-05
source_file: 7fd6f8f9768c254c498a80035a27b7a2.jpg
kind: dashboard-app
mode: operate
updated: 2026-10-20
---

# DS-05 - Ethereal Finance Dashboard

> **Peta link:** [[DS-00 - Peta Visual Design|Peta visual]] · [[09 - Design|Hub modul]] · [[DS-PAL - Palet Utama JitsuinFi|Palet utama]]

![DS-05](7fd6f8f9768c254c498a80035a27b7a2.jpg)

## 1. Identitas
| | |
|---|---|
| File | `09-Design/7fd6f8f9768c254c498a80035a27b7a2.jpg`, 736×552 |
| Jenis | Shot konsep dashboard keuangan pribadi bernama "ethereal", di dalam bingkai perangkat kaca, latar gradasi lavender |
| Sumber atau pembuat | Tidak tercantum di file |
| Mode | **Operate** (memantau saldo, pengeluaran, langganan) |

## 2. Yang terlihat (apa adanya)
- **Nav:** logo "ethereal", tab pill (Dashboard aktif putih, Statistics, Transactions, My wallet), ikon cari dan notifikasi, foto profil.
- **Judul** "My Dashboard".
- **Kartu saldo gradasi** mint ke lime: "Total balance" `120,456,50 $` (tertulis dengan koma, bukan titik), "+$2,456 revenue from last month", tombol hitam "Transfer", tombol putih "Top Up" dengan ikon.
- **Income** `+2,456 $` (lencana hijau +15.7%) dan **Expense** `-1,124 $` (lencana merah -10.7%), "This week's income/expense".
- **Revenue flow** (Monthly): batang ungu transparan Apr – Aug (+$4.1K … +$2.4K); batang Aug lavender terang dengan tooltip `$2,456.00 +16%`.
- **Expense split** (Aug): donat multi-warna "Total 1,124 $" dengan legenda Food 30%, Entertainment 10%, Health 10%, Transportation 15%, Bills 20%, Miscellaneous 15%.
- **My cards (3):** tumpukan kartu (oranye, PayPal hijau-kuning, Visa ungu `**** 6902`), satu kartu kaca buram terbuka: nomor `4156 6727 1439 6902`, nama "Micky Larson", `07/25`; tombol "Add +".
- **Subscriptions (5):** deret logo bulat (Discord, Apple, Spotify, Dribbble, Telegram), daftar iCloud `$2.99` (Next 15 July), Discord Nitro `$8.99`, Telegram `$4.99`, Dribbble.
- **Recent transactions (234):** Telegram, lencana "Successful", `04.07.2023 12:40 AM`, `**4352`, `-$4.99`.

## 3. Style
- **Dark navy-violet + gradasi pastel aurora** (mint, lime, lavender, ungu). Lembut, "melayang", sesuai nama *ethereal*.
- **Kaca** pada kartu bank yang terbuka dan bingkai perangkat.
- Bento grid kartu dengan radius besar; lencana delta hijau dan merah; donat warna-warni.
- Desimal ditulis kecil dan naik (`2,456 $`, `$2.99`): pola harga ritel.

## 4. POV dan komposisi
- **Kamera:** layar tampak depan datar di dalam bingkai berkilau; latar lavender buram memberi kesan "melayang".
- **Grid:** tiga kolom; kolom kanan (kartu + langganan) memanjang penuh sebagai panel dompet.
- **Urutan baca:** saldo (terbesar, satu-satunya permukaan terang berwarna) → arus masuk dan keluar → grafik → dompet → transaksi.

## 5. Makna
- **Uang sebagai sesuatu yang ringan dan menyenangkan**: gradasi lembut menggantikan nuansa bank yang kaku.
- Kartu bertumpuk = dompet fisik. Langganan dengan "Next 15 July" = uang yang akan keluar.
- Hijau dan merah = naik dan turun, konvensi pasar.

## 6. Warna terukur
| Hex | Peran yang terlihat | Calon token |
|---|---|---|
| `#242532` / `#232331` | Latar layar | `--raw-color-ink-950` → `--background` (gelap) |
| `#393A48` / `#313142` | Kartu di atas latar | `--surface-raised` |
| `#7AE1C7` → `#CEF58C` | Gradasi kartu saldo | `--gradient-value` (dua primitive mint dan lime) |
| `#DDB7FE` | Batang terpilih, sorotan | `--raw-color-lavender-200` → `--state-selected` |
| `#A690DF` | Kartu Visa, aksen ungu | `--raw-color-violet-400` → `--accent` |
| Hijau, merah lencana | Delta naik, turun | `--delta-up`, `--delta-down` |
| `#BEACC5` / `#DED8E7` | Latar presentasi | — |

Kontras: teks hitam di atas gradasi mint-lime baik; teks abu kecil di atas `#242532` lemah.

## 7. Tipografi
- Sans geometris (mirip "Plus Jakarta Sans" atau "Outfit"; tidak terverifikasi). Angka saldo ±30 px, judul ±24 px, label ±10 px.
- Satuan mata uang superskrip kecil setelah angka.

## 8. Komponen terdeteksi
| Komponen | Fungsi | Catatan |
|---|---|---|
| Kartu saldo hero | Angka terpenting + aksi | Satu-satunya permukaan gradasi |
| Metrik dengan lencana delta | Income, expense | Hijau/merah |
| Grafik batang dengan tooltip | Tren bulanan | Batang terpilih terang |
| Donat dengan legenda | Komposisi | Enam kategori |
| Tumpukan kartu + kartu terbuka | Dompet | Kartu kaca menampilkan nomor |
| Daftar langganan | Tagihan berulang dan tanggal berikutnya | Logo + harga + menu |
| Tabel transaksi | Riwayat + status | Lencana "Successful" |

## 9. Gerak yang tersirat
- `Inview`: donat menggambar busurnya, batang tumbuh.
- `Hover`: tooltip muncul di batang; kartu di tumpukan terangkat.
- `SpringTrigger`: kartu terpilih membuka (kaca) dari tumpukan.
- `Handle`: gulir daftar langganan.

## 10. Relevansi untuk JitsuinFi
| Bisa diambil | Ke mana |
|---|---|
| Donat komposisi | Layar anggota dana (SEQ-05, `#/member`): porsi dana per kelas diskon atau tenor |
| Daftar "Next 15 July" | Layar buyer: tagihan per jatuh tempo, tanggal berikutnya |
| Tabel transaksi dengan status | Daftar txid (registrasi, advance, settled) dengan jumlah konfirmasi |
| Metrik naik/turun | Financier: advance keluar vs pelunasan masuk |
| Satu permukaan hero berwarna, sisanya netral | Satu fokus per layar (misalnya saldo yang harus dibayar) |

| Bertentangan | Alasan |
|---|---|
| Nomor kartu dan nama pemilik ditampilkan | JitsuinFi tidak menampilkan identitas atau nomor rekening; dana di alamat shielded |
| Logo merek (Visa, PayPal, Apple, Discord, Spotify, Telegram, Dribbble) | Merek pihak lain |
| Gradasi mint, lime, lavender | Tidak ada di [[DS-PAL - Palet Utama JitsuinFi]]; gradasi yang mungkin: Catalina → Absolute Zero di dalam "air" |
| Donat warna-warni enam warna | Palet utama hanya punya dua keluarga; kategori perlu dibedakan dengan nada, bukan pelangi |

## 11. Pertanyaan terbuka
- Layar anggota dana (`#/member`) mau dibuat seperti panel dompet ini?
