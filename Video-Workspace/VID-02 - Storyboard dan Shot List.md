---
tags: [video, "VID-02"]
---

# VID-02 - Storyboard dan Shot List

**Bagian dari:** [[Video-Workspace]] · Terkait: [[VID-01 - Naskah 2 Menit]] · [[VID-03 - Checklist Rekaman]]

## Shot list v3 (2026-10-27, mengikuti [[VID-01 - Naskah 2 Menit]] v3)
Semua shot direkam user sendiri (passkey, HP, konsol production, dan suara tidak bisa direkam agent). Path = URL production. "Klik" = urutan tindakan persis. Label tombol diambil dari kode frontend `9d30581` (PR #81); kalau label di layar berbeda, ikuti layar dan catat di sini.

| Shot | Waktu | Durasi | Perangkat / profil | Path | Klik dan gerak | Yang harus terlihat | Status |
|---|---|---|---|---|---|---|---|
| S01 | 0:00 – 0:11 | 11 dtk | Desktop, profil `TES-video` (logout) | `https://jitsuinfi.vercel.app` | Buka, biarkan hero bermain 11 detik tanpa klik. Di editor: overlay tiga baris "saw the invoice / asked the buyer / controlled the cash", centang merah berubah hijau pada kata "does all three" | Badge "Live on Zcash testnet, Ironwood pool", cerita kota berjalan | TODO |
| S02 | 0:11 – 0:20 | 9 dtk | Desktop `TES-video` | `https://jitsuinfi.vercel.app` bab 2 指紋 ("One fingerprint per invoice.") | Scroll pelan ke bab 2; tekan "One zat more" dua kali; berhenti saat "{d} of 64 digits changed." tampil | N berubah hampir semua digit | TODO |
| S03 | 0:20 – 0:24 | 4 dtk | Desktop `TES-video` | Dari nav landing "Open the demo" → `/app` | Klik "Open the demo"; di denah kantor registri arahkan kursor ke ruang "Try to double-finance", klik | Lobi 登記所, pin ruangan | TODO |
| S04 | 0:24 – 0:46 | 22 dtk | Desktop `TES-video` | `/try` | (1) Tunggu "Reading the board…" selesai. (2) Ubah "Amount due in ZEC" satu digit. (3) "Offer it to financier B" → cap 偽. (4) "Put back the original". (5) "Offer it to financier B" → cap 重 "Already pledged.", benang merah ke papan, tag "Exhibit A" muncul | 偽 lalu 重 dari papan testnet hidup (bukan "saved board") | TODO |
| S05 | 0:46 – 0:57 | 11 dtk | Desktop `TES-video` | `/try` bagian Exhibit A, lalu `/verify` | Klik tag "Take it home ↓"; tunjukkan kartu Exhibit A (tanpa nama invoice). Potong ke `/verify`: "Use Case File #0417's Exhibit A" → "Hand it to the registry"; tahan saat lensa menyapu dan hanko 重 jatuh | "Double signature on the board", Entry ① dan ② dengan blok | TODO |
| S06 | 0:57 – 1:05 | 8 dtk | Desktop `TES-video` | `/outsider`, lalu `/rates` | `/outsider`: biarkan palang sensor menutup 請求書, sorot pita papan (4 dtk). `/rates`: tunjukkan grafik, tekan "Raise k" sekali (4 dtk) | Tidak ada nominal atau pihak; kelas tampil hanya dari k ≥ 5 | TODO |
| S07 | 1:05 – 1:26 | 21 dtk | Desktop profil `TES-supplier` + iPhone/Android PWA `TES-buyer` | Supplier: `/supplier/invoices/new`; buyer: ikon app JitsuinFi di layar utama HP | Supplier: isi "The buyer this invoice is for" (kontak buyer yang sudah ada), nominal, tanggal jatuh tempo, pilih PDF → "Create invoice" → kirim ke buyer. Potong ke HP (rekaman layar HP): buka app dari ikon, ketuk lonceng inbox → surat invoice → periksa → tanda tangan → Face ID / sidik jari → "Signature sent". Kembali ke desktop: `/supplier/deal/<ref>` rute 照 署 menyala, pilih "JitsuinFi testnet financier" dari direktori, isi "Advance you ask (ZEC)", kirim penawaran | Satu sentuhan passkey di HP; tanpa menempel teks | TODO |
| S08 | 1:26 – 1:38 | 12 dtk | Desktop profil `TES-financier` (passkey konsol production milik user) | `https://jitsuinfi-console.vercel.app/console` | Masuk dengan passkey (potong dialog). In-tray: penawaran tersegel dengan cap "Fits your private mandate" → terima. Dipercepat: entri papan 登, segel surat 印 dari supplier dan buyer (inbox masing-masing), lalu tombol persetujuan advance → passkey → "Approved with your passkey. The advance is on its way." | Rute deal 照 署 登 印 金; tanpa saldo atau alamat wallet penuh | TODO |
| S09 | 1:38 – 1:46 | 8 dtk | HP PWA `TES-buyer`, lalu desktop `TES-supplier` | Buyer: Pay → slip; supplier: `/supplier/deal/<ref>` | HP: "Show payment QR" (QR terlihat 1 dtk, label "sped up"); bayar dari wallet testnet buyer di luar layar. Desktop: rute sampai 済 "Settled." → "Check it on Verify" → `/verify` hanko 真 | "Bundle is genuine" / 真, txid settled di layar | TODO |
| S10 | 1:46 – 1:52 | 6 dtk | Slide atau desktop | `Video-Workspace/assets/slides-hnk18.html` (kartu batas) atau `/try` panel "Notice: what this does not stop" | Tampilkan kalimat batas N-13 | Kalimat batas terbaca | TODO |
| S11 | 1:52 – 1:56 | 4 dtk | Slide | `slides-hnk18.html` (kartu penutup) | Tagline dua baris + `jitsuinfi.vercel.app` + `github.com/JitsuinFi` | URL terbaca | TODO |

### Cadangan bila deal nyata gagal saat rekam
- S07 – S09 boleh memakai rekaman deal lain hari yang sama asalkan txid-nya nyata dan dicatat di README. Jangan memakai konsol demo (`jitsuinfi-console-demo.vercel.app`) untuk S08: di sana "nothing here moves money", jadi tidak ada advance.
- Kalau node production tidak menjawab saat rekam, `/try` dan `/verify` tetap jalan dengan papan tersimpan dan menyebutnya; rekam ulang setelah node pulih agar S04 memukul papan hidup (syarat D-40).
- Klip 20 detik [[VID-07 - Klip 20 Detik Coba Curang]] (`/try/play`, tanpa klik) bisa menggantikan S04 – S05 bila waktu habis.

## Shot list v2 (2026-10-22, diganti v3)
| Shot | Durasi | Jenis | Isi layar | Sumber | Status |
|---|---|---|---|---|---|
| 01 | 15 dtk | Motion text | Tiga centang merah menjadi hijau (N-06) | Slide HNK-18.T2 | TODO |
| 02 | 7 dtk | Screen recording | Landing: noren 登記所, seal 印 | `jitsuinfi.vercel.app` | TODO |
| 03 | 10 dtk | Screen recording | `/try` Case File #0417, amplop kit terbuka | `app.html#/try` | TODO |
| 04 | 20 dtk | Screen recording | Ubah nominal → 偽; kirim apa adanya → 重 | `app.html#/try` | TODO |
| 05 | 13 dtk | Screen recording | Exhibit A, `/verify` 重 | `app.html#/verify` | TODO |
| 06 | 10 dtk | Screen recording | Lensa: tahan tombol | `app.html#/try` (lensa) | TODO |
| 07 | 15 dtk | Screen recording | Konsol: kotak surat, 内規, cap 適/外/待, rute 案件 | `jitsuinfi-console.vercel.app` (atau konsol demo) | TODO |
| 08 | 15 dtk | Slide | Batas N-13 + threat model | Slide HNK-18.T2 | TODO |
| 09 | 10 dtk | Slide | Tagline + URL | Slide HNK-18.T2 | TODO |

## Shot list v1 (diganti)
| Shot | Durasi | Jenis | Isi layar | Sumber/aset | Status |
|---|---|---|---|---|---|
| 01 | 12 dtk | Motion text | "One invoice. Financed twice." | Editor video | TODO |
| 02 | 13 dtk | Diagram | Registry terpusat vs chain publik | Slide | TODO |
| 03 | 10 dtk | Logo + tagline | JitsuinFi, tagline nullifier | Slide | TODO |
| 04 | 20 dtk | Screen recording | Web/CLI: buat invoice, buyer sign, financier register | Rekaman layar | TODO |
| 05 | 10 dtk | Screen recording | Explorer: transaksi shielded tanpa isi | Browser | TODO |
| 06 | 20 dtk | Screen recording | Supplier → financier B → tertangkap + bukti | Rekaman layar | TODO |
| 07 | 13 dtk | Terminal + web | `jitsuin verify` + halaman indeks | Terminal + browser | TODO |
| 08 | 12 dtk | Slide | Threat model ringkas | Slide | TODO |
| 09 | 5 dtk | Slide | Tagline + URL | Slide | TODO |

## Aturan visual
- Resolusi export 1920×1080; persiapan rinci (jendela, zoom, profil, data) di [[VID-03 - Checklist Rekaman]].
- Satu warna aksen konsisten; tanpa transisi berlebihan.
- Kursor diperbesar atau di-highlight di bagian demo.
