---
tags: [flow, backlog]
status: DITETAPKAN
progress: 11/11 SELESAI
updated: 2026-10-20
---

# DFD-2.2 - Penerbitan dan Tanda Tangan Invoice-backlogs

**Diagram:** [[DFD-2.2 - Penerbitan dan Tanda Tangan Invoice]] · Rencana: [[FD-01 - Keputusan Usulan dan Gelombang Kerja]] · [[FD-02 - Penelusuran Business Flow ke Backlog]] · Backlog: [[Backlog]]

Task untuk proses 2.1 – 2.8. Aturan kolom sama dengan [[DFD-2.1 - Identitas dan Sesi-backlogs]].

Kolom Status mengikuti langkah 6 "Audit flow diagram" di [[Workflow Development]]: `TODO` → `DIKERJAKAN` → `AUDIT` (semua task backlog-nya DONE) → `SELESAI (tanggal, bukti)` atau `GAGAL AUDIT (tanggal, alasan)`; `DITUNDA` hanya dengan keputusan user. Antrean audit tampil di setiap `python3 scripts/sync-vault.py` (lewat `scripts/check-backlogs.py`). Backlog ini ditetapkan 2026-10-20 (D-32).

## Task

| ID | Elemen | Task | Selesai bila | Ref | Task backlog | Owner | Status |
|---|---|---|---|---|---|---|---|
| BL-D22-01 | 2.1, F2.01 – F2.04 | Layar buyer "Bagikan key invoice": kirim `invoice_pk(k)` ke kontak supplier lewat relay; salin manual tetap ada | Supplier menerima `invoice_pk(k)` tanpa salin-tempel | P-04, P-09 | HNK-25.T2, HNK-32.T6 | Hans | SELESAI (2026-10-22, audit: E2E lokal testnet (`e2e-fe2.mjs`, deal `TES-INV-FE-11588`): buyer "Send this key to the supplier" (relay, ditandatangani key invoice itu), supplier "Use for my next invoice", baris buyer invoice terisi tanpa salin-tempel; skrip gagal bila field kosong) |
| BL-D22-02 | 2.2, F2.06 – F2.07 | Turunan key per invoice supplier di `jitsuin-core` + `jitsuin-wasm`: keyed BLAKE2b, personalisasi sendiri, input unik per invoice dengan prefiks panjang; test vector | Master + input yang sama memberi key yang sama; input berbeda memberi key berbeda; vector tercatat | P-03 | HNK-24.T1 | Hans | SELESAI (2026-10-20, `a252568`, U-HNK-24.1) |
| BL-D22-03 | 2.2, F2.05, F2.08 | Layar supplier memakai key turunan; tombol unduh JSON plaintext dihapus; `invoice_id` yang sudah dipakai ditolak | Tidak ada unduhan secret; `invoice_id` kembar memunculkan pesan | P-03 | HNK-24.T2 | Hans | SELESAI (2026-10-20, `17a01ea`: tanpa unduhan secret; nomor invoice yang dipakai ulang ditolak, I-HNK-24.3) |
| BL-D22-04 | 2.4 | Invoice sebagai lembar kertas (polish) | Sesuai HNK-21.T2 | HNK-21.T2 | HNK-21.T2 | Dex | SELESAI (2026-10-22, audit: invoice ditulis di lembar 請求書 di production (frontend PR #45, lalu PR #47 React dengan paritas visual 0,00 %); E2E lokal testnet `TES-INV-FE-36210` membuat invoice di lembar itu sampai settled) |
| BL-D22-05 | 2.5, F2.16 – F2.18 | Pesan relay "invoice" berisi invoice kanonik + PDF syarat terenkripsi; batas ukuran PDF | Pesan sesuai skema C-04; PDF di atas batas ditolak dengan pesan | C-04, P-04 | HNK-23.T1, HNK-23.T7 | Hans | SELESAI (2026-10-22, audit: skema `invoice.sign_request` (framing `JTSM`, satu lampiran PDF, `MAX_ATTACHMENT` 2 MiB, `relay-message.ts:23`, `:334`); uji "a PDF over 2 MiB is refused" (`tests/relay-message.test.ts:46`, 80/80); E2E lokal testnet `TES-INV-FE-36210`: invoice + PDF sampai di inbox buyer, "Terms PDF matches the invoice") |
| BL-D22-06 | 2.6, F2.19 – F2.22 | Layar buyer: input PDF syarat, cek SHA-256 dengan `terms_hash`, tampilkan apakah `buyer_pk` = `invoice_pk(k)` | Hash salah atau key salah memunculkan peringatan sebelum tombol tanda tangan aktif | C-05 | HNK-25.T1 | Hans | SELESAI (2026-10-20: hash PDF atau key salah memunculkan peringatan dan tombol tanda tangan tetap mati; I-HNK-25.3; PR #11 `dd63246`) |
| BL-D22-07 | 2.6, F2.21, D4 | Simpan invoice yang diterima di penyimpanan lokal buyer (lintas sesi) | Invoice masih ada setelah tab ditutup dan dibuka lagi | C-07 | HNK-25.T1 | Hans | SELESAI (2026-10-20: invoice yang diterima disimpan di store terenkripsi buyer; di browser, sesi baru dengan secret yang sama masih menampilkan `TES-INV-T25` dari sesi sebelumnya; PR #12 `56b337a`) |
| BL-D22-08 | 2.7, F2.26 – F2.27 | Kirim `buyer_signature` ke supplier lewat relay | Supplier menerima tanda tangan tanpa salin-tempel | P-04 | HNK-23.T7 | Hans | SELESAI (2026-10-22, audit: E2E lokal testnet `TES-INV-FE-36210`: buyer mengirim tanda tangan lewat relay, supplier mengambilnya dari inbox lalu menawarkan ke financier; entri `c64bd680…6575`) |
| BL-D22-09 | 2.8, F2.28 – F2.31 | Kartu supplier: cek tanda tangan buyer (`bundleBuild`), simpan invoice + tanda tangan sah | Tanda tangan palsu ditolak dengan pesan; yang sah tersimpan di deal | C-06 | HNK-24.T4 | Hans | SELESAI (2026-10-20, `17a01ea`: tanda tangan palsu ditolak, yang sah tersimpan, I-HNK-24.3) |
| BL-D22-10 | 2.8, D4 | Simpan dokumen deal supplier lintas sesi | Deal masih ada setelah tab ditutup | C-07 | HNK-24.T3 | Hans | SELESAI (2026-10-20, `17a01ea`: deal supplier bertahan setelah reload dan unlock ulang, I-HNK-24.3) |
| BL-D22-11 | Uji | E2E BF-02: supplier menerbitkan, buyer menandatangani lewat relay, supplier memeriksa | Satu siklus `TES-` lulus di HNK-17 | HNK-17 | HNK-17.T4 | Hans | SELESAI (2026-10-25, audit: E2E production `TES-INV-PROD-1996` (HNK-17.T4, DEAL VERIFIED 3/3) dan E2E lokal testnet `TES-INV-FE-11588` (HNK-32.T6): supplier menerbitkan, buyer menandatangani lewat relay, supplier memeriksa dan menyimpan) |

## Sudah ada (tanpa task baru)

- 2.3 Hash file syarat (`documentHash`), 2.4 invoice kanonik dan N (`invoiceEncode`, `invoiceDecode`), 2.7 tanda tangan buyer yang menolak invoice untuk key lain (`buyerSignInvoice`).
