---
tags: [flow, backlog]
status: DITETAPKAN
progress: 0/19 SELESAI
updated: 2026-10-20
---

# DFD-2.1 - Identitas dan Sesi-backlogs

**Diagram:** [[DFD-2.1 - Identitas dan Sesi]] · Rencana: [[FD-01 - Keputusan Usulan dan Gelombang Kerja]] · [[FD-02 - Penelusuran Business Flow ke Backlog]] · Backlog: [[Backlog]]

Task yang dibutuhkan supaya proses 1.1 – 1.7 berjalan seperti digambar. Kolom Ref menunjuk baris FD-01 (`P-xx`, `K-x`), celah FD-02 (`C-xx`), atau task lama (`HNK-xx.Tn`); estimasi jam ada di baris yang dirujuk. Task baru yang ditemukan saat penelusuran file ini ditandai **baru** dan ditambahkan ke FD-02. Kolom Task backlog menunjuk task di [[Backlog]] (dibuat 2026-10-20, D-30).

Kolom Status mengikuti langkah 6 "Audit flow diagram" di [[Workflow Development]]: `TODO` → `DIKERJAKAN` → `AUDIT` (semua task backlog-nya DONE) → `SELESAI (tanggal, bukti)` atau `GAGAL AUDIT (tanggal, alasan)`; `DITUNDA` hanya dengan keputusan user. Antrean audit tampil di setiap `python3 scripts/sync-vault.py` (lewat `scripts/check-backlogs.py`). Backlog ini ditetapkan 2026-10-20 (D-32).

## Task

| ID | Elemen | Task | Selesai bila | Ref | Task backlog | Owner | Status |
|---|---|---|---|---|---|---|---|
| BL-D21-01 | 1.1, F1.01 – F1.05 | Satu `create()` per orang: `user.name` netral peran, `excludeCredentials` dari profil, `residentKey` dan UV required, ekstensi PRF (boleh `prf.eval` langsung) | Klik Daftar dua kali tidak membuat credential kedua; satu passkey dipakai untuk supplier, buyer, dan anggota | P-01 | HNK-22.T1 | Dave | TODO |
| BL-D21-02 | 1.1, F1.05 | Authenticator tanpa PRF ditolak dengan pesan dan petunjuk menghapus credential yatim | Di authenticator tanpa PRF muncul pesan, tidak ada key yang diturunkan | P-01 | HNK-22.T1 | Dave | TODO |
| BL-D21-03 | D8, F1.06, F1.10 | Profil lokal non-rahasia (credential id, peran, label) dengan `try/catch`; dipakai sebagai `allowCredentials` | Dengan localStorage kosong atau diblokir, daftar dan masuk tetap jalan | P-01 | HNK-22.T1 | Dave | TODO |
| BL-D21-04 | 1.2, F1.11 – F1.13 | `get()` dengan `prf.eval.first` = SHA-256 salt peran dan `second` = SHA-256 salt inbox; peran supplier, buyer, anggota | Output PRF first dan second berbeda per peran; buyer tetap memakai salt lama (key buyer lama tidak berubah) | P-02 | HNK-22.T2 | Dave | TODO |
| BL-D21-05 | 1.3, F1.14 – F1.15 | Turunkan key peran dan tampilkan sidik jari key publik setelah masuk | Sidik jari sama di dua perangkat dengan passkey tersinkron yang sama, berbeda untuk passkey lain | P-01 | HNK-22.T2 | Dave | TODO |
| BL-D21-06 | 1.3 (anggota) | Peran anggota dana: tanpa key tanda tangan, hanya key kotak surat | Layar anggota tidak pernah meminta stempel | P-01 | HNK-22.T2 | Dave | TODO |
| BL-D21-07 | 1.4, F1.15 – F1.16 | Key kotak surat X25519 dari PRF second dan `mailbox_id` = BLAKE2b(`mailbox_pk`) di `jitsuin-wasm` | Test vector: PRF tetap menghasilkan `mailbox_pk` dan `mailbox_id` tetap; dependensi kripto disetujui Hans dulu | P-04 | HNK-23.T2 | Dex | TODO |
| BL-D21-08 | 1.4, F1.18 – F1.19 | Endpoint relay `POST /api/mailbox` (daftar `mailbox_pk` + bukti kepemilikan) | Id yang disimpan relay sama dengan hitungan klien; pendaftaran tanpa bukti ditolak | P-04 | HNK-23.T4 | Dex | TODO |
| BL-D21-09 | 1.4 (baca) | Baca kotak surat dengan challenge yang dienkripsi ke `mailbox_pk` | Pihak lain yang tahu `mailbox_id` tidak bisa membaca daftar pesan | P-04 | HNK-23.T4 | Dex | TODO |
| BL-D21-10 | 1.4, F1.17 | Key kotak surat financier dibuat dan disimpan di node; node mendaftarkan kotak suratnya ke relay | Konsol membaca pesan financier lewat `/node/mail/*` tanpa key di browser | P-05, P-11 | HNK-26.T4 | Dex | TODO |
| BL-D21-11 | 1.4, F1.20 – F1.27, D19 | Kartu kontak (QR dan teks): buat, tampilkan, impor kontak rekan ke D19, cocokkan sidik jari di luar sistem; kartu buyer tanpa `identity_pk` | Supplier dan buyer bisa saling menambah kontak; kontak tampil dengan peran dan sidik jari | C-01 | HNK-22.T5 | Dave | TODO |
| BL-D21-12 | 1.5, F1.28 – F1.32 | Stempel: setiap tanda tangan meminta PRF baru, key diturunkan sebagai `Uint8Array` dan dinolkan; di sesi hanya key kotak surat dan key publik; kunci setelah 15 menit idle atau tab ditutup | Tidak ada master atau key tanda tangan yang tersisa di memori setelah stempel (dicek di devtools) | P-07 | HNK-22.T4 | Dave | TODO |
| BL-D21-13 | 1.5 | **Baru.** API `jitsuin-wasm` menerima key sebagai byte (`Uint8Array`), bukan string hex, supaya bisa dinolkan | Fungsi tanda tangan wasm punya varian byte; varian hex lama tetap untuk mode demo | C-30 | HNK-27.T9 | Hans | TODO |
| BL-D21-14 | 1.6, F1.33, F1.38 | Skrip setup node: `zcash-devtool init` (seed di node), key financier, key kotak surat, `init-fvk` UFVK papan | Satu perintah menyiapkan node testnet dari nol; tidak ada seed atau key di log | P-05 | HNK-26.T1 | Dex | TODO |
| BL-D21-15 | 1.6, F1.34 – F1.37, D9 | Pairing: kode sekali pakai + challenge, `create()` untuk `rp.id` domain node, verifikasi attestation, simpan credential di D9 | Kode yang sudah dipakai atau kedaluwarsa ditolak; credential tersimpan | P-05 | HNK-26.T2 | Dex | TODO |
| BL-D21-16 | 1.6 (layar) | Halaman pairing di konsol node | Operator bisa memasangkan passkey dari browser di origin node | P-05 | HNK-26.T2 | Dex | TODO |
| BL-D21-17 | 1.7, F1.39 – F1.43 | Sesi konsol: challenge sekali pakai dengan kedaluwarsa, cek origin, `rpIdHash`, flag UV, signature; cookie `Secure`, `__Host-`, `HttpOnly`, `SameSite=Strict` | Assertion ulang (replay) ditolak; cookie tanpa flag itu tidak pernah dikirim | P-05, P-11 | HNK-26.T3 | Dex | TODO |
| BL-D21-18 | 1.1, 1.2 (`rp.id`) | Isi `rp.id` eksplisit setelah domain final dipilih | Passkey di jitsuinfi.vercel.app tidak bentrok dengan preview atau localhost | SEQ-00 catatan | HNK-22.T1 | Dave | TODO |
| BL-D21-19 | Uji | Kasus uji PRF dengan authenticator nyata dan dua perangkat tersinkron; uji stateless (localStorage dikosongkan, key sama) | Dua kasus tercatat PASS di TEST-HNK-10 | C-03 | HNK-22.T7 | Dave | TODO |

## Sudah ada (tanpa task baru)

- `masterFromPasskey` dan `createPasskey` untuk buyer (`src/lib/passkey.ts`); disesuaikan oleh BL-D21-01 dan BL-D21-04.
- `buyerKeys` di `jitsuin-wasm` (1.3 untuk buyer).

## Keputusan yang dibutuhkan

- Dependensi kripto untuk X25519 + AEAD (wasm dan node) dan verifikasi WebAuthn di node (BL-D21-07, BL-D21-15, BL-D21-17).
- Pemulihan passkey yang hilang (roadmap, FD-01).
