---
tags: [flow, backlog]
status: DITETAPKAN
progress: 8/10 SELESAI
updated: 2026-10-20
---

# DFD-2.5 - Pelunasan dan Settled-backlogs

**Diagram:** [[DFD-2.5 - Pelunasan dan Settled]] · Rencana: [[FD-01 - Keputusan Usulan dan Gelombang Kerja]] · [[FD-02 - Penelusuran Business Flow ke Backlog]] · Backlog: [[Backlog]]

Task untuk proses 5.1 – 5.6. Aturan kolom sama dengan [[DFD-2.1 - Identitas dan Sesi-backlogs]].

Kolom Status mengikuti langkah 6 "Audit flow diagram" di [[Workflow Development]]: `TODO` → `DIKERJAKAN` → `AUDIT` (semua task backlog-nya DONE) → `SELESAI (tanggal, bukti)` atau `GAGAL AUDIT (tanggal, alasan)`; `DITUNDA` hanya dengan keputusan user. Antrean audit tampil di setiap `python3 scripts/sync-vault.py` (lewat `scripts/check-backlogs.py`). Backlog ini ditetapkan 2026-10-20 (D-32).

## Task

| ID | Elemen | Task | Selesai bila | Ref | Task backlog | Owner | Status |
|---|---|---|---|---|---|---|---|
| BL-D25-01 | 5.1, F5.02 – F5.05 | QR pelunasan hanya untuk surat `Sealed` (s0, s1, s2 diperiksa dengan `assignmentStatus`), alamat bayar ditampilkan | Surat tanpa s2 atau surat palsu tidak menghasilkan QR | K-2 | HNK-25.T4, HNK-32.T2 | Hans | SELESAI (2026-10-22, audit ulang setelah HNK-32.T2, frontend PR #49: QR hanya untuk surat tersimpan dengan tiga segel `Sealed`; E2E lokal: surat tempelan ditolak "this is not the letter you sealed for this invoice" dan tidak ada QR; `payProblems` diuji) |
| BL-D25-02 | 5.1 | Pengingat jatuh tempo lokal di layar buyer | Deal yang jatuh tempo dalam 7 hari tampil di kotak masuk buyer | C-18 | HNK-25.T5 | Hans | SELESAI (2026-10-22, audit: `dueSoon` (`buyer-invoices.ts:101`) diuji "financed invoices due within a week are reminded" (`tests/buyer-invoices.test.ts:42`); banner 期 di daftar invoice buyer (`BuyerPage.tsx:674-684`)) |
| BL-D25-03 | 5.2 – 5.3, F5.10 – F5.14 | Penjadwal berkala di node: sync, `repayment`, `Repayment::status`; tenggang dan tanggal dari konfigurasi node | Status deal diperbarui otomatis tanpa operator | C-20 | HNK-26.T11 | Hans | SELESAI (2026-10-22, audit: `drive_all` tiap 120 dtk memanggil `repayment` dan `status` dengan tenggang dari mandat (`main.rs:1359-1364`, `:1477`); E2E lokal testnet `TES-INV-FE-36210`: pelunasan `bab221b3…4771` lalu settled `85d12ce6…d030` tanpa aksi operator) |
| BL-D25-04 | 5.3, F5.14 | Tampilan status pelunasan dan sengketa di konsol: klaim buyer + txid, ekspor bukti | `Claimed` / `Disputed` / `Overdue` tampil dengan bukti yang bisa diunduh | C-21, C-22 | HNK-26.T13, HNK-32.T5 | Hans | AUDIT (2026-10-22, audit ulang setelah HNK-32.T5, frontend PR #52: bukti JTSE kini bisa diunduh di samping salin; sisa: status `Claimed` / `Disputed` / `Overdue` belum pernah tampil dengan deal nyata (butuh deal testnet yang lewat jatuh tempo)) |
| BL-D25-05 | 5.4, F5.19 | Settle tanpa klaim buyer menampilkan error yang terbaca | Pembayaran tanpa klaim tidak membuat entri settled dan alasannya tampil | C-13 | HNK-21.T9 | Hans | SELESAI (2026-10-22, audit: penolakan yang disebut baris ini punya kalimat di `explain.ts`, diuji `tests/explain.test.ts`) |
| BL-D25-06 | 5.5, F5.20 – F5.23 | Penjadwal mengingat txid `settled` yang sudah dikirim | Dua poll berturut-turut sebelum tertambang tidak memposting dua entri settled | K-5 | HNK-26.T12 | Hans | SELESAI (2026-10-22, audit: cabang settled hanya jalan bila `meta.settled_txid` kosong (`main.rs:1353`, `:1393`), `drive` diserialkan `deal_lock`, `post_settled` mengembalikan entri yang sudah ada (`settlement.rs:357`); E2E lokal testnet `TES-INV-FE-36210`: satu `settled_txid` `85d12ce6…d030` meski dipoll berulang) |
| BL-D25-07 | 5.5 | Keputusan D-xx: siapa memegang spending key untuk posting `settled` (P-12) | Keputusan tercatat di [[Decision Log]] | P-12 | D-31 | Hans | SELESAI (2026-10-20, keputusan D-31) |
| BL-D25-08 | 5.6, F5.25 | **Baru.** Financier mengirim bundel JTSB (surat + dokumen pelunasan) ke buyer dan supplier lewat relay setelah settled | Buyer dan supplier punya bundel yang bisa diperiksa terhadap papan | C-29 | HNK-26.T18 | Hans | SELESAI (2026-10-22, audit: E2E lokal testnet `TES-INV-FE-36210`: `bundle_sent: true`, supplier dan buyer menyimpan bundel (dicek `verifyBundle`), `/verify` "Bundle is genuine" dengan papan live sampai blok 4528099) |
| BL-D25-09 | 5.6, F5.24 – F5.27 | Status pelunasan di layar buyer dan supplier (`bundleOnBoard` + snapshot) | Buyer dan supplier melihat "settled tepat waktu / terlambat" tanpa unggah file | C-21, P-06 | HNK-25.T7 | Hans | SELESAI (2026-10-22, audit: buyer dan supplier membaca status dari bundel tersimpan dan papan live lewat `bundleOnBoard`, tanpa unggah file (`BuyerPage.tsx:650-661`, `SupplierPage.tsx:199-210`); `boardStatus` diuji; bundel `TES-INV-FE-36210` memberi "Settled yes, on time") |
| BL-D25-10 | Uji | Bayar QR dari Zodl (SPK-04) atau `zcash-devtool`; dana testnet untuk peserta uji | Satu pembayaran QR tertambang dan menjadi `Settled` | SPK-04, C-19 | HNK-25.T8 | Hans | DIKERJAKAN |

## Sudah ada (tanpa task baru)

- 5.1 QR dengan kuitansi + klaim (`buyerRepayment`), 5.2 pencocokan (`repayment`), 5.3 status (`Repayment::status`), 5.4 countersign (`settle`, `covering_height`), 5.5 posting (`post_settled`).
