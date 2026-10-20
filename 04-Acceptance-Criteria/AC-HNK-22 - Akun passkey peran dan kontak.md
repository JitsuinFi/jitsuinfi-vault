---
tags: [ac, "HNK-22"]
type: ac
id: HNK-22
phase: F5
lead: Dave
owners: [Dave]
status: TODO
updated: 2026-10-20
---

# AC-HNK-22 - Akun passkey peran dan kontak

> **Peta link:** [[AC Hub]] · [[Backlog]] · **AC** · [[TEST-HNK-22 - Akun passkey peran dan kontak|Test]] · [[ES-HNK-22 - Akun passkey peran dan kontak|Exec Summary]]

**Lead:** Dave #dave · **Tim:** Dave #dave · Dibuat 2026-10-20 dari [[FD-01 - Keputusan Usulan dan Gelombang Kerja]] dan [[FD-02 - Penelusuran Business Flow ke Backlog]] (D-30)

**Item:** HNK-22 · **Fase:** F5 · **Dependency:** HNK-10

## Deskripsi
Akun = satu passkey per orang (WebAuthn PRF) untuk supplier, buyer, dan anggota dana di web app: daftar, masuk, tambah atau ganti peran, stempel per tanda tangan, kartu kontak, dan kotak masuk per peran. Desain: [[SEQ-00 - Autentikasi dan Onboarding]], [[DFD-2.1 - Identitas dan Sesi]], usulan P-01, P-02, P-07 (disetujui D-30). Task rinci: [[DFD-2.1 - Identitas dan Sesi-backlogs]], [[SEQ-00 - Autentikasi dan Onboarding-backlogs]].

## Acceptance criteria
Status per kriteria: `TODO` / `PASS` / `FAIL` / `BLOCKED`, wajib dengan tanggal dan bukti (commit, txid, log, id tes).

| ID | Kriteria | Status | Tanggal | Bukti |
|---|---|---|---|---|
| AC-HNK-22.1 | Satu passkey dipakai untuk supplier, buyer, dan anggota; klik Daftar dua kali tidak membuat credential kedua. | TODO | — | — |
| AC-HNK-22.2 | Masuk di perangkat kedua dengan passkey tersinkron menghasilkan sidik jari key yang sama; localStorage kosong tidak mengubah key. | TODO | — | — |
| AC-HNK-22.3 | Key buyer lama (salt `jitsuin/buyer/master/v1`) tidak berubah setelah migrasi. | TODO | — | — |
| AC-HNK-22.4 | Setelah stempel, tidak ada master atau key tanda tangan di memori tab; sesi terkunci setelah 15 menit idle. | TODO | — | — |
| AC-HNK-22.5 | Supplier dan buyer bisa saling menambah kontak; kotak masuk menampilkan dokumen baru tanpa muat ulang. | TODO | — | — |

## Deviasi
_Kosong._ Kalau implementasi menyimpang dari keputusan, tulis di sini **dan** di [[Backlog]] bagian Log Deviasi. Tidak ada perubahan diam-diam.
