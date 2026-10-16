---
tags: [ac, "HNK-02"]
type: ac
id: HNK-02
phase: F1
lead: Hans
owners: [Hans, Dex]
status: BLOCKED
updated: 2026-10-16
---

# AC-HNK-02 - Nullifier dan entri papan registry

> **Peta link:** [[AC Hub]] · [[Backlog]] · **AC** · [[TEST-HNK-02 - Nullifier dan entri papan registry|Test]] · [[ES-HNK-02 - Nullifier dan entri papan registry|Exec Summary]]

**Item:** HNK-02 · **Fase:** F1 · **Dependency:** HNK-01

**Lead:** Hans #hans · **Tim:** Hans #hans, Dex #dex

## Deskripsi
Hitung N = BLAKE2b-256 (personalisasi `JitsuinNullifier`) atas tanda tangan buyer, lalu encode entri papan (magic, tipe, N, commitment financier, bucket diskon dan tenor, tanda tangan supplier) dengan prefix memo `0xFF`.

## Acceptance criteria
Status per kriteria: `TODO` / `PASS` / `FAIL` / `BLOCKED`, wajib dengan tanggal dan bukti (commit, txid, log, id tes).

| ID | Kriteria | Status | Tanggal | Bukti |
|---|---|---|---|---|
| AC-HNK-02.1 | N deterministik dari tanda tangan buyer; test vector tercatat. | BLOCKED | 2026-10-16 | Menunggu keputusan **DEV-04** (nullifier dari tanda tangan vs dari invoice kanonik), lihat [[Backlog]] |
| AC-HNK-02.2 | Entri ter-encode ≤ 512 byte dan decode roundtrip identik. | PASS | 2026-10-16 | commit `c0d6981` (repo lokal `jitsuinfi-zcash/`); verifikasi sementara Hans: program di scratchpad memakai `jitsuin-core` lewat path dependency, 21/21 pemeriksaan lulus (bukan unit test resmi): memo 512 byte, entri 136 byte, roundtrip identik (dengan dan tanpa padding) |
| AC-HNK-02.3 | Tanda tangan supplier (key sementara) atas isi entri terverifikasi; entri tanpa tanda tangan valid ditolak (anti-griefing). | PASS | 2026-10-16 | commit `c0d6981` (repo lokal `jitsuinfi-zcash/`); verifikasi sementara Hans: program di scratchpad memakai `jitsuin-core` lewat path dependency, 21/21 pemeriksaan lulus (bukan unit test resmi): key salah dan signature diubah → gagal. Penolakan entri invalid saat scan = HNK-04 |
| AC-HNK-02.4 | (HNK-02.T3, Dex) Commitment financier = H(pubkey financier ‖ salt), tidak membuka identitas financier. | TODO | — | — |
| AC-HNK-02.5 | Format didokumentasikan di [[Format Data]]. | PASS | 2026-10-16 | [[Format Data]] sesuai implementasi (offset 0–136, padding nol wajib) |

## Deviasi
**DEV-04 (usulan, menunggu user):** kriteria AC-HNK-02.1 akan berubah menjadi "N deterministik dari byte kanonik invoice" kalau disetujui. Lihat [[Backlog]] Log Deviasi.

_Catatan sebelumnya:_ Kalau implementasi menyimpang dari keputusan, tulis di sini **dan** di [[Backlog]] bagian Log Deviasi. Tidak ada perubahan diam-diam.
