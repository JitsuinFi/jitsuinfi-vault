---
tags: [ac, "HNK-19"]
type: ac
id: HNK-19
phase: F3
lead: Hans
owners: [Hans]
status: PASS
updated: 2026-10-17
---

# AC-HNK-19 - Jitsuin Seal tanda tangan berantai dan Sign-to-Pay

> **Peta link:** [[AC Hub]] · [[Backlog]] · **AC** · [[TEST-HNK-19 - Jitsuin Seal tanda tangan berantai dan Sign-to-Pay|Test]] · [[ES-HNK-19 - Jitsuin Seal tanda tangan berantai dan Sign-to-Pay|Exec Summary]]

**Lead:** Hans #hans · **Tim:** Hans #hans

**Item:** HNK-19 · **Fase:** F3 · **Dependency:** HNK-05, HNK-06

## Deskripsi
Adopsi konsep SignBaliola (D-21): dokumen invoice, surat pengalihan, dan pelunasan ditandatangani beberapa pihak secara berurutan dengan seal berantai. Advance hanya cair setelah surat pengalihan tersegel Supplier dan Buyer, dan tanda tangan Financier ikut dalam transaksi advance (Sign-to-Pay). Pelunasan sah hanya dengan tanda tangan buyer dan financier. Desain: [[Desain Jitsuin Seal]].

## Acceptance criteria
Status per kriteria: `TODO` / `PASS` / `FAIL` / `BLOCKED`, wajib dengan tanggal dan bukti (commit, txid, log, id tes).

| ID | Kriteria | Status | Tanggal | Bukti |
|---|---|---|---|---|
| AC-HNK-19.1 | Seal berantai: urutan salah, role ganda, satu key untuk dua role, dan isi seal yang diubah ditolak; policy lengkap menghasilkan `Sealed`. | PASS | 2026-10-17 | `b007a26`; unit `seal::tests` (6): urutan policy, loncat/tukar urutan, signer salah, dokumen lain, tamper, rantai putus, satu key dua role (`SelfApproval`), decoder ketat |
| AC-HNK-19.2 | Surat pengalihan kanonik memuat N, nominal, jatuh tempo, `financier_pk`, alamat bayar, dan `terms_hash`; tersegel Supplier lalu Buyer dan terverifikasi. | PASS | 2026-10-17 | `fdc399e`; unit `assignment::tests` (3). Testnet: surat untuk `TES-INV-0003-1792179703` tersegel Supplier lalu Buyer → `Incomplete { next: Financier }`; seal Supplier saja ditolak oleh alur |
| AC-HNK-19.3 | Advance tidak bisa dikirim sebelum seal Supplier dan Buyer valid; memo advance memuat kuitansi dan seal Financier dalam satu transaksi shielded. | PASS | 2026-10-17 | `f9fee3e`. Testnet: `pay_advance` ditolak di `AwaitAssignment` sebelum surat tersegel; advance `501e40dafff4d2b7bcedf1adb9535522dc8977b6c6c8f8d3da55e00574335ccb` (30000 zat, fee 10000 zat) membawa kuitansi + 1 seal Financier dalam satu memo; supplier memverifikasi kuitansi `Valid` dan surat `Sealed` |
| AC-HNK-19.4 | Entri `settled` memuat tanda tangan buyer dan financier; klaim buyer tanpa pembayaran berakhir `Disputed`, bukan `Settled`. | PASS | 2026-10-17 | `f07787b`. Unit `a_lying_buyer_never_reaches_settled` (klaim 50.000 tapi kirim 1.000 → `Claimed` lalu `Disputed`). Testnet: pelunasan `d59014b726554404fc5729c8699d0d029fab7a3900485241d632c50bf4aadaf0` dengan klaim buyer; watchdog `Unpaid` (4 dtk) → `Settled` (45 dtk); entri `settled` `dcba74c63a701057d0e6e5f2cee4391b509d393c792801449c772c9552b7cad3` (tinggi 4509304) dua tanda tangan valid, `on_time=true`, lookup register tetap `Registered`; posting ulang memakai entri yang sama |
| AC-HNK-19.5 | Satu siklus penuh `TES-INV-0003` di testnet (DEV-03), semua txid tercatat. | PASS | 2026-10-17 | Testnet (DEV-03), 302 dtk: entri `33b8f3b0aa754e790e9c7fac0ae7dc08ce8612a8c26620d551d790e1ea390a56`, advance `501e40dafff4d2b7bcedf1adb9535522dc8977b6c6c8f8d3da55e00574335ccb`, pelunasan `d59014b726554404fc5729c8699d0d029fab7a3900485241d632c50bf4aadaf0`, `settled` `dcba74c63a701057d0e6e5f2cee4391b509d393c792801449c772c9552b7cad3`. Bundel verifikasi diuji terhadap papan (lihat TEST) |

## Deviasi
- **DEV-06**: surat pengalihan dikerjakan di HNK-19.T2 (dari HNK-06.T1).
- **DEV-07**: alur financier mendapat gerbang `AwaitAssignment`.
- **DEV-08**: entri `settled` dua tanda tangan menggantikan layout `aff284d`.

_Catatan:_ Kalau implementasi menyimpang dari keputusan, tulis di sini **dan** di [[Backlog]] bagian Log Deviasi. Tidak ada perubahan diam-diam.
