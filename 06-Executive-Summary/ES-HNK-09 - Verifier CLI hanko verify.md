---
tags: [es, "HNK-09"]
type: es
id: HNK-09
phase: F4
lead: Dex
owners: [Dex, Dave]
status: PARSIAL
updated: 2026-10-19
---

# ES-HNK-09 - Verifier CLI hanko verify

> **Peta link:** [[Exec Summary Hub]] · [[Backlog]] · [[AC-HNK-09 - Verifier CLI hanko verify|AC]] · [[TEST-HNK-09 - Verifier CLI hanko verify|Test]] · **Exec Summary**

**Lead:** Dex #dex · **Tim:** Dex #dex, Dave #dave

## Apa diubah
- Crate baru `jitsuin-cli` (biner `jitsuin`) di jitsuinfi-zcash PR #4: `jitsuin verify` membaca papan secara live dengan UFVK papan (wallet watch-only `zcash-devtool` + `jitsuin_board::scan`) atau dari snapshot JSON (bentuk yang sama dengan data papan untuk web app), menampilkan semua entri dalam urutan papan, lalu mengecek bukti tanda tangan ganda dan bundel verifikasi. Semua vonis memakai fungsi `jitsuin-core`/`jitsuin-board`, tanpa aturan baru. Output teks atau `--json`; exit 0 lulus, 1 ada cek gagal, 2 salah pakai/input/jaringan.
- `jitsuin-wallet`: `Devtool::init_fvk` (wallet view-only; scan pertama wajib `--birthday` supaya tidak mulai dari ujung chain).
- `Dockerfile` (zcash-devtool `b532d4c` + `jitsuin`, runtime Debian slim, non-root) dan `.dockerignore` (tanpa wallet/key).
- Workflow `verifier-image.yml`: `docker build` tanpa cache di runner bersih (waktu dicatat), contoh di dalam container harus sama dengan `expected-output.txt`, langkah scan papan sungguhan aktif bila variabel `BOARD_UFVK` diisi.
- `examples/verify/`: papan, bukti, dan bundel contoh (sintetis, txid `a1a1…`) + output yang diharapkan.
- README "Verify the board": perintah Docker dan `cargo install`.

## Hasil vs KPI (angka riil)
| KPI | Target | Aktual |
|---|---|---|
| Waktu instal sampai hasil | ≤ 10 menit | **gagal untuk build dari sumber**: 9 mnt 10 dtk dan 14 mnt 28 dtk pada dua build dingin di runner GitHub 4 vCPU (550 dan 868 dtk, hampir semuanya kompilasi zcash-devtool) + verifikasi contoh < 1 dtk; image 197 MB. Jalur ≤ 10 mnt = image jadi (pull), menunggu izin Hans |
| Langkah README yang gagal | 0 | 0 untuk contoh (CI menjalankan perintah README dan `diff`); papan sungguhan belum |

## Status
**PARSIAL** — T1 dan T2 di PR #4 (menunggu review Hans). AC-HNK-09.3 PASS. AC-HNK-09.1 dan SPK-11 FAIL untuk build dari sumber (9–15 menit); fallback image jadi menunggu izin Hans (usulan D-28). Sisa: scan papan sungguhan (UFVK papan, AC-HNK-09.2 dan I-HNK-09.1), README papan sungguhan (T3, Dave).

## Risiko tersisa
- Scan live butuh `zcash-devtool`, yang berat untuk di-build dari sumber. Jalur cepat untuk juri = image jadi (registry) atau binary prebuilt (fallback SPK-11); menerbitkannya butuh izin Hans.
- Parser `jitsuin-wallet` terikat output teks devtool commit `b532d4c` (ES-HNK-03); image mem-pin commit itu.
- Repo masih private sampai 28 Okt: `cargo install --git` repo JitsuinFi baru bisa setelah publik; sekarang `--path` dari checkout.
- Urutan tx dalam blok berasal dari lightwalletd (sama dengan HNK-04); juri yang curiga bisa memakai `--lightwalletd` lain.

## Bukti
- Commit: `0bdd311` (jitsuinfi-zcash PR #4, branch `dex/hnk-09-verify`)
- ID tes: U-HNK-09.1 PASS, U-HNK-09.2 PASS, I-HNK-09.1 BLOCKED (UFVK papan)
- Persetujuan user untuk push/deploy: push branch + PR atas izin Dex; merge menunggu review Hans
