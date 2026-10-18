---
tags: [architecture, decisions]
---

# Decision Log

**Bagian dari:** [[07 - Architecture]] · Kembali: [[START-HERE]] · Terkait: [[Backlog]] (Log Deviasi) · [[Rencana Fase]]

Keputusan user bersifat final. Perubahan keputusan dicatat sebagai baris baru (bukan mengedit baris lama).

| ID | Tanggal | Keputusan | Alasan |
|---|---|---|---|
| D-01 | 2026-10-16 | Fokus pada piutang/invoice dagang saja | Hanya piutang yang jaminan anti-gandanya utuh tanpa lembaga resmi |
| D-02 | 2026-10-16 | Nama proyek **Hanko** (sebelumnya Faktur Tunggal); versi gabungan **Hanko Vault** | Arti "stempel tanda tangan" pas dengan desain; tagline nullifier |
| D-03 | 2026-10-16 | Kode AVAL tidak dipakai; repo baru; AVAL diungkapkan di deskripsi; email ke organizer | Aturan "existing products are not" dan Originality |
| D-04 | 2026-10-16 | Mainnet dengan crate stabil; bukan testnet NU7, bukan WebZjs | NU7 hanya testnet sampai deadline; WebZjs tidak mendukung Ironwood |
| D-05 | 2026-10-16 | Tanpa TEE, cross-chain, ZSA, smart contract | Biaya, risiko kebocoran, dan ZSA belum di mainnet |
| D-06 | 2026-10-16 | Track **Private Markets** (private credit) | Tesis organizer "price public, participants private" + indeks suku bunga publik |
| D-07 | 2026-10-16 | Hanko Vault hanya stretch (HNK-15) | Scope; hukum lebih berat |
| D-08 | 2026-10-16 | Script vault versi Python (`scripts/*.py`); `.ps1` disimpan di `scripts/windows/` | PowerShell tidak terpasang di Mac ini |
| D-09 | 2026-10-16 | Ide affiliate diserahkan ke teman sebagai team terpisah | Satu submission per akun dan per team |
| D-10 | 2026-10-16 | Versi di-pin untuk mainnet: Rust 1.99.1; `zcash_client_backend =0.24.0`, `zcash_client_sqlite =0.22.0`, `pczt =0.9.3`, `zcash_protocol =0.10.6`, `ed25519-dalek` 2.2.x (bukan 3.0.0), `blake2b_simd =1.0.5` | SPK-01: build hijau dan mengenal NU6.3/Ironwood; 3.0.0 bentrok `sha2` |
| D-11 | _Usulan, menunggu user_ | Publikasikan **UFVK** akun papan registry (bukan UIVK) | SPK-05: `zcash-devtool init-fvk` hanya menerima UFVK; akun papan hanya menerima dana, jadi UFVK tidak membuka hal sensitif |
| D-12 | 2026-10-16 | Endpoint lightwalletd utama `zec.rocks:443`; cadangan `na`/`eu`/`ap`/`sa.zec.rocks` | SPK-02: semua sehat dan tersinkron dengan Blockchair |
| D-13 | 2026-10-16 | **Opsi B (hybrid):** development dan uji integrasi di **testnet** sampai menjelang submit; mainnet hanya untuk demo akhir kalau ZEC tersedia. Satu set crate **pre-release** yang di-pin (`=0.25.0-pre.2` / `=0.23.0-pre.2` / `=0.10.0-pre.2` / `=0.11.0-pre.1`) dipakai untuk kedua jaringan | Keputusan user; SPK-19: crate stabil tidak bisa bertransaksi di testnet NU7, crate pre-release bisa di keduanya |
| D-14 | 2026-10-16 | Repo GitHub dibuat oleh user nanti; sementara **repo lokal** `zkSNARK/hanko/` dengan commit lokal, tanpa remote dan tanpa push | Keputusan user; sesuai workflow langkah 5 |
| D-15 | 2026-10-16 | **Zodl opsional.** Semua peran memakai wallet CLI `zcash-devtool` selama development | Keputusan user; wallet web (WebZjs) tidak mendukung Ironwood |
| D-16 | 2026-10-17 | Nama proyek diganti **JitsuinFi** (menggantikan D-02 Hanko); org GitHub `jitsuinfi`; repo lokal `zkSNARK/jitsuinfi-zcash/`; crate `jitsuin-core`; magic `JTSI`/`JTS1`; personalisasi nullifier `JitsuinNullifier`. ID backlog `HNK-xx` tetap. Catatan spike dan baris decision log lama tidak diubah (sejarah) | Org `hanko` di GitHub sudah dipakai; *jitsuin* = stempel terdaftar, cocok dengan registry + keunikan + pengakuan buyer |
| D-17 | 2026-10-17 | Repo modular di org GitHub `JitsuinFi`, semua **private** sampai menjelang submit: `jitsuinfi-zcash` (infra Zcash: `jitsuin-core`, `jitsuin-wallet`), `jitsuinfi-vault` (vault ini), lalu `jitsuinfi-backend` (deploy Railway) dan `jitsuinfi-frontend` (deploy Vercel) saat kodenya mulai. Kalau FE+BE jadi monorepo, namanya `JitsuinFi`. Repo lokal: `zkSNARK/jitsuinfi-zcash/` | Keputusan user; aturan ZECATHON membolehkan repo dibuka publik pada 28 Okt |
| D-18 | _Usulan, menunggu user_ | Entri papan `settled` (HNK-06.T4): field N diisi `settled_tag = BLAKE2b-256(N ‖ "settled")`, field commitment diisi **nol**, bucket disalin dari entri register, dan field tanda tangan diisi **financier** (key jangka panjang, pembuka commitment), bukan supplier. Diverifikasi dengan `financier_pk` dari surat pengalihan | Financier yang menerima pelunasan dan mem-posting entri; supplier tidak terlibat saat buyer membayar. Commitment entri register bersifat publik, jadi menyalinnya akan menautkan kedua entri. Alternatif: tanda tangan buyer (`buyer_pk` ada di invoice, jadi semua pemegang invoice bisa memverifikasi), tapi buyer harus menandatangani entri kedua |
| D-19 | 2026-10-17 | Menggantikan usulan D-18: entri `settled` ditandatangani **buyer dan financier** (dua tanda tangan). Buyer menyatakan sudah membayar, financier menyatakan sudah menerima; klaim sepihak bukan lunas | Keputusan user ("gas keduanya"); bukti terkuat dan selaras dengan pola multi-approver SignBaliola |
| D-20 | 2026-10-17 | **Tanpa commitment fee buyer.** Komitmen buyer = seal buyer di surat pengalihan. Riwayat pembayaran buyer menjadi **standar minimal** sebelum financier membiayai (HNK-20) | Keputusan user; deposit tidak bisa dikunci di pool shielded tanpa smart contract, versi transparan membocorkan nominal |
| D-21 | 2026-10-17 | **Adopsi konsep SignBaliola** sebagai *Jitsuin Seal*: tanda tangan multi-pihak berurutan per dokumen, dokumen tertahan sampai lengkap, ditambah Sign-to-Pay dan seal privat. Konsep saja, tanpa kode SignBaliola. N (DEV-04) menjadi id dokumen untuk semua seal. Lihat [[Desain Jitsuin Seal]] | Keputusan user ("adopsi SignBaliola, lebih matang, commercial ready, lebih menjual"); kode SignBaliola milik Baliola dan aturan Originality |
| D-22 | 2026-10-17 | Semua task tanda tangan dan advance dipegang **Hans**, termasuk surat pengalihan (HNK-06.T1, sebelumnya Dex) dan item baru HNK-19, HNK-20 | Keputusan user ("bagian ttd advance masukin ke saya semua aja") |
| D-23 | 2026-10-17 | Verifikasi ganda pelunasan memakai **watchdog deterministik** (akses baca lewat viewing key; tanda tangan financier hanya dibuat bila pembayaran yang cocok ditambang). **AI agent tidak menjadi hakim**; AI hanya asisten **lokal opsional** untuk menjelaskan status dan menyusun draf surat sengketa, tanpa seed, spending key, atau viewing key, dan tanpa provider cloud | Keputusan user ("gas"); kebenaran pelunasan ditentukan tanda tangan + chain, AI cloud dengan viewing key = kebocoran |
| D-24 | 2026-10-17 | **Go untuk HNK-15 (JitsuinFi Vault, stretch).** Hans mengerjakan T2 (uji solvabilitas lewat viewing key akun operasional + memo root kewajiban); T1 Merkle sum tree tetap Dex, T3 halaman anggota tetap Dave | Keputusan user ("Gas HNK-15"); bagian inti Hans F3 (HNK-05, HNK-06, HNK-07) sudah selesai sebelum batas 23 Okt |
| D-25 | 2026-10-18 | Hans (dibantu agent) mem-backup sementara task Dave (owner dan label tetap Dave) yang tidak butuh manusia: FE (scaffold, layar), dokumen, spesifikasi, naskah demo. **Semua lokal**: repo `jitsuinfi-frontend` dibuat lokal tanpa remote, tidak ada push sampai user menyetujui. Task yang butuh manusia (rekrut uji pengguna HNK-13, rekam video HNK-14.T1) tetap Dave; disiapkan naskahnya | Keputusan user ("kerjakan punyaku dan punya Dave … stay local semua dulu") |
