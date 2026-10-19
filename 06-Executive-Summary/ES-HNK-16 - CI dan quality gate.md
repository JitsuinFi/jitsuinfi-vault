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
**PARSIAL** — AC 16.1–16.3 PASS: cek lokal (19 Okt), CI hijau di PR dan di `main` setelah merge (`317d59b`), gitleaks 0 temuan. Sisa AC-HNK-16.4 (branch protection): tidak tersedia untuk repo private di paket Free, jadi dinyalakan saat repo publik 28 Okt.

## Risiko tersisa
- Tanpa branch protection, PR merah masih bisa di-merge. Mitigasi sampai 28 Okt: Hans hanya me-merge PR dengan CI hijau.
- gitleaks belum terpasang lokal di mesin Dex (CI tetap menjalankannya).

## Bukti
- Commit: `317d59b` (jitsuinfi-zcash PR #1, di-merge ke `main` oleh Hans 2026-10-19)
- ID tes: U-HNK-16.1 PASS, I-HNK-16.1 PASS (https://github.com/JitsuinFi/jitsuinfi-zcash/actions/runs/39152530625), CI `main` https://github.com/JitsuinFi/jitsuinfi-zcash/actions/runs/39215984762
- Persetujuan user untuk push/deploy: push branch + PR atas izin Dex; merge oleh Hans (review) 2026-10-19
