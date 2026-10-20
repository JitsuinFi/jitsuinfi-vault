---
tags: [flow, backlog]
status: DITETAPKAN
progress: 0/4 SELESAI
updated: 2026-10-20
---

# DFD-1 - Proses Utama-backlogs

**Diagram:** [[DFD-1 - Proses Utama]] · Rencana: [[FD-01 - Keputusan Usulan dan Gelombang Kerja]] · [[FD-02 - Penelusuran Business Flow ke Backlog]] · Backlog: [[Backlog]]

DFD-1 adalah roll-up dari level 2, jadi task-nya ada di backlog level 2 per proses. Halaman ini hanya indeks, ditambah task yang menyangkut level 1 sendiri.

Kolom Status mengikuti langkah 6 "Audit flow diagram" di [[Workflow Development]]: `TODO` → `DIKERJAKAN` → `AUDIT` (semua task backlog-nya DONE) → `SELESAI (tanggal, bukti)` atau `GAGAL AUDIT (tanggal, alasan)`; `DITUNDA` hanya dengan keputusan user. Antrean audit tampil di setiap `python3 scripts/sync-vault.py` (lewat `scripts/check-backlogs.py`). Backlog ini ditetapkan 2026-10-20 (D-32).

## Indeks per proses

| Proses | Backlog | Jumlah task | Isi utama |
|---|---|---|---|
| 1.0 Identitas, sesi, kotak surat | [[DFD-2.1 - Identitas dan Sesi-backlogs]] | 19 | Passkey satu per orang, salt per peran, kotak surat, kartu kontak, stempel, pairing dan sesi konsol node |
| 2.0 Terbitkan dan tanda tangani invoice | [[DFD-2.2 - Penerbitan dan Tanda Tangan Invoice-backlogs]] | 11 | Key per invoice supplier, invoice dan tanda tangan lewat relay, cek hash di layar buyer, penyimpanan deal lokal |
| 3.0 Registrasi papan | [[DFD-2.3 - Registrasi Papan-backlogs]] | 15 | Penawaran dan penolakan, salt dan kelas, API deal, kartu entri supplier, pemulihan `register()`, persistensi `Flow` |
| 4.0 Pengalihan dan advance | [[DFD-2.4 - Pengalihan dan Advance-backlogs]] | 14 | Alamat per deal, surat lewat relay, `assignmentDecode`, segel dengan isi terbaca, persetujuan operator, `Done` setelah konfirmasi, cek nominal advance |
| 5.0 Pelunasan dan settled | [[DFD-2.5 - Pelunasan dan Settled-backlogs]] | 10 | QR hanya untuk `Sealed`, pengingat, penjadwal, sengketa, txid settled diingat, bundel ke buyer dan supplier |
| 6.0 Riwayat buyer | [[DFD-2.6 - Riwayat Buyer-backlogs]] | 10 | Permintaan bertanda tangan, persetujuan buyer, `k` otomatis, registri KYC, API `check_buyer`, policy, riwayat saya |
| 7.0 Deteksi pembiayaan ganda | [[DFD-2.7 - Deteksi Pembiayaan Ganda-backlogs]] | 6 | `proof_from_lookup` di node, posisi di wasm, kartu bukti ganda, `verifyProofOnBoard` |
| 8.0 Verifikasi dan indeks publik | [[DFD-2.8 - Verifikasi dan Indeks Publik-backlogs]] | 8 | UFVK papan untuk juri, CLI dan Docker, snapshot relay, teks Verify dan orang luar, halaman indeks |
| 9.0 Solvabilitas dana | [[DFD-2.9 - Solvabilitas Dana-backlogs]] | 8 | Merkle sum tree, setoran dan kuitansi, jalur Merkle per periode, CLI solvabilitas, halaman anggota |

## Task level 1

| ID | Elemen | Task | Selesai bila | Ref | Task backlog | Owner | Status |
|---|---|---|---|---|---|---|---|
| BL-D1-01 | Penyimpanan bersama D7, D19 | Skema pesan relay untuk semua aliran D7 di level 2 (jenis, versi, pengirim, batas ukuran) | Setiap aliran D7 di DFD-2.1 – 2.9 punya jenis pesan di skema | C-04 | HNK-23.T1 | Hans | TODO |
| BL-D1-02 | Penyimpanan bersama D4 | Penyimpanan dokumen deal lintas sesi di perangkat supplier dan buyer (IndexedDB terenkripsi dengan key dari PRF) | Semua aliran ke D4 di sisi supplier dan buyer bertahan setelah tab ditutup | C-07 | HNK-24.T3 | Hans | TODO |
| BL-D1-03 | Penyimpanan bersama D11, D2 | Persistensi state deal dan dokumen deal di node | Semua aliran ke D11 bertahan setelah node restart | C-16 | HNK-26.T10 | Hans | TODO |
| BL-D1-04 | Balancing | Setiap perubahan level 2 dijalankan lewat `scripts/build-dfd.py` (cek balancing) | Skrip lulus sebelum commit | — | — | Semua | ATURAN |
