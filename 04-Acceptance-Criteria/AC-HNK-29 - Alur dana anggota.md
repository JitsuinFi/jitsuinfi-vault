---
tags: [ac, "HNK-29"]
type: ac
id: HNK-29
phase: F7
lead: Hans
owners: [Hans]
status: TODO
updated: 2026-10-20
---

# AC-HNK-29 - Alur dana anggota

> **Peta link:** [[AC Hub]] · [[Backlog]] · **AC** · [[TEST-HNK-29 - Alur dana anggota|Test]] · [[ES-HNK-29 - Alur dana anggota|Exec Summary]]

**Lead:** Hans #hans · **Tim:** Hans #hans · Dibuat 2026-10-20 dari [[FD-01 - Keputusan Usulan dan Gelombang Kerja]] dan [[FD-02 - Penelusuran Business Flow ke Backlog]] (D-30)

**Item:** HNK-29 · **Fase:** F7 · **Dependency:** HNK-15, HNK-23

## Deskripsi
Sisi manajer dan anggota JitsuinFi Vault di luar Merkle sum tree (HNK-15.T1) dan halaman anggota (HNK-15.T3): pencatatan setoran dan kuitansi lewat relay, jalur Merkle per periode, verifikasi inklusi terhadap root JTLR, batas uji di halaman anggota. Desain: [[SEQ-05 - Anggota Dana]], [[DFD-2.9 - Solvabilitas Dana]]. Task rinci: [[DFD-2.9 - Solvabilitas Dana-backlogs]].

## Acceptance criteria
Status per kriteria: `TODO` / `PASS` / `FAIL` / `BLOCKED`, wajib dengan tanggal dan bukti (commit, txid, log, id tes).

| ID | Kriteria | Status | Tanggal | Bukti |
|---|---|---|---|---|
| AC-HNK-29.1 | Anggota menerima kuitansi berisi id setoran dan nominal. | TODO | — | — |
| AC-HNK-29.2 | Setiap anggota menerima jalur untuk periode terbaru; jalur dari tree lain ditolak. | TODO | — | — |
| AC-HNK-29.3 | Halaman anggota menampilkan batas uji dan tidak pernah meminta UFVK dikirim ke server. | TODO | — | — |

## Deviasi
_Kosong._ Kalau implementasi menyimpang dari keputusan, tulis di sini **dan** di [[Backlog]] bagian Log Deviasi. Tidak ada perubahan diam-diam.
