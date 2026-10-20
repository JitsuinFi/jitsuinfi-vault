---
tags: [ac, "HNK-24"]
type: ac
id: HNK-24
phase: F5
lead: Hans
owners: [Hans]
status: PARSIAL
updated: 2026-10-20
---

# AC-HNK-24 - Alur deal di layar supplier

> **Peta link:** [[AC Hub]] · [[Backlog]] · **AC** · [[TEST-HNK-24 - Alur deal di layar supplier|Test]] · [[ES-HNK-24 - Alur deal di layar supplier|Exec Summary]]

**Lead:** Hans #hans · **Tim:** Hans #hans · Dibuat 2026-10-20 dari [[FD-01 - Keputusan Usulan dan Gelombang Kerja]] dan [[FD-02 - Penelusuran Business Flow ke Backlog]] (D-30)

**Item:** HNK-24 · **Fase:** F5 · **Dependency:** HNK-22, HNK-23, HNK-27

## Deskripsi
Layar supplier menjalankan seluruh deal tanpa salin-tempel: key per invoice dari master, cek tanda tangan buyer, tawaran ke financier, tanda tangan entri papan, segel surat dengan isi terbaca, status advance, timeline per deal, dokumen tersimpan lintas sesi. Desain: [[SEQ-01 - Supplier]], [[PG-01 - Peta Halaman per Peran]]. Task rinci: [[SEQ-01 - Supplier-backlogs]].

## Acceptance criteria
Status per kriteria: `TODO` / `PASS` / `FAIL` / `BLOCKED`, wajib dengan tanggal dan bukti (commit, txid, log, id tes).

| ID | Kriteria | Status | Tanggal | Bukti |
|---|---|---|---|---|
| AC-HNK-24.1 | Supplier menyelesaikan satu deal `TES-` dari invoice sampai advance tanpa salin-tempel. | TODO | 2026-10-20 | Seluruh alur jalan dengan salin-tempel (I-HNK-24.3); tanpa salin-tempel menunggu relay HNK-23 |
| AC-HNK-24.2 | Tidak ada unduhan secret; master + input yang sama memberi key per invoice yang sama (test vector). | PASS | 2026-10-20 | Vector (`a252568`, U-HNK-24.1); layar tanpa unduhan secret dan menolak nomor invoice ganda (`17a01ea`, I-HNK-24.3) |
| AC-HNK-24.3 | Deal masih ada setelah tab ditutup dan dibuka lagi. | PASS | 2026-10-20 | `c7d4b1b`, `17a01ea`: deal tersimpan, terbaca lagi setelah reload dan unlock ulang; passkey lain melihat 0 deal (I-HNK-24.3) |
| AC-HNK-24.4 | Isi surat (alamat bayar, `financier_pk`, `terms_hash`) tampil dan PDF surat dicek sebelum segel. | PASS | 2026-10-20 | `17a01ea`, I-HNK-24.3 |
| AC-HNK-24.5 | Timeline menunjukkan langkah berikutnya untuk tiap deal. | PASS | 2026-10-20 | `17a01ea`, U-HNK-24.4, I-HNK-24.3 |

## Deviasi
- DEV-15: T2 dan T4 – T9 milik Dave dikerjakan Hans sebagai backup (disetujui user).
- DEV-16: BL-D22-07 dan BL-D1-02 dipetakan ulang ke HNK-25.T1 (penyimpanan di layar buyer); disetujui user 2026-10-20. Lihat [[Backlog]] Log Deviasi.
