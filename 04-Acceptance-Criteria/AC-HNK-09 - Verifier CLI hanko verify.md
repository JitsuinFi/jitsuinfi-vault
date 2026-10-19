---
tags: [ac, "HNK-09"]
type: ac
id: HNK-09
phase: F4
lead: Dex
owners: [Dex, Dave]
status: PARSIAL
updated: 2026-10-19
---

# AC-HNK-09 - Verifier CLI hanko verify

> **Peta link:** [[AC Hub]] · [[Backlog]] · **AC** · [[TEST-HNK-09 - Verifier CLI hanko verify|Test]] · [[ES-HNK-09 - Verifier CLI hanko verify|Exec Summary]]

**Item:** HNK-09 · **Fase:** F4 · **Dependency:** HNK-04, HNK-07, SPK-11

**Lead:** Dex #dex · **Tim:** Dex #dex, Dave #dave

## Deskripsi
CLI untuk juri: memindai papan dari data mainnet nyata dan memverifikasi entri serta bukti tanda tangan ganda, tanpa butuh ZEC.

## Acceptance criteria
Status per kriteria: `TODO` / `PASS` / `FAIL` / `BLOCKED`, wajib dengan tanggal dan bukti (commit, txid, log, id tes).

| ID | Kriteria | Status | Tanggal | Bukti |
|---|---|---|---|---|
| AC-HNK-09.1 | Instal via Docker atau `cargo install` di mesin bersih ≤ 10 menit. | FAIL | 2026-10-19 | Dua build dingin di runner GitHub bersih (ubuntu-latest, 4 vCPU), tanpa cache: **550 dtk** (https://github.com/JitsuinFi/jitsuinfi-zcash/actions/runs/39239022151; zcash-devtool 7 mnt 23 dtk + jitsuin 1 mnt 10 dtk) dan **868 dtk** (https://github.com/JitsuinFi/jitsuinfi-zcash/actions/runs/39239847330; zcash-devtool 12 mnt 3 dtk + jitsuin 1 mnt 57 dtk). Hampir semua waktu = kompilasi `zcash-devtool` dari sumber, dan itu juga yang dilakukan `cargo install`. Verifikasi contoh setelahnya < 1 dtk, image 197 MB. Build dari sumber tidak bisa dijamin ≤ 10 menit → fallback [[SPK-11 - Distribusi verifier CLI di mesin bersih\|SPK-11]]: image jadi di registry (pull ±200 MB) atau binary prebuilt, butuh izin Hans (usulan D-28). |
| AC-HNK-09.2 | Memverifikasi entri papan mainnet dan bundel bukti yang dicantumkan di README. | TODO | 2026-10-19 | Kode siap (jitsuinfi-zcash PR #4, `0bdd311`): `jitsuin verify --ufvk` memindai papan lewat `jitsuin_board::scan`, lalu mengecek bukti tanda tangan ganda (`verify` + `verify_proof_on_board`) dan bundel (`verify` + `bundle_on_board`). Sudah jalan pada papan contoh (sintetis) di dalam container. Menunggu UFVK + blok pertama papan (D-11 masih usulan) dan entri mainnet (D-13: mainnet hanya untuk demo akhir). |
| AC-HNK-09.3 | Tidak butuh spending key atau ZEC. | PASS | 2026-10-19 | `jitsuin verify` hanya menerima UFVK: `init-fvk` membuat akun view-only (devtool menolak `send` dari akun view-only, SPK-05). Tidak ada opsi seed, identity, atau spending key. Papan contoh diverifikasi tanpa jaringan dan tanpa ZEC (`tests/samples.rs`, CI `verifier image`). |
| AC-HNK-09.4 | README berisi perintah persis dan output yang diharapkan. | TODO | 2026-10-19 | Sebagian: README PR #4 berisi perintah Docker dan `cargo install` persis + output contoh (`examples/verify/expected-output.txt`, dicek `diff` di CI). Perintah untuk papan sungguhan + outputnya = HNK-09.T3 (Dave), setelah UFVK papan ada. |

## Deviasi
_Kosong._ Kalau implementasi menyimpang dari keputusan, tulis di sini **dan** di [[Backlog]] bagian Log Deviasi. Tidak ada perubahan diam-diam.
