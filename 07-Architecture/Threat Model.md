---
tags: [architecture, security]
---

# Threat Model

**Bagian dari:** [[07 - Architecture]] · Kembali: [[START-HERE]] · Terkait: [[Arsitektur JitsuinFi]] · [[Format Data]] · [[Desain Jitsuin Seal]] · [[Mode Confidential]]

> **Final (HNK-11.T1, 2026-10-18)**, ditinjau ulang setelah HNK-05 – HNK-07, HNK-19, HNK-20, dan HNK-15.T2 diimplementasikan dan diuji di testnet. Aturan juri: "Leaks are disqualifying." Setiap kebocoran punya mitigasi atau dinyatakan terang-terangan sebagai risiko tersisa.

## Siapa melihat apa

| Pihak | Melihat | Tidak melihat |
|---|---|---|
| Publik / pengamat chain (block explorer) | Ada transaksi shielded; waktu (blok); jumlah action; fee | Isi memo, nominal, alamat, pihak. Semua transaksi uji: input dan output shielded (`transparent=false`) |
| Pemegang viewing key papan (siapa pun) | Entri register: N, commitment financier, bucket diskon/tenor, tag riwayat (jenis `0x03`); entri `settled`: `settled_tag`, flag tepat waktu, dua tanda tangan; waktu (blok) | Isi invoice, identitas supplier/buyer/financier, nominal. Tanda tangan tidak bisa dicek tanpa key dari invoice. Entri `settled` tidak bisa ditautkan ke entri register-nya |
| Financier A (yang membiayai) | Invoice, surat pengalihan, nominal advance, pelunasan dari buyer, klaim buyer | Invoice dan financier lain; riwayat buyer di luar yang diserahkan buyer |
| Financier B (ditawari invoice yang sama) | Invoice itu, bahwa N sudah terdaftar, bukti tanda tangan ganda | Siapa financier A (hanya commitment bergaram) dan nominal advance A |
| Supplier | Invoice-nya, advance + seal financier (Sign-to-Pay) | Financier lain; riwayat buyer |
| Buyer | Invoice yang ditandatanganinya, surat pengalihan (alamat bayar dan key financier) | Nominal advance; financier lain |
| Financier yang diberi riwayat buyer | Untuk setiap invoice buyer yang dibiayai: N, nominal, jatuh tempo, key financier, status (lunas tepat waktu/terlambat/gagal bayar/berjalan) | Supplier dan isi invoice lama; invoice yang tidak dibiayai lewat JitsuinFi |
| Anggota dana (viewing key akun operasional, HNK-15) | Saldo kas; setiap advance (N, nominal, jatuh tempo); pelunasan masuk; root kewajiban; nominal setiap setoran (tanpa identitas) | Supplier dan buyer; isi invoice; simpanan anggota lain (kecuali lewat nominal setoran) |
| Operator web (hosting frontend) | Permintaan file statis | Key apa pun: tanda tangan dan derivasi key terjadi di browser (`jitsuin-wasm`); CSP melarang request ke pihak ketiga |
| Backend financier | Apa pun yang diproses wallet financier | Key buyer dan supplier |
| Server lightwalletd | IP dan pola sync klien | Isi transaksi shielded |

## Kebocoran yang diketahui dan mitigasinya

| Kebocoran | Mitigasi | Sisa risiko |
|---|---|---|
| Metadata waktu dan jumlah entri di papan | Entri hanya berisi hash tanpa identitas; dinyatakan di deskripsi | Pola aktivitas papan terlihat |
| N yang sama muncul dua kali (pembiayaan ganda atau griefing) | Orang luar tidak bisa memverifikasi tanda tangan tanpa invoice, jadi tidak bisa membedakan penipuan dari griefing | Orang luar tahu "ada konflik", tanpa tahu invoice atau pihaknya |
| Bucket indeks bisa mempersempit identitas | Indeks hanya menampilkan kelas tenor, dan kelas diskon di dalamnya, yang punya minimal k = 5 invoice (`jitsuin_core::index::K`, HNK-08); kelas di bawah k tidak diberi angka; entri `settled` tidak membawa bucket | Kelas tiap entri tetap terbaca pemegang viewing key papan; ambang k hanya untuk agregat. Pasar kecil = anonymity set kecil |
| Entri palsu menggeser indeks | Tiap N dihitung sekali (entri pertama di urutan papan); setiap posting butuh fee | Orang luar tidak bisa mengecek tanda tangan supplier, jadi entri griefing yang lebih dulu menentukan kelas N itu dan N palsu ikut terhitung. Pemegang bundel bisa mengecek dealnya sendiri (`jitsuin verify --bundle`) |
| Tag riwayat pertama bisa dihitung siapa pun yang tahu `identity_pk` buyer | Hanya pihak yang pernah ber-KYC dengan buyer mengetahui `identity_pk`; tag berikutnya butuh sertifikat bertanda tangan | Pemegang `identity_pk` bisa menemukan invoice pertama buyer |
| QR ZIP-321 di tempat umum membuka alamat financier, nominal, dan memo pelunasan | QR hanya ditampilkan di layar buyer untuk dipindai langsung | Kalau QR bocor, alamat dan nominal terlihat |
| IP terlihat oleh lightwalletd | `zcash-devtool` mendukung `--connection tor`; dinyatakan di sini | Default tanpa Tor |
| Input transparan membocorkan pengirim | Wallet menandai `touches_transparent`; semua alur memakai pool shielded | Pengguna yang memaksa tetap bocor |
| Viewing key dana membuka nominal setoran dan advance | Pisahkan akun setoran (viewing key hanya untuk auditor) dari akun operasional | Pemegang viewing key operasional melihat semua nominal |
| Viewing key yang dibagikan tidak bisa dicabut | Akun ZIP-32 terpisah per peran/periode | Pemegang lama tetap bisa melihat data lama |
| Bundel bukti dan bundel verifikasi berisi invoice | Hanya diserahkan ke pihak berwenang (auditor, juri, pengadilan); verifikasi berjalan di browser tanpa upload | Penerima bundel mengetahui deal |

## Serangan dan penanganannya

| Serangan | Penanganan | Sisa risiko |
|---|---|---|
| Supplier membiayakan invoice yang sama dua kali | N dari byte kanonik invoice (DEV-04); financier B berhenti sebelum membayar; bukti tanda tangan ganda (offline, tanpa transaksi) | — (diuji testnet, HNK-07) |
| Signer buyer bernonce acak membuat dua tanda tangan valid | N tidak lagi bergantung pada tanda tangan (DEV-04) | — |
| Invoice fiktif (supplier dan buyer bersekongkol) | Due diligence financier; riwayat buyer (HNK-20); audit sampel | Tidak bisa dideteksi registry |
| Griefing: entri palsu untuk N orang lain | Entri wajib bertanda tangan key supplier dari invoice; entri lain diabaikan | Hanya menambah kebisingan papan |
| Financier membayar sebelum surat pengalihan lengkap | State machine `AwaitAssignment`; seal financier ikut di transaksi advance (Sign-to-Pay) | Ditegakkan software financier, bukan chain |
| Pembiayaan ganda muncul setelah entri terkonfirmasi, atau reorg | Cek papan terakhir sebelum bayar: `DoubleFinanced` berhenti, reorg kembali ke `AwaitConfirmation` | — |
| Buyer mengaku sudah bayar padahal tidak | Tanda tangan financier hanya dibuat watchdog bila pembayaran yang cocok ditambang; klaim berhenti di `Claimed` lalu `Disputed`; klaim palsu bertanda tangan buyer menjadi bukti | — |
| Financier menyangkal pelunasan yang benar | Buyer memegang txid, kuitansi, dan klaimnya | Payment disclosure (ZIP-311) masih draft: buyer belum bisa membuktikan pembayaran shielded ke pihak ketiga |
| Financier lalai mem-posting `settled` | Kewajiban posting jadi syarat allowlist | Buyer tampak gagal bayar sampai sengketa selesai |
| Buyer menyembunyikan gagal bayar (rantai dipotong, dicabangkan, atau mengaku baru) | Rantai riwayat dijangkarkan di papan (DEV-10): ekor tersembunyi, cabang, dan "buyer baru" terdeteksi | — (diuji testnet, HNK-20) |
| Buyer mulai bersih dengan identitas baru | Key identitas diikat KYC oleh financier terdaftar; buyer baru dapat plafon kecil | Penegakan di luar protokol |
| Riwayat palsu lewat financier fiktif (Sybil) | Allowlist financier terdaftar | Allowlist dikelola di luar protokol |
| Griefing ekor rantai riwayat | Entri palsu untuk posisi yang sudah diungkap diabaikan (harus bertanda tangan key supplier di sertifikat) | Pihak yang pernah melihat sertifikat terakhir buyer bisa menghambat pembiayaan berikutnya |
| Root kewajiban palsu dikirim ke alamat dana | Root wajib bertanda tangan key manajer | — (diuji testnet, HNK-15) |
| Manajer dana membiayai invoice fiktif bersama kaki tangannya | Terlihat sebagai gagal bayar; audit sampel | Tidak bisa dibuktikan sebagai penipuan dari chain |
| Tidak ada smart contract: pelunasan bergantung pada buyer membayar ke alamat yang benar | Surat pengalihan bertanda tangan buyer (Pasal 613 KUHPerdata); riwayat buyer | Penegakan lebih lemah dari smart contract |
| Pengalihan confidential (buyer tidak diberi tahu) | Lihat [[Mode Confidential]]: opsi terpisah dengan peringatan | Financier harus percaya supplier meneruskan pembayaran |
| Operator web menyisipkan skrip pencuri key | CSP same-origin; tanpa CDN; key tidak pernah disimpan atau dikirim | Operator yang mengganti file app tetap bisa menyerang; pengguna yang hati-hati bisa membangun app sendiri dari repo |
| Transport lightwalletd putus | Retry untuk `sync`/`enhance`; `pay` tidak pernah di-retry (bisa terkirim dua kali) | — |

## Tambahan untuk arsitektur target (usulan, 2026-10-20)

Baris berikut berlaku begitu usulan di [[FD-00 - Arsitektur Target dan Legenda]] dibangun (relay P-04, snapshot P-06, konsol node P-05/P-11). Tabel di atas tetap menggambarkan kode yang ada sekarang.

| Pihak atau kebocoran | Melihat / risiko | Mitigasi usulan | Sisa risiko |
|---|---|---|---|
| Relay dokumen dan proxy (rewrite Vercel, Railway) | `mailbox_pk`, `mailbox_id`, ciphertext, masa simpan; IP pengirim (`X-Forwarded-For`), kotak surat tujuan, ukuran, waktu. Karena relay juga memindai papan (P-06), pesan supplier ke financier bisa dikorelasikan dengan entri papan berikutnya | Padding, batching, atau jeda; pisahkan layanan snapshot dari kotak surat; baca kotak surat wajib bukti kepemilikan | Isi tidak terbaca, metadata terlihat. Baris "Operator web" di atas (hanya file statis) tidak berlaku lagi untuk relay |
| Penyedia basis data relay (Supabase, D-33) | Semua yang disimpan relay: `mailbox_pk`, `mailbox_id`, ciphertext, ukuran, waktu masuk dan baca; tidak melihat isi. Pihak ketiga kedua selain Railway, bisa dipaksa menyerahkan metadata | Simpan hanya yang perlu; hapus setelah masa simpan; tidak menyimpan IP; kredensial hanya di Railway; koneksi TLS; tidak ada akses dari browser | Metadata terlihat oleh dua penyedia (Railway, Supabase) |
| Email dan username akun (D-34) | Sekarang: siapa pun yang memegang perangkat atau profil browser melihat email dan username di `localStorage` (bukan key). Nanti, setelah akun pindah ke server: Railway dan Supabase menyimpan email; email + `mailbox_id` menautkan orang sungguhan ke semua deal-nya | Email hanya untuk akun dan notifikasi, tidak pernah ditulis ke papan atau memo; simpan terpisah dari kotak surat; email boleh opsional; hapus akun menghapus email | Identitas asli tertaut ke aktivitas di sisi penyedia akun |
| Skrip yang disuntikkan di web app | Begitu `POST /api/mailbox` same-origin ada, CSP `connect-src 'self'` tidak lagi mencegah pencurian: skrip bisa meminta PRF dengan setiap salt peran dan mengirim hasilnya ke kotak surat penyerang | Trusted Types atau render ketat dokumen yang ditempel; penulisan kotak surat hanya sealed box dengan rate limit; SRI atau build yang bisa direproduksi | Baris "Operator web menyisipkan skrip pencuri key" di atas menjadi lebih kuat: pengiriman keluar kini mungkin di dalam CSP |
| Satu kotak surat per peran | `mailbox_pk` buyer sama di semua kartu kontak, jadi rekan yang bersekongkol atau relay bisa menghubungkan semua invoice seorang buyer meskipun `invoice_pk(k)` berbeda | Kotak surat per deal untuk surat ke buyer | Keterhubungan di antara rekan buyer |
| Pemegang sertifikat k | Supplier (untuk entri bertag) dan setiap financier yang diminta riwayat (termasuk yang menolak) bisa menghitung tag invoice berikutnya buyer, memantau, atau mengganggu (`UndisclosedSuccessor`) | Varian wasm yang hanya menerima `history_tag` 32 byte, supaya sertifikat k tetap di financier | Financier yang diminta tetap memegang rantai |
| Dokumen deal di perangkat (HNK-24.T3) | Siapa pun yang memegang perangkat atau profil browser melihat jumlah record dan peran (supplier/buyer), bukan isi atau N: isi AES-256-GCM dengan key dari passkey, nama record HMAC | Key hanya dari PRF passkey peran; diimpor sebagai WebCrypto key non-extractable | Skrip yang berjalan di tab saat sesi terbuka bisa membaca lewat store yang sudah dibuka |
| Pesan relay tanpa autentikasi pengirim | Siapa pun yang tahu `mailbox_id` bisa menyisipkan penawaran, surat palsu (surat JTSA tidak bertanda tangan sampai s2), atau permintaan riwayat palsu. Selama kode salin-tempel (HNK-24.T6): permintaan entri palsu dengan `salt` pilihan penyerang membuat supplier menandatangani entri yang komitmennya tidak dikenali financier; bila entri itu diposting lebih dulu, deal berhenti (`AlreadyFinanced`), tanpa uang hilang | Node menandatangani pesannya dengan `financier_pk`; layar memeriksa terhadap kontak yang diverifikasi di luar sistem; QR hanya untuk surat `Sealed` | Kontak pertama tetap harus diverifikasi di luar sistem |

## Di luar cakupan
- Kekuatan hukum tanda tangan elektronik tidak tersertifikasi (UU ITE, PP 71/2019) dan pengalihan piutang: perlu review ahli hukum.
- Regulasi menghimpun dana anggota (JitsuinFi Vault): diposisikan sebagai demo.
- Keamanan perangkat pengguna (malware di browser atau OS).
