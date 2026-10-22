---
tags: [flow, backlog]
status: DITETAPKAN
progress: 14/15 SELESAI
updated: 2026-10-20
---

# DFD-2.3 - Registrasi Papan-backlogs

**Diagram:** [[DFD-2.3 - Registrasi Papan]] · Rencana: [[FD-01 - Keputusan Usulan dan Gelombang Kerja]] · [[FD-02 - Penelusuran Business Flow ke Backlog]] · Backlog: [[Backlog]]

Task untuk proses 3.1 – 3.9. Aturan kolom sama dengan [[DFD-2.1 - Identitas dan Sesi-backlogs]].

Kolom Status mengikuti langkah 6 "Audit flow diagram" di [[Workflow Development]]: `TODO` → `DIKERJAKAN` → `AUDIT` (semua task backlog-nya DONE) → `SELESAI (tanggal, bukti)` atau `GAGAL AUDIT (tanggal, alasan)`; `DITUNDA` hanya dengan keputusan user. Antrean audit tampil di setiap `python3 scripts/sync-vault.py` (lewat `scripts/check-backlogs.py`). Backlog ini ditetapkan 2026-10-20 (D-32).

## Task

| ID | Elemen | Task | Selesai bila | Ref | Task backlog | Owner | Status |
|---|---|---|---|---|---|---|---|
| BL-D23-01 | 3.1, F3.01 | Layar supplier "Tawarkan ke financier": pilih kontak, advance yang diminta, alamat shielded baru untuk deal ini | Pesan penawaran terkirim ke kotak surat financier | C-08 | HNK-24.T5 | Hans | SELESAI (2026-10-21, lokal, belum merge: `deal.offer` dikirim tersegel ke kotak surat financier dari kartu kontak + key yang dicek fingerprint-nya; vektor app dibaca node di `offer.rs`). Sebelumnya GAGAL AUDIT 2026-10-20 (kode salin-tempel) |
| BL-D23-02 | 3.1, F3.01 – F3.04 | Node menerima penawaran: decode, cek tanda tangan buyer (`verify_invoice`) sebelum `Deal` disimpan, operator menetapkan advance dan `min_confirmations` ≥ 1 | Penawaran dengan tanda tangan buyer palsu ditolak tanpa transaksi (F3.03) | C-09 | HNK-26.T5 | Hans | SELESAI (2026-10-21, lokal, belum merge: `offer::tests::forged_offers_are_refused` (buyer palsu, pengirim bukan key supplier, body diubah, advance > nominal) dan `reads_an_offer_made_by_the_web_app`; tidak ada yang disimpan atau dikirim untuk penawaran yang ditolak; konsol dicek dengan node tiruan) |
| BL-D23-03 | 3.1 | Tolak atau kedaluwarsa penawaran: pesan ke supplier | Supplier melihat penawaran ditolak atau kedaluwarsa | C-10 | HNK-26.T6, HNK-32.T6 | Hans | SELESAI (2026-10-22, audit: E2E lokal `TES-INV-FE-18524-D`: konsol menolak penawaran dengan alasan, supplier "Note and free the invoice" dari inbox, kartu deal menampilkan "Declined — TES: outside this financier's rules. Offer it to another financier."; kedaluwarsa 7 hari memakai jalur pesan yang sama, `expire_offers`) |
| BL-D23-04 | 3.2, F3.05, F3.08 | Salt komitmen dari library (CSPRNG 32 byte), disimpan per (invoice, financier), dipakai ulang saat retry | Retry untuk invoice yang sama memberi komitmen yang sama | P-08 | HNK-27.T1 | Hans | SELESAI (2026-10-20, `748d451`, U-HNK-27.1; DEV-14 disetujui) |
| BL-D23-05 | 3.2, F3.06, F3.08 | Kelas dari `classes_for(nominal, advance, tanggal advance, jatuh tempo)`; `Deal` membawa kelas; `check_entry` memeriksa kelas | Entri dengan kelas lain ditolak `EntryMismatch`; indeks `jitsuin index` tidak lagi kosong | K-1 | HNK-27.T2 | Hans | SELESAI (audit 2026-10-22: penolakan kelas lain terbukti di U-HNK-27.2; indeks tidak kosong: 5 entri berkelas di papan testnet, `jitsuin index` menampilkan `31-60 days  5  3-5%` (I-HNK-27.1), jitsuinfi-zcash PR #27) |
| BL-D23-06 | 3.2, F3.07, F3.09 | Kirim pembuka komitmen dan kelas ke supplier lewat relay | Supplier menerima pembuka komitmen dan kelas | P-04 | HNK-23.T8 | Hans | SELESAI (2026-10-22, audit: `opening_message` (node `src/offer.rs:217`) mengirim `financier_pk`, `salt`, `discount`, `tenor` bertanda tangan `financier_pk`; E2E lokal testnet `TES-INV-FE-36210`: supplier memakai permintaan entri itu lalu menandatangani entri `c64bd680…6575`) |
| BL-D23-07 | 3.3, F3.10 – F3.11 | API `POST /node/deals` membungkus `Flow::new` | Deal tidak lengkap (konfirmasi 0, advance 0, surat bukan milik invoice) ditolak dengan pesan | HNK-05.T3 | HNK-05.T3 | Hans | SELESAI (audit 2026-10-22: deal lahir dari `POST /node/console/offers/{id}/accept`, tidak ada `POST /node/deals`. Konfirmasi 0 dan advance 0 ditolak `offer::accept` dan lagi oleh `Flow::new` (test node `a_deal_starts_from_accepted_terms_and_reloads`, tidak ada yang tersimpan); surat untuk invoice lain ditolak `Flow::new` (test `jitsuin-flow` `financier.rs`). jitsuinfi-node PR #33 `2236a2a`) |
| BL-D23-08 | 3.5, F3.20 – F3.21 | Status cek papan di konsol (bebas, sudah dibiayai, lanjut setelah crash) | Tiap hasil lookup tampil dengan label yang terbaca | HNK-05.T4 | HNK-26.T16, HNK-32.T3 | Hans | SELESAI (2026-10-22, audit ulang setelah HNK-32.T3, node PR #35 + frontend PR #50: bebas = stasiun "Board checked" lalu langkah berikutnya, sudah dibiayai = "Already financed by another financier (first entry …). The deal stopped here: no entry was posted and no money left this node.", dibiayai ganda = kalimat + kartu 重; uji `a_stopped_deal_shows_a_code_and_the_entry_that_came_first` dan `stopReason`) |
| BL-D23-09 | 3.6, F3.22 – F3.27 | Kartu supplier "Tanda tangani entri papan" (0x01 atau 0x03 dengan sertifikat k atau tag) memakai fungsi entri wasm dengan parameter kelas | Entri yang ditandatangani lolos `check_entry` di node | C-15, K-1 | HNK-24.T6 | Hans | SELESAI (2026-10-20, `17a01ea`: entri membawa komitmen dari pembuka financier dan kelas 3/1, berstatus Registered di snapshot uji, I-HNK-24.3) |
| BL-D23-10 | 3.6, F3.22 | Varian entri bertag yang hanya menerima `history_tag` 32 byte | Supplier tidak lagi membutuhkan sertifikat k penuh | K-10 | HNK-27.T8 | Hans | SELESAI (2026-10-20, `8897517`, U-HNK-27.9) |
| BL-D23-11 | 3.7, F3.31 | Penolakan `EntryMismatch` tampil terbaca di konsol dan dikirim ke supplier | Supplier melihat alasan penolakan entri | C-13 | HNK-21.T9 | Hans | SELESAI (2026-10-22, audit: penolakan yang disebut baris ini punya kalimat di `explain.ts`, diuji `tests/explain.test.ts`) |
| BL-D23-12 | 3.8, F3.33 – F3.36 | `Register`: terima `BoardChecked` sebelum posting, cari entri yang sudah terkirim sebelum posting ulang | Restart setelah posting tidak membuat posting kedua; konflik yang muncul sebelum posting menjadi `Stopped` | K-4 | HNK-27.T5 | Hans | SELESAI (2026-10-20, `fef1d15`, U-HNK-27.4 – .5; uji crash testnet I-HNK-27.2 menyusul) |
| BL-D23-13 | 3.3 – 3.9, D11 | Persistensi state deal di node (serialisasi `Flow` dan dokumen deal) | Node yang di-restart melanjutkan deal dari state terakhir | C-16 | HNK-26.T10 | Hans | SELESAI (2026-10-22, audit: `Flow` diserialisasi JTSF ke `deals/<N>.flow` dan dimuat ulang tiap putaran `drive` (node `src/main.rs:1230`); uji `a_restored_snapshot_resumes_the_deal_in_every_state` dan `resumes_from_an_entry_posted_earlier` lulus) |
| BL-D23-14 | 3.9, F3.37 – F3.42 | Progres konfirmasi di konsol (n dari `min_confirmations`) | Konsol menampilkan hitungan konfirmasi sampai `AwaitAssignment` | HNK-05.T4 | HNK-26.T16, HNK-32.T4 | Hans | SELESAI (2026-10-22, audit ulang setelah HNK-32.T4, node PR #36 + frontend PR #51: E2E lokal testnet `TES-INV-FE-1185` konsol "Entry posted: 0 of 1 confirmations", `TES-INV-FE-53023` meta `entry_confirmations: 3`) |
| BL-D23-15 | Uji | Integrasi testnet: entri dengan kelas tertambang, `jitsuin index` menampilkan kelas (k = 5 butuh minimal 5 deal), crash dan restart sesudah posting | Kasus tercatat di TEST item terkait | HNK-04.T4, HNK-17 | HNK-17.T4 | Hans | TODO |

## Sudah ada (tanpa task baru)

- 3.4 Pindai papan (`scan`), 3.5 lookup N (`lookup`, `Flow::on_board`), 3.9 tunggu konfirmasi (`wait_for_confirmation`): diuji testnet lewat CLI scratchpad.

## Roadmap

- F3.32 menyimpan entri yang ditawarkan untuk bukti (P-14): tidak dibangun sebelum submit.
