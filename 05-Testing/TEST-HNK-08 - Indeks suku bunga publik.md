---
tags: [test, "HNK-08"]
type: test
id: HNK-08
phase: F4
lead: Dex
owners: [Dex, Hans]
unit: PASS
integrasi: BLOCKED
e2e: TODO
updated: 2026-10-19
---

# TEST-HNK-08 - Indeks suku bunga publik

> **Peta link:** [[Testing Hub]] · [[Backlog]] · [[AC-HNK-08 - Indeks suku bunga publik|AC]] · **Test** · [[ES-HNK-08 - Indeks suku bunga publik|Exec Summary]]

**Lead:** Dex #dex · **Tim:** Dex #dex, Hans #hans 

## 1. Unit
Logika murni, cepat, tanpa DB dan tanpa chain.

| ID | Kasus | Hasil | Tanggal | Bukti |
|---|---|---|---|---|
| U-HNK-08.1 | Agregasi bucket | PASS | 2026-10-19 | `jitsuin-core` `aggregation_counts_each_invoice_once_with_its_first_entry` (12 entri → 11 invoice, entri kedua N 0 diabaikan, median bawah, "other"), `settled_entries_do_not_count`; `jitsuin-board` `rate_index_is_the_same_in_any_collection_order`; CLI `index_sample_matches_the_expected_output` (`examples/index/`: 18 entri, 17 invoice, 1 tidak diungkap, 1 kelas salah) — PR #5 (`90a64c7`) |
| U-HNK-08.2 | Ambang k | PASS | 2026-10-19 | `classes_below_k_are_not_shown_and_k_cannot_be_lowered` (4 invoice → tidak tampil; 5 → tampil; k=1 dinaikkan ke 5; k=6 menyembunyikan lagi), `index_json_and_higher_k` (kelas di bawah k tanpa angka di JSON; `--k 6` → 1 kelas; `--k 2` ditolak exit 2) |

## 2. Integrasi
Skrip vs DB/chain sungguhan. Semua artefak memakai prefix `TES-` (invoice, akun, label, order).

| ID | Skenario | Hasil | Tanggal | Bukti (txid/log) |
|---|---|---|---|---|
| I-HNK-08.1 | Indeks dari entri `TES-` di papan uji | BLOCKED | 2026-10-19 | Butuh ≥ 5 entri `TES-` berkelas di papan uji testnet (`registerEntry` web masih `0/0`) dan UFVK papan untuk `jitsuin index --ufvk`. Dex belum punya wallet testnet. |

**Bukti pembersihan:** sisa artefak off-chain `TES-` = **0** (uji unit dan contoh sintetis saja). Artefak on-chain tidak bisa dihapus; catat txid-nya di tabel di atas. Data produksi tidak boleh tersentuh.

## 3. E2E
Panduan langkah demi langkah untuk user.

- [x] Buka halaman indeks dan cocokkan dengan hasil `jitsuin index`.

| Langkah | Hasil diharapkan | Hasil aktual | Status |
|---|---|---|---|
| 1 | Buka `app.html#/index`, pilih snapshot papan, tekan Show index; cocokkan dengan `jitsuin index --board` file yang sama | 2026-10-20, build produksi lokal: papan contoh `examples/index/board-sample.json`: "2 of 5 tenor classes published", 31-60 hari 9 invoice median 2-3% (2-3%: 6, other: 3), 61-90 hari 5 invoice median 3-5%, sisanya "fewer than 5 invoices", sama baris per baris dengan `expected-output.txt`; k = 6: 1 kelas; k = 2 dinaikkan ke 5. Papan testnet: 6 invoice, tidak ada kelas, sama dengan `expected-index.txt`. Mobile 375 px: tanpa scroll horizontal | PASS |
