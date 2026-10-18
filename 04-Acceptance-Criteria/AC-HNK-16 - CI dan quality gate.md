---
tags: [ac, "HNK-16"]
type: ac
id: HNK-16
phase: F1
lead: Dex
owners: [Dex]
status: PARSIAL
updated: 2026-10-19
---

# AC-HNK-16 - CI dan quality gate

> **Peta link:** [[AC Hub]] · [[Backlog]] · **AC** · [[TEST-HNK-16 - CI dan quality gate|Test]] · [[ES-HNK-16 - CI dan quality gate|Exec Summary]]

**Item:** HNK-16 · **Fase:** F1 · **Dependency:** SPK-01, SPK-14

**Lead:** Dex #dex · **Tim:** Dex #dex

## Deskripsi
Pipeline yang membuat langkah 1 workflow bisa diverifikasi: `cargo fmt --check`, `cargo check`, `cargo clippy -- -D warnings`, `cargo test`, `npx tsc --noEmit`, build frontend, dan secret scanning (gitleaks). Satu perintah lokal + GitHub Actions (aktif setelah push disetujui user).

## Acceptance criteria
Status per kriteria: `TODO` / `PASS` / `FAIL` / `BLOCKED`, wajib dengan tanggal dan bukti (commit, txid, log, id tes).

| ID | Kriteria | Status | Tanggal | Bukti |
|---|---|---|---|---|
| AC-HNK-16.1 | Satu perintah lokal (misalnya `just check` atau `make check`) menjalankan semua cek dan gagal kalau ada yang merah. | TODO | 2026-10-19 | `bash scripts/check.sh` ada di jitsuinfi-zcash PR #1 (`317d59b`) (fmt, check, clippy -D warnings, test, wasm build, gitleaks; `set -euo pipefail`). Belum dijalankan lokal: Rust belum terpasang di laptop Dex. |
| AC-HNK-16.2 | Workflow GitHub Actions menjalankan cek yang sama dan hijau di branch utama. | TODO | 2026-10-19 | Hijau di PR (https://github.com/JitsuinFi/jitsuinfi-zcash/actions/runs/39152530625): rust 3m10s, gitleaks 6s. Hijau di `main` setelah PR di-merge. |
| AC-HNK-16.3 | Secret scanning: 0 temuan; `.gitignore` mencakup seed, key, `.env`, dan DB wallet. | PASS | 2026-10-19 | gitleaks 8.21.2 seluruh riwayat: 0 temuan (https://github.com/JitsuinFi/jitsuinfi-zcash/actions/runs/39152530625). `.gitignore`: seed, mnemonic, age, `.env*`, sqlite/db, `wallet-*/` + ditambah `*.key`, `*.pem`, `keys/`. |
| AC-HNK-16.4 | Test yang gagal memblokir merge. | BLOCKED | 2026-10-19 | Butuh branch protection `main` dengan dua job sebagai required check; pengaturan admin repo (Hans). |

## Deviasi
_Kosong._ Kalau implementasi menyimpang dari keputusan, tulis di sini **dan** di [[Backlog]] bagian Log Deviasi. Tidak ada perubahan diam-diam.
