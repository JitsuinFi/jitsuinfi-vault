---
tags: [test, "HNK-20"]
type: test
id: HNK-20
phase: F3
lead: Hans
owners: [Hans]
unit: PASS
integrasi: PASS
e2e: TODO
updated: 2026-10-17
---

# TEST-HNK-20 - Riwayat pembayaran buyer standar minimal

> **Peta link:** [[Testing Hub]] · [[Backlog]] · [[AC-HNK-20 - Riwayat pembayaran buyer standar minimal|AC]] · **Test** · [[ES-HNK-20 - Riwayat pembayaran buyer standar minimal|Exec Summary]]

**Lead:** Hans #hans · **Tim:** Hans #hans

## 1. Unit
Logika murni, cepat, tanpa DB dan tanpa chain.

| ID | Kasus | Hasil | Tanggal | Bukti |
|---|---|---|---|---|
| U-HNK-20.1 | Derivasi key per invoice dan sertifikat delegasi | PASS | 2026-10-17 | core `history::tests` (3) + `entry::tests::tagged_register_entry_roundtrip` (`f03cfb1`) |
| U-HNK-20.2 | Verifier bukti riwayat (valid, allowlist, palsu) | PASS | 2026-10-17 | board `history::tests` (4) (`687f2b4`) |
| U-HNK-20.3 | Policy standar minimal di alur financier | PASS | 2026-10-17 | flow `history::tests` (2) + `financier::history_tag_is_required_when_the_deal_has_one` (`e53ce12`) |

## 2. Integrasi
Skrip vs DB/chain sungguhan. Semua artefak memakai prefix `TES-` (invoice, akun, label, order).

| ID | Skenario | Hasil | Tanggal | Bukti (txid/log) |
|---|---|---|---|---|
| I-HNK-20.1 | Bukti riwayat dari entri `settled` hasil HNK-19.T5 diverifikasi terhadap papan testnet | PASS (testnet, DEV-03) | 2026-10-17 | Skenario sendiri `hist-it` (`TES-INV-0004`, buyer baru), karena deal HNK-19.T5 belum memakai key per invoice: entri `89af294e09372d137cb9eae95b7b1ba8c7710bb9d14fe2584b4b8951f8cba4bf`, advance `2c33b0b0104014ff75d0a1e9d644c953724534feba16f96daa98895fc922cd08`, pelunasan `1d9f54ca37c4dcf74e65f79d00102c209d912d0889086376f4078b67190a875e`, `settled` `c60c777ec90cde166324df723ff7695149301f24db0f4d421f68c78dd62845fa`, entri deal 1 `fe7136876222e31921b7dd14ecf8b7a5efdeaf8a0c12179badc15389dd1db608`. Deal 0 lunas tepat waktu, deal 1 gagal bayar, deal 2 ditolak, penyembunyian dan klaim buyer baru terdeteksi. Total 509 dtk |

**Catatan run:** run pertama berhenti di `fin.register` dengan `Error: transport error` dari lightwalletd saat sync; tidak ada transaksi terkirim (dicek di `list-tx` wallet-a). Diperbaiki dengan retry untuk `sync`/`enhance` (`8128d63`, `pay` sengaja tidak di-retry), lalu skenario diulang dan lulus.

**Bukti pembersihan:** sisa artefak off-chain `TES-` = **0** (tidak ada DB; sertifikat hanya di memori). Artefak on-chain tidak bisa dihapus; catat txid-nya di tabel di atas. Data produksi tidak boleh tersentuh.

## 3. E2E
Panduan langkah demi langkah untuk user.

- [ ] _TODO langkah E2E_

| Langkah | Hasil diharapkan | Hasil aktual | Status |
|---|---|---|---|
| 1 | _TODO_ | — | TODO |
