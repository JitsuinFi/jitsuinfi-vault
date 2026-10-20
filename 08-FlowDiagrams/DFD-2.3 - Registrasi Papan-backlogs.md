---
tags: [flow, backlog]
status: DRAF
updated: 2026-10-20
---

# DFD-2.3 - Registrasi Papan-backlogs

**Diagram:** [[DFD-2.3 - Registrasi Papan]] · Rencana: [[FD-01 - Keputusan Usulan dan Gelombang Kerja]] · [[FD-02 - Penelusuran Business Flow ke Backlog]] · Backlog: [[Backlog]]

Task untuk proses 3.1 – 3.9. Aturan kolom sama dengan [[DFD-2.1 - Identitas dan Sesi-backlogs]].

## Task

| ID | Elemen | Task | Selesai bila | Ref | Task backlog | Owner |
|---|---|---|---|---|---|---|
| BL-D23-01 | 3.1, F3.01 | Layar supplier "Tawarkan ke financier": pilih kontak, advance yang diminta, alamat shielded baru untuk deal ini | Pesan penawaran terkirim ke kotak surat financier | C-08 | HNK-24.T5 | Dave |
| BL-D23-02 | 3.1, F3.01 – F3.04 | Node menerima penawaran: decode, cek tanda tangan buyer (`verify_invoice`) sebelum `Deal` disimpan, operator menetapkan advance dan `min_confirmations` ≥ 1 | Penawaran dengan tanda tangan buyer palsu ditolak tanpa transaksi (F3.03) | C-09 | HNK-26.T5 | Dex |
| BL-D23-03 | 3.1 | Tolak atau kedaluwarsa penawaran: pesan ke supplier | Supplier melihat penawaran ditolak atau kedaluwarsa | C-10 | HNK-26.T6 | Dex |
| BL-D23-04 | 3.2, F3.05, F3.08 | Salt komitmen dari library (CSPRNG 32 byte), disimpan per (invoice, financier), dipakai ulang saat retry | Retry untuk invoice yang sama memberi komitmen yang sama | P-08 | HNK-27.T1 | Hans |
| BL-D23-05 | 3.2, F3.06, F3.08 | Kelas dari `classes_for(nominal, advance, tanggal advance, jatuh tempo)`; `Deal` membawa kelas; `check_entry` memeriksa kelas | Entri dengan kelas lain ditolak `EntryMismatch`; indeks `jitsuin index` tidak lagi kosong | K-1 | HNK-27.T2 | Hans |
| BL-D23-06 | 3.2, F3.07, F3.09 | Kirim pembuka komitmen dan kelas ke supplier lewat relay | Supplier menerima pembuka komitmen dan kelas | P-04 | HNK-23.T8 | Dex |
| BL-D23-07 | 3.3, F3.10 – F3.11 | API `POST /node/deals` membungkus `Flow::new` | Deal tidak lengkap (konfirmasi 0, advance 0, surat bukan milik invoice) ditolak dengan pesan | HNK-05.T3 | HNK-05.T3 | Dex |
| BL-D23-08 | 3.5, F3.20 – F3.21 | Status cek papan di konsol (bebas, sudah dibiayai, lanjut setelah crash) | Tiap hasil lookup tampil dengan label yang terbaca | HNK-05.T4 | HNK-26.T16 | Dex |
| BL-D23-09 | 3.6, F3.22 – F3.27 | Kartu supplier "Tanda tangani entri papan" (0x01 atau 0x03 dengan sertifikat k atau tag) memakai fungsi entri wasm dengan parameter kelas | Entri yang ditandatangani lolos `check_entry` di node | C-15, K-1 | HNK-24.T6 | Dave |
| BL-D23-10 | 3.6, F3.22 | Varian entri bertag yang hanya menerima `history_tag` 32 byte | Supplier tidak lagi membutuhkan sertifikat k penuh | K-10 | HNK-27.T8 | Hans |
| BL-D23-11 | 3.7, F3.31 | Penolakan `EntryMismatch` tampil terbaca di konsol dan dikirim ke supplier | Supplier melihat alasan penolakan entri | C-13 | HNK-21.T9 | Dave |
| BL-D23-12 | 3.8, F3.33 – F3.36 | `Register`: terima `BoardChecked` sebelum posting, cari entri yang sudah terkirim sebelum posting ulang | Restart setelah posting tidak membuat posting kedua; konflik yang muncul sebelum posting menjadi `Stopped` | K-4 | HNK-27.T5 | Hans |
| BL-D23-13 | 3.3 – 3.9, D11 | Persistensi state deal di node (serialisasi `Flow` dan dokumen deal) | Node yang di-restart melanjutkan deal dari state terakhir | C-16 | HNK-26.T10 | Hans |
| BL-D23-14 | 3.9, F3.37 – F3.42 | Progres konfirmasi di konsol (n dari `min_confirmations`) | Konsol menampilkan hitungan konfirmasi sampai `AwaitAssignment` | HNK-05.T4 | HNK-26.T16 | Dex |
| BL-D23-15 | Uji | Integrasi testnet: entri dengan kelas tertambang, `jitsuin index` menampilkan kelas (k = 5 butuh minimal 5 deal), crash dan restart sesudah posting | Kasus tercatat di TEST item terkait | HNK-04.T4, HNK-17 | HNK-17.T4 | Dave |

## Sudah ada (tanpa task baru)

- 3.4 Pindai papan (`scan`), 3.5 lookup N (`lookup`, `Flow::on_board`), 3.9 tunggu konfirmasi (`wait_for_confirmation`): diuji testnet lewat CLI scratchpad.

## Roadmap

- F3.32 menyimpan entri yang ditawarkan untuk bukti (P-14): tidak dibangun sebelum submit.
