---
tags: [video, "VID-01"]
---

# VID-01 - Naskah 2 Menit

**Bagian dari:** [[Video-Workspace]] · Terkait: [[VID-02 - Storyboard dan Shot List]] · [[JitsuinFi - Ringkasan Proyek]]

> **Naskah v3 (2026-10-27, HNK-14.T1).** Total **1:56** (cadangan 4 detik; batas keras 2:00). Narasi bahasa Inggris, dibaca user; subtitle disarankan. Mengikuti UI yang live per 27 Okt (landing bab, lobi `/app`, `/try`, supplier → buyer lewat inbox, konsol, `/verify` 真, `/outsider` + `/rates`). Urutan tetap tumpukan D-40: hook N-06, merek N-10, M-07 + M-01 + M-03 (N-08) + M-04, N-09 + N-12, N-15, N-13, tagline. N-07 (Ironwood) **dibuang di v3** karena waktu; tetap boleh dipakai di README atau tanya-jawab. Klik per shot, path persis, dan sumber rekaman ada di [[VID-02 - Storyboard dan Shot List]]; persiapan di [[VID-03 - Checklist Rekaman]].

## Naskah v3 (dipakai)
| Waktu | Shot | Layar | Voice-over (EN, dibaca persis) | Kata |
|---|---|---|---|---|
| 0:00 – 0:11 | S01 | Landing `https://jitsuinfi.vercel.app` hero, overlay tiga centang merah menjadi hijau | "First Brands' lenders never saw an invoice, never asked the buyer, never controlled the cash. JitsuinFi does all three, and no outsider sees the deal." | 26 |
| 0:11 – 0:20 | S02 | Landing bab 2 指紋: tekan "One zat more", digit N berubah | "Japan registers seals so they can't be forged, and the registrar never reads your contracts. JitsuinFi does that for invoices." | 21 |
| 0:20 – 0:24 | S03 | Lobi `/app` (kantor registri), klik ruang "Try to double-finance" | (tanpa narasi; suara ruang atau musik pelan) | 0 |
| 0:24 – 0:46 | S04 | `/try` Case File #0417: ubah nominal → 偽; "Put back the original" → "Offer it to financier B" → 重 + benang merah | "Case File 0417. Kurogane Trading's invoice is sealed by its buyer and already financed. You are financier B. Change one digit: the buyer's seal breaks. Send it as it is: the live testnet board already holds its fingerprint." | 38 |
| 0:46 – 0:57 | S05 | Exhibit A di `/try`, lalu `/verify` → "Use Case File #0417's Exhibit A" → "Hand it to the registry" → 重 | "B takes home Exhibit A. Double-signing gets a validator slashed; here it gets a supplier caught, and anyone can check it." | 21 |
| 0:57 – 1:05 | S06 | `/outsider` palang sensor, lalu `/rates` (k ≥ 5) | "Outsiders see a fingerprint and ciphertext. Rates appear only once five invoices share a class." | 15 |
| 1:05 – 1:26 | S07 | Deal nyata: supplier desktop Write → kirim; buyer di HP (PWA) buka inbox (ikon lonceng) → tanda tangan passkey | "Now a real deal on testnet. The supplier writes an invoice; it lands in the buyer's inbox on a phone, and one passkey touch signs it. Buyers already sign when rules require it, and they earn a payment history." | 39 |
| 1:26 – 1:38 | S08 | Konsol financier: penawaran tersegel dengan cap "Fits your private mandate", terima, "Approve with passkey", rute deal | "Before paying, the lender asks Zcash whether the invoice was sold, and learns nothing else. Its node matches sealed offers against a private mandate: order flow, no order book." | 29 |
| 1:38 – 1:46 | S09 | Buyer: slip 払込票 "Show payment QR" (dipercepat), status Settled 済, "Check it on Verify" → 真 | "Advance and repayment stay shielded. The settled deal checks out: genuine." | 11 |
| 1:46 – 1:52 | S10 | Kartu batas (slide HNK-18.T2) atau panel "Notice: what this does not stop" di `/try` | "A fake invoice the buyer itself co-signs is out of scope; credit diligence still applies." | 15 |
| 1:52 – 1:56 | S11 | Tagline + `jitsuinfi.vercel.app` + `github.com/JitsuinFi` | "Zcash stops double-spending. JitsuinFi stops double-financing." | 6 |

Total narasi 221 kata dalam 116 detik (rata-rata 1,9 kata per detik; S08 paling rapat, 2,4 kata per detik). Kalau rekaman suara melewati 1:58, potong dulu kalimat kedua S07 ("Buyers already sign…"), lalu S03.

### Catatan rekaman v3
- Semua layar dari production (`jitsuinfi.vercel.app`, konsol `jitsuinfi-console.vercel.app` milik user); papan testnet hidup, bukan salinan bawaan. Kalau banner "saved board" muncul di `/try`, ulangi setelah node menjawab.
- Bagian menunggu blok (S07 – S09) dipercepat dan diberi label "sped up" di pojok.
- Txid yang tampil harus nyata dan ada di README (setelah tabel txid production ditambahkan, lihat [[Submission - Checklist Publikasi Repo]]).
- Data `TES-` saja; Kurogane Trading fiktif. Tidak ada nama, email, alamat wallet pribadi, seed, kode pairing, atau tautan kontak yang terbaca di layar.
- Jangan pakai "$2.3B financed twice" (W-15); label jaringan "Zcash testnet, Ironwood pool" (W-17).

## Naskah v2 (2026-10-22, diganti v3)
> **Naskah v2 (2026-10-22, D-40).** Total 1:55 (cadangan 5 detik). Narasi bahasa Inggris, subtitle opsional. Urutan mengikuti tumpukan D-40: hook N-06, merek N-10, M-07 + M-02 + M-01 + M-03 (N-08) + M-04, N-09 + N-12, N-15, N-13, tagline. Klip 0:22 – 0:55 juga berdiri sendiri sebagai klip 20 detik (VID-07). N-07 dipakai versi yang sudah dicek fakta di [[JDG-06 - Narasi dan Positioning]].

| Waktu | Segmen | Layar (app) | Narasi |
|---|---|---|---|
| 0:00 – 0:15 | Hook N-06 | Tiga baris dengan centang merah: "saw the invoice", "asked the buyer", "controlled the cash"; satu per satu menjadi hijau | "First Brands' lenders never saw an invoice, never asked the buyer, never controlled the cash. JitsuinFi does all three, and no outsider sees the deal." |
| 0:15 – 0:22 | Merek N-10 + N-07 | Landing: noren 登記所, seal 印 | "Japan registers seals so they can't be forged, and the registrar never reads your contracts. We register invoices so they can't be sold twice, and nobody reads them." |
| 0:22 – 0:32 | M-07 + M-02 | `/try`: Case File #0417, amplop kit invoice tersegel terbuka | "Case File 0417. Kurogane Trading has one invoice, signed by its buyer, and two financiers this morning. You are the second." |
| 0:32 – 0:52 | M-01 dua pintu keluar | `/try`: ubah nominal → cap 偽 (seal retak); kirim apa adanya → cap 重 dari papan testnet hidup | "Change one digit, and the buyer's seal breaks. Send it as it is, and the board already holds its fingerprint. Every try ends here or here." |
| 0:52 – 1:05 | M-03 klimaks, N-08 | Exhibit A diunduh, `/verify` menampilkan 重 dengan dua tanda tangan supplier | "Double-signing gets a validator slashed. Here it gets a supplier caught: the second signature is the proof, and anyone can check it." |
| 1:05 – 1:15 | M-04 lensa | Tahan tombol: invoice terbakar menjadi N, ciphertext, tinggi blok | "This is all the chain shows: a fingerprint and ciphertext. No parties, no amount." |
| 1:15 – 1:30 | N-09 + N-12, N-15 | Konsol financier: penawaran tersegel di kotak surat, cap 適/外/待 dari 内規, rute deal 照 署 登 印 金 済 | "Before paying, any lender asks Zcash whether the invoice was sold, and learns nothing else. Buyers already sign when rules require it. Each financier matches sealed offers against its own private mandate: order flow, no order book." |
| 1:30 – 1:45 | Batas N-13 | Panel "what this does not stop" + tautan threat model | "A fake invoice the buyer itself co-signs is out of scope: credit diligence still applies. What leaks and what is trusted is in our threat model." |
| 1:45 – 1:55 | Penutup | Tagline + URL demo dan repo | "Zcash stops double-spending. JitsuinFi stops double-financing." |

## Catatan rekaman
- Rekam di build production setelah deploy #42 – #44; papan testnet hidup (`/api/board`), bukan salinan.
- Bagian menunggu konfirmasi dipercepat dengan label "sped up".
- Txid yang tampil harus nyata dan tercantum di README (W-09).
- Data `TES-` saja; tidak ada nama atau data perusahaan nyata (M-07 memakai Kurogane Trading fiktif).
- Jangan pakai "$2.3B financed twice" (W-15).

## Naskah v1 (2026-10-18, diganti)
> Draf. Total target 1:55 (sisakan 5 detik cadangan). Narasi bahasa Inggris (juri internasional); subtitle opsional.

| Waktu | Segmen | Layar | Narasi (draf) |
|---|---|---|---|
| 0:00–0:12 | Hook | Teks besar: "One invoice. Financed twice." | "Invoice fraud starts simple: a supplier sells the same invoice to two financiers." |
| 0:12–0:25 | Masalah | Diagram: registry terpusat vs chain publik | "Today you stop it with a central registry that sees every deal, or a public chain that shows who supplies whom. Both leak trade secrets." |
| 0:25–0:35 | Solusi | Logo JitsuinFi + tagline | "Zcash stops double-spending. JitsuinFi stops double-financing." |
| 0:35–0:55 | Demo 1: terbit dan daftar | Supplier membuat invoice, buyer menandatangani, financier A memeriksa papan dan mendaftar | "The buyer signs. The financier derives a nullifier, checks the shielded registry, and registers it." |
| 0:55–1:05 | Demo 2: tidak terlihat | Explorer menampilkan transaksi tanpa isi | "On-chain, nobody sees the invoice, the amount, or the parties." |
| 1:05–1:25 | Demo 3: momen kunci | Supplier mencoba ke financier B → tertangkap + bukti tanda tangan ganda | "Same invoice, second financier: caught instantly, with cryptographic proof the supplier signed twice." |
| 1:25–1:38 | Verifikasi juri | Terminal `jitsuin verify` atas txid mainnet + halaman indeks suku bunga | "Anyone can verify the registry, and see the public rate index: price public, participants private." |
| 1:38–1:50 | Kejujuran | Slide threat model singkat | "What leaks, what doesn't, and what's still trusted: it's all in our threat model." |
| 1:50–1:55 | Penutup | Tagline + URL repo dan demo | "JitsuinFi. Every invoice, sealed once." |

## Catatan
- Bagian demo dipercepat; tampilkan label "sped up" saat menunggu konfirmasi.
- Semua txid yang tampil harus nyata dan dicantumkan di README.
- Pakai data `TES-` yang terlihat realistis, bukan data pribadi siapa pun.
