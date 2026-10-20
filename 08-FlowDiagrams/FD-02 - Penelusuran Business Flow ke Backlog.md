---
tags: [flow, planning]
status: DITETAPKAN
updated: 2026-10-20
---

# FD-02 - Penelusuran Business Flow ke Backlog

**Bagian dari:** [[08 - FlowDiagrams]] · Keputusan dan gelombang: [[FD-01 - Keputusan Usulan dan Gelombang Kerja]] · Usulan: [[FD-00 - Arsitektur Target dan Legenda]] · Backlog: [[Backlog]]

FD-01 menyusun rencana per usulan (P-xx) dan per temuan kode (K-x). Dokumen ini menelusuri arah sebaliknya: setiap **business flow** end to end, langkah demi langkah dari sequence dan DFD, lalu menandai apa yang kurang di tiap lapisan (core/wasm, node, relay, layar, uji). Hasilnya:

- langkah yang sudah tertutup task lama di [[Backlog]] (ditulis `HNK-xx.Tn`);
- langkah yang tertutup baris FD-01 (ditulis `P-xx` atau `K-x`);
- **celah baru** yang belum ada di mana pun (ditulis `C-xx`, daftar lengkap di bagian akhir).

Bagian terakhir mengelompokkan semuanya menjadi calon item HNK-22 – HNK-29. Rincian task per diagram (ID `BL-…`, dengan kriteria selesai) ada di file `-backlogs` di samping tiap diagram, misalnya [[DFD-2.1 - Identitas dan Sesi-backlogs]]. Calon item baru masuk [[Backlog]] setelah keputusan FD-01 diisi.

Lapisan yang dipakai di kolom "Kurang": **W** = wasm/core, **N** = node financier (`jitsuin-flow` + API), **R** = relay, **L** = layar web, **U** = uji.

## BF-01 Onboarding, identitas, dan kontak

Sumber: [[SEQ-00 - Autentikasi dan Onboarding]], [[DFD-2.1 - Identitas dan Sesi]], [[PG-01 - Peta Halaman per Peran]] (Akun).

| Langkah | Peran | Sekarang | Kurang | Task |
|---|---|---|---|---|
| Daftar satu passkey per orang, pilih peran pertama | Supplier, buyer, anggota | Buyer saja, `create()` bisa berulang | L | P-01 |
| Masuk, salt per peran, sidik jari key | Semua peran web | Buyer saja | L | P-01, P-02 |
| Tambah atau ganti peran | Semua peran web | Belum ada | L | P-01 |
| Beranda per peran (navigasi, peran aktif) | Semua | Lima tab simulasi | L | HNK-21.T1 (ubah isi: navigasi per peran, bukan tab) |
| Buat kotak surat, daftarkan `mailbox_pk` | Semua | Belum ada | W, R, L | P-04 |
| Tukar kartu kontak (QR/tempel), simpan kontak rekan, verifikasi sidik jari di luar sistem | Semua | Belum ada | L | **C-01** |
| Daftarkan `identity_pk` buyer setelah KYC di sisi financier | Financier | Belum ada (di luar protokol) | N, L | **C-02** |
| Kunci sesi 15 menit, stempel per tanda tangan | Supplier, buyer | Master hex di memori modul | L | P-07 |
| Passkey hilang | Semua | Tidak ada jalur | — | Roadmap (FD-01); catat di submission |
| Uji PRF dengan authenticator nyata (key sama di dua perangkat tersinkron) | — | Belum tercatat | U | **C-03** |

## BF-02 Penerbitan invoice dan tanda tangan buyer

Sumber: [[SEQ-01 - Supplier]] bagian 1–2, [[SEQ-02 - Buyer]] bagian 1–2, [[DFD-2.2 - Penerbitan dan Tanda Tangan Invoice]].

| Langkah | Peran | Sekarang | Kurang | Task |
|---|---|---|---|---|
| Buyer membagikan `invoice_pk(k)` ke supplier | Buyer | Salin manual | R, L | P-04, P-09 |
| Key per invoice dari master supplier | Supplier | Acak + unduh JSON | W, L | P-03 |
| Isi invoice, hash file syarat, kanonik, N | Supplier | ADA | L (lembar kertas) | HNK-21.T2 |
| Kirim invoice + PDF syarat ke buyer | Supplier | Salin manual, PDF di luar sistem | R, L | P-04; **C-04** (batas ukuran PDF dan format pesan) |
| Buyer membuka invoice, cek hash PDF, cek `buyer_pk` di layar | Buyer | Decode ADA, cek di layar belum | L | **C-05** (sebelumnya hanya disebut di FD-00 §6 sebagai HNK-21) |
| Tanda tangan buyer, kirim balik | Buyer | ADA (salin) | R, L | P-04, HNK-21.T3 |
| Supplier memeriksa tanda tangan buyer | Supplier | Fungsi ADA, kartu belum | L | **C-06** |
| Simpan dokumen deal di perangkat lintas sesi | Supplier, buyer | Hanya memori tab | W, L | **C-07** |

## BF-03 Penawaran ke financier

Sumber: [[SEQ-01 - Supplier]] bagian 3, [[SEQ-03 - Financier]] bagian 1–1b, [[DFD-2.3 - Registrasi Papan]] 3.1–3.2.

| Langkah | Peran | Sekarang | Kurang | Task |
|---|---|---|---|---|
| Supplier memilih financier dari kontak, menentukan advance, alamat baru per deal | Supplier | Belum ada | L | **C-08**, K-11 |
| Financier menerima penawaran, cek tanda tangan buyer, menetapkan advance dan konfirmasi | Financier | Belum ada | N, L | P-05, **C-09** |
| Financier menolak penawaran atau tidak menjawab (pesan tolak, kedaluwarsa penawaran) | Financier, supplier | Belum ada jalur | N, R, L | **C-10** |
| Salt dan komitmen, kelas dari `classes_for` | Financier (node) | Salt diisi pemanggil, kelas 0/0 | W, N | P-08, K-1 |
| Surat JTSA + PDF surat dibuat sebelum `Flow::new` | Financier | Kartu ada, teks urutan salah | L | HNK-21.T4 (perbaiki teks) |
| Alamat bayar diversified dari wallet node | Financier (node) | Diketik operator | N | K-11 |

## BF-04 Pemeriksaan riwayat buyer

Sumber: [[SEQ-02 - Buyer]] bagian 3, [[SEQ-03 - Financier]] bagian 2, [[DFD-2.6 - Riwayat Buyer]].

| Langkah | Peran | Sekarang | Kurang | Task |
|---|---|---|---|---|
| Financier mengirim permintaan bertanda tangan | Financier (node) | Belum ada | N, R | P-04 |
| Buyer melihat permintaan, menyetujui, menerbitkan sertifikat k | Buyer | Kartu ADA, `k` diketik | L | P-09, HNK-21.T3 |
| Rantai ke financier, sertifikat k (atau hanya tag) ke supplier | Buyer | Belum ada | W, R | P-04, K-10 |
| Financier menjalankan `check_buyer` dengan `MinimumStandard` di node | Financier (node) | Flow ADA; layar hanya `verifyHistory` tanpa standar | N, L | **C-11** |
| Kelola allowlist, standar minimal, tenggang | Financier | Struktur ADA | N, L | **C-12** |
| Tolak dengan alasan yang terbaca (`NotAnchored`, `Equivocation`, `FinancierNotAllowed`, `UndisclosedSuccessor`, di bawah standar) | Financier | Error mentah | L | **C-13** |
| Buyer memeriksa riwayatnya sendiri | Buyer | wasm ADA, kartu belum | L | **C-14** (butuh P-06) |

## BF-05 Registrasi di papan

Sumber: [[SEQ-01 - Supplier]] bagian 4, [[SEQ-03 - Financier]] bagian 3–5, [[DFD-2.3 - Registrasi Papan]] 3.3–3.9.

| Langkah | Peran | Sekarang | Kurang | Task |
|---|---|---|---|---|
| `Flow::new`, cek papan, `lookup` | Financier (node) | ADA lewat CLI scratchpad | N (API) | HNK-05.T3 |
| Permintaan entri ke supplier (dengan `history_tag`) | Financier (node) | Belum ada | N, R | P-04, P-05 |
| Supplier menandatangani entri (0x01 / 0x03) dengan kelas | Supplier | wasm ADA (0/0), kartu belum | W, L | K-1, **C-15** |
| `check_entry`, tolak `EntryMismatch` ke layar | Financier (node) | ADA | L | **C-13** |
| Posting entri, pemulihan crash, cek papan ulang | Financier (node) | ADA tanpa pemulihan | N | K-4 |
| Tunggu konfirmasi, tampilkan progres | Financier | ADA di flow, layar belum | L | HNK-05.T4 |
| State deal bertahan saat node restart | Financier (node) | Hanya memori | N | **C-16** |

## BF-06 Pengalihan dan seal

Sumber: [[SEQ-01 - Supplier]] bagian 5, [[SEQ-02 - Buyer]] bagian 4, [[SEQ-03 - Financier]] bagian 6, [[DFD-2.4 - Pengalihan dan Advance]] 4.1–4.4.

| Langkah | Peran | Sekarang | Kurang | Task |
|---|---|---|---|---|
| Surat + PDF surat sampai ke supplier dan buyer | Financier | Salin manual | R | P-04 |
| Supplier dan buyer membaca isi surat, cek PDF surat, menyegel | Supplier, buyer | Seal ADA, isi tidak terbaca | W, L | P-13, HNK-21.T2/T3 |
| Seal s0, s1 sampai ke node; `AssignmentSealed` | Financier (node) | ADA di flow | N, R | P-04, P-05 |
| Seal salah: alasan terbaca, state tetap | Financier | Error mentah | L | **C-13** |

## BF-07 Advance Sign-to-Pay

Sumber: [[SEQ-03 - Financier]] bagian 7, [[SEQ-01 - Supplier]] bagian 6, [[DFD-2.4 - Pengalihan dan Advance]] 4.5–4.8.

| Langkah | Peran | Sekarang | Kurang | Task |
|---|---|---|---|---|
| Operator menyetujui pembayaran per deal (assertion passkey) | Financier | Belum ada | N, L | P-07 (financier), P-05 |
| Cek terakhir, idempotensi, kirim advance | Financier (node) | ADA (diuji testnet) | N | K-7 (`Done` setelah terkonfirmasi) |
| s2 diteruskan ke buyer, txid ke supplier | Financier (node) | Belum ada | N, R | P-04 |
| Supplier melihat status advance; cek nominal = advance yang disepakati | Supplier | Belum ada | W, L | K-6, **C-17** |
| Verifikasi kuat dari wallet supplier sendiri (CLI lokal) | Supplier | Fungsi ADA, tanpa perintah | W (CLI) | Roadmap (FD-01) |

## BF-08 Pelunasan dan settled

Sumber: [[SEQ-02 - Buyer]] bagian 5, [[SEQ-03 - Financier]] bagian 8, [[DFD-2.5 - Pelunasan dan Settled]].

| Langkah | Peran | Sekarang | Kurang | Task |
|---|---|---|---|---|
| Pengingat jatuh tempo (lokal atau pesan dari node) | Buyer | Belum ada | L | **C-18** |
| QR hanya untuk surat `Sealed`, alamat ditampilkan | Buyer | QR dari surat apa pun | W, L | K-2 |
| Buyer membayar dari Zodl (uji SPK-04) atau `zcash-devtool` | Buyer | Belum diuji | U | SPK-04, **C-19** (dana testnet untuk peserta demo) |
| Penjadwal berkala: cocokkan, status, `settled` | Financier (node) | Fungsi ADA, tanpa penjadwal | N | **C-20**, K-5, P-12 |
| Tampilan status pelunasan per deal | Financier, buyer, supplier | Belum ada | L | **C-21** (butuh P-06 untuk buyer/supplier) |

## BF-09 Telat bayar, sengketa, gagal bayar

Sumber: [[SEQ-02 - Buyer]] jalur sengketa, [[DFD-2.5 - Pelunasan dan Settled]] 5.3.

| Langkah | Peran | Sekarang | Kurang | Task |
|---|---|---|---|---|
| Status `Claimed` / `Disputed` / `Overdue` / `Partial` terlihat dengan bukti (klaim buyer + txid) | Financier | `Repayment::status` ADA | N, L | **C-22** |
| Ekspor bukti sengketa untuk pihak berwenang | Financier | Belum ada | W, L | **C-22** |
| Settled terlambat tercatat sebagai `late` di riwayat buyer | Sistem | ADA (flag) | U | HNK-17 (E2E) |

## BF-10 Deteksi pembiayaan ganda

Sumber: [[SEQ-03 - Financier]] bagian 3 dan jalur B, [[SEQ-01 - Supplier]] jalur nakal, [[DFD-2.7 - Deteksi Pembiayaan Ganda]].

| Langkah | Peran | Sekarang | Kurang | Task |
|---|---|---|---|---|
| `Stopped(AlreadyFinanced)` terlihat dan menghentikan deal | Financier | ADA di flow | L | HNK-05.T4 |
| `Stopped(DoubleFinanced)` membuat bukti lengkap (`proof_from_lookup`) | Financier (node) | Fungsi tanpa pemanggil | N | **C-23** |
| Kartu "Bukti ganda" dan unduh untuk pihak berwenang | Financier | Belum ada | L | **C-23** |
| Bukti dari wasm dengan posisi papan | — | Tanpa posisi | W | K-3 |
| Verify di web mencocokkan posisi dengan snapshot | Verifier | Posisi hanya diklaim | W, L | K-8 |

## BF-11 Verifikasi publik dan orang luar

Sumber: [[SEQ-04 - Verifier dan Orang Luar]], [[DFD-2.8 - Verifikasi dan Indeks Publik]].

| Langkah | Peran | Sekarang | Kurang | Task |
|---|---|---|---|---|
| `jitsuin verify` dan `jitsuin index` untuk juri | Verifier | ADA (review) | U | HNK-09.T1–T3 |
| Snapshot papan otomatis di Verify | Verifier | Diunggah sebagai file | R, L | P-06 |
| Verdict bundel menyebut surat dan settled dengan benar ("every seal checks out" muncul juga saat surat belum lengkap) | Verifier | Teks menyesatkan | L | **C-24** |
| Halaman orang luar menyebut yang terlihat pemegang UFVK papan (jenis entri, kelas, flag tepat waktu), bukan "hanya hash dan tanda tangan" | Orang luar | Teks keliru (TM #14) | L | **C-25** |
| Halaman indeks bunga | Publik | Belum ada | W, L | HNK-08.T3, K-9 |
| Publikasi UFVK papan untuk juri | — | D-11 masih usulan | — | **C-26** (keputusan) |

## BF-12 Dana anggota (JitsuinFi Vault)

Sumber: [[SEQ-05 - Anggota Dana]], [[DFD-2.9 - Solvabilitas Dana]].

| Langkah | Peran | Sekarang | Kurang | Task |
|---|---|---|---|---|
| Setoran dicatat sebagai daun, kuitansi ke kotak surat anggota | Manajer | Belum ada | N, R | HNK-15.T1, **C-27** |
| Root per periode | Manajer | ADA | — | — |
| Jalur Merkle per periode ke anggota, verifikasi inklusi | Manajer, anggota | Belum ada | W, N, R | HNK-15.T1, **C-27** |
| Pemindaian lokal + perintah CLI solvabilitas | Anggota | Fungsi ADA, tanpa perintah | W (CLI) | **C-28** |
| Halaman laporan anggota | Anggota | Belum ada | L | HNK-15.T3 |

## Celah baru (belum ada di FD-01 maupun backlog)

| ID | Celah | Lapisan | Estimasi | Kandidat |
|---|---|---|---|---|
| C-01 | Tukar dan simpan kartu kontak (QR/tempel), verifikasi sidik jari di luar sistem, daftar kontak per peran | L | 2 | Hans |
| C-02 | Registri `identity_pk` buyer hasil KYC di node financier (input ke 6.4) | N, L | 1 | Dex |
| C-03 | Kasus uji PRF dengan authenticator nyata dan dua perangkat tersinkron (TEST-HNK-10) | U | 1 | Hans |
| C-04 | Skema pesan relay: jenis pesan (penawaran, invoice, tanda tangan, surat, seal, sertifikat, permintaan, txid, kuitansi), versi, batas ukuran PDF | R, W | 2 | Hans |
| C-05 | Layar buyer: input PDF syarat, cek hash, perbandingan `buyer_pk` = `invoice_pk(k)` | L | 1 | Hans |
| C-06 | Kartu supplier: cek tanda tangan buyer (`bundleBuild`) | L | 1 | Hans |
| C-07 | Penyimpanan dokumen deal lintas sesi di perangkat (IndexedDB terenkripsi dengan key dari PRF), karena relay hanya menyimpan pesan sementara | W, L | 3 | Hans |
| C-08 | Layar supplier "Tawarkan ke financier": pilih kontak, advance, alamat baru | L | 1 | Hans |
| C-09 | Konsol: daftar penawaran masuk, terima dengan syarat (advance, konfirmasi) | L, N | 2 | Dex |
| C-10 | Tolak atau kedaluwarsa penawaran (pesan ke supplier) | N, R, L | 1 | Dex |
| C-11 | API `check_buyer` di node dengan `MinimumStandard`, menyimpan `history_tag` di deal | N | 1 | Hans |
| C-12 | Pengaturan policy di konsol: allowlist, standar minimal, tenggang | L, N | 2 | Hans |
| C-13 | Pesan error yang terbaca untuk semua penolakan (riwayat, `EntryMismatch`, seal salah) di semua layar | L | 1 | Hans |
| C-14 | Kartu "Riwayat saya" di layar buyer (`verifyHistory` + snapshot) | L | 1 | Hans |
| C-15 | Kartu supplier "Tanda tangani entri papan" (0x01 / 0x03) | L | 1 | Hans |
| C-16 | Persistensi state deal di node (serialisasi `Flow` dan dokumen deal), lanjut setelah restart | N | 3 | Hans |
| C-17 | Status advance di layar supplier (txid, nominal, kecocokan dengan yang disepakati) | L | 1 | Hans |
| C-18 | Pengingat jatuh tempo lokal di layar buyer | L | 1 | Hans |
| C-19 | Dana testnet untuk peserta uji (HNK-13) dan panduan bayar QR | U | 1 | Hans |
| C-20 | Penjadwal pelunasan berkala di node (interval, tenggang dari konfigurasi) | N | 2 | Dex |
| C-21 | Status pelunasan per deal di konsol, layar buyer, dan supplier | L | 1 | Hans |
| C-22 | Tampilan dan ekspor sengketa (klaim buyer + txid) di konsol | L, W | 2 | Hans |
| C-23 | Pemanggil `proof_from_lookup` di node untuk `DoubleFinanced` + kartu "Bukti ganda" | N, L | 2 | Hans |
| C-24 | Teks verdict bundel di layar Verify sesuai status surat dan settled | L | 0,5 | Hans |
| C-25 | Teks dan tabel halaman orang luar sesuai TM #13–#14 | L | 0,5 | Hans |
| C-26 | Keputusan D-11: publikasi UFVK + birthday papan untuk juri | — | 0 | Hans (keputusan) |
| C-27 | Pencatatan setoran dan pengiriman kuitansi + jalur Merkle per periode lewat relay | N, R | 2 | Dex |
| C-28 | Perintah CLI solvabilitas untuk anggota (`member_view` + `solvency`) | W | 1 | Hans |
| C-29 | Financier mengirim bundel JTSB ke buyer dan supplier setelah settled (DFD-2.5 5.6) | N, R | 1 | Dex |
| C-30 | API `jitsuin-wasm` menerima key sebagai byte supaya bisa dinolkan (DFD-2.1 1.5) | W | 1 | Hans |
| C-31 | Kotak masuk per peran: ambil pesan setelah masuk dan berkala, tampilkan sebagai tindakan (SEQ-00, SEQ-02) | L | 1 | Hans |
| C-32 | Halaman "Daftar deal" supplier: timeline per N (PG-01 s1) | L | 2 | Hans |
| C-33 | Pipeline deal per state dan detail deal di konsol (PG-01 f1, f4) | L, N | 2 | Dex |

Total celah baru 45 jam: Hans 15, Dex 11, Dave 19. C-29 – C-33 ditemukan saat menyusun backlog per diagram (file `-backlogs`).

Porsi gabungan FD-01 + FD-02 (dasar D-29 setelah HNK-21 dan HNK-05.T4 pindah ke Dex: Hans 75, Dex 53, Dave 48):

| Orang | Sebelum | FD-01 | FD-02 | Total | Porsi |
|---|---|---|---|---|---|
| Hans | 75 | 19 | 15 | 109 | 39,5% |
| Dex | 53 | 19 | 11 | 83 | 30,1% |
| Hans | 48 | 17 | 19 | 84 | 30,4% |
| **Total** | 176 | 55 | 45 | 276 | |

Celah yang dekat dengan kode Hans (skema pesan, penyimpanan terenkripsi, `check_buyer`, persistensi `Flow`, sengketa, bukti ganda) diberikan ke Hans supaya porsinya tetap 40%.

## Calon item backlog

**Dibuat 2026-10-20 (D-30)** sebagai HNK-22 – HNK-29 di [[Backlog]]. Pembagian final berbeda sedikit dari kandidat di bawah supaya porsi tetap 40/30/30 (antara lain P-09 dan `rateIndex` ke Hans, alamat per deal di node ke Dex); owner final ada di kolom Owner tiap file `-backlogs`.

Pengelompokan per business flow. Task lama yang sudah ada tetap di itemnya; kolom "Isi" menyebut apa yang ditarik ke item baru.

| Calon | Judul | Isi | Pemilik utama |
|---|---|---|---|
| HNK-22 | Akun passkey, peran, dan kontak | P-01, P-02, P-07, C-01, C-03, C-31 | Hans |
| HNK-23 | Relay kotak surat end to end | P-04, P-11, C-04; menyerap HNK-10.T4 (skeleton backend) dan HNK-10.T5 (deploy Railway) | Dex (C-04 Hans, P-11 Dave) |
| HNK-24 | Alur deal di layar supplier | P-03, C-06, C-07, C-08, C-15, C-17, C-32, K-11 (sisi supplier) | Hans (dari Dave, D-35; P-03, C-07 Hans) |
| HNK-25 | Alur deal di layar buyer | C-05, C-14, C-18, K-2, P-09 | Hans |
| HNK-26 | Konsol dan API node financier | P-05, C-02, C-09, C-10, C-11, C-12, C-16, C-20, C-21, C-22, C-23, C-29, C-33, K-5, K-11 (sisi node); bergantung HNK-05.T3/T4 | Dex (C-11, C-16, C-22, C-23 Hans; C-12, C-21 Dave) |
| HNK-27 | Perbaikan protokol dan flow | P-08, P-13, K-1, K-3, K-4, K-6, K-7, K-10, C-28, C-30 | Hans |
| HNK-28 | Verifikasi publik lengkap | P-06, K-8, K-9, C-24, C-25, C-26; bersama HNK-08.T3 | Dex (layar Hans, D-35) |
| HNK-29 | Alur dana anggota | C-27; bersama HNK-15.T1 dan HNK-15.T3 | Dex |
| — | Pesan error terbaca (C-13) dan regresi E2E per business flow | Masuk HNK-21 (C-13) dan HNK-17 (E2E BF-01 – BF-12) | Hans |

HNK-21 tetap untuk polish visual. Isi T1–T6 menyesuaikan halaman per peran di PG-01 setelah HNK-22, HNK-24, HNK-25, dan HNK-26 ada.

Dependensi baru yang mungkin dibutuhkan (enkripsi sealed box X25519 + AEAD di browser dan di node, penyimpanan IndexedDB) harus ditanyakan ke Hans sebelum dipasang.
