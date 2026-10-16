---
tags: [es, "HNK-01"]
type: es
id: HNK-01
phase: F1
lead: Hans
owners: [Hans, Dex, Dave]
status: PARSIAL
updated: 2026-10-16
---

# ES-HNK-01 - Format invoice kanonik dan tanda tangan buyer

> **Peta link:** [[Exec Summary Hub]] · [[Backlog]] · [[AC-HNK-01 - Format invoice kanonik dan tanda tangan buyer|AC]] · [[TEST-HNK-01 - Format invoice kanonik dan tanda tangan buyer|Test]] · **Exec Summary**

**Lead:** Hans #hans · **Tim:** Hans #hans, Dex #dex, Dave #dave

## Apa diubah
- Crate baru `jitsuin-core` (repo lokal `zkSNARK/jitsuinfi-zcash/`): struct `Invoice`, encoding kanonik deterministik (`to_canonical_bytes`), decoder ketat (`from_canonical_bytes`), validasi field, `sign_invoice` (cek kecocokan key buyer) dan `verify_invoice` (`verify_strict`).
- Workspace Rust di-pin ke 1.99.1 (`rust-toolchain.toml`); `ed25519-dalek` 2.2 (D-10).
- `.gitignore` menolak seed, file `.age`, `.env`, dan DB wallet.
- Langkah 1 hijau: `cargo fmt --check`, `cargo check`, `cargo clippy -D warnings`, `cargo build`.

## Hasil vs KPI (angka riil)
| KPI | Target | Aktual |
|---|---|---|
| Test vector deterministik | 100% identik | Identik (verifikasi sementara) |
| Waktu sign + verify per invoice | < 10 ms | Belum diukur |

## Status
**PARSIAL** (lihat alasan di Risiko tersisa).

## Risiko tersisa
- Unit test resmi dan file test vector belum ada (HNK-01.T3, Dex).
- Review [[Format Data]] oleh Dave (HNK-01.T4).
- Waktu sign + verify belum diukur.
- Signer buyer non-deterministik → lihat DEV-04 (dampaknya di HNK-02).

## Bukti
- Commit: `c0d6981` (lokal, belum ada remote)
- ID tes: verifikasi sementara 21/21 lulus (scratchpad); unit test resmi belum
- Persetujuan user untuk push/deploy: **disetujui 2026-10-17**, di-push ke `JitsuinFi/jitsuinfi-zcash` (private)
