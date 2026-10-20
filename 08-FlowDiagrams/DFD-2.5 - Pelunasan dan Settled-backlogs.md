---
tags: [flow, backlog]
status: DITETAPKAN
progress: 1/10 SELESAI
updated: 2026-10-20
---

# DFD-2.5 - Pelunasan dan Settled-backlogs

**Diagram:** [[DFD-2.5 - Pelunasan dan Settled]] · Rencana: [[FD-01 - Keputusan Usulan dan Gelombang Kerja]] · [[FD-02 - Penelusuran Business Flow ke Backlog]] · Backlog: [[Backlog]]

Task untuk proses 5.1 – 5.6. Aturan kolom sama dengan [[DFD-2.1 - Identitas dan Sesi-backlogs]].

Kolom Status mengikuti langkah 6 "Audit flow diagram" di [[Workflow Development]]: `TODO` → `DIKERJAKAN` → `AUDIT` (semua task backlog-nya DONE) → `SELESAI (tanggal, bukti)` atau `GAGAL AUDIT (tanggal, alasan)`; `DITUNDA` hanya dengan keputusan user. Antrean audit tampil di setiap `python3 scripts/sync-vault.py` (lewat `scripts/check-backlogs.py`). Backlog ini ditetapkan 2026-10-20 (D-32).

## Task

| ID | Elemen | Task | Selesai bila | Ref | Task backlog | Owner | Status |
|---|---|---|---|---|---|---|---|
| BL-D25-01 | 5.1, F5.02 – F5.05 | QR pelunasan hanya untuk surat `Sealed` (s0, s1, s2 diperiksa dengan `assignmentStatus`), alamat bayar ditampilkan | Surat tanpa s2 atau surat palsu tidak menghasilkan QR | K-2 | HNK-25.T4 | Dave | TODO |
| BL-D25-02 | 5.1 | Pengingat jatuh tempo lokal di layar buyer | Deal yang jatuh tempo dalam 7 hari tampil di kotak masuk buyer | C-18 | HNK-25.T5 | Dave | TODO |
| BL-D25-03 | 5.2 – 5.3, F5.10 – F5.14 | Penjadwal berkala di node: sync, `repayment`, `Repayment::status`; tenggang dan tanggal dari konfigurasi node | Status deal diperbarui otomatis tanpa operator | C-20 | HNK-26.T11 | Dex | TODO |
| BL-D25-04 | 5.3, F5.14 | Tampilan status pelunasan dan sengketa di konsol: klaim buyer + txid, ekspor bukti | `Claimed` / `Disputed` / `Overdue` tampil dengan bukti yang bisa diunduh | C-21, C-22 | HNK-26.T13 | Hans | TODO |
| BL-D25-05 | 5.4, F5.19 | Settle tanpa klaim buyer menampilkan error yang terbaca | Pembayaran tanpa klaim tidak membuat entri settled dan alasannya tampil | C-13 | HNK-21.T9 | Dave | TODO |
| BL-D25-06 | 5.5, F5.20 – F5.23 | Penjadwal mengingat txid `settled` yang sudah dikirim | Dua poll berturut-turut sebelum tertambang tidak memposting dua entri settled | K-5 | HNK-26.T12 | Dex | TODO |
| BL-D25-07 | 5.5 | Keputusan D-xx: siapa memegang spending key untuk posting `settled` (P-12) | Keputusan tercatat di [[Decision Log]] | P-12 | D-31 | Hans | SELESAI (2026-10-20, keputusan D-31) |
| BL-D25-08 | 5.6, F5.25 | **Baru.** Financier mengirim bundel JTSB (surat + dokumen pelunasan) ke buyer dan supplier lewat relay setelah settled | Buyer dan supplier punya bundel yang bisa diperiksa terhadap papan | C-29 | HNK-26.T18 | Dex | TODO |
| BL-D25-09 | 5.6, F5.24 – F5.27 | Status pelunasan di layar buyer dan supplier (`bundleOnBoard` + snapshot) | Buyer dan supplier melihat "settled tepat waktu / terlambat" tanpa unggah file | C-21, P-06 | HNK-25.T7 | Dave | TODO |
| BL-D25-10 | Uji | Bayar QR dari Zodl (SPK-04) atau `zcash-devtool`; dana testnet untuk peserta uji | Satu pembayaran QR tertambang dan menjadi `Settled` | SPK-04, C-19 | HNK-25.T8 | Dave | TODO |

## Sudah ada (tanpa task baru)

- 5.1 QR dengan kuitansi + klaim (`buyerRepayment`), 5.2 pencocokan (`repayment`), 5.3 status (`Repayment::status`), 5.4 countersign (`settle`, `covering_height`), 5.5 posting (`post_settled`).
