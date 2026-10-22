---
tags: [test, "HNK-17"]
type: test
id: HNK-17
phase: F6
lead: Hans
owners: [Hans]
unit: TODO
integrasi: TODO
e2e: TODO
updated: 2026-10-22
---

# TEST-HNK-17 - QA E2E lintas item

> **Peta link:** [[Testing Hub]] · [[Backlog]] · [[AC-HNK-17 - QA E2E lintas item|AC]] · **Test** · [[ES-HNK-17 - QA E2E lintas item|Exec Summary]]

**Lead:** Hans #hans · **Tim:** Hans #hans 

## 1. Unit
Logika murni, cepat, tanpa DB dan tanpa chain.

| ID | Kasus | Hasil | Tanggal | Bukti |
|---|---|---|---|---|
| U-HNK-17.1 | N/A — item ini logika murni atau dokumen; tidak menyentuh DB/chain (dicatat, bukan dilewati) | TODO | — | — |

## 2. Integrasi
Skrip vs DB/chain sungguhan. Semua artefak memakai prefix `TES-` (invoice, akun, label, order).

| ID | Skenario | Hasil | Tanggal | Bukti (txid/log) |
|---|---|---|---|---|
| I-HNK-17.1 | N/A — item ini adalah eksekusi E2E | TODO | — | — |

**Bukti pembersihan:** sisa artefak off-chain `TES-` = _TODO_ (target **0**). Artefak on-chain tidak bisa dihapus; catat txid-nya di tabel di atas. Data produksi tidak boleh tersentuh.

## 3. E2E

### Hasil E2E testnet lokal, putaran 1 (HNK-17.T1, 2026-10-22)
Dijalankan dari mesin Hans dengan `jitsuin-flow` langsung ke `testnet.zec.rocks` (tanpa node Railway): wallet uji `wallet-a` = financier A, `wallet-b` = supplier dan buyer, key baru per run. Invoice `TES-INV-E2E1-77210`, `terms_hash` = SHA-256 file PDF invoice nyata (`a9924b5f…20db`), surat pengalihan juga PDF (hash dicek di surat). N `9043345834514421fc558049b78441ab01d89a35f8eaae95682bbfc50c83dfc0`.

| Langkah | Hasil | Bukti |
|---|---|---|
| Buyer menandatangani invoice (PDF syarat) | PASS | tanda tangan buyer di bundel |
| Financier A cek papan → `AwaitSupplierSignature`; supplier menandatangani entri untuk komitmen A; A memposting | PASS | entri `62ff4a57068eb71ef50b78a692369d1c6ed1e968c0891e15cc4a8e39fb35a910` (blok 4527411) |
| Konfirmasi → `AwaitAssignment`; segel supplier dan buyer → `Pay` | PASS | — |
| Advance 90 000 zat + segel financier (Sign-to-Pay) → `Done` | PASS | advance `a8130e334146727bd13e548a9cd8972bb8f8efa39600e418cfd6cd7e0634e9a0` |
| Buyer melunasi 100 000 zat lewat permintaan QR (kuitansi + klaim di memo) | PASS | pelunasan `f14249878530eff63ae72a02748ca8ed12b0026a7ed40432743b706f47946517` |
| A melihat pelunasan ter-mine → entri `settled` dua tanda tangan | PASS | settled `0c377146708c758eae644e15e3e7f89c398ed043c6416503579b56c4c8efdbb9` (blok 4527419, tepat waktu) |
| Supplier menawarkan invoice yang sama ke financier B; B cek papan dulu, tidak membayar; bukti tanda tangan ganda dari tawaran | PASS | — |
| `jitsuin verify --ufvk <papan> --bundle --proof` pada papan live | PASS (5 cek, 0 gagal): "DEAL VERIFIED", "DOUBLE FINANCING PROVEN" | keluaran disimpan di scratchpad `e2e/out/verify-output.txt` |

Biaya testnet: sekitar 0,0002 ZEC fee + advance 0,0009 (kembali ke wallet uji) + pelunasan 0,001. Artefak off-chain hanya di scratchpad; tidak ada DB.

### Hasil E2E putaran 2 (HNK-17.T2, 2026-10-22): HNK-08 – HNK-11
Tester: agent (bukan penulis kode item; DEV-35). Papan testnet live, tip 4529049 (snapshot dari node lokal `/node/board`, isi sama dengan node production).

| Item | Langkah | Hasil | Bukti |
|---|---|---|---|
| HNK-08 Indeks suku bunga | `jitsuin index --board <snapshot>` dibandingkan dengan `https://jitsuinfi.vercel.app/rates` (papan live dari node production) | PASS | Keduanya: 23 entri register, 20 invoice, 9 tidak diungkap, 0 invalid; tenor 31-60 hari 5 invoice, median diskon 3-5 %; kelas lain "fewer than 5" (k = 5); halaman membaca papan "live scan up to block 4529049" |
| HNK-09 Verifier CLI | `jitsuin verify --board <snapshot> --bundle` atas bundel deal `TES-INV-FE-53023` dari aplikasi web | PASS | "DEAL VERIFIED", 3/3 cek (tanda tangan buyer dan tiga segel; registrasi sekali, entri `877c2502…5c3f`; settled `327391f2…7716` tepat waktu) |
| HNK-10 Web app per peran | E2E lokal testnet lewat aplikasi React (supplier, buyer, konsol financier, relay, node): `TES-INV-FE-36210`, `-53023`, `-1185` | PASS | Siklus sampai settled dan `/verify` "Bundle is genuine" (rincian di I-HNK-31.3, I-HNK-32.1); bug yang ditemukan dicatat sebagai HNK-32 (8 baris GAGAL AUDIT, T8 devtool menggantung) |
| HNK-11 Halaman orang luar | `https://jitsuinfi.vercel.app/outsider` di production | PASS | Halaman tampil tanpa error console; klaim cocok dengan papan: entri tanpa kelas diungkap tercatat 0/0 (9 dari 23), N tidak bisa dihubungkan ke invoice tanpa invoicenya |

### Bug yang ditemukan dan retest (HNK-17.T3, 2026-10-22)
Sumber: audit flow diagram (langkah 6) dan E2E lokal testnet lewat aplikasi React. Semua dicatat sebagai task [[AC-HNK-32 - Perbaikan hasil audit flow|HNK-32]].

| Bug | Langkah reproduksi | Perbaikan | Retest | Hasil |
|---|---|---|---|---|
| Buyer bisa menyegel surat tanpa cek PDF (BL-D24-06) | Langkah 3 buyer: tempel kode surat dan segel supplier apa saja, tekan "Seal as buyer": segel dibuat tanpa cek | frontend PR #48 (HNK-32.T1) | E2E `TES-INV-FE-11588`: segel hanya aktif setelah "Check letter" lolos; unit `tests/buyer-letter.test.ts` | PASS |
| Surat tempelan menghasilkan QR ke alamat lain (BL-D25-01) | Langkah 5: ganti kode surat dengan surat lain, tekan "Show payment QR": QR muncul | frontend PR #49 (HNK-32.T2) | E2E (5 run): "this is not the letter you sealed for this invoice", tanpa QR | PASS |
| Tombol QR aktif sebelum s2 (BL-S02-02) | Buka langkah 5 sebelum advance dibayar: tombol aktif | frontend PR #55 | E2E 2026-10-22 15:35 UTC: mati sebelum s2, aktif setelah s2 | PASS |
| Alasan berhenti tampil sebagai dump Debug (BL-D23-08, BL-D27-01) | Tawarkan invoice yang sudah dibiayai financier lain: konsol "Stopped: AlreadyFinanced { winner: BoardRecord … }" | node PR #35, frontend PR #50 (HNK-32.T3) | unit node `a_stopped_deal_shows_a_code_and_the_entry_that_came_first`, frontend `stopReason` | PASS (unit; deal berhenti nyata belum) |
| Konsol tanpa hitungan konfirmasi (BL-D23-14) | Setelah entri diposting: hanya "waiting for its confirmations" | node PR #36, frontend PR #51 (HNK-32.T4) | E2E `TES-INV-FE-1185`: "Entry posted: 0 of 1 confirmations" | PASS |
| Bukti hanya bisa disalin (BL-D25-04, BL-D27-04) | Deal Overdue atau 重: tidak ada unduhan | frontend PR #52 (HNK-32.T5) | E2E Overdue `TES-INV-OD-27953`: kartu "Repayment overdue", file diunduh, `jitsuin verify --evidence` HOLDS (Overdue); kartu 重 belum dengan deal nyata | PASS (Overdue) |
| `zcash-devtool enhance` menggantung, semua deal berhenti (HNK-32.T8) | lightwalletd tidak menjawab saat pindai papan: proses 5+ menit, kunci rantai node tertahan | zcash PR #29, node PR #39 | unit `a_read_that_never_answers_is_stopped` | PASS (unit) |
| Riwayat dicek ulang setelah crash (BL-D26-06) | Crash setelah tag disimpan di flow, sebelum meta: putaran berikut cek lagi | node PR #37 | unit: tag bertahan setelah muat ulang | PASS (unit) |
| Galat jaringan node tampil mentah di konsol | Pembayaran saat lightwalletd gagal: "board: lightwalletd: error sending request …" | frontend PR #52 (`explain`) | unit `tests/explain.test.ts` | PASS (unit) |
| Menit GitHub Actions habis | Railway menjeda deploy: job deploy menunggu sampai 5 jam di runner, diulang tiap jam | node PR #40 (gagal cepat, ulang tiap 6 jam) | CI #40 lulus | PASS |

### Runbook E2E testnet (HNK-17.T4, disiapkan 2026-10-22)
Dijalankan begitu Railway pulih. Semua invoice memakai prefix `TES-`. Isi kolom "Hasil aktual" dengan txid atau tangkapan layar.

**Prasyarat** (cek berurutan; berhenti kalau satu gagal):
1. `GET https://financier-node-production.up.railway.app/node/console/mandate` menjawab 401/403, bukan 404. Artinya node = main terbaru: `deals.rs`, riwayat buyer, mandat privat.
2. `GET https://relay-production-27dc.up.railway.app/api/health` → 200.
3. Production Vercel menyajikan main sesudah #42–#44: header app menampilkan "Testnet", konsol punya isian "Grace after due date".
4. Saldo wallet financier node minimal 0,002 ZEC testnet: 2 entri × 10.000 zat, advance uji 50.000 zat, fee, cadangan. Isi dari wallet uji `~/.hanko-tes/testnet/wallet-a` ke alamat di `/node/info`; seed tidak pernah keluar dari folder itu.
5. Konsol financier sudah di-pairing dengan passkey operator. Kalau undangan belum ada, jalankan skrip undangan (`pairing.json` lewat SFTP Railway).
6. Dua profil browser terpisah: supplier dan buyer, masing-masing dengan passkey sendiri. Kalau authenticator tidak punya PRF, pakai "Use test data" dengan dua secret berbeda.
7. Wallet buyer testnet (Zodl atau `zcash-devtool`, wallet-b) berisi ≥ 0,001 ZEC untuk membayar QR.

| Langkah | BF | Aksi | Hasil diharapkan | Hasil aktual | Status |
|---|---|---|---|---|---|
| 1 | BF-01 | Supplier, buyer, financier masuk; tukar kartu kontak, cocokkan sidik jari | Kotak surat "ready" di ketiga layar; kotak masuk terbuka sendiri | — | TODO |
| 2 | BF-02 | Supplier membuat `TES-INV-E2E1` (jatuh tempo +3 hari), kirim ke buyer; buyer cek PDF dan tanda tangan | Supplier menerima tanda tangan lewat kotak surat; status "signed, sent" | — | TODO |
| 3 | BF-03 | Supplier memilih financier di direktori (atau kartu), kirim penawaran dengan alamat buyer | Konsol: penawaran 認, cap 適/外/待 per aturan, sisa hari kedaluwarsa | — | TODO |
| 4 | BF-04 | Set mandat privat "Buyer history 0" + KYC mati, lalu Accept. Ulangi dengan riwayat aktif di deal kedua | Tanpa riwayat: pembuka komitmen langsung. Dengan riwayat: buyer menerima "History request", node menulis hasil cek di 案件 | — | TODO |
| 5 | BF-05 | Supplier "Use this entry request" lalu "Sign entry" | Entri otomatis ke node; 案件: 署 lalu 登; txid entri di papan (`/verify` papan live) | txid entri: — | TODO |
| 6 | BF-06 | Tunggu konfirmasi; supplier "Keep the letter" lalu segel; buyer "Keep the letter", "Keep the seal" lalu segel | Surat PDF di kedua layar; hash PDF = `terms_hash`; 案件 menjadi Pay | — | TODO |
| 7 | BF-07 | Konsol: "Approve with passkey: pay …" | Advance terkirim dengan segel financier; supplier menerima "Advance paid" dan txid; buyer menerima segel s2; 案件 金 lalu 済 | txid advance: — | TODO |
| 8 | BF-08 | Buyer step 5: QR muncul hanya setelah surat lengkap; bayar dari wallet-b | Node: repayment Settled, entri settled diposting; supplier dan buyer menerima bundel; status "settled on time" | txid pelunasan: —, settled: — | TODO |
| 9 | BF-09 | Deal kedua: jatuh tempo lewat tanpa bayar (atau bayar sebagian) | 案件: "Repayment overdue/claimed" dan tombol salin bukti JTSE | — | TODO |
| 10 | BF-10 | Supplier menawarkan `TES-INV-E2E1` ke financier kedua (node demo atau CLI) | Financier kedua: deal berhenti 重, Exhibit A bisa disalin dan lolos di `/verify` | — | TODO |
| 11 | BF-11 | Orang luar membuka `/verify` dan "What outsiders see" dengan bundel dan Exhibit A | Verdict 認/重 tanpa membuka pihak atau nominal | — | TODO |
| 12 | BF-12 | Dana: catat setoran anggota, permintaan tarik, tutup periode dengan passkey | Anggota menerima kuitansi, jalur 認, pembayaran; `jitsuin fund --path` = INCLUDED | — | TODO |

Setelah selesai: audit 32 baris BL berstatus AUDIT (`check-backlogs.py --strict`), lalu catat txid di README zcash (W-09).

- [ ] Jalankan panduan E2E HNK-01 – HNK-07 (putaran 1).
- [ ] Jalankan panduan E2E HNK-08 – HNK-11 (putaran 2).
- [ ] Retest semua bug yang sudah diperbaiki.
