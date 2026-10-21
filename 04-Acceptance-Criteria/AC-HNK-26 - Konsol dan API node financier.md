---
tags: [ac, "HNK-26"]
type: ac
id: HNK-26
phase: F5
lead: Hans
owners: [Hans]
status: TODO
updated: 2026-10-20
---

# AC-HNK-26 - Konsol dan API node financier

> **Peta link:** [[AC Hub]] · [[Backlog]] · **AC** · [[TEST-HNK-26 - Konsol dan API node financier|Test]] · [[ES-HNK-26 - Konsol dan API node financier|Exec Summary]]

**Lead:** Hans #hans · **Tim:** Hans #hans · Dibuat 2026-10-20 dari [[FD-01 - Keputusan Usulan dan Gelombang Kerja]] dan [[FD-02 - Penelusuran Business Flow ke Backlog]] (D-30)

**Item:** HNK-26 · **Fase:** F5 · **Dependency:** HNK-05.T3, HNK-23, HNK-27

## Deskripsi
Node financier sebagai server milik financier dengan konsol di origin node (P-05, P-11): setup, pairing passkey, sesi, kotak surat financier, penawaran, cek riwayat dengan standar minimal, policy, persistensi state, penjadwal pelunasan, sengketa, bukti pembiayaan ganda, pipeline per state. Desain: [[SEQ-03 - Financier]]. Task rinci: [[SEQ-03 - Financier-backlogs]]. API dasar tetap di HNK-05.T3, integrasi layar di HNK-05.T4.

## Acceptance criteria
Status per kriteria: `TODO` / `PASS` / `FAIL` / `BLOCKED`, wajib dengan tanggal dan bukti (commit, txid, log, id tes).

| ID | Kriteria | Status | Tanggal | Bukti |
|---|---|---|---|---|
| AC-HNK-26.1 | Operator menjalankan satu deal `TES-` dari penawaran sampai settled hanya dari konsol di origin node. | TODO | — | — |
| AC-HNK-26.2 | Node yang di-restart di tengah deal melanjutkan dari state terakhir tanpa posting ganda. | TODO | 2026-10-20 | Library: snapshot `JTSF` (`23be34a`, U-HNK-26.2). Restart node sungguhan (I-HNK-26.2) menunggu node |
| AC-HNK-26.3 | Assertion ulang (replay) ditolak; advance tidak terkirim tanpa persetujuan operator untuk deal itu. | TODO | 2026-10-21 | Bagian replay PASS: assertion sama dikirim ulang 410, assertion lama untuk challenge baru 403 (jitsuinfi-node PR #5, uji browser lokal); sesi produksi berjalan. Bagian persetujuan advance: gerbang `pay::advance` + approval passkey per intent ada (HNK-26.T15, `0f99c30`), menunggu deal API yang membayar lewat gerbang itu |
| AC-HNK-26.4 | Status pelunasan diperbarui otomatis; dua poll sebelum tertambang tidak memposting dua entri settled. | TODO | — | — |
| AC-HNK-26.5 | `Stopped(DoubleFinanced)` menghasilkan bukti yang lolos `jitsuin verify`. | TODO | 2026-10-20 | Library: `0ee55c6`, U-HNK-26.4 (bukti lolos `verify_proof_on_board`, aturan yang sama dengan `jitsuin verify`). Belum di node: bukti belum disimpan di deal |

## Deviasi
_Kosong._ Kalau implementasi menyimpang dari keputusan, tulis di sini **dan** di [[Backlog]] bagian Log Deviasi. Tidak ada perubahan diam-diam.
