---
tags: [ac, "HNK-06"]
type: ac
id: HNK-06
phase: F3
lead: Hans
owners: [Dex, Hans, Dave]
status: PARSIAL
updated: 2026-10-17
---

# AC-HNK-06 - Pengalihan hak tagih dan pelunasan

> **Peta link:** [[AC Hub]] · [[Backlog]] · **AC** · [[TEST-HNK-06 - Pengalihan hak tagih dan pelunasan|Test]] · [[ES-HNK-06 - Pengalihan hak tagih dan pelunasan|Exec Summary]]

**Item:** HNK-06 · **Fase:** F3 · **Dependency:** HNK-05

**Lead:** Hans #hans · **Tim:** Dex #dex, Hans #hans, Dave #dave

## Deskripsi
Surat pengalihan ditandatangani supplier dan buyer. Buyer membayar ke financier saat jatuh tempo dengan memo yang merujuk N. Status lunas tercatat (opsional entri settled).

## Acceptance criteria
Status per kriteria: `TODO` / `PASS` / `FAIL` / `BLOCKED`, wajib dengan tanggal dan bukti (commit, txid, log, id tes).

| ID | Kriteria | Status | Tanggal | Bukti |
|---|---|---|---|---|
| AC-HNK-06.1 | Pengalihan memuat N, alamat bayar financier, dan tanda tangan supplier + buyer; terverifikasi. | TODO | — | — |
| AC-HNK-06.2 | Pembayaran buyer dengan memo N terdeteksi financier dan dicocokkan. | PASS | 2026-10-17 | Testnet: buyer (wallet-b) membayar dari URI ZIP-321 hasil `repayment_request` (tx `b29fd4e1755159e2088777e6f2a31284908db3997722763206ac2efe489f7118`, 50000 zat). Financier (wallet-a) mencocokkan ke N: kuitansi `JTR1` tipe pelunasan, tanda tangan buyer valid, nominal = output (verdict `Valid`, ditolak 0). Status `Unpaid` (4 dtk) → `Settled` (60 dtk). Commit `aff284d` |
| AC-HNK-06.3 | Status lunas tercatat; entri `H(N ‖ "settled")` opsional di papan. | PASS | 2026-10-17 | Status `Settled` tercatat dari pembayaran valid yang sudah ditambang (tinggi 4509102). Entri `settled` sebelum lunas ditolak (`NotSettled` 0/50000 zat). Entri `settled` `a81cd2045664e83a4141278f4878c401d6181344b90d02526fb2b61205e5e858` di papan (tinggi 4509105, tag `420b…` = `settled_tag(N)`, commitment nol); `lookup` N tetap `Registered`; posting ulang memakai entri yang sama. Penanda tangan entri = financier, **usulan D-18 menunggu user** |
| AC-HNK-06.4 | Mode confidential (buyer tidak diberi tahu) didokumentasikan sebagai opsi beserta risikonya. | TODO | — | — |

## Deviasi
Tidak ada deviasi. Detail yang belum ada di spesifikasi (penanda tangan dan isi commitment entri `settled`) diajukan sebagai **D-18** di [[Decision Log]], menunggu keputusan user.

_Catatan:_ Kalau implementasi menyimpang dari keputusan, tulis di sini **dan** di [[Backlog]] bagian Log Deviasi. Tidak ada perubahan diam-diam.
