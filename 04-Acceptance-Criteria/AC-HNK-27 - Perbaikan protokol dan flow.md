---
tags: [ac, "HNK-27"]
type: ac
id: HNK-27
phase: F3
lead: Hans
owners: [Hans]
status: TODO
updated: 2026-10-20
---

# AC-HNK-27 - Perbaikan protokol dan flow

> **Peta link:** [[AC Hub]] · [[Backlog]] · **AC** · [[TEST-HNK-27 - Perbaikan protokol dan flow|Test]] · [[ES-HNK-27 - Perbaikan protokol dan flow|Exec Summary]]

**Lead:** Hans #hans · **Tim:** Hans #hans · Dibuat 2026-10-20 dari [[FD-01 - Keputusan Usulan dan Gelombang Kerja]] dan [[FD-02 - Penelusuran Business Flow ke Backlog]] (D-30)

**Item:** HNK-27 · **Fase:** F3 · **Dependency:** HNK-05, HNK-19, HNK-20

## Deskripsi
Perbaikan kode dari audit diagram (FD-00 §6) dan usulan kecil yang disetujui D-30: salt komitmen dari library, kelas diskon/tenor, `assignmentDecode`, posisi papan di bukti wasm, pemulihan `register()`, konfirmasi ulang, `Done` setelah konfirmasi, cek nominal advance, entri bertag tanpa sertifikat penuh, API wasm berbasis byte, CLI solvabilitas.

## Acceptance criteria
Status per kriteria: `TODO` / `PASS` / `FAIL` / `BLOCKED`, wajib dengan tanggal dan bukti (commit, txid, log, id tes).

| ID | Kriteria | Status | Tanggal | Bukti |
|---|---|---|---|---|
| AC-HNK-27.1 | Retry untuk invoice yang sama memberi komitmen yang sama; tidak ada JTSP dari retry. | TODO | — | — |
| AC-HNK-27.2 | Entri bertanda tangan membawa kelas sungguhan; `jitsuin index` tidak lagi kosong untuk ≥ 5 deal per kelas. | TODO | — | — |
| AC-HNK-27.3 | Restart setelah posting tidak membuat posting kedua; advance tidak dibayar dengan konfirmasi di bawah minimum setelah reorg. | TODO | — | — |
| AC-HNK-27.4 | Advance kurang dari yang disepakati gagal diverifikasi. | TODO | — | — |
| AC-HNK-27.5 | Bukti dari wasm dengan posisi lolos `jitsuin verify`. | TODO | — | — |

## Deviasi
_Kosong._ Kalau implementasi menyimpang dari keputusan, tulis di sini **dan** di [[Backlog]] bagian Log Deviasi. Tidak ada perubahan diam-diam.
