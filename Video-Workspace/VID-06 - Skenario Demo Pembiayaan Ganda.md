---
tags: [video, "VID-06"]
---

# VID-06 - Skenario Demo Pembiayaan Ganda

**Bagian dari:** [[Video-Workspace]] · Item: HNK-07.T5 di [[Backlog]] · Terkait: [[VID-01 - Naskah 2 Menit]] · [[TEST-HNK-07 - Deteksi pembiayaan ganda dan bukti tanda tangan ganda|TEST-HNK-07]]

> Naskah adegan "momen kunci" (VID-01 menit 1:05–1:25), 2026-10-18. Memakai artefak testnet yang sudah ada, jadi bisa direkam tanpa menunggu konfirmasi baru.

## Cerita
Supplier yang sama mencoba menjual invoice `TES-INV-0003` ke financier kedua. Financier B memeriksa papan sebelum membayar, menemukan N sudah terdaftar, lalu mendapat bukti bahwa supplier menandatangani dua kali. Tidak ada uang yang berpindah.

## Persiapan
- [ ] Web app berjalan (`npm run build && npm run preview` di `jitsuinfi-frontend`), tab Verify terbuka.
- [ ] File bukti dari `proof-it` disiapkan (bukti dari tawaran, 710 karakter) sebagai `double-signature.proof.txt`.
- [ ] Terminal dengan output `proof-it` (testnet) siap ditampilkan.
- [ ] Tidak ada secret atau seed di layar.

## Adegan
| # | Durasi | Layar | Yang terjadi | Narasi |
|---|---|---|---|---|
| 1 | 4 dtk | Terminal | Baris `1 financier B stopped: AlreadyFinanced, winner 33b8f3b0.. (no payment, no tx)` | "A second financier gets the same invoice. Before paying, it checks the board." |
| 2 | 4 dtk | Terminal | Baris `2 offer proof: … offline valid` | "It already holds the supplier's signed offer. That is all it needs." |
| 3 | 8 dtk | Web, tab Verify | Tempel bukti → klik Verify → banner merah "Caught: the supplier signed this invoice twice" + dua commitment berbeda | "Two registrations, one invoice, both signed with the supplier's key from the invoice the buyer signed. Verified in the browser." |
| 4 | 4 dtk | Web, tab "What outsiders see" | Tabel publik vs tersembunyi + kartu explorer | "Outsiders only see hashes. No parties, no amounts." |

## Varian balapan (opsional, kalau waktu cukup)
Kedua entri sudah di papan: `33b8f3b0…` (blok 4509299) dan `05d5aa7a…` (blok 4509521). Bukti dari papan menunjukkan urutan keduanya.

## Bukti untuk deskripsi
- Entri A `33b8f3b0aa754e790e9c7fac0ae7dc08ce8612a8c26620d551d790e1ea390a56`
- Entri B `05d5aa7a02a33c14d460922468745fb4d6d814daa83989eed22b21c0540c79eb`
