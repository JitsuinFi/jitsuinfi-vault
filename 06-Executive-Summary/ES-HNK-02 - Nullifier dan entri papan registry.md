---
tags: [es, "HNK-02"]
type: es
id: HNK-02
phase: F1
lead: Hans
owners: [Hans, Dex]
status: PARSIAL
updated: 2026-10-17
---

# ES-HNK-02 - Nullifier dan entri papan registry

> **Peta link:** [[Exec Summary Hub]] · [[Backlog]] · [[AC-HNK-02 - Nullifier dan entri papan registry|AC]] · [[TEST-HNK-02 - Nullifier dan entri papan registry|Test]] · **Exec Summary**

**Lead:** Hans #hans · **Tim:** Hans #hans, Dex #dex

## Apa diubah
- `BoardEntry` di `jitsuin-core`: `sign` (key sementara supplier), `verify` (`verify_strict`), `to_memo_bytes` (memo 512 byte: marker `0xFF` ZIP-302, magic `JTS1`, kind, N, commitment, bucket, signature, padding nol), `from_memo_bytes` (decoder ketat, padding wajib nol).
- Nullifier sengaja belum diimplementasikan (DEV-04).

## Hasil vs KPI (angka riil)
| KPI | Target | Aktual |
|---|---|---|
| Ukuran entri | ≤ 512 byte (target sekitar 136) | 136 byte |
| Cakupan unit test modul | semua fungsi publik | Belum (unit test resmi = HNK-02.T4, Dex) |

## Status
**PARSIAL** (lihat alasan di Risiko tersisa).

## Risiko tersisa
- HNK-02.T1 nullifier selesai (`40d7656`, DEV-04 disetujui).
- HNK-02.T3: commitment sudah (`6b5c343`, DEV-09); manajemen salt (Dex) belum.
- Unit test resmi belum (HNK-02.T4, Dex).

## Bukti
- Commit: `c0d6981`, `40d7656` (nullifier, lokal)
- ID tes: verifikasi sementara 21/21 lulus (scratchpad); unit test resmi belum
- Persetujuan user untuk push/deploy: **disetujui 2026-10-17**, di-push ke `JitsuinFi/jitsuinfi-zcash` (private)
