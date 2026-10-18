---
tags: [es, "HNK-16"]
type: es
id: HNK-16
phase: F1
lead: Dex
owners: [Dex]
status: PARSIAL
updated: 2026-10-19
---

# ES-HNK-16 - CI dan quality gate

> **Peta link:** [[Exec Summary Hub]] · [[Backlog]] · [[AC-HNK-16 - CI dan quality gate|AC]] · [[TEST-HNK-16 - CI dan quality gate|Test]] · **Exec Summary**

**Lead:** Dex #dex · **Tim:** Dex #dex

## Apa diubah
- `scripts/check.sh`: satu perintah lokal untuk semua cek, berhenti di kegagalan pertama.
- `.github/workflows/ci.yml`: job `rust` (fmt, check, clippy -D warnings, test, wasm build) dan job `secrets` (gitleaks seluruh riwayat, binary di-pin 8.21.2) pada push ke `main` dan setiap PR.
- `.gitignore`: ditambah `*.key`, `*.pem`, `keys/`.

## Hasil vs KPI (angka riil)
| KPI | Target | Aktual |
|---|---|---|
| Waktu pipeline (CI, cache dingin) | < 5 menit | 3m10s (rust), 6s (gitleaks) |
| Tes workspace | semua lulus | 82 lulus, 0 gagal |
| Temuan secret | 0 | 0 (seluruh riwayat) |

## Status
**PARSIAL** — CI hijau di PR. Belum: merge ke `main`, branch protection (AC-HNK-16.4, admin), uji script lokal (AC-HNK-16.1).

## Risiko tersisa
- Tanpa branch protection, PR merah masih bisa di-merge.
- Script lokal belum diuji di mesin Dex (Windows, Rust belum terpasang).

## Bukti
- Commit: `317d59b` (branch `dex/hnk-16-ci`, jitsuinfi-zcash PR #1 (`317d59b`))
- ID tes: I-HNK-16.1 PASS (https://github.com/JitsuinFi/jitsuinfi-zcash/actions/runs/39152530625)
- Persetujuan user untuk push/deploy: _belum_
