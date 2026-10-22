---
tags: [test, "HNK-32"]
type: test
id: HNK-32
phase: F6
unit: TODO
integrasi: TODO
e2e: TODO
updated: 2026-10-22
---

# TEST-HNK-32 - Perbaikan hasil audit flow

> **Peta link:** [[Testing Hub]] · [[Backlog]] · [[AC-HNK-32 - Perbaikan hasil audit flow|AC]] · **Test** · [[ES-HNK-32 - Perbaikan hasil audit flow|Exec Summary]]

## 1. Unit
Logika murni, cepat, tanpa DB dan tanpa chain.

| ID | Kasus | Hasil | Tanggal | Bukti |
|---|---|---|---|---|
| U-HNK-32.1 | Segel buyer ditolak untuk PDF salah dan financier lain | PASS | 2026-10-22 | `tests/buyer-letter.test.ts` (PDF salah, tanpa PDF, invoice lain, segel supplier tidak berlaku); E2E lokal testnet `TES-INV-FE-53023` (FE stack T1 – T5, node T3 + T4): `jitsuin verify --bundle` DEAL VERIFIED 3/3 (entri `877c2502…5c3f`, settled `327391f2…7716`, tepat waktu): segel lolos setelah "Check letter" |
| U-HNK-32.2 | QR pelunasan ditolak untuk surat tanpa rantai `Sealed` atau surat yang berbeda dari surat tersimpan | PASS | 2026-10-22 | `payProblems` di `tests/buyer-letter.test.ts`; E2E lokal testnet `TES-INV-FE-53023` (FE stack T1 – T5, node T3 + T4): `jitsuin verify --bundle` DEAL VERIFIED 3/3 (entri `877c2502…5c3f`, settled `327391f2…7716`, tepat waktu): surat tempelan ditolak "this is not the letter you sealed for this invoice", QR asli dibayar `3329e0a9…ec40` |
| U-HNK-32.3 | Setiap varian `Stop` dipetakan ke kode dan kalimat | PASS | 2026-10-22 | node `a_stopped_deal_shows_a_code_and_the_entry_that_came_first`; frontend `stopReason` di `tests/explain.test.ts` (kode baru dan dump lama) |
| U-HNK-32.4 | Hitungan konfirmasi dari tinggi entri dan tip | PASS | 2026-10-22 | node `confirmations_count_from_the_entry_height_to_the_tip`; E2E lokal testnet `TES-INV-FE-53023` (FE stack T1 – T5, node T3 + T4): `jitsuin verify --bundle` DEAL VERIFIED 3/3 (entri `877c2502…5c3f`, settled `327391f2…7716`, tepat waktu): meta node `entry_confirmations: 3` |

## 2. Integrasi
Skrip vs DB/chain sungguhan. Semua artefak memakai prefix `TES-` (invoice, akun, label, order).

| ID | Skenario | Hasil | Tanggal | Bukti (txid/log) |
|---|---|---|---|---|
| I-HNK-32.1 | E2E lokal testnet diperluas (HNK-32.T6): kirim key, simpan kontak, tolak penawaran, permintaan riwayat, lalu siklus sampai settled | PASS | 2026-10-22 | Deal `TES-INV-FE-1185` (skrip `e2e-fe2.mjs`): kontak supplier dan buyer saling disimpan dan sidik jari ditandai compared; key buyer lewat relay mengisi baris buyer invoice tanpa salin-tempel; mandat privat `min_buyer_history: 0` (POST 200), node meminta riwayat, buyer mengirim, konsol "Buyer history passed"; konsol "Entry posted: 0 of 1 confirmations"; surat dicek sebelum segel; surat tempelan ditolak; advance `1169dac7…ffde39b5`, pelunasan `262b1ac7…c46e`, settled `06eabeda…3746`, `/verify` "Bundle is genuine". Ulang penuh `TES-INV-FE-11588`: semua langkah lulus, kartu riwayat buyer "1 on time · 0 late · 0 open · 0 defaulted"; penawaran kedua `TES-INV-FE-18524-D` ditolak, kartu supplier "Declined — TES: outside this financier's rules." |
| I-HNK-32.2 | File bukti yang diunduh dari konsol lolos `/verify` | TODO | — | — |

**Bukti pembersihan:** sisa artefak off-chain `TES-` = _TODO_ (target **0**). Artefak on-chain tidak bisa dihapus; catat txid-nya di tabel di atas. Data produksi tidak boleh tersentuh.
