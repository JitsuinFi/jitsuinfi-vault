---
tags: [ac, "HNK-25"]
type: ac
id: HNK-25
phase: F5
lead: Dave
owners: [Hans, Dave]
status: TODO
updated: 2026-10-20
---

# AC-HNK-25 - Alur deal di layar buyer

> **Peta link:** [[AC Hub]] · [[Backlog]] · **AC** · [[TEST-HNK-25 - Alur deal di layar buyer|Test]] · [[ES-HNK-25 - Alur deal di layar buyer|Exec Summary]]

**Lead:** Dave #dave · **Tim:** Hans #hans, Dave #dave · Dibuat 2026-10-20 dari [[FD-01 - Keputusan Usulan dan Gelombang Kerja]] dan [[FD-02 - Penelusuran Business Flow ke Backlog]] (D-30)

**Item:** HNK-25 · **Fase:** F5 · **Dependency:** HNK-22, HNK-23, HNK-27

## Deskripsi
Layar buyer: cek PDF syarat dan key, nomor invoice `k` otomatis dengan rantai yang tertambat, persetujuan permintaan riwayat, segel surat dengan isi terbaca, QR hanya untuk surat `Sealed`, pengingat, status pelunasan, dan riwayat sendiri. Desain: [[SEQ-02 - Buyer]]. Task rinci: [[SEQ-02 - Buyer-backlogs]].

## Acceptance criteria
Status per kriteria: `TODO` / `PASS` / `FAIL` / `BLOCKED`, wajib dengan tanggal dan bukti (commit, txid, log, id tes).

| ID | Kriteria | Status | Tanggal | Bukti |
|---|---|---|---|---|
| AC-HNK-25.1 | Buyer tidak mengetik `k`; relay yang menghapus sertifikat terakhir terdeteksi. | TODO | — | — |
| AC-HNK-25.2 | Hash PDF atau key yang salah memunculkan peringatan sebelum tanda tangan. | TODO | — | — |
| AC-HNK-25.3 | Surat tanpa s2 atau surat palsu tidak menghasilkan QR. | TODO | — | — |
| AC-HNK-25.4 | Satu pembayaran QR tertambang dan menjadi `Settled`, statusnya terlihat di layar buyer dan supplier. | TODO | — | — |
| AC-HNK-25.5 | Riwayat sendiri tampil tanpa unggah file. | TODO | — | — |

## Deviasi
_Kosong._ Kalau implementasi menyimpang dari keputusan, tulis di sini **dan** di [[Backlog]] bagian Log Deviasi. Tidak ada perubahan diam-diam.
