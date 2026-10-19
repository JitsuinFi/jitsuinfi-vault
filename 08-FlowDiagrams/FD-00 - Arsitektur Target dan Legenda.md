---
tags: [flow, architecture]
status: DRAF
updated: 2026-10-19
---

# FD-00 - Arsitektur Target dan Legenda

**Bagian dari:** [[08 - FlowDiagrams]] · Kembali: [[START-HERE]] · Terkait: [[Arsitektur JitsuinFi]] · [[Desain Jitsuin Seal]] · [[Format Data]] · [[Threat Model]] · [[Decision Log]]

> Dibuat 2026-10-19 atas permintaan user: halaman internal web app sekarang baru simulasi (salin-tempel kode antar tab, tanpa login, tanpa peran). Folder ini menggambarkan **bagaimana seharusnya** JitsuinFi berjalan end to end, dari auth sampai pelunasan, dan menandai mana yang **sudah ada** di kode dan mana yang **usulan**. Usulan P-01 – P-14 di bawah belum diputuskan; tiap usulan perlu jawaban Hans sebelum dibangun (D-29: pekerjaan baru diutamakan untuk Dex dan Dave).

## 1. Status yang dipakai di semua diagram

| Tanda | Arti | Contoh |
|---|---|---|
| **ADA** | Kode ada di repo dan teruji (unit test atau testnet) | `jitsuin-flow::financier::Flow`, `buyerSignInvoice` di `jitsuin-wasm` |
| **PARSIAL** | Inti ada (core, flow, wasm), tapi layar, API, atau integrasinya belum | Supplier menandatangani entri register: fungsi wasm ada, kartu di layar supplier belum |
| **USULAN** | Belum ada; desain target yang perlu keputusan | Kotak surat terenkripsi (P-04) |

Di sequence diagram, catatan hijau = ADA, kuning = USULAN, biru = PARSIAL. Di DFD, proses atau penyimpanan bergaris putus-putus kuning = USULAN.

## 2. Notasi DFD

DFD memakai notasi gaya Gane–Sarson dengan garis siku (PlantUML `linetype ortho`):

| Bentuk | Arti |
|---|---|
| Kotak biru tebal | Entitas eksternal (orang atau sistem di luar JitsuinFi) |
| Kotak sudut membulat merah | Proses (bernomor: 1.0, 1.1, …) |
| Kotak abu-abu berawalan `D` | Penyimpanan data |
| Teks di tengah garis (`F…`) | Aliran data; detailnya di tabel aliran di bawah tiap diagram |

Aliran data selalu bernomor (`F1`, `F1.3`, `F2.4.1`, …) supaya garis tidak dipenuhi teks. Arti lengkap tiap aliran ada di tabel di bawah diagram.

## 3. Komponen target

| Komponen | Isi | Status | Repo |
|---|---|---|---|
| Web app | Halaman per peran, statis, CSP same-origin, tanpa CDN | PARSIAL (layar simulasi, HNK-10) | `jitsuinfi-frontend` |
| `jitsuin-wasm` | Semua kriptografi di browser: invoice, tanda tangan, seal, kuitansi, sertifikat, verifikasi bundel, bukti, riwayat. Juga `financierSealAssignment` dan `financierSettle` (dipakai landing); `financierSettle` menentukan tepat waktu dari tanggal kuitansi, sedangkan alur node memakai waktu blok | ADA | `jitsuinfi-zcash/crates/jitsuin-wasm` |
| Authenticator passkey | Platform authenticator (iCloud Keychain, Google Password Manager, kunci keamanan) dengan ekstensi WebAuthn PRF | ADA untuk buyer (`src/lib/passkey.ts`); peran lain USULAN | perangkat pengguna |
| Relay dokumen | Kotak surat terenkripsi end-to-end antar pihak + endpoint snapshot papan | USULAN (P-04, P-06) | `jitsuinfi-backend` (D-17) |
| Node financier | `jitsuin-flow` (state machine, watchdog) + wallet `zcash-devtool` (spending key) + key financier + API untuk konsol financier | PARSIAL: flow ADA, API HNK-05.T3 belum | `jitsuinfi-zcash` + backend financier |
| Pemindai papan | Wallet watch-only dengan UFVK papan (D-11 usulan): `scan`, `lookup`, `settled`, `rate_index` | ADA | `jitsuin-board` |
| `jitsuin` CLI | `jitsuin verify`, `jitsuin index` untuk juri dan auditor | ADA (PR #4, #6) | `jitsuin-cli` |
| lightwalletd | `zec.rocks` (D-12) | eksternal | — |
| Zodl | Wallet pengguna: menerima advance (supplier), membayar QR ZIP-321 (buyer) | eksternal, opsional (D-15, SPK-04) | — |

## 4. Usulan yang perlu keputusan

| ID | Usulan | Alasan | Dampak |
|---|---|---|---|
| P-01 | **Akun = passkey.** Tanpa email, password, OTP, atau akun pengguna di server. Daftar = membuat passkey; masuk = meminta output PRF. Identitas bisa dibangun ulang hanya dari passkey (uji "stateless": localStorage dikosongkan atau perangkat baru, key tetap sama). Server hanya menyimpan ciphertext kotak surat (relay) dan public key credential financier (node) | Pola Mera / WebAuthn PRF ([[Desain Jitsuin Seal]] §9) | Halaman login dan daftar baru; tidak ada tabel pengguna |
| P-02 | **Satu salt per peran dan kegunaan:** `jitsuin/buyer/master/v1` (sudah dipakai), `jitsuin/supplier/master/v1`, `jitsuin/<peran>/inbox/v1`. Financier tidak butuh salt key (key di node, P-05). Satu orang boleh memegang beberapa peran dengan key terpisah. Catatan: `SelfApproval` hanya membandingkan key, jadi satu orang yang menjadi supplier sekaligus buyer dengan key berbeda tidak tertangkap; larangan itu kebijakan, bukan protokol | Satu passkey, banyak key terisolasi | Pilihan peran setelah masuk |
| P-03 | **Key per invoice supplier diturunkan dari master supplier dan `invoice_id`** (keyed BLAKE2b, pola sama dengan key buyer), menggantikan key acak + unduh JSON plaintext | Menutup temuan pra-review TM #10 (secret diunduh plaintext) | Fungsi baru di `jitsuin-core` dan `jitsuin-wasm` |
| P-04 | **Relay dokumen = kotak surat end-to-end.** Dokumen deal (invoice, tanda tangan, entri, surat, seal, sertifikat, txid advance) dienkripsi di browser untuk kunci kotak surat penerima (X25519 dari salt inbox + AEAD). Server hanya menyimpan ciphertext, id kotak surat, dan masa simpan (misalnya 30 hari untuk pesan; rantai sertifikat buyer tanpa kedaluwarsa, lihat P-09). Memo yang diteruskan relay hanya petunjuk: bukti uang + seal satu transaksi tetap dari wallet penerima | Menggantikan salin-tempel; server tidak bisa membaca isi deal | Repo `jitsuinfi-backend` (Railway), endpoint `/api/mailbox` lewat P-11 |
| P-05 | **Key financier tinggal di node financier**, bersama spending key wallet. Pairing sekali: seed dibuat di node, UFVK papan diimpor watch-only, public key credential operator disimpan. Operator masuk ke konsol node dengan assertion passkey (WebAuthn standar, diverifikasi node) | Watchdog harus menandatangani `settled` otomatis begitu pembayaran ditambang; advance memo dibangun di node | API HNK-05.T3 memakai sesi dari assertion passkey; lihat P-12 |
| P-06 | **Endpoint snapshot papan** di relay: hasil `scan` dengan UFVK papan (D-11) sebagai JSON `[{txid, height, tx_index, output_index, memo}]`. Browser memverifikasi sendiri; kelengkapan snapshot tetap kepercayaan pada relay, jadi verifikasi yang menentukan memakai `jitsuin verify` | wasm tidak punya I/O jaringan; temuan pra-review Spec #23 | Satu endpoint baca-saja; tanpa data pengguna |
| P-07 | **Sesi:** key hanya di memori tab; terkunci setelah 15 menit idle atau tab ditutup. Setiap seal (印) meminta passkey ulang dengan user verification: satu sentuhan = satu stempel | Tanda tangan adalah tindakan hukum (Pasal 613 KUHPerdata untuk surat pengalihan) | Pola UX konsisten di semua peran |
| P-08 | **Salt komitmen financier dibuat library** (CSPRNG 32 byte per deal), tidak pernah diisi pengguna | Temuan pra-review TM #7 | Perubahan kecil di `jitsuin-flow` dan `jitsuin-wasm` |
| P-09 | **Indeks invoice buyer `k` dihitung otomatis** dari rantai sertifikat buyer sendiri (disimpan terenkripsi tanpa kedaluwarsa), bukan diketik. Belum ada aturan untuk invoice yang tidak jadi dibiayai atau beberapa invoice yang berjalan bersamaan: `k` bisa dipakai ulang (satu `invoice_pk` di dua invoice dapat ditautkan) | Salah ketik `k` merusak rantai riwayat | Layar buyer; mungkin perubahan di `jitsuin-core` |
| P-10 | **Anggota dana tidak pernah mengirim UFVK ke server.** Pemindaian dengan UFVK berjalan di CLI lokal anggota; halaman anggota hanya membaca hasil pindaian lokal | UFVK membuka semua nominal dana (Threat Model) | Halaman HNK-15.T3 menerima snapshot lokal |
| P-11 | **Semua panggilan browser tetap same-origin.** CSP `connect-src 'self'` dipertahankan; relay dan snapshot papan dijangkau lewat rewrite Vercel (`/api/*`), konsol financier disajikan oleh node sendiri (`/node/*` di origin node) | CSP sekarang memblokir origin lain; cookie `SameSite=Strict` hanya untuk origin yang sama | Konfigurasi `vercel.json`, CORS tidak dibuka |
| P-12 | **Konflik dengan D-23.** D-23 menulis watchdog "akses baca lewat viewing key", tetapi `post_settled` (kode yang sudah ada) mem-posting entri `settled` memakai spending wallet node. Pilihan: (a) catat keputusan baru: node memegang spending key dan memposting otomatis; (b) pisahkan penandatangan (watchdog, baca saja + key financier) dari pemosting (wallet terpisah) | Dokumen dan kode harus sama | Keputusan D-xx baru |
| P-13 | **Tambah `assignmentDecode` di `jitsuin-wasm`** dan tampilkan isi surat (alamat bayar, nominal, jatuh tempo, financier) sebelum supplier dan buyer menyegel | Seal buyer adalah pengakuan tertulis (Pasal 613 KUHPerdata); sekarang layar menyegel surat yang isinya tidak terbaca | Fungsi wasm baru + layar |
| P-14 | **Bukti tanda tangan ganda yang lolos `jitsuin verify`.** Financier meminta entri bertanda tangan supplier sebelum cek papan (supaya punya entri B), dan bukti disusun dengan posisi papan (`proof_from_offer`, atau `doubleSignProof` wasm ditambah argumen posisi) | `Flow` sekarang meminta entri hanya setelah `NotFound`; wasm `doubleSignProof` tidak mengisi posisi sehingga CLI menolak bukti | Urutan alur financier + fungsi wasm |

## 5. Jaringan, biaya, dan papan

- Development dan uji integrasi di **testnet** (D-13; lightwalletd `testnet.zec.rocks`); mainnet hanya untuk demo akhir kalau ZEC tersedia (SPK-10).
- Setiap posting ke papan (entri register, entri `settled`) = 10 000 zat ke alamat papan **ditambah** fee ZIP-317 (sekitar 10 000 zat). Root kewajiban dana = self-send dengan memo.
- UFVK dan tinggi awal papan belum dipublikasikan (D-11 masih usulan); diagram yang memakai "UFVK papan" mengasumsikan D-11 disetujui.
- Mode confidential ([[Mode Confidential]]) adalah roadmap: hanya dicatat di [[SEQ-01 - Supplier]], tidak digambar di DFD.

## 6. Temuan kode dari audit diagram (2026-10-19)

| Temuan | Bukti | Usulan |
|---|---|---|
| Kelas diskon/tenor tidak pernah dihitung: `classes_for` hanya dipanggil di test; wasm `supplierRegisterEntry` selalu menandatangani 0/0; `Deal` tidak punya kelas dan `check_entry` tidak memeriksanya. Akibatnya indeks bunga selalu kosong | `jitsuin-core/src/index.rs:102`, `jitsuin-wasm/src/api.rs` | Hitung kelas di 3.2 dan ikutkan di entri ([[DFD-2.3 - Registrasi Papan]]) |
| wasm `doubleSignProof` tidak mengisi posisi papan; `jitsuin verify` menolak bukti tanpa posisi entri pertama | `jitsuin-wasm/src/api.rs:457`, `jitsuin-cli/src/verify.rs:154` | P-14 |
| Tidak ada `assignmentDecode` di wasm | daftar export `jitsuin-wasm/src/lib.rs` | P-13 |
| `register()` tanpa cek papan ulang dan tanpa pemulihan setelah crash (beda dengan `sent_advance`) | `jitsuin-flow/src/financier.rs` | Tambah pencarian entri terkirim sebelum posting ulang |
| Layar Buyer tidak punya input file syarat dan cek hash; layar Financier tidak punya kartu bukti ganda | `src/pages/buyer.ts`, `src/pages/financier.ts` | HNK-21 |

## 7. Apa yang tidak berubah

- Semua aturan protokol di [[Format Data]] dan [[Desain Jitsuin Seal]]: N, entri papan, seal berantai, Sign-to-Pay, `settled` dua tanda tangan, rantai riwayat, bukti tanda tangan ganda.
- Uang hanya bergerak di pool shielded; papan hanya menerima memo.
- Tidak ada smart contract, TEE, CDN pihak ketiga, atau AI sebagai hakim (D-05, D-23).
