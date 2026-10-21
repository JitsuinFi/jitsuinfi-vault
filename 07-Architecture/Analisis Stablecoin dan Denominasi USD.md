---
tags: [analisis, "W-04", "D-50"]
type: spec
status: ROADMAP
updated: 2026-10-22
---

# Analisis Stablecoin dan Denominasi USD

> **Peta link:** [[Decision Log]] (D-50) · [[JDG-05 - Register Titik Lemah]] (W-04) · [[Submission - Deskripsi]] · [[Threat Model]] · [[Format Data]]

Pertanyaan user (2026-10-22): bisakah user membayar dengan USDC/USDT, diproses dalam ZEC, dan tetap tersembunyi? Latar: W-04, volatilitas ZEC selama tenor tidak bisa diterima pasar factoring. Pembanding: OwnaFarm ([[JDG-B01 - OwnaFarm]]) memakai token uji `GOLD` di testnet Mantle, tanpa patokan yang disebut, dan tetap juara.

## Fakta (dicek 2026-10-22)
- Zcash hanya punya satu aset, ZEC. Stablecoin belum bisa hidup di shielded pool.
- Zcash Shielded Assets (ZSA, ZIP 226 / 227, QEDIT): token buatan, termasuk stablecoin, di pool Orchard. Kodenya sudah diaudit eksternal, tetapi aktivasi belum diputuskan dan ZSA tidak masuk NU7 (5 November 2026: blok 25 detik, retirement transaksi v4, NSM).
- Wallet Zodl (dulu Zashi) punya swap lewat NEAR Intents: USDC/BTC/SOL masuk menjadi ZEC di alamat shielded baru, dan keluar dari alamat shielded ke aset lain. Laporan pihak ketiga: sekitar $600 juta volume per Maret 2026. Sumber berbeda soal apakah ZEC hasil swap masuk sebentar sebagai transparan sebelum di-shield; cek ulang di dokumentasi Zodl sebelum dipakai di pitch.
- Atomic swap (HTLC) tidak bisa dari sisi shielded karena shielded pool tidak punya script; sisi transparan bocor.
- Railgun / Aztec memberi USDC privat di Ethereum. Tidak ditemukan jalur ke shielded pool Zcash yang terbukti tidak tertaut, dan unshield membuka nominal.

## Inti: pisahkan satuan nilai dari aset yang bergerak
**Invoice berdenominasi USD, dibayar dengan ZEC shielded pada kurs saat bayar.**

```
Buyer (USDC) ──swap Zodl──▶ ZEC shielded, alamat baru ──QR JitsuinFi──▶ financier (shielded)
Financier ──swap keluar dari alamat shielded──▶ USDC (bila mau)
```

- Volatilitas hilang: buyer membayar `nilai USD ÷ harga ZEC` saat jatuh tempo dan memegang ZEC hanya beberapa menit; advance dinilai dengan kurs saat advance. Tidak ada pihak yang memegang ZEC selama tenor kecuali financier memilih begitu.
- Kurs tanpa kepercayaan buta: kuitansi pelunasan buyer mencantumkan kurs dan nilai USD; financier menandatangani balik di entri `settled` (dua tanda tangan yang sudah ada). Dengan feed harga publik bertanda tangan, siapa pun mencocokkan kurs.
- Tidak perlu ZK baru: nominal pembayaran sudah tidak terlihat publik.

## Yang terlihat publik
| Langkah | Terlihat | Tidak terlihat |
|---|---|---|
| Buyer swap USDC → ZEC | alamat USDC buyer mengirim X USDC ke alamat deposit Intents, waktu | untuk invoice apa, financier mana, alamat Zcash tujuan |
| Bayar ZEC ke financier | tidak ada | semuanya |
| Financier swap ZEC → USDC | alamat USDC financier menerima Y | asal dana, deal mana |

Sisa celah: korelasi nominal dan waktu di sisi stablecoin. Mitigasi: bayar dari alamat baru atau exchange, jeda, nominal dibulatkan atau dipecah.

## Kelayakan
| Opsi | Privasi | Siap sekarang | Biaya kerja |
|---|---|---|---|
| Invoice USD + bayar ZEC shielded + swap Zodl | Baik (sisa: korelasi sisi stablecoin) | Swap: ya (mainnet). Protokol: belum | 1,5 – 2 hari (invoice v2, kuitansi berkurs, cek `settled` berkurs, wasm, node, layar); tidak bisa didemokan di testnet (swap hanya mainnet) |
| Stablecoin ZSA di shielded pool | Terbaik, tanpa swap | Tidak (aktivasi belum diputuskan) | Kecil di sisi JitsuinFi: kolom aset di invoice |
| Bridge / swap publik langsung | Lemah | Ya | Kecil, tetapi melanggar kriteria Privacy |
| Atomic swap HTLC | Bocor (transparan) | — | Ditolak |

## Keputusan (D-50)
Submission tetap ZEC. W-04 dijawab dengan narasi tiga lapis: denominasi USD (v2), jalur masuk/keluar lewat swap shielded Zodl yang sudah jalan di mainnet, stablecoin ZSA native bila aktif. Kode v2 hanya setelah E2E testnet lulus dan bila waktu tersisa.

Sumber: CoinDesk (2025-10-09, Zashi + NEAR Intents), Electric Coin Company "Zashi Swaps: Decentralized On-Ramp is Live", forum Zcash (on-ramp dan off-ramp Zashi), KuCoin (beli ZEC tanpa KYC 2026), ZecHub "Arborist Call Update — October 15, 2026", Baltex (Aztec vs Railgun 2026), blog Aztec, HackQuest OwnaFarm.
