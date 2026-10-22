---
tags: [ac, "HNK-27"]
type: ac
id: HNK-27
phase: F3
lead: Hans
owners: [Hans]
status: PARSIAL
updated: 2026-10-20
---

# AC-HNK-27 - Perbaikan protokol dan flow

> **Peta link:** [[AC Hub]] · [[Backlog]] · **AC** · [[TEST-HNK-27 - Perbaikan protokol dan flow|Test]] · [[ES-HNK-27 - Perbaikan protokol dan flow|Exec Summary]]

**Lead:** Hans #hans · **Tim:** Hans #hans · Dibuat 2026-10-20 dari [[FD-01 - Keputusan Usulan dan Gelombang Kerja]] dan [[FD-02 - Penelusuran Business Flow ke Backlog]] (D-30)

**Item:** HNK-27 · **Fase:** F3 · **Dependency:** HNK-05, HNK-19, HNK-20

## Deskripsi
Perbaikan kode dari audit diagram (FD-00 §6) dan usulan kecil yang disetujui D-30: salt komitmen, kelas diskon/tenor, `assignmentDecode`, posisi papan di bukti wasm, pemulihan `register()`, konfirmasi ulang, `Done` setelah konfirmasi, cek nominal advance, entri bertag tanpa sertifikat penuh, API wasm berbasis byte, CLI solvabilitas.

## Acceptance criteria
Status per kriteria: `TODO` / `PASS` / `FAIL` / `BLOCKED`, wajib dengan tanggal dan bukti (commit, txid, log, id tes).

| ID | Kriteria | Status | Tanggal | Bukti |
|---|---|---|---|---|
| AC-HNK-27.1 | Retry untuk invoice yang sama memberi komitmen yang sama; tidak ada JTSP dari retry. | PASS | 2026-10-20 | `748d451`; U-HNK-27.1, vector dicek silang Python |
| AC-HNK-27.2 | Entri bertanda tangan membawa kelas sungguhan; `jitsuin index` tidak lagi kosong untuk ≥ 5 deal per kelas. | PASS | 2026-10-22 | Kode `d5f98d0` (U-HNK-27.2 PASS); I-HNK-27.1 PASS: 5 entri berkelas di papan testnet, `jitsuin index` menampilkan `31-60 days  5  3-5%` (jitsuinfi-zcash `34e4851`). Node mengisi kelas dari `deal_classes` saat Accept |
| AC-HNK-27.3 | Restart setelah posting tidak membuat posting kedua; advance tidak dibayar dengan konfirmasi di bawah minimum setelah reorg. | PASS | 2026-10-20 | `fef1d15`, `b6f33d5`; U-HNK-27.4, U-HNK-27.5, U-HNK-27.6 (logika `Flow` dan pencarian tx terkirim). Uji crash testnet I-HNK-27.2 masih TODO |
| AC-HNK-27.4 | Advance kurang dari yang disepakati gagal diverifikasi. | PASS | 2026-10-20 | `a10185f`; U-HNK-27.7 |
| AC-HNK-27.5 | Bukti dari wasm dengan posisi lolos `jitsuin verify`. | PASS | 2026-10-20 | `14803af`; U-HNK-27.8 (`verify_proof_on_board`, fungsi yang dipanggil `jitsuin verify`) |

## Deviasi
- **DEV-14:** salt komitmen diturunkan (keyed BLAKE2b dari key financier dan N) alih-alih CSPRNG yang disimpan per (invoice, financier) seperti teks P-08. Hasilnya sama untuk retry (komitmen yang sama), tanpa penyimpanan dan tanpa dependensi baru; tetap tidak bisa ditebak tanpa key financier. Lihat [[Backlog]] Log Deviasi. **Disetujui user 2026-10-20** ("Setuju DEV-14, gas push dan buka PR").
