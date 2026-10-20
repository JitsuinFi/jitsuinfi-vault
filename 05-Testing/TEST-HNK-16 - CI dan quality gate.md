---
tags: [test, "HNK-16"]
type: test
id: HNK-16
phase: F1
lead: Dex
owners: [Dex]
unit: PASS
integrasi: PASS
e2e: PASS
updated: 2026-10-19
---

# TEST-HNK-16 - CI dan quality gate

> **Peta link:** [[Testing Hub]] · [[Backlog]] · [[AC-HNK-16 - CI dan quality gate|AC]] · **Test** · [[ES-HNK-16 - CI dan quality gate|Exec Summary]]

**Lead:** Dex #dex · **Tim:** Dex #dex 

## 1. Unit
Logika murni, cepat, tanpa DB dan tanpa chain.

| ID | Kasus | Hasil | Tanggal | Bukti |
|---|---|---|---|---|
| U-HNK-16.1 | Script cek lokal gagal dengan exit code ≠ 0 saat satu cek merah | PASS | 2026-10-19 | Format salah disisipkan sementara di `jitsuin-core/src/lib.rs` → `check.sh` berhenti di langkah fmt, exit 1; dikembalikan (git status bersih). Run hijau: exit 0, 38 dtk. |

## 2. Integrasi
Skrip vs DB/chain sungguhan. Semua artefak memakai prefix `TES-` (invoice, akun, label, order).

| ID | Skenario | Hasil | Tanggal | Bukti (txid/log) |
|---|---|---|---|---|
| I-HNK-16.1 | Jalankan pipeline penuh di repo bersih (clone baru) | PASS | 2026-10-19 | Runner GitHub = clone baru: fmt, check, clippy -D warnings, test (82 lulus: 14+34+24+6+4), wasm build, gitleaks 0 temuan — https://github.com/JitsuinFi/jitsuinfi-zcash/actions/runs/39152530625 |

**Bukti pembersihan:** sisa artefak off-chain `TES-` = **0** (item ini tidak membuat artefak `TES-`). Artefak on-chain tidak bisa dihapus; catat txid-nya di tabel di atas. Data produksi tidak boleh tersentuh.

## 3. E2E
Panduan langkah demi langkah untuk user.

- [x] Developer menjalankan satu perintah cek dan membaca hasilnya.

| Langkah | Hasil diharapkan | Hasil aktual | Status |
|---|---|---|---|
| 1 | Di root `jitsuinfi-zcash`: `bash scripts/check.sh` → tiap langkah dicetak `== …`, akhir `All checks passed.`, exit 0 | Laptop Dex 2026-10-19 (setelah rebase PR #2 ke `main`): `SKIP_WASM=1 bash scripts/check.sh` 14 dtk (cache hangat), 96 tes lulus, `All checks passed.` | PASS |
