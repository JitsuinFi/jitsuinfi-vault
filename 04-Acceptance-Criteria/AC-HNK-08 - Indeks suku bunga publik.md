---
tags: [ac, "HNK-08"]
type: ac
id: HNK-08
phase: F4
lead: Dex
owners: [Dex, Hans]
status: PARSIAL
updated: 2026-10-19
---

# AC-HNK-08 - Indeks suku bunga publik

> **Peta link:** [[AC Hub]] · [[Backlog]] · **AC** · [[TEST-HNK-08 - Indeks suku bunga publik|Test]] · [[ES-HNK-08 - Indeks suku bunga publik|Exec Summary]]

**Item:** HNK-08 · **Fase:** F4 · **Dependency:** HNK-04

**Lead:** Dex #dex · **Tim:** Dex #dex, Hans #hans 

## Deskripsi
Entri membawa bucket diskon dan tenor (tanpa nominal dan pihak). Indeks dihitung dari papan dan ditampilkan: "harga publik, partisipan gelap".

## Acceptance criteria
Status per kriteria: `TODO` / `PASS` / `FAIL` / `BLOCKED`, wajib dengan tanggal dan bukti (commit, txid, log, id tes).

| ID | Kriteria | Status | Tanggal | Bukti |
|---|---|---|---|---|
| AC-HNK-08.1 | Bucket diskon dan tenor ada di entri dan tervalidasi. | PASS | 2026-10-19 | jitsuinfi-zcash PR #5 (`90a64c7`): kelas di offset 70/71 entri (format tidak berubah), tabel kelas di `jitsuin-core/src/index.rs` dan [[Format Data]]. `validate_classes` / `BoardEntry::classes()`: dua-duanya diisi atau `0/0`, selain itu `Error::InvalidBucket`. `classes_for(nominal, advance, tgl advance, jatuh tempo)` memberi kode yang ditandatangani supplier. Tes: `classes_cover_their_ranges_without_gaps`, `deal_classes_from_amounts_and_dates`, `entry_classes_are_validated`. Decoder tidak diubah: entri dengan kelas salah tetap dihitung sebagai registrasi (cek pembiayaan ganda tidak bisa dihindari), hanya dikeluarkan dari indeks. |
| AC-HNK-08.2 | Indeks bisa dihitung ulang dari papan oleh siapa pun (reproducible). | PASS | 2026-10-19 | `jitsuin_board::rate_index` mengurutkan entri ke urutan papan dulu, jadi dua scanner dengan papan yang sama mendapat indeks identik (`rate_index_is_the_same_in_any_collection_order`: urutan dibalik → hasil sama). Siapa pun: `jitsuin index --ufvk <UFVK papan>` atau `--board <snapshot>`. Uji dengan papan sungguhan = I-HNK-08.1. |
| AC-HNK-08.3 | Indeks hanya ditampilkan bila minimal k entri per bucket (k dicatat). | PASS | 2026-10-19 | **k = 5** (`jitsuin_core::index::K`, usulan D-27). Kelas tenor, dan kelas diskon di dalamnya, hanya ditampilkan bila punya ≥ 5 invoice; kelas di bawah k tidak diberi angka (sisa per tenor hanya sebagai total "other"). k bisa dinaikkan (`--k 8`), tidak bisa diturunkan. Tes: `classes_below_k_are_not_shown_and_k_cannot_be_lowered`, `index_json_and_higher_k`. |
| AC-HNK-08.4 | Tampilan indeks tersedia di web. | TODO | 2026-10-19 | HNK-08.T3 (Hans, dari Dave, D-35). Bahan siap: `jitsuin index --json` memuat tabel kelas + label; web perlu entri dengan kelas (`registerEntry` di jitsuin-wasm masih menandatangani `0/0`). |

## Deviasi
_Kosong._ Kalau implementasi menyimpang dari keputusan, tulis di sini **dan** di [[Backlog]] bagian Log Deviasi. Tidak ada perubahan diam-diam.
