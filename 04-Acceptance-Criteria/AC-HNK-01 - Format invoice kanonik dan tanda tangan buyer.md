---
tags: [ac, "HNK-01"]
type: ac
id: HNK-01
phase: F1
lead: Hans
owners: [Hans, Dex, Dave]
status: PASS
updated: 2026-10-16
---

# AC-HNK-01 - Format invoice kanonik dan tanda tangan buyer

> **Peta link:** [[AC Hub]] · [[Backlog]] · **AC** · [[TEST-HNK-01 - Format invoice kanonik dan tanda tangan buyer|Test]] · [[ES-HNK-01 - Format invoice kanonik dan tanda tangan buyer|Exec Summary]]

**Item:** HNK-01 · **Fase:** F1 · **Dependency:** SPK-06

**Lead:** Hans #hans · **Tim:** Hans #hans, Dex #dex, Dave #dave

## Deskripsi
Definisikan format invoice kanonik (field berurutan, encoding deterministik) dan tanda tangan Ed25519 deterministik oleh buyer. Fondasi nullifier.

## Acceptance criteria
Status per kriteria: `TODO` / `PASS` / `FAIL` / `BLOCKED`, wajib dengan tanggal dan bukti (commit, txid, log, id tes).

| ID | Kriteria | Status | Tanggal | Bukti |
|---|---|---|---|---|
| AC-HNK-01.1 | Encoding kanonik deterministik: invoice yang sama selalu menghasilkan byte yang sama (test vector tercatat). | PASS | 2026-10-16 | commit `c0d6981` (repo lokal `jitsuinfi-zcash/`); verifikasi sementara Hans: program di scratchpad memakai `jitsuin-core` lewat path dependency, 21/21 pemeriksaan lulus (bukan unit test resmi). Test vector: supplier sk 32×`0x01`, buyer sk 32×`0x02`, `TES-INV-0001`, 1.000.000.000 zat, hari 20.377 → 20.437, terms 32×`0x09` → 130 byte, lihat [[Format Data]] |
| AC-HNK-01.2 | Invoice memuat public key sementara supplier (32 byte) dan public key buyer. | PASS | 2026-10-16 | commit `c0d6981` (repo lokal `jitsuinfi-zcash/`): field `supplier_ephemeral_pk` dan `buyer_pk` (32 byte, divalidasi sebagai titik Ed25519) |
| AC-HNK-01.3 | Tanda tangan buyer atas byte kanonik identik bila diulang (RFC 8032). | PASS | 2026-10-16 | commit `c0d6981` (repo lokal `jitsuinfi-zcash/`); verifikasi sementara Hans: program di scratchpad memakai `jitsuin-core` lewat path dependency, 21/21 pemeriksaan lulus (bukan unit test resmi): sign 2× identik |
| AC-HNK-01.4 | Verifikasi gagal bila satu field diubah. | PASS | 2026-10-16 | commit `c0d6981` (repo lokal `jitsuinfi-zcash/`); verifikasi sementara Hans: program di scratchpad memakai `jitsuin-core` lewat path dependency, 21/21 pemeriksaan lulus (bukan unit test resmi): amount diubah → `verify_strict` gagal; key salah → `KeyMismatch` |
| AC-HNK-01.5 | Format didokumentasikan di [[Format Data]] dan cocok dengan implementasi. | PASS | 2026-10-16 | [[Format Data]] diperbarui: magic `JTSI`, version, panjang `invoice_id`. Review Dave (HNK-01.T4) masih terbuka |

## Deviasi
_Kosong._ Kalau implementasi menyimpang dari keputusan, tulis di sini **dan** di [[Backlog]] bagian Log Deviasi. Tidak ada perubahan diam-diam.
