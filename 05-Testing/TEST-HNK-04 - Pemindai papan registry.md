---
tags: [test, "HNK-04"]
type: test
id: HNK-04
phase: F2
lead: Hans
owners: [Hans, Dex]
unit: PASS
integrasi: TODO
e2e: TODO
updated: 2026-10-17
---

# TEST-HNK-04 - Pemindai papan registry

> **Peta link:** [[Testing Hub]] · [[Backlog]] · [[AC-HNK-04 - Pemindai papan registry|AC]] · **Test** · [[ES-HNK-04 - Pemindai papan registry|Exec Summary]]

**Lead:** Hans #hans · **Tim:** Hans #hans, Dex #dex

## 1. Unit
Logika murni, cepat, tanpa DB dan tanpa chain.

| ID | Kasus | Hasil | Tanggal | Bukti |
|---|---|---|---|---|
| U-HNK-04.1 | Aturan urutan dan tie-break | PASS | 2026-10-17 | `collect_orders_and_rejects_bad_memos`, `collect_requires_tx_order` (`cargo test -p jitsuin-board`) |
| U-HNK-04.2 | Deteksi N ganda dari daftar entri | PASS | 2026-10-17 | `first_valid_entry_wins_and_double_financing_is_reported`, `repost_with_same_commitment_is_not_a_conflict` |
| U-HNK-04.3 | Filter entri invalid | PASS | 2026-10-17 | memo rusak ditolak (`collect_…`), signature salah diabaikan (`first_valid_…`); parser `GetBlock`: `parses_vtx_order_and_reverses_txid`, `rejects_truncated` |

## 2. Integrasi
Skrip vs DB/chain sungguhan. Semua artefak memakai prefix `TES-` (invoice, akun, label, order).

| ID | Skenario | Hasil | Tanggal | Bukti (txid/log) |
|---|---|---|---|---|
| I-HNK-04.1 | Posting 3 entri `TES-` (1 invalid) ke papan uji, lalu scan → 2 valid dan 1 ditolak | PASS | 2026-10-17 | Run integrasi sementara (scratchpad `board-it`), tx `b8a272a87ad9023f3a00a6ffb630e8a584ba0a279af624cda939426c75809970`: 1 entri ganda + 1 griefing + 1 rusak → 2 format-valid, 1 ditolak; lookup `DoubleFinanced`. Script resmi = HNK-04.T4 (Dex) |

**Bukti pembersihan:** sisa artefak off-chain `TES-` = _TODO_ (target **0**). Artefak on-chain tidak bisa dihapus; catat txid-nya di tabel di atas. Data produksi tidak boleh tersentuh.

## 3. E2E
Panduan langkah demi langkah untuk user.

- [ ] `jitsuin board scan` menampilkan tabel entri dan statusnya.

| Langkah | Hasil diharapkan | Hasil aktual | Status |
|---|---|---|---|
| 1 | _TODO_ | — | TODO |
