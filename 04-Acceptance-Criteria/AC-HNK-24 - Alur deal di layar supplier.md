---
tags: [ac, "HNK-24"]
type: ac
id: HNK-24
phase: F5
lead: Dave
owners: [Hans, Dave]
status: TODO
updated: 2026-10-20
---

# AC-HNK-24 - Alur deal di layar supplier

> **Peta link:** [[AC Hub]] · [[Backlog]] · **AC** · [[TEST-HNK-24 - Alur deal di layar supplier|Test]] · [[ES-HNK-24 - Alur deal di layar supplier|Exec Summary]]

**Lead:** Dave #dave · **Tim:** Hans #hans, Dave #dave · Dibuat 2026-10-20 dari [[FD-01 - Keputusan Usulan dan Gelombang Kerja]] dan [[FD-02 - Penelusuran Business Flow ke Backlog]] (D-30)

**Item:** HNK-24 · **Fase:** F5 · **Dependency:** HNK-22, HNK-23, HNK-27

## Deskripsi
Layar supplier menjalankan seluruh deal tanpa salin-tempel: key per invoice dari master, cek tanda tangan buyer, tawaran ke financier, tanda tangan entri papan, segel surat dengan isi terbaca, status advance, timeline per deal, dokumen tersimpan lintas sesi. Desain: [[SEQ-01 - Supplier]], [[PG-01 - Peta Halaman per Peran]]. Task rinci: [[SEQ-01 - Supplier-backlogs]].

## Acceptance criteria
Status per kriteria: `TODO` / `PASS` / `FAIL` / `BLOCKED`, wajib dengan tanggal dan bukti (commit, txid, log, id tes).

| ID | Kriteria | Status | Tanggal | Bukti |
|---|---|---|---|---|
| AC-HNK-24.1 | Supplier menyelesaikan satu deal `TES-` dari invoice sampai advance tanpa salin-tempel. | TODO | — | — |
| AC-HNK-24.2 | Tidak ada unduhan secret; master + input yang sama memberi key per invoice yang sama (test vector). | TODO | 2026-10-20 | Turunan key dan vector PASS (`a252568`, U-HNK-24.1). Sisa: layar tanpa unduhan secret (HNK-24.T2) |
| AC-HNK-24.3 | Deal masih ada setelah tab ditutup dan dibuka lagi. | TODO | 2026-10-20 | Store terenkripsi PASS (`c7d4b1b`, U-HNK-24.3, I-HNK-24.2: bertahan setelah reload). Sisa: layar supplier menyimpan deal ke store (HNK-24.T4 – T9) |
| AC-HNK-24.4 | Isi surat (alamat bayar, `financier_pk`, `terms_hash`) tampil dan PDF surat dicek sebelum segel. | TODO | — | — |
| AC-HNK-24.5 | Timeline menunjukkan langkah berikutnya untuk tiap deal. | TODO | — | — |

## Deviasi
_Kosong._ Kalau implementasi menyimpang dari keputusan, tulis di sini **dan** di [[Backlog]] bagian Log Deviasi. Tidak ada perubahan diam-diam.
