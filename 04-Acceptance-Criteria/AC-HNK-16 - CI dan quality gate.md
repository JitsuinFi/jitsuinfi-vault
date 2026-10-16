---
tags: [ac, "HNK-16"]
type: ac
id: HNK-16
phase: F1
lead: Dex
owners: [Dex]
status: TODO
updated: 2026-10-16
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
| AC-HNK-16.1 | Satu perintah lokal (misalnya `just check` atau `make check`) menjalankan semua cek dan gagal kalau ada yang merah. | TODO | — | — |
| AC-HNK-16.2 | Workflow GitHub Actions menjalankan cek yang sama dan hijau di branch utama. | TODO | — | — |
| AC-HNK-16.3 | Secret scanning: 0 temuan; `.gitignore` mencakup seed, key, `.env`, dan DB wallet. | TODO | — | — |
| AC-HNK-16.4 | Test yang gagal memblokir merge. | TODO | — | — |

## Deviasi
_Kosong._ Kalau implementasi menyimpang dari keputusan, tulis di sini **dan** di [[Backlog]] bagian Log Deviasi. Tidak ada perubahan diam-diam.
