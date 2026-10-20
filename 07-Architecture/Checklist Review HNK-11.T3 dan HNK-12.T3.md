---
tags: [architecture, review, checklist]
---

# Checklist Review HNK-11.T3 dan HNK-12.T3

**Bagian dari:** [[Backlog]] · Bahan: [[Pra-review Spesifikasi dan Threat Model]] · Dokumen yang direview: [[Threat Model]] dan `jitsuinfi-zcash/docs/zip-shielded-receivable-registry.md` · Terkait: [[Decision Log]] · [[Format Data]]

> Disiapkan 2026-10-20 oleh agent. **Review-nya tetap oleh Hans sendiri (DEV-11).** Checklist ini hanya mengurutkan pekerjaan dan menandai temuan pra-review (2026-10-19) yang berubah karena kode sesudahnya. Nomor baris di pra-review bisa sudah bergeser: cari nama fungsinya.

## Cara pakai

1. Baca bagian **A** (yang berubah sejak pra-review) supaya tidak memutuskan hal yang sudah selesai.
2. Putuskan lima keputusan di bagian **B** dulu; banyak temuan lain mengikutinya.
3. Kerjakan tabel **C** (threat model) dan **D** (spesifikasi): buka kode, cocokkan klaim, lalu isi kolom **Keputusan** di [[Pra-review Spesifikasi dan Threat Model]] dengan `terima`, `tolak`, atau `tunda`, plus satu kalimat alasan.
4. Tutup dengan bagian **E**: perbarui dokumen, catat bukti, dan buat task untuk temuan yang butuh kode.

Format isi kolom Keputusan: `terima: <perubahan teks atau task>` · `tolak: <alasan>` · `tunda: <sampai kapan / task>`.

## A. Berubah sejak pra-review (2026-10-19)

- [ ] **UFVK papan sekarang publik** (D-11, PR #10 `c73009b`, `examples/testnet/board-ufvk.txt`). Di threat model, "pemegang viewing key papan" sekarang berarti **siapa pun**. Naikkan tingkat temuan yang bergantung padanya: TM #1 (operator lightwalletd membuka entri dari IP), TM #3 (korelasi register dan settled), TM #5 dan #13 (bucket, jenis entri, txid terbaca), TM #14 (tabel halaman orang luar).
- [ ] **Salt komitmen sudah diturunkan dari key financier dan N** (HNK-27.T1, `748d451`, `commitment_salt` di `jitsuin-core/src/entry.rs`). Keputusan B2, TM #7, Spec #12 (bagian salt), dan Spec #17 kemungkinan sudah terjawab. Cek: salt tidak lagi dari pemanggil di alur financier (`Financier::commitment_opening`), lalu putuskan apakah parameter `salt` di `supplier::sign_register_entry` dan wasm tetap wajar (supplier menerima opening dari financier).
- [ ] **Indeks publik dengan ambang k = 5 sudah ada** (HNK-08, `jitsuin index`, `rate_index`). TM #5 sekarang setengah benar: agregat memakai k, tetapi bucket tiap entri tetap terbaca semua orang (UFVK publik).
- [ ] **Arti bucket sudah didefinisikan di kode** (`classes_for`, HNK-27.T2). Spec #12 tinggal menyalin tabel kelas ke spesifikasi (README sudah punya tabelnya).
- [ ] **Posisi bukti JTSP sekarang dicek terhadap papan** (`ProofOnBoard`, HNK-28.T2). Spec #15: verifikasi posisi sudah ada di CLI dan layar Verify; layout JTSP tetap belum dispesifikasikan.
- [ ] **Permukaan baru yang belum ada di pra-review:**
  - [ ] Akun passkey: profil (username, email) disimpan lokal (D-34); PRF per peran (HNK-22).
  - [ ] Skema pesan relay `JTSM` (HNK-23.T1): apa yang terlihat relay (penerima `to`, ukuran, waktu) masuk threat model?
  - [ ] Snapshot deal `JTSF` (HNK-26.T10): disimpan node, memuat invoice dan surat; perlu enkripsi di disk?
  - [ ] File bukti pelunasan `JTSE` (HNK-26.T13): nilai dan tinggi output tidak bertanda tangan; siapa penerimanya dan apa yang ia pelajari?
  - [ ] Kelas indeks `0/0` default, supplier opt-in (D-42, W-14): cek baris bucket indeks di threat model dan bagian Classes di spesifikasi.
  - [ ] Operator relay dan node financier (W-10, HNK-30.T10).
  - [ ] Riwayat buyer otomatis (HNK-25.T2): tag penerus di papan dipakai untuk mendeteksi sertifikat hilang; terkait keputusan B1.

## B. Lima keputusan dulu

- [ ] **B1. Griefing riwayat buyer** (Spec #1, TM #6). Buka `jitsuin-board/src/history.rs` (`own_chain`, cek penerus `UndisclosedSuccessor`). Cocokkan: entri `0x03` palsu dengan tag berikutnya membuat riwayat buyer ditolak. Pilih (a) peringatan + bantahan, (b) ikat tag ke identity key buyer, atau (c) batasan yang diketahui. Catatan: HNK-25.T2 sekarang juga memakai tag penerus (`successor_on_board` memblokir penerbitan), jadi pilihan ini juga menyentuh layar buyer.
- [ ] **B2. Salt komitmen** (TM #7). Lihat bagian A; kemungkinan cukup `terima: sudah diperbaiki di HNK-27.T1` setelah dicek.
- [ ] **B3. Tor** (TM #2, TM #1). `jitsuin-wallet/src/lib.rs` dan `jitsuin-board/src/lwd.rs`: flag `--connection tor` tidak diteruskan. Pilih: implementasikan, atau ubah klaim menjadi "belum diimplementasikan" plus saran node sendiri.
- [ ] **B4. OVK dan alamat supplier di dana** (TM #4). Perlu uji: `zcash-devtool list-tx` di wallet UFVK-saja dana (`~/.hanko-tes/testnet/fund-watch`), lihat apakah alamat penerima advance terlihat. Hasilnya menentukan TM L22.
- [ ] **B5. Nama jaringan "NU7, Ironwood"** (Spec #22, TM #8). Konfirmasi nama dan semantik pool; dipakai di spesifikasi, README (`Status: ... Zcash testnet (NU7)`), deskripsi submission, dan halaman orang luar.

## C. Threat model (HNK-11.T3)

Urut dari tingkat tertinggi. Centang setelah kolom Keputusan terisi.

- [ ] **TM #1** lightwalletd melihat `GetTransaction(txid)`, IP penyiar, tinggi papan. Naik karena UFVK publik (A).
- [ ] **TM #3** `settled` tertaut bagi pemegang N dan lewat korelasi tenor/waktu.
- [ ] **TM #6** `identity_pk` di tiap sertifikat; pemegang ujung rantai memantau invoice berikutnya (terkait B1).
- [ ] **TM #8** explorer melihat lebih dari jumlah action dan fee; perpindahan pool membuka nominal.
- [ ] **TM #4** OVK (B4).
- [ ] **TM #2** Tor (B3).
- [ ] **TM #5** indeks k (lihat A: setengah benar).
- [ ] **TM #7** salt (B2).
- [ ] **TM #9** QR/URI juga membawa N, nominal, jatuh tempo; tombol Copy; argv devtool terlihat di `ps`.
- [ ] **TM #10** halaman supplier mengunduh secret per invoice sebagai JSON plaintext: cek `jitsuinfi-frontend/src/pages/supplier.ts` masih begitu setelah HNK-24.
- [ ] **TM #11** `touches_transparent` hanya cek output dan tidak dipanggil di `pay` (masih benar per 2026-10-20: hanya dipakai di test).
- [ ] **TM #12** jeda register lalu advance.
- [ ] **TM #13** jenis entri dan txid terbaca (UFVK publik).
- [ ] **TM #14** tabel `outsider.ts`: tambah baris bucket, flag tepat/telat, jenis entri, waktu blok (pekerjaan teks: HNK-28.T5).
- [ ] **TM #15** alamat dipakai ulang antar-deal.
- [ ] **TM #16** bukti tanda tangan ganda juga memuat invoice penuh dan kedua entri.
- [ ] Baris **"terverifikasi benar"** di pra-review: baca sekali, setujui atau tandai.

## D. Spesifikasi (HNK-12.T3)

- [ ] **Spec #1** griefing riwayat (B1).
- [ ] **Spec #2** re-post entri bertag dihitung `Equivocation`, padahal `lookup` menerima re-post.
- [ ] **Spec #3** indeks tx: peringkat dalam compact block (`lib.rs`, `enumerate()` saat `block_txids`) vs indeks full node. Penting karena posisi JTSP dan README juri memakai `tx_index`.
- [ ] **Spec #4** indeks output dari devtool; `Position` tanpa pool; hanya entri tertambang.
- [ ] **Spec #5** flag tepat waktu: waktu blok (flow) vs tanggal kuitansi (`financierSettle` wasm).
- [ ] **Spec #6** prasyarat countersign: kuitansi per output = nilai output, seal klaim buyer.
- [ ] **Spec #7** input untuk membangun ulang seal settled.
- [ ] **Spec #8** tabel entri settled: panjang 167 byte, tag tidak ditandatangani, flag hanya di seal financier.
- [ ] **Spec #9** `DocKind::Invoice` tidak dipakai.
- [ ] **Spec #10** arti `flag` seal per dokumen dan peran.
- [ ] **Spec #11** decoder key: titik valid vs small-order.
- [ ] **Spec #12** salt dan bucket (lihat A: salt diturunkan, kelas sudah ada di kode).
- [ ] **Spec #13** bagian Privacy: bucket dan jenis 0x03 terbaca semua orang (UFVK publik).
- [ ] **Spec #14** cek verifier riwayat: N berbeda, allowlist, hasil `Open`.
- [ ] **Spec #15** layout JTSP; posisi sekarang dicek (A).
- [ ] **Spec #16** layout JTSB.
- [ ] **Spec #17** komitmen berbeda dari financier yang sama (A: kemungkinan selesai lewat salt turunan).
- [ ] **Spec #18** subbagian Transport (ZIP-321, base64url, ≤ 512 byte).
- [ ] **Spec #19** fee: posting papan 10 000 zat, siapa memegang spending key papan.
- [ ] **Spec #20** shielded-only tidak ditegakkan.
- [ ] **Spec #21** solvabilitas dana menghitung pelunasan tanpa cek tanda tangan/tertambang.
- [ ] **Spec #22** NU7 / Ironwood (B5).
- [ ] **Spec #23** browser memercayai posisi dan kelengkapan papan dari JSON backend.
- [ ] **Spec #24** daftar crate tanpa `jitsuin-wallet` (sekarang juga `jitsuin-flow`, `jitsuin-wasm`, `jitsuin-cli`).
- [ ] Baris **"terverifikasi benar"** di pra-review: baca sekali, setujui atau tandai.
- [ ] Format baru sejak spesifikasi ditulis: tentukan masuk spesifikasi atau cukup [[Format Data]]: `JTSM` (relay), `JTSF` (snapshot deal), `JTSE` (bukti pelunasan).

## E. Penutupan

- [ ] Semua kolom **Keputusan** di [[Pra-review Spesifikasi dan Threat Model]] terisi.
- [ ] [[Threat Model]] diperbarui untuk setiap `terima` (klaim yang dilebih-lebihkan diganti, ancaman yang hilang ditambah dengan mitigasi atau risiko sisa: AC-HNK-11.2).
- [ ] `jitsuinfi-zcash/docs/zip-shielded-receivable-registry.md` diperbarui untuk setiap `terima`; test vector tetap lulus (`cargo test --workspace`, AC-HNK-12.2).
- [ ] Teks halaman orang luar (`outsider.ts`, HNK-28.T5) dan bab 6 landing (HNK-18.T4) dicek terhadap TM #3, #5, #6, #14.
- [ ] Setiap `terima` yang butuh kode jadi task di [[Backlog]] (contoh: Tor, cek input transparan, alamat per deal).
- [ ] Keputusan desain (B1, B3) dicatat di [[Decision Log]].
- [ ] HNK-11.T3 dan HNK-12.T3 di [[Backlog]] jadi DONE dengan tanggal dan tautan ke pra-review; ES-HNK-11 dan ES-HNK-12 diperbarui.
- [ ] `python3 scripts/sync-vault.py` (Broken 0) dan `python3 scripts/check-backlogs.py --strict`.
