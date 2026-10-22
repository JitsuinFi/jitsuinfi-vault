---
tags: [ac, "HNK-32"]
type: ac
id: HNK-32
phase: F6
status: TODO
updated: 2026-10-22
---

# AC-HNK-32 - Perbaikan hasil audit flow

> **Peta link:** [[AC Hub]] · [[Backlog]] · **AC** · [[TEST-HNK-32 - Perbaikan hasil audit flow|Test]] · [[ES-HNK-32 - Perbaikan hasil audit flow|Exec Summary]]

**Item:** HNK-32 · **Fase:** F6 · **Dependency:** HNK-21, HNK-26, HNK-31 · **Sumber:** audit langkah 6 [[Workflow Development]] tanggal 2026-10-22 atas 42 baris BL

## Deskripsi
Audit flow diagram 2026-10-22 menandai 8 baris GAGAL AUDIT dan menyisakan 10 baris AUDIT yang belum punya bukti. Item ini memperbaiki celahnya. Dua di antaranya menyangkut keamanan: buyer bisa menyegel surat tanpa cek PDF, dan QR pelunasan bisa dibuat dari surat tempelan tanpa rantai segel. Selesai bila semua baris BL yang menunjuk ke HNK-32 diaudit ulang dan berlabel SELESAI (atau DITUNDA dengan keputusan user).

## Acceptance criteria
Status per kriteria: `TODO` / `PASS` / `FAIL` / `BLOCKED`, wajib dengan tanggal dan bukti (commit, txid, log, id tes).

| ID | Kriteria | Status | Tanggal | Bukti |
|---|---|---|---|---|
| AC-HNK-32.1 | **Segel buyer terkunci:** buyer tidak bisa menyegel surat yang PDF-nya tidak cocok dengan `terms_hash` atau yang financier-nya bukan financier penawaran; alasannya tampil (BL-D24-06) | TODO | — | — |
| AC-HNK-32.2 | **QR hanya untuk surat tersegel:** QR pelunasan hanya muncul untuk surat tersimpan dengan rantai tiga segel `Sealed`; surat lain ditolak dengan alasan, ada unit test penolakan (BL-D25-01, BL-S02-02) | TODO | — | — |
| AC-HNK-32.3 | **Alasan berhenti terbaca:** konsol menampilkan kalimat, bukan dump Debug, untuk setiap `Stop`; "sudah dibiayai" berbunyi berhenti tanpa transaksi (BL-D23-08, BL-D27-01) | TODO | — | — |
| AC-HNK-32.4 | **Konfirmasi terlihat:** konsol menampilkan jumlah konfirmasi entri terhadap minimum (BL-D23-14) | TODO | — | — |
| AC-HNK-32.5 | **Bukti bisa diunduh:** JTSE dan Exhibit A + bukti lengkap bisa diunduh sebagai file dari konsol, dan file itu lolos `/verify` atau `jitsuin verify` (BL-D25-04, BL-D27-04) | TODO | — | — |
| AC-HNK-32.6 | **E2E lokal diperluas:** kirim key lewat relay, simpan kontak, tolak penawaran, dan permintaan riwayat lulus di testnet (BL-D21-11, BL-D22-01, BL-D23-03, BL-D26-01 – 09) | PASS | 2026-10-22 | I-HNK-32.1: `TES-INV-FE-11588` dan `TES-INV-FE-18524-D` |
| AC-HNK-32.7 | **Tanpa regresi:** `npm test` frontend dan `cargo test` node lulus; siklus E2E lokal tetap sampai settled; nol pelanggaran CSP | TODO | — | — |
| AC-HNK-32.8 | **Lingkup halaman anggota diputuskan user** dan baris BL-D29-07 ditutup sesuai keputusan itu | PASS | 2026-10-22 | Keputusan user: halaman membaca output CLI; BL-D29-07 SELESAI dengan E2E dana testnet (kartu Solvency "Solvent in period 2") |
