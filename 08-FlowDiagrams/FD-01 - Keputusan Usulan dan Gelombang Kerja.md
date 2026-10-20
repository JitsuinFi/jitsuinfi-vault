---
tags: [flow, planning]
status: DISETUJUI
updated: 2026-10-20
---

# FD-01 - Keputusan Usulan dan Gelombang Kerja

**Bagian dari:** [[08 - FlowDiagrams]] · Usulan: [[FD-00 - Arsitektur Target dan Legenda]] · Backlog: [[Backlog]] · Porsi kerja: [[Decision Log]] D-26, D-29

Tabel ini mengubah usulan P-01 – P-14 dan temuan kode FD-00 §6 menjadi rencana kerja sampai submit 28 Okt. Tujuannya semuanya selesai; gelombang hanya menentukan urutan, karena gelombang berikutnya bergantung pada fondasi gelombang sebelumnya. **Keputusan Hans 2026-10-20: setuju semua sesuai rekomendasi (D-30, D-31).** Baris yang disetujui sudah menjadi item HNK-22 – HNK-29 di [[Backlog]]; porsi final ada di bagian Revisi 2026-10-20 di sana.

Estimasi adalah jam kasar untuk satu orang, termasuk unit test dan pembaruan dokumen. Kandidat pemilik mengikuti D-29 dan dihitung di bagian akhir supaya total tetap 40/30/30. Task Dave tetap atas nama Dave dengan catatan "backup sementara: Hans".

## Gelombang 1 - Fondasi: akun, key, surat, perbaikan kode (21–23 Okt)

Tidak butuh server baru. Semua bisa diuji di web app dan testnet seperti sekarang.

| ID | Isi singkat | Estimasi | Kandidat | Tergantung | Diagram | Keputusan Hans |
|---|---|---|---|---|---|---|
| P-01 | Satu passkey per orang (`excludeCredentials`, nama netral peran), daftar dan masuk untuk supplier, buyer, anggota dana, sidik jari key publik, navigasi per peran | 4 | Dave | — | SEQ-00, DFD-2.1 1.1–1.3, PG-01 Akun || Setuju (2026-10-20, D-30) |
| P-02 | Salt per peran dan salt inbox; financier tanpa salt di browser | 1 | Dave | P-01 | SEQ-00, DFD-2.1 1.2 || Setuju (2026-10-20, D-30) |
| P-03 | Key per invoice supplier dari master (BLAKE2b berpersonalisasi, input unik per invoice), ganti backup JSON plaintext | 3 | Hans | P-01 | SEQ-01 bagian 1, DFD-2.2 2.2 || Setuju (2026-10-20, D-30) |
| P-07 | Stempel: PRF baru per tanda tangan, key sebagai `Uint8Array` lalu dinolkan, kunci 15 menit | 3 | Dave | P-01 | SEQ-00 Sesi, DFD-2.1 1.5 || Setuju (2026-10-20, D-30) |
| P-08 | Salt komitmen dari library, disimpan per (invoice, financier), dipakai ulang saat retry | 1 | Hans | — | SEQ-03 1b, DFD-2.3 3.2 || Setuju (2026-10-20, D-30) |
| P-13 | wasm `assignmentDecode` + tampilan isi surat dan cek PDF surat di layar supplier dan buyer | 2 | Hans | — | SEQ-01 bagian 5, SEQ-02 bagian 4, DFD-2.4 4.2–4.3 || Setuju (2026-10-20, D-30) |
| K-1 | Kelas diskon/tenor: `classes_for` di 3.2, parameter kelas di API entri wasm, cek di `check_entry` (indeks tidak lagi kosong) | 3 | Hans | — | DFD-2.3 3.2, DFD-2.8 8.6 || Setuju (2026-10-20, D-30) |
| K-2 | QR pelunasan hanya untuk surat `Sealed`, alamat bayar ditampilkan | 1 | Dave | P-13 | SEQ-02 bagian 5, DFD-2.5 5.1 || Setuju (2026-10-20, D-30) |
| K-3 | `doubleSignProof` di wasm menerima posisi papan (lolos `jitsuin verify`) | 1 | Hans | — | DFD-2.7 7.3 || Setuju (2026-10-20, D-30) |
| K-4 | `register()`: terima `BoardChecked` di `Register` dan cari entri yang sudah terkirim sebelum posting ulang | 3 | Hans | — | SEQ-03 bagian 4–5, DFD-2.3 3.8 || Setuju (2026-10-20, D-30) |
| K-5 | Penjadwal pelunasan mengingat txid `settled` yang sudah dikirim | 1 | Dex | — | SEQ-03 bagian 8, DFD-2.5 5.5 || Setuju (2026-10-20, D-30) |
| K-6 | Bandingkan advance yang diterima dengan advance yang disepakati | 1 | Hans | — | SEQ-01 bagian 6, DFD-2.4 4.8 || Setuju (2026-10-20, D-30) |
| K-7 | `Done` baru setelah advance terkonfirmasi; hitung ulang konfirmasi untuk entri yang ditambang ulang | 2 | Hans | — | SEQ-03 bagian 5 dan 7, DFD-2.4 4.5 || Setuju (2026-10-20, D-30) |
| P-12 | Keputusan D-xx: node memegang spending key dan memposting `settled` otomatis, atau penandatangan dan pemosting dipisah | 0 | Hans (keputusan) | — | SEQ-03 bagian 8 || Setuju: opsi (a), D-31 |

## Gelombang 2 - Antarpihak: relay, node, konsol (23–26 Okt)

Mengganti salin-tempel. Butuh `jitsuinfi-backend` (D-17) dan API node.

| ID | Isi singkat | Estimasi | Kandidat | Tergantung | Diagram | Keputusan Hans |
|---|---|---|---|---|---|---|
| P-04 | Relay kotak surat end-to-end: `mailbox_id` turunan, baca dengan bukti kepemilikan, pesan financier ditandatangani node, kartu kontak (D19), PDF ikut terenkripsi | 10 | Dex | P-01, P-02 | SEQ-00 Daftar/Masuk, DFD-2.1 1.4, semua lane D7 || Setuju (2026-10-20, D-30) |
| P-11 | Rewrite Vercel `/api/*` ke relay; konsol financier di origin node; CSP tetap `connect-src 'self'` | 2 | Dave | P-04 | FD-00 P-11, PG-01 || Setuju (2026-10-20, D-30) |
| P-05 | Pairing passkey konsol, sesi konsol (challenge, origin, `rpIdHash`, UV, cookie `__Host-`), key kotak surat financier di node; di atas API HNK-05.T3 (3 jam, sudah di backlog) | 5 | Dex | P-04, HNK-05.T3 | SEQ-00 Pairing/Konsol, SEQ-03, DFD-2.1 1.6–1.7 || Setuju (2026-10-20, D-30) |
| P-06 | Endpoint snapshot papan same-origin untuk Verify, status pelunasan, riwayat sendiri | 3 | Dex | P-11 | SEQ-04 bagian D, DFD-2.8 8.7 || Setuju (2026-10-20, D-30) |
| HNK-21 | Polish halaman internal mengikuti PG-01 (sudah di backlog, 14 jam; pindah ke Dex menurut D-29) | (14) | Dex | P-01, P-04 | PG-01 || Setuju (2026-10-20, D-30) |

## Gelombang 3 - Lengkapi (26–27 Okt)

| ID | Isi singkat | Estimasi | Kandidat | Tergantung | Diagram | Keputusan Hans |
|---|---|---|---|---|---|---|
| P-09 | Nomor invoice `k` otomatis dari rantai yang tertambat, kepala rantai bertanda tangan | 3 | Dave | P-04, P-06 | SEQ-02 Masuk, DFD-2.6 || Setuju (2026-10-20, D-30) |
| K-8 | wasm `verifyProofOnBoard(proof, snapshot)` dipakai layar Verify | 2 | Hans | P-06, K-3 | SEQ-04 bagian D, DFD-2.7 7.4 || Setuju (2026-10-20, D-30) |
| K-9 | wasm `rateIndex(snapshot, k)` untuk halaman indeks HNK-08.T3 (halamannya sudah di backlog) | 1 | Dave | P-06, K-1 | SEQ-04 bagian C, DFD-2.8 8.6 || Setuju (2026-10-20, D-30) |
| K-10 | Varian wasm entri bertag yang hanya menerima `history_tag` (sertifikat k tetap di financier) | 1 | Hans | — | SEQ-02 bagian 3, DFD-2.3 3.6 || Setuju (2026-10-20, D-30) |
| K-11 | Alamat diversified baru per deal dari wallet node; minta alamat baru dari supplier | 2 | Dave | P-05 | SEQ-03 1b, DFD-2.4 4.1 || Setuju (2026-10-20, D-30) |
| P-10 | Halaman anggota membaca hasil pindaian lokal (HNK-15.T3, sudah di backlog atas nama Dave) | (4) | Dave | — | SEQ-05, DFD-2.9 9.8 || Setuju (2026-10-20, D-30) |

## Roadmap atau keputusan saja (tidak dibangun sebelum submit, kecuali Hans memutuskan lain)

| ID | Alasan | Keputusan Hans |
|---|---|---|
| P-14 | Tidak aman seperti tertulis: JTSP membuktikan dua tanda tangan, bukan niat menipu. Butuh perubahan format entri (penawaran eksklusif yang kedaluwarsa) dan verifikasi baru. Bukti `DoubleFinanced` sudah bisa tanpa P-14 (`proof_from_lookup`) || Tunda (2026-10-20) |
| Pemulihan passkey | Perlu keputusan desain (backup master terenkripsi atau rotasi identitas lewat KYC); cukup dicatat sebagai risiko di submission || Tunda (2026-10-20) |
| Kotak surat per deal, padding/batching relay | Mengurangi keterhubungan dan metadata relay; tambahan setelah relay dasar berjalan || Tunda (2026-10-20) |
| Jeda acak sebelum `Pay` | Menunggu keputusan TM #12 / #15 di [[Pra-review Spesifikasi dan Threat Model]] || Tunda (2026-10-20) |
| Verifikasi advance lewat CLI lokal supplier | Fungsi ada; perintah CLI baru bisa menyusul setelah K-6 || Tunda (2026-10-20) |

## Porsi kerja setelah rencana ini

Dasar D-29: total 176 jam, Hans 91 (termasuk HNK-21 14 jam dan HNK-05.T4 2 jam yang dipindah ke Dex), Dex 37, Dave 48. Setelah pemindahan D-29: Hans 75, Dex 53, Dave 48.

| Orang | Sebelum | Kerja baru (FD-01) | Total | Porsi | Target |
|---|---|---|---|---|---|
| Hans | 75 | 19 (P-03, P-08, P-13, K-1, K-3, K-4, K-6, K-7, K-8, K-10) | 94 | 40,7% | 40% |
| Dex | 53 | 19 (P-04, P-05, P-06, K-5) | 72 | 31,2% | 30% |
| Dave | 48 | 17 (P-01, P-02, P-07, P-09, P-11, K-2, K-9, K-11) | 65 | 28,1% | 30% |
| **Total** | 176 | 55 | 231 | || Setuju (2026-10-20, D-30) |

Selisih Dave −1,9% dan Hans +0,7% bisa ditutup dengan memindahkan K-6 dan K-10 (2 jam) ke Dave: Hans 92 (39,8%), Dex 72 (31,2%), Dave 67 (29,0%). Angka dihitung ulang saat item dibuat di [[Backlog]]. Celah tambahan dari penelusuran business flow dan porsi gabungannya ada di [[FD-02 - Penelusuran Business Flow ke Backlog]].
