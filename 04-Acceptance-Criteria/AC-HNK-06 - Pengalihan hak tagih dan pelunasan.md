---
tags: [ac, "HNK-06"]
type: ac
id: HNK-06
phase: F3
lead: Hans
owners: [Dex, Hans, Dave]
status: TODO
updated: 2026-10-16
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
| AC-HNK-06.2 | Pembayaran buyer dengan memo N terdeteksi financier dan dicocokkan. | TODO | — | — |
| AC-HNK-06.3 | Status lunas tercatat; entri `H(N ‖ "settled")` opsional di papan. | TODO | — | — |
| AC-HNK-06.4 | Mode confidential (buyer tidak diberi tahu) didokumentasikan sebagai opsi beserta risikonya. | TODO | — | — |

## Deviasi
_Kosong._ Kalau implementasi menyimpang dari keputusan, tulis di sini **dan** di [[Backlog]] bagian Log Deviasi. Tidak ada perubahan diam-diam.
