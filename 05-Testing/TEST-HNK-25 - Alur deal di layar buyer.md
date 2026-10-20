---
tags: [test, "HNK-25"]
type: test
id: HNK-25
phase: F5
unit: PASS
integrasi: PARSIAL
e2e: TODO
updated: 2026-10-20
---

# TEST-HNK-25 - Alur deal di layar buyer

> **Peta link:** [[Testing Hub]] · [[Backlog]] · [[AC-HNK-25 - Alur deal di layar buyer|AC]] · **Test** · [[ES-HNK-25 - Alur deal di layar buyer|Exec Summary]]

## 1. Unit
Logika murni, cepat, tanpa DB dan tanpa chain.

| ID | Kasus | Hasil | Tanggal | Bukti |
|---|---|---|---|---|
| U-HNK-25.1 | `k` dihitung dari rantai tertambat | PASS | 2026-10-20 | `jitsuin-board` `the_next_index_comes_from_the_anchored_chain`, wasm `history_and_proofs_in_the_browser` (`88af897`); `tests/buyer-history.test.ts` (`0e59952`), `npm test` 44/44 |
| U-HNK-25.2 | QR ditolak untuk surat belum `Sealed` | TODO | — | — |
| U-HNK-25.3 | Cek sebelum tanda tangan (PDF dan key) | PASS | 2026-10-20 | jitsuinfi-frontend `tests/buyer-check.test.ts` (3 tes): keduanya benar = siap; PDF salah atau tidak ada = tanda tangan mati; key lain ditolak lebih dulu (`cc9abb1`, PR #11) |

## 2. Integrasi
Skrip vs DB/chain sungguhan. Semua artefak memakai prefix `TES-` (invoice, akun, label, order).

| ID | Skenario | Hasil | Tanggal | Bukti (txid/log) |
|---|---|---|---|---|
| I-HNK-25.1 | Pembayaran QR testnet sampai `Settled` | TODO | — | — |
| I-HNK-25.2 | Layar buyer di browser (dev server, authenticator palsu): sign up `tes_buyer2`; kunci berikutnya `#0`; tanda tangan invoice `TES-INV-K0` tanpa mengetik `k`; sertifikat #0 tersimpan, terbit ulang ditolak, `#1`; papan dengan entri bertag: `#1`; papan kosong: sertifikat #0 dibuang, `#0`; papan dengan entri tetapi perangkat tanpa sertifikat: peringatan "history is ahead of this device" dan penerbitan diblokir | PASS | 2026-10-20 | IndexedDB dan profil di origin 5173 dihapus (sisa 0) |
| I-HNK-25.3 | Layar buyer, build produksi, sesi buyer test data, invoice `TES-INV-T25` (PDF syarat 0.05 ZEC, 30 hari) | PASS | 2026-10-20 | Tanpa PDF: 待 "Add the terms PDF"; PDF lain: 拒 "The PDF is not the invoiced document"; invoice untuk key lain: 拒 "Not addressed to you"; keduanya benar: 認 "Ready to sign", key #0, tanda tangan jadi; invoice diedit: tanda tangan terkunci lagi. Artefak uji di scratchpad sesi, dihapus |

**Bukti pembersihan:** sisa artefak off-chain `TES-` = _TODO_ (target **0**). Artefak on-chain tidak bisa dihapus; catat txid-nya di tabel di atas. Data produksi tidak boleh tersentuh.

## 3. E2E
Panduan langkah demi langkah untuk user.

- [ ] Tanda tangani invoice
- [ ] Setujui permintaan riwayat
- [ ] Segel surat
- [ ] Bayar QR
- [ ] Lihat riwayat saya

| Langkah | Hasil diharapkan | Hasil aktual | Status |
|---|---|---|---|
| 1 | _TODO_ | — | TODO |
