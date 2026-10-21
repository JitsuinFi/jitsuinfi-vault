---
tags: [flow, backlog]
status: DITETAPKAN
progress: 2/4 SELESAI
updated: 2026-10-20
---

# SEQ-00 - Autentikasi dan Onboarding-backlogs

**Diagram:** [[SEQ-00 - Autentikasi dan Onboarding]] · Task data dan proses: [[DFD-2.1 - Identitas dan Sesi-backlogs]] · Rencana: [[FD-01 - Keputusan Usulan dan Gelombang Kerja]] · [[FD-02 - Penelusuran Business Flow ke Backlog]] · Backlog: [[Backlog]]

Backlog sequence merujuk task di backlog DFD (rumah tetap tiap task, supaya tidak dobel) dan hanya menambah task khusus urutan, layar, dan uji per peran (`BL-S00-xx`).

Kolom Status mengikuti langkah 6 "Audit flow diagram" di [[Workflow Development]]: `TODO` → `DIKERJAKAN` → `AUDIT` (semua task backlog-nya DONE) → `SELESAI (tanggal, bukti)` atau `GAGAL AUDIT (tanggal, alasan)`; `DITUNDA` hanya dengan keputusan user. Antrean audit tampil di setiap `python3 scripts/sync-vault.py` (lewat `scripts/check-backlogs.py`). Backlog ini ditetapkan 2026-10-20 (D-32).

## Pemetaan per bagian

| Bagian | Langkah di sequence | Task |
|---|---|---|
| Daftar | Cek WebAuthn dan HTTPS, mode demo test secret | BL-S00-01 |
| Daftar | `create()` satu kali, PRF, credential yatim | BL-D21-01, BL-D21-02, BL-D21-18 |
| Daftar | `get()` dengan salt peran dan salt inbox, turunan key, sidik jari | BL-D21-04, BL-D21-05, BL-D21-06 |
| Daftar | Kotak surat, `mailbox_id` turunan, daftar ke relay | BL-D21-07, BL-D21-08 |
| Daftar | Profil lokal, kartu kontak | BL-D21-03, BL-D21-11 |
| Masuk | `get()` dengan `allowCredentials`, key identik, sidik jari | BL-D21-04, BL-D21-05 |
| Masuk | Baca kotak surat dengan bukti kepemilikan, dekripsi dokumen | BL-D21-09, BL-S00-02 |
| Tambah atau ganti peran | `get()` credential yang sama dengan salt peran lain | BL-D21-01, BL-S00-03 |
| Sesi dan stempel | PRF per stempel, `Uint8Array` dinolkan, kunci 15 menit | BL-D21-12, BL-D21-13 |
| Pairing node | Setup node, kode pairing, `create()` untuk rp node, attestation | BL-D21-14, BL-D21-15, BL-D21-16 |
| Konsol node | Challenge, assertion, cookie | BL-D21-17 |
| Catatan keamanan | `rp.id` eksplisit, pemulihan passkey, CSP setelah relay | BL-D21-18, BL-D0-08; pemulihan = roadmap |

## Task khusus sequence

| ID | Bagian | Task | Selesai bila | Ref | Task backlog | Owner | Status |
|---|---|---|---|---|---|---|---|
| BL-S00-01 | Daftar | Mode demo: browser tanpa WebAuthn atau bukan HTTPS memakai test secret; label "data uji saja" jelas di layar | Mode demo hanya muncul bila passkey tidak tersedia | SEQ-00 catatan | HNK-22.T1 | Hans | SELESAI (2026-10-20, `7814fbc`, U-HNK-22.1, I-HNK-22.2: test secret hanya bila passkey tidak tersedia atau authenticator tanpa PRF, berlabel data uji) |
| BL-S00-02 | Masuk | Kotak masuk per peran: ambil pesan baru setelah masuk dan secara berkala, tampilkan sebagai tindakan yang perlu dikerjakan | Dokumen yang dikirim rekan muncul tanpa muat ulang halaman | C-31 | HNK-22.T6 | Hans | AUDIT (2026-10-22: task selesai di kode dan merged; diaudit di E2E testnet HNK-17.T4) |
| BL-S00-03 | Tambah atau ganti peran | Pilihan peran setelah masuk dan navigasi per peran (menggantikan lima tab simulasi) | Pengguna dengan dua peran berpindah peran tanpa daftar ulang | P-01, HNK-21.T1 | HNK-22.T3 | Hans | SELESAI (2026-10-20, `7814fbc`, U-HNK-22.1, I-HNK-22.2: ganti peran dengan passkey yang sama, satu sentuhan, tanpa daftar ulang) |
| BL-S00-04 | Semua | E2E BF-01: daftar, masuk di perangkat kedua, tambah peran, tukar kontak, stempel, pairing konsol | Satu siklus lulus di HNK-17 | HNK-17 | HNK-17.T4 | Hans | TODO |
