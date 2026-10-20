---
tags: [es, "HNK-08"]
type: es
id: HNK-08
phase: F4
lead: Dex
owners: [Dex, Hans]
status: PARSIAL
updated: 2026-10-19
---

# ES-HNK-08 - Indeks suku bunga publik

> **Peta link:** [[Exec Summary Hub]] · [[Backlog]] · [[AC-HNK-08 - Indeks suku bunga publik|AC]] · [[TEST-HNK-08 - Indeks suku bunga publik|Test]] · **Exec Summary**

**Lead:** Dex #dex · **Tim:** Dex #dex, Hans #hans 

## Apa diubah
- `jitsuin-core/src/index.rs` (jitsuinfi-zcash PR #5): tabel kelas diskon (7) dan tenor (5) + `0` = tidak diungkap; `classes_for` menghitung kode dari nominal, advance, dan tanggal; `validate_classes` / `BoardEntry::classes`; `RateIndex::compute`: tiap N sekali dengan entri pertamanya, per kelas tenor: jumlah invoice, median bawah kelas diskon, kelas diskon ≥ k, sisanya total "other". `Error::InvalidBucket` baru.
- `jitsuin-board::rate_index`: mengurutkan ke urutan papan dulu (reproducible).
- `jitsuin index` (`--ufvk` atau `--board`, `--k`, `--json` dengan tabel kelas) + contoh pasar `examples/index/`.
- [[Format Data]] bagian "Bucket indeks" diisi tabel kelas; [[Threat Model]] baris bucket diperjelas + baris baru "entri palsu menggeser indeks". Menutup temuan pra-review TM #5 (klaim ambang k tanpa kode).

## Hasil vs KPI (angka riil)
| KPI | Target | Aktual |
|---|---|---|
| Reproducibility indeks | hasil identik dari 2 scanner | identik (urutan koleksi dibalik → `RateIndex` sama); papan sungguhan belum |
| Ambang k | dicatat | k = 5 (`index::K`), bisa dinaikkan, tidak bisa diturunkan |

## Status
**PARSIAL** — T1 dan T2 sudah di `main` (`61ca636`). PR #5 sempat ditumpuk di branch PR #4, jadi saat di-merge isinya masuk ke branch itu, bukan ke `main`; Hans memindahkannya ke `main` lewat PR #6 (19 Okt). AC 08.1–08.3 PASS. Sisa: halaman web (T3, Hans, dari Dave, D-35), uji papan sungguhan (I-HNK-08.1), web/wasm harus menandatangani kelas sungguhan.

## Risiko tersisa
- Orang luar tidak bisa mengecek tanda tangan supplier: entri griefing yang lebih dulu menentukan kelas N itu, dan N palsu ikut terhitung. Setiap posting butuh fee; pemegang bundel bisa mengecek dealnya sendiri.
- Kelas tiap entri tetap terbaca pemegang viewing key papan; k hanya melindungi agregat yang ditampilkan.
- `registerEntry` di jitsuin-wasm masih menandatangani `0/0`, jadi indeks live kosong sampai web memakai `classes_for` (Hans).
- Tabel kelas dan k = 5 masih usulan (D-27); kalau Hans mengubahnya, entri lama tetap valid selama kodenya tidak dipakai ulang untuk arti lain.

## Bukti
- Commit: `90a64c7` (jitsuinfi-zcash PR #5, branch `dex/hnk-08-index`)
- ID tes: U-HNK-08.1 PASS, U-HNK-08.2 PASS, I-HNK-08.1 BLOCKED
- Persetujuan user untuk push/deploy: push branch + PR atas izin Dex; di-review dan di-merge Hans 2026-10-19 (PR #5, lalu PR #6 ke `main`, `61ca636`)
