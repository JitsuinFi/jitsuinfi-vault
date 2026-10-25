---
tags: [flow, backlog]
status: DITETAPKAN
progress: 9/10 SELESAI
updated: 2026-10-20
---

# DFD-2.6 - Riwayat Buyer-backlogs

**Diagram:** [[DFD-2.6 - Riwayat Buyer]] · Rencana: [[FD-01 - Keputusan Usulan dan Gelombang Kerja]] · [[FD-02 - Penelusuran Business Flow ke Backlog]] · Backlog: [[Backlog]]

Task untuk proses 6.1 – 6.8. Aturan kolom sama dengan [[DFD-2.1 - Identitas dan Sesi-backlogs]].

Kolom Status mengikuti langkah 6 "Audit flow diagram" di [[Workflow Development]]: `TODO` → `DIKERJAKAN` → `AUDIT` (semua task backlog-nya DONE) → `SELESAI (tanggal, bukti)` atau `GAGAL AUDIT (tanggal, alasan)`; `DITUNDA` hanya dengan keputusan user. Antrean audit tampil di setiap `python3 scripts/sync-vault.py` (lewat `scripts/check-backlogs.py`). Backlog ini ditetapkan 2026-10-20 (D-32).

## Task

| ID | Elemen | Task | Selesai bila | Ref | Task backlog | Owner | Status |
|---|---|---|---|---|---|---|---|
| BL-D26-01 | 6.1, F6.01 – F6.03 | Pesan "permintaan riwayat" dari node, ditandatangani `financier_pk` | Buyer menerima permintaan; permintaan dengan tanda tangan salah ditolak | P-04 | HNK-23.T8, HNK-32.T6 | Hans | SELESAI (2026-10-22, audit: E2E lokal testnet (`e2e-fe2.mjs`, deal `TES-INV-FE-11588`): mandat privat `min_buyer_history: 0`, node mengirim `history.request` dan buyer menerimanya di inbox ("Send my history"); tanda tangan salah ditolak di `verifyHeader` / `MailboxCard.tsx`, diuji `tests/relay-message.test.ts`) |
| BL-D26-02 | 6.2, F6.04 – F6.06 | Layar buyer: permintaan riwayat dengan nama kontak financier, tombol setujui atau tolak | Buyer melihat siapa yang meminta dan untuk invoice apa sebelum menyetujui | C-01, P-04 | HNK-25.T2, HNK-32.T6 | Hans | SELESAI (2026-10-22, audit: E2E lokal testnet (`e2e-fe2.mjs`, deal `TES-INV-FE-11588`): permintaan tampil di inbox buyer dengan teks `describe` (financier, invoice, jumlah, jatuh tempo) sebelum tombol "Send my history"; menolak = tidak menjawab, `BuyerPage.tsx:579-586`) |
| BL-D26-03 | 6.2, F6.07 – F6.10, D13 | Nomor `k` otomatis dari rantai yang tertambat; sertifikat yang tidak pernah tertambat dibuang; kepala rantai bertanda tangan disimpan terenkripsi di relay | Buyer tidak mengetik `k`; relay yang menghapus sertifikat terakhir terdeteksi | P-09 | HNK-25.T2, HNK-32.T6 | Hans | SELESAI (2026-10-22, audit: E2E lokal testnet (`e2e-fe2.mjs`, deal `TES-INV-FE-11588`): `k` otomatis ("Next invoice in your history #0", lalu key #1 untuk invoice kedua tanpa diketik); sertifikat tak tertambat dibuang dan relay yang tertinggal atau bercabang terdeteksi, diuji `tests/buyer-history.test.ts` (`reconcile`, `dropTail`); salinan di slot `state` relay) |
| BL-D26-04 | 6.3, F6.11 – F6.14 | Kirim rantai 0..k + `identity_pk` ke financier yang meminta, dan `history_tag` (atau sertifikat k) ke supplier | Financier dan supplier menerima isi yang dibutuhkan saja | P-04, K-10 | HNK-23.T7, HNK-32.T6 | Hans | SELESAI (2026-10-22, audit: E2E lokal testnet (`e2e-fe2.mjs`, deal `TES-INV-FE-11588`): buyer mengirim `history.chain` (sertifikat 0..k + `identity_pk`) ke financier, node lulus "Buyer history passed: 0 earlier invoices"; supplier menerima `history_tag` lewat pembuka komitmen node, entri tertanda tangan dengan tag; catatan: tag sampai ke supplier lewat node, bukan langsung dari buyer) |
| BL-D26-05 | 6.4, F6.16, D5 | Registri `identity_pk` buyer hasil KYC di node financier, dipakai saat memeriksa rantai | Rantai dengan `identity_pk` yang tidak terdaftar ditandai | C-02 | HNK-26.T7 | Hans | SELESAI (2026-10-21, lokal, belum merge: `buyers::tests` (tambah, ubah label, hapus, tersimpan; key salah ditolak; rantai tanpa atau dengan `identity_pk` tak terdaftar ditandai); konsol dicek dengan node tiruan) |
| BL-D26-06 | 6.5 – 6.6, F6.18 – F6.26 | API `POST /node/history/check` memanggil `check_buyer` dengan `MinimumStandard`, menyimpan laporan dan `history_tag` di deal | Hasil lulus menyimpan `history_tag`; retry setelah crash memakai tag yang tersimpan tanpa cek ulang | C-11 | HNK-26.T8, HNK-32.T6 | Hans | SELESAI (2026-10-22, audit: `check_buyer` dengan `MinimumStandard` dari mandat, tag di deal dan meta (E2E lokal testnet (`e2e-fe2.mjs`, deal `TES-INV-FE-11588`)); retry setelah crash memakai tag tersimpan tanpa cek ulang: node `ed15c4d` (`deals::checked_tag`, `buyer_history` mengirim ulang pembuka dengan tag itu), uji `a_deal_starts_from_accepted_terms_and_reloads` (tag bertahan setelah muat ulang), `cargo test` 51/51) |
| BL-D26-07 | 6.5, F6.22 | Alasan penolakan riwayat terbaca (`NotAnchored`, `Equivocation`, `FinancierNotAllowed`, `UndisclosedSuccessor`, di bawah standar) | Tiap alasan punya teks yang menjelaskan artinya | C-13 | HNK-21.T9 | Hans | SELESAI (2026-10-22, audit: penolakan yang disebut baris ini punya kalimat di `explain.ts`, diuji `tests/explain.test.ts`) |
| BL-D26-08 | 6.7, F6.27 – F6.28 | Pengaturan policy di konsol: allowlist financier, standar minimal, tenggang | Operator mengubah policy tanpa mengedit kode; nilai bertahan setelah restart | C-12 | HNK-26.T9 | Hans | SELESAI (2026-10-22, audit: allowlist tambahan, standar tepat waktu dan tenggang diubah di konsol 内規 tanpa kode, disimpan di `private-mandate.json`) |
| BL-D26-09 | 6.8, F6.29 – F6.32 | Kartu "Riwayat saya" di layar buyer (`verifyHistory` dengan allowlist dari sertifikat sendiri + snapshot) | Buyer melihat status tiap invoice tanpa unggah file | C-14, P-06 | HNK-25.T6, HNK-32.T6 | Hans | SELESAI (2026-10-22, audit: E2E lokal testnet (`e2e-fe2.mjs`, deal `TES-INV-FE-11588`): kartu "My payment history" menampilkan "1 on time · 0 late · 0 open · 0 defaulted" dan per invoice "#0 · due 2026-11-21 · 0.001 ZEC paid on time", dicek terhadap papan live blok 4529082, tanpa unggah file) |
| BL-D26-10 | Uji | Integrasi testnet: dua invoice berurutan dengan riwayat, invoice kedua lolos standar | Kasus tercatat di TEST-HNK-20 atau HNK-17 | HNK-17 | HNK-17.T4 | Hans | AUDIT (2026-10-25, audit: satu invoice dengan riwayat lulus (`TES-INV-FE-11588`, "Buyer history passed: 0 earlier invoices"); sisa: dua invoice berurutan untuk buyer yang sama, invoice kedua lolos standar dengan riwayat invoice pertama) |

## Sudah ada (tanpa task baru)

- 6.2 sertifikat (`buyerHistoryCert`), 6.4 verifikasi rantai (`verify_certs`), 6.5 cocokkan dengan papan (`verify_history`), 6.6 standar minimal (`MinimumStandard::evaluate`, `check_buyer`), struktur `HistoryPolicy`.

## Keputusan yang dibutuhkan

- Griefing `UndisclosedSuccessor` (Spec #1 di [[Pra-review Spesifikasi dan Threat Model]]): belum ada jalur bantahan.
