---
tags: [flow, backlog]
status: DITETAPKAN
progress: 0/8 SELESAI
updated: 2026-10-20
---

# DFD-2.9 - Solvabilitas Dana-backlogs

**Diagram:** [[DFD-2.9 - Solvabilitas Dana]] · Rencana: [[FD-01 - Keputusan Usulan dan Gelombang Kerja]] · [[FD-02 - Penelusuran Business Flow ke Backlog]] · Backlog: [[Backlog]] · Item: [[AC-HNK-15 - Stretch JitsuinFi Vault|HNK-15]]

Task untuk proses 9.1 – 9.8. Aturan kolom sama dengan [[DFD-2.1 - Identitas dan Sesi-backlogs]].

Kolom Status mengikuti langkah 6 "Audit flow diagram" di [[Workflow Development]]: `TODO` → `DIKERJAKAN` → `AUDIT` (semua task backlog-nya DONE) → `SELESAI (tanggal, bukti)` atau `GAGAL AUDIT (tanggal, alasan)`; `DITUNDA` hanya dengan keputusan user. Antrean audit tampil di setiap `python3 scripts/sync-vault.py` (lewat `scripts/check-backlogs.py`). Backlog ini ditetapkan 2026-10-20 (D-32).

## Task

| ID | Elemen | Task | Selesai bila | Ref | Task backlog | Owner | Status |
|---|---|---|---|---|---|---|---|
| BL-D29-01 | 9.1, D15 | Merkle sum tree kewajiban (daun id acak + nominal, root, total, jalur) | Root dan total cocok dengan jumlah setoran; jalur tiap daun terverifikasi | HNK-15.T1 | HNK-15.T1 | Dex | TODO |
| BL-D29-02 | 9.1, F9.01 – F9.04 | Pencatatan setoran di node manajer: deteksi setoran masuk, id anggota acak, kuitansi ke kotak surat anggota | Anggota menerima kuitansi berisi id setoran dan nominal | C-27 | HNK-29.T1 | Dex | TODO |
| BL-D29-03 | 9.2, F9.05 – F9.08 | Root dan total dari Merkle sum tree diteruskan ke `post_liability_root` | Root yang diposting sama dengan root tree periode itu | HNK-15.T1 | HNK-15.T1 | Dex | TODO |
| BL-D29-04 | 9.6, F9.19 – F9.20 | Kirim jalur Merkle tiap anggota setelah setiap root lewat relay | Setiap anggota menerima jalur untuk periode terbaru | C-27 | HNK-29.T2 | Dex | TODO |
| BL-D29-05 | 9.7, F9.21 – F9.24 | Verifikasi inklusi: jalur berakhir di root JTLR terbaru dan jumlah root = total JTLR | Jalur dari tree lain ditolak | HNK-15.T1, C-27 | HNK-29.T2 | Dex | TODO |
| BL-D29-06 | 9.4 – 9.5 | Perintah CLI solvabilitas untuk anggota (`member_view` + `solvency`); `SolvencyPolicy.grace_days` dihapus atau dipakai | Anggota mendapat verdict solvent / tidak / belum ada root dari CLI lokal | C-28 | HNK-27.T10 | Hans | TODO |
| BL-D29-07 | 9.8, F9.25 – F9.26 | Halaman anggota membaca hasil pindaian lokal | Laporan tampil tanpa UFVK dikirim ke server | HNK-15.T3, P-10 | HNK-15.T3 | Dave | TODO |
| BL-D29-08 | Uji | Integrasi testnet: dua setoran, satu advance, satu root, verdict solvent, inklusi kedua anggota | Kasus tercatat di TEST-HNK-15 | HNK-17 | HNK-17.T4 | Dave | TODO |

## Sudah ada (tanpa task baru)

- 9.2 root kewajiban (`post_liability_root`, `LiabilityRoot`), 9.3 watch-only (`init_fvk`), 9.4 tampilan dana (`fund_view`, `member_view`), 9.5 solvabilitas (`solvency`): diuji testnet (HNK-15.T2).

## Keputusan yang dibutuhkan

- Sisi aset dinyatakan manajer sendiri (nilai JTN1 tidak terikat ke advance): batasi atau catat sebagai risiko (lihat [[SEQ-05 - Anggota Dana]]).
