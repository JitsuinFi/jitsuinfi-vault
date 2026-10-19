---
tags: [flow, architecture]
status: DRAF
updated: 2026-10-20
---

# FD-00 - Arsitektur Target dan Legenda

**Bagian dari:** [[08 - FlowDiagrams]] · Kembali: [[START-HERE]] · Terkait: [[Arsitektur JitsuinFi]] · [[Desain Jitsuin Seal]] · [[Format Data]] · [[Threat Model]] · [[Decision Log]]

> Dibuat 2026-10-19 atas permintaan user: halaman internal web app sekarang baru simulasi (salin-tempel kode antar tab, tanpa login, tanpa peran). Folder ini menggambarkan **bagaimana seharusnya** JitsuinFi berjalan end to end, dari auth sampai pelunasan, dan menandai mana yang **sudah ada** di kode dan mana yang **usulan**. Usulan P-01 – P-14 di bawah belum diputuskan; tiap usulan perlu jawaban Hans sebelum dibangun (D-29: pekerjaan baru diutamakan untuk Dex dan Dave).

## 1. Status yang dipakai di semua diagram

| Tanda | Arti | Contoh |
|---|---|---|
| **ADA** | Kode ada di repo dan teruji (unit test atau testnet) | `jitsuin-flow::financier::Flow`, `buyerSignInvoice` di `jitsuin-wasm` |
| **PARSIAL** | Inti ada (core, flow, wasm), tapi layar, API, atau integrasinya belum | Supplier menandatangani entri register: fungsi wasm ada, kartu di layar supplier belum |
| **USULAN** | Belum ada; desain target yang perlu keputusan. Di PG-01 halaman usulan juga ditulis USULAN (dengan ID item) | Kotak surat terenkripsi (P-04) |
| **Belum diuji** | Kode ada, tetapi belum ada kasus uji yang tercatat | Key passkey identik di perangkat baru |

Warna catatan di sequence diagram: hijau = ADA, biru = PARSIAL, kuning = USULAN, merah muda = temuan atau celah yang perlu diperbaiki, putih = keterangan netral. Di DFD, proses bergaris penuh = ADA atau PARSIAL (rinciannya di kolom Status tabel proses), proses atau penyimpanan bergaris putus-putus kuning = USULAN. Di PG-01, kotak hijau = halaman simulasi yang sudah ada, kuning putus-putus = USULAN.

## 2. Notasi DFD

DFD memakai notasi gaya Gane–Sarson dengan garis siku (PlantUML `linetype ortho`):

| Bentuk | Arti |
|---|---|
| Kotak biru tebal | Entitas eksternal (orang atau sistem di luar JitsuinFi) |
| Kotak sudut membulat merah | Proses (bernomor: 1.0, 1.1, …) |
| Kotak abu-abu berawalan `D` | Penyimpanan data |
| Teks di tengah garis | Aliran data; detailnya di tabel aliran di bawah tiap diagram |

Aliran data selalu bernomor supaya garis tidak dipenuhi teks: `K1` di level 0, `F1` di level 1, `F1.01` di level 2 (aliran ke-1 proses 1.0). Level 2 ditulis di `scripts/dfd_model.py`; `scripts/build-dfd.py` membuat DFD-1 dan DFD-2.x darinya, menulis ulang pemetaan level 0, dan memeriksa balancing.

## 3. Komponen target

| Komponen | Isi | Status | Repo |
|---|---|---|---|
| Web app | Halaman per peran untuk supplier, buyer, anggota dana, verifier; statis, CSP same-origin, tanpa CDN | PARSIAL (layar simulasi, HNK-10) | `jitsuinfi-frontend` |
| `jitsuin-wasm` | Semua kriptografi di browser: invoice, tanda tangan, seal, kuitansi, sertifikat, verifikasi bundel, bukti, riwayat. Juga `financierSealAssignment` dan `financierSettle` (dipakai landing); `financierSettle` menentukan tepat waktu dari tanggal kuitansi, sedangkan alur node memakai waktu blok | ADA | `jitsuinfi-zcash/crates/jitsuin-wasm` |
| Authenticator passkey | Platform authenticator (iCloud Keychain, Google Password Manager) atau security key dengan ekstensi WebAuthn PRF. Security key terikat ke satu perangkat | ADA untuk buyer (`src/lib/passkey.ts`); peran lain USULAN | perangkat pengguna |
| Relay dokumen | Kotak surat terenkripsi end-to-end antar pihak + endpoint snapshot papan | USULAN (P-04, P-06) | `jitsuinfi-backend` (D-17) |
| Node financier | `jitsuin-flow` (state machine, penjadwal pelunasan) + wallet `zcash-devtool` (spending key) + key financier + key kotak surat financier + API dan konsol financier di origin node | PARSIAL: flow ADA, API HNK-05.T3 dan konsol belum | `jitsuinfi-zcash` + backend financier |
| Pemindai papan | Wallet watch-only dengan UFVK papan (D-11 usulan): `scan`, `lookup`, `settled`, `rate_index` | ADA | `jitsuin-board` |
| `jitsuin` CLI | `jitsuin verify`, `jitsuin index` untuk juri dan auditor | ADA (PR #4, #6) | `jitsuin-cli` |
| Verifikasi advance di sisi supplier | `jitsuin` CLI lokal + wallet watch-only supplier sendiri; menjalankan `received_advances` dan `verify_sign_to_pay` di luar browser | USULAN (fungsi ADA, hanya dipanggil unit test) | `jitsuin-cli`, `jitsuin-flow::supplier` |
| Pemindai lokal anggota dana | `zcash-devtool` watch-only dengan UFVK akun operasional + `fund_view` / `solvency` | PARSIAL (fungsi ADA, belum ada perintah CLI) | `jitsuin-flow::fund` |
| lightwalletd | `testnet.zec.rocks:443` (testnet, default kode; SPK-19, SPK-02) dan `zec.rocks:443` (mainnet, D-12) | eksternal | — |
| Zodl | Wallet pengguna: menerima advance (supplier), membayar QR ZIP-321 (buyer) | eksternal, opsional (D-15, SPK-04) | — |

## 4. Usulan yang perlu keputusan

| ID | Usulan | Alasan | Dampak |
|---|---|---|---|
| P-01 | **Akun = passkey.** Tanpa email, password, OTP, atau akun pengguna di server. Satu passkey per orang: daftar = satu `create()` (nama netral peran, `excludeCredentials`); menambah peran = `get()` dengan salt peran itu; masuk = meminta output PRF dengan `allowCredentials` dari profil bila ada; web app menampilkan sidik jari key publik. Identitas bisa dibangun ulang hanya dari passkey (uji "stateless"). Server menyimpan kotak surat (`mailbox_pk`, `mailbox_id` turunan, ciphertext, masa simpan) di relay dan public key credential financier di node. **Pemulihan belum ada:** passkey hilang = semua key hilang, deal berjalan berakhir sebagai gagal bayar (buyer tidak bisa menandatangani klaim), dan key identitas yang terikat KYC tidak bisa dirotasi. Pilihan: backup master terenkripsi, atau rotasi identitas lewat KYC; passkey kedua tidak menghasilkan PRF yang sama | Pola Mera / WebAuthn PRF ([[Desain Jitsuin Seal]] §9) | Halaman login dan daftar baru; tidak ada tabel pengguna, hanya tabel kotak surat dengan id turunan; keputusan pemulihan |
| P-02 | **Satu salt per peran dan kegunaan:** SHA-256 dari `jitsuin/buyer/master/v1` (sudah dipakai), `jitsuin/supplier/master/v1`, dan `jitsuin/<peran>/inbox/v1` untuk peran di web app (supplier, buyer, anggota dana). Financier tidak memakai salt apa pun di browser: key dan kotak suratnya di node (P-05). Satu orang boleh memegang beberapa peran dengan key terpisah. Catatan: `SelfApproval` hanya membandingkan key, jadi satu orang yang menjadi supplier sekaligus buyer dengan key berbeda tidak tertangkap; larangan itu kebijakan, bukan protokol | Satu passkey, banyak key terisolasi | Pilihan peran setelah masuk |
| P-03 | **Key per invoice supplier diturunkan dari master supplier**, menggantikan key acak + unduh JSON plaintext. Keyed BLAKE2b dengan personalisasi sendiri (misalnya `JitsuinSupplKey_`) dan input unik per invoice dengan prefiks panjang (penghitung, atau `invoice_id` + `buyer_pk` / nonce yang disimpan dengan deal). Bukan `invoice_id` polos: id bebas sering dipakai ulang, dan id yang sama memberi `supplier_ephemeral_pk` yang sama sehingga pemegang satu invoice bisa menemukan entri lain supplier di papan. UI menolak `invoice_id` yang dipakai ulang | Menutup temuan pra-review TM #10 (secret diunduh plaintext) tanpa membuka keterhubungan antar invoice | Fungsi baru di `jitsuin-core` dan `jitsuin-wasm` |
| P-04 | **Relay dokumen = kotak surat end-to-end.** Dokumen deal (invoice, tanda tangan, PDF syarat dan PDF surat, entri, surat, seal, sertifikat, txid advance) dienkripsi di browser atau node untuk `mailbox_pk` penerima (X25519 dari salt inbox + AEAD), dengan `mailbox_pk` penerima dari kartu kontak (D19). `mailbox_id` = BLAKE2b(`mailbox_pk`), dihitung ulang klien di perangkat baru. Relay menyimpan `mailbox_pk`, `mailbox_id`, ciphertext, dan masa simpan (misalnya 30 hari untuk pesan; rantai sertifikat buyer tanpa kedaluwarsa, lihat P-09). Membaca kotak surat wajib bukti kepemilikan (challenge yang dienkripsi ke `mailbox_pk`). Pesan dari financier (surat, permintaan riwayat) ditandatangani node dengan `financier_pk`, dan layar memeriksa `financier_pk` terhadap kontak yang diverifikasi di luar sistem; surat JTSA sendiri tidak bertanda tangan sampai s2. Relay dan proxy tidak bisa membaca isi tetapi melihat metadata (IP pengirim, kotak surat tujuan, ukuran, waktu) dan bisa mengorelasikan pesan supplier ke financier dengan entri papan berikutnya; pertimbangkan padding, batching, jeda, dan pisahkan layanan snapshot dari kotak surat. Memo yang diteruskan relay hanya petunjuk: bukti uang + seal satu transaksi tetap dari wallet penerima | Menggantikan salin-tempel; server tidak bisa membaca isi deal | Repo `jitsuinfi-backend` (Railway), endpoint `/api/mailbox` lewat P-11; baris relay/proxy baru di [[Threat Model]] |
| P-05 | **Key financier tinggal di node financier**, bersama spending key wallet dan key kotak surat financier. Pairing sekali (satu-satunya pendaftaran financier): seed dibuat di node, UFVK papan diimpor watch-only, passkey operator didaftarkan untuk `rp.id` domain node. Operator masuk ke konsol node dengan assertion passkey: challenge sekali pakai dengan kedaluwarsa, cek origin, `rpIdHash`, flag UV, signature; cookie `Secure`, `__Host-`, `HttpOnly`, `SameSite=Strict`. WebAuthn butuh domain (bukan IP) dan HTTPS, atau localhost / tunnel SSH | Penjadwal harus menandatangani `settled` otomatis begitu pembayaran ditambang; memo advance dibangun di node | API HNK-05.T3 memakai sesi dari assertion passkey; lihat P-12 |
| P-06 | **Endpoint snapshot papan** di relay: hasil `scan` dengan UFVK papan (D-11) sebagai JSON `[{txid, height, tx_index, output_index, memo}]`. Browser memverifikasi sendiri; kelengkapan snapshot tetap kepercayaan pada relay, jadi verifikasi yang menentukan memakai `jitsuin verify` | wasm tidak punya I/O jaringan; temuan pra-review Spec #23 | Satu endpoint baca-saja; tanpa data pengguna |
| P-07 | **Sesi dan stempel untuk key di browser (supplier, buyer).** Di memori tab hanya key kotak surat dan key publik; terkunci setelah 15 menit idle atau tab ditutup. Setiap seal (印) meminta PRF baru dengan user verification, key tanda tangan diturunkan sebagai `Uint8Array` lalu dinolkan: satu sentuhan = satu stempel. Ini cek niat (UX), bukan kontrol keamanan: skrip di tab yang sama tetap bisa meminta PRF. Untuk financier, node menandatangani s2 dan `settled` otomatis; aturan persetujuannya: satu assertion operator per deal sebelum `Pay` | Tanda tangan adalah tindakan hukum (Pasal 613 KUHPerdata untuk surat pengalihan) | Pola UX supplier dan buyer; aturan persetujuan di konsol financier |
| P-08 | **Salt komitmen financier dibuat library** (CSPRNG 32 byte), disimpan per (invoice, financier) dan dipakai ulang saat retry, tidak pernah diisi pengguna. Salt baru setiap retry memberi dua komitmen untuk satu financier = JTSP yang sah melawan supplier jujur (Spec #17) | Temuan pra-review TM #7 | Perubahan kecil di `jitsuin-flow` dan `jitsuin-wasm` |
| P-09 | **Indeks invoice buyer `k` dihitung otomatis** dari rantai sertifikat buyer sendiri (disimpan terenkripsi tanpa kedaluwarsa), bukan diketik. `k` hanya menghitung sertifikat yang sudah tertambat di papan; sertifikat yang tidak pernah tertambat (financier tidak jadi registrasi) dibuang sebelum pengungkapan berikutnya, karena kalau tidak `verify_history` gagal (`NotAnchored`). Sebelum menerbitkan sertifikat k, buyer menjalankan `verifyHistory` atas rantainya sendiri dan menolak bila tag penerus sudah ada. Relay menyimpan kepala rantai bertanda tangan (indeks, hash) supaya penghapusan sertifikat terakhir terdeteksi (`k` dipakai ulang = `invoice_pk` sama di dua invoice dan riwayat bercabang) | Salah ketik `k` merusak rantai riwayat | Layar buyer; mungkin perubahan di `jitsuin-core` |
| P-10 | **Anggota dana tidak pernah mengirim UFVK ke server.** Pemindaian dengan UFVK berjalan di CLI lokal anggota; halaman anggota hanya membaca hasil pindaian lokal | UFVK membuka semua nominal dana (Threat Model) | Halaman HNK-15.T3 menerima snapshot lokal |
| P-11 | **Semua panggilan browser tetap same-origin.** CSP `connect-src 'self'` dipertahankan. Web app (supplier, buyer, anggota dana, verifier) menjangkau relay dan snapshot papan lewat rewrite Vercel (`/api/*`). Konsol financier disajikan oleh node di origin node; node memegang key kotak surat financier dan meneruskan relay di `/node/mail/*`, jadi konsol tidak memanggil origin lain dan financier tidak punya salt di web app Vercel. Karena `vercel.app` ada di Public Suffix List, web app dan node selalu beda site: cookie `SameSite=Strict` node tidak terkirim dari web app, dan `connect-src 'self'` memblokir fetch-nya. Begitu relay ada, CSP tidak lagi mencegah pencurian key: skrip yang disuntikkan bisa meminta PRF dan menulis hasilnya ke kotak surat penyerang di origin yang sama. Mitigasi: Trusted Types atau render ketat dokumen yang ditempel, penulisan kotak surat hanya sealed box dengan rate limit, SRI atau build yang bisa direproduksi | CSP sekarang memblokir origin lain | Konfigurasi `vercel.json`, konsol node, CORS tidak dibuka; catat di [[Threat Model]] |
| P-12 | **Konflik dengan D-23.** D-23 menulis watchdog "akses baca lewat viewing key", tetapi `post_settled` (kode yang sudah ada) mem-posting entri `settled` memakai spending wallet node. Pilihan: (a) catat keputusan baru: node memegang spending key dan memposting otomatis; (b) pisahkan penandatangan (penjadwal, baca saja + key financier) dari pemosting (wallet terpisah) | Dokumen dan kode harus sama | Keputusan D-xx baru |
| P-13 | **Tambah `assignmentDecode` di `jitsuin-wasm`** dan tampilkan isi surat (alamat bayar, nominal, jatuh tempo, `financier_pk`, `terms_hash`) sebelum supplier dan buyer menyegel; layar mencocokkan SHA-256 PDF surat dengan `terms_hash` | Seal buyer adalah pengakuan tertulis (Pasal 613 KUHPerdata); sekarang layar menyegel surat yang isinya tidak terbaca | Fungsi wasm baru + layar |
| P-14 | **Bukti tanda tangan ganda yang lolos `jitsuin verify`, tanpa menjebak supplier jujur.** Meminta entri bertanda tangan sebelum cek papan memberi financier entri B, tetapi juga membuat JTSP yang sah melawan supplier jujur: (a) financier yang menolak setelah menerima entri (misalnya riwayat ditolak) menyimpannya, lalu ketika supplier dibiayai pihak lain membuat `proof_from_offer`; (b) financier A yang registrasi lalu mundur tidak pernah melepas N, jadi penawaran ulang ke B menjadi "Caught"; (c) salt baru setiap retry (lihat P-08). Verifikasi JTSP tidak bisa membedakan ini dari penipuan: **JTSP membuktikan dua tanda tangan, bukan niat menipu.** Sebelum diadopsi: tanda tangan pra-cek menjadi penawaran eksklusif yang kedaluwarsa (tinggi kedaluwarsa di entri bertanda tangan, atau pelepasan bertanda tangan saat menolak atau mundur), dan bukti hanya diterima bila entri pemenang tertambang sebelum kedaluwarsa; salt deterministik atau disimpan (P-08). Untuk `DoubleFinanced` bukti lengkap sudah bisa dari `proof_from_lookup`. Web: tambah `verifyProofOnBoard(proof, snapshot)` di wasm untuk layar Verify, dan `doubleSignProof` diberi argumen posisi; sampai itu posisi di web ditulis "diklaim" | `Flow` sekarang meminta entri hanya setelah `NotFound`; wasm `doubleSignProof` tidak mengisi posisi sehingga CLI menolak bukti; web tidak memeriksa posisi | Urutan alur financier, format entri (kedaluwarsa), fungsi wasm; kalau tidak diadopsi, urutan sekarang dipertahankan |

## 5. Jaringan, biaya, dan papan

- Development dan uji integrasi di **testnet** (D-13; lightwalletd `testnet.zec.rocks:443`); mainnet (`zec.rocks:443`, D-12) hanya untuk demo akhir kalau ZEC tersedia (SPK-10).
- Setiap posting ke papan (entri register, entri `settled`) = 10 000 zat ke alamat papan **ditambah** fee ZIP-317 (sekitar 10 000 zat). Root kewajiban dana = self-send 10 000 zat dengan memo ke akun operasional: uangnya kembali, yang terpakai hanya fee.
- UFVK dan tinggi awal papan belum dipublikasikan (D-11 masih usulan); diagram yang memakai "UFVK papan" mengasumsikan D-11 disetujui.
- Mode confidential ([[Mode Confidential]]) adalah roadmap: hanya dicatat di [[SEQ-01 - Supplier]], tidak digambar di DFD.

## 6. Temuan kode dari audit diagram (2026-10-19, diperbarui 2026-10-20)

| Temuan | Bukti | Usulan |
|---|---|---|
| Kelas diskon/tenor tidak pernah dihitung: `classes_for` hanya dipanggil di test; fungsi entri wasm (`supplierRegisterEntry`, `supplierRegisterHistoryEntry`) menandatangani 0/0 tetap; `Deal` tidak punya kelas dan `check_entry` tidak memeriksanya. Akibatnya indeks bunga selalu kosong | `jitsuin-core/src/index.rs:102`, `jitsuin-wasm/src/api.rs:431-439` | Hitung kelas di 3.2, beri parameter kelas pada API entri wasm, periksa di `check_entry` ([[DFD-2.3 - Registrasi Papan]]) |
| wasm `doubleSignProof` tidak mengisi posisi papan; `jitsuin verify` menolak bukti tanpa posisi entri pertama; `verifyProof` di web tidak memeriksa papan | `jitsuin-wasm/src/api.rs:457`, `jitsuin-cli/src/verify.rs:154`, `src/pages/verify.ts:66` | P-14 |
| `proof_from_lookup` dan `proof_from_offer` tidak punya pemanggil di node; entri yang ditawarkan tidak disimpan setelah `Register` (diganti txid) | `jitsuin-board/src/lib.rs:287-310`, `jitsuin-flow/src/financier.rs:180-186` | Panggil `proof_from_lookup` di `Stopped(DoubleFinanced)`; simpan entri tawaran hanya bila P-14 diadopsi |
| Tidak ada `assignmentDecode` di wasm | daftar export `jitsuin-wasm/src/lib.rs` | P-13 |
| `register()` tanpa cek papan ulang dan tanpa pemulihan setelah crash (beda dengan `sent_advance`). `Flow` menolak `BoardChecked` di `AwaitSupplierSignature` dan `Register`, jadi cek ulang butuh transisi baru | `jitsuin-flow/src/financier.rs:172-179`, `:340-352` | Terima `BoardChecked` di `Register` (`NotFound`: state tetap; komitmen lain: `Stopped`) sebelum posting; cari entri yang sudah terkirim sebelum posting ulang |
| `post_settled` hanya melihat settled yang sudah tertambang; penjadwal berkala akan memposting ulang di setiap poll antara broadcast dan tertambang (10 000 zat + fee tiap kali) | `jitsuin-flow/src/settlement.rs:170-183`, `jitsuin-board/src/lib.rs:171-173` | Penjadwal menyimpan txid settled yang terkirim atau memeriksa tx wallet yang tertunda |
| Advance yang diterima tidak dibandingkan dengan advance yang disepakati: kuitansi hanya dicek sama dengan nilai output, jadi financier bisa membayar kurang dan surat tetap `Sealed` | `jitsuin-flow/src/receipts.rs:73-80`, `jitsuin-flow/src/supplier.rs:66-78` | Bandingkan `receipt.amount_zat` dengan advance di penawaran (4.8) |
| `Done` tercapai saat advance terkirim, bukan tertambang; `sent_advance` tidak memeriksa tinggi tambang, jadi retry setelah tx kedaluwarsa mencatat `Done` tanpa uang sampai | `jitsuin-flow/src/financier.rs:289-310` | Cek konfirmasi advance sebelum `Done` |
| Entri yang ditambang ulang di tinggi lain tidak mengulang hitungan konfirmasi (`on_board` memakai posisi lama) | `jitsuin-flow/src/financier.rs:232-235` | Hitung ulang dari posisi pemenang terbaru |
| `SolvencyPolicy.grace_days` tidak pernah dibaca: tenggang dipakai di `member_view`/`fund_view` | `jitsuin-flow/src/fund.rs:58-62`, `:204-218` | Hapus field atau pakai di `solvency` |
| Nilai piutang dana (`face_zat` di JTN1) tidak terikat ke advance atau invoice | `jitsuin-core/src/fund.rs:26-30`, `jitsuin-flow/src/fund.rs:121-147` | Batasi nilai terhadap advance atau wajibkan entri register yang cocok |
| `buyerRepayment` membuat QR dari surat apa pun yang ditempel, tanpa cek `Sealed` | `jitsuin-wasm/src/api.rs:151-179` | QR hanya untuk surat `Sealed` (DFD-2.5 5.1) |
| Supplier memegang sertifikat k penuh padahal wasm hanya memakai `cert.tag()` | `jitsuin-wasm/src/api.rs:586-606` | Varian wasm yang menerima `history_tag` 32 byte saja |
| Layar Buyer tidak punya input file syarat dan cek hash; layar Financier tidak punya kartu bukti ganda; teks kartu surat di `financier.ts:17` bertentangan dengan urutan surat sebelum `Flow::new` | `src/pages/buyer.ts`, `src/pages/financier.ts` | HNK-21 |

## 7. Apa yang tidak berubah

- Semua aturan protokol di [[Format Data]] dan [[Desain Jitsuin Seal]]: N, entri papan, seal berantai, Sign-to-Pay, `settled` dua tanda tangan, rantai riwayat, bukti tanda tangan ganda.
- Uang hanya bergerak di pool shielded; papan hanya menerima memo.
- Tidak ada smart contract, TEE, CDN pihak ketiga, atau AI sebagai hakim (D-05, D-23).
