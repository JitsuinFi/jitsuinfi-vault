---
tags: [hub, backlog]
---

# Backlog

**Bagian dari:** [[03 - Backlog]] · Kembali: [[START-HERE]] · Terkait: [[Rencana Fase]] · [[Workflow Development]] · [[Dashboard]]

Item dengan **ID stabil** `HNK-xx`, dipecah menjadi task `HNK-xx.Tn` dengan label owner. Setiap item punya tiga artefak: AC, Test, dan Exec Summary (pola Hub + satu file per item). Urutan fase = urutan dependency.

## Aturan
- Status item dibaca dari file AC dan ES (frontmatter), bukan ditulis ulang di sini.
- **Lead** item menulis Exec Summary dan memastikan AC terisi; **owner task** mengerjakan task-nya dan mengisi bukti.
- **Deviasi dari keputusan ditulis eksplisit di Log Deviasi** di bawah, dengan ID `DEV-xx`. Keputusan user final; tidak ada perubahan diam-diam.
- Pemindahan task antar orang juga dicatat sebagai `DEV-xx`.
- Item baru: `python3 scripts/new-item.py --kind item --id HNK-xx --title "..." --phase Fx`, lalu tambahkan baris dan task-nya di sini.

## Tim dan pembagian kerja

Target pembagian: **Hans 40% · Dex 30% · Dave 30%**. Hans wajib memegang seluruh integrasi Zcash serta bagian backend dan FE yang krusial.

| Orang | Label | Tanggung jawab |
|---|---|---|
| **Hans** | #hans | Semua integrasi Zcash (wallet, memo, viewing key, papan, ZIP-321, transaksi), core kripto, backend krusial, dan bagian FE krusial (tanda tangan buyer, integrasi layar financier, verifikasi bukti). Akun pendaftar: submit final dan email ke organizer. |
| **Dex** | #dex | Backend pendukung (API, CLI, surat pengalihan, indeks), verifier CLI dan distribusinya, CI/quality gate, uji integrasi, DevOps Railway, repo dan lisensi. |
| **Dave** | #dave | FE non-krusial (scaffold, layout, halaman indeks, halaman orang luar), dokumentasi dan spesifikasi, threat model, QA E2E independen, uji pengguna, video, dan materi pitch. |

### Beban kerja (estimasi jam, spike + item inti, tanpa stretch HNK-15)

| Orang | Jam | Porsi | Target |
|---|---|---|---|
| Hans #hans | 62 | 41% | 40% |
| Dex #dex | 45 | 29% | 30% |
| Dave #dave | 46 | 30% | 30% |
| **Total** | **153** | 100% | 100% |

**Revisi 2026-10-17 (D-22):** HNK-19 (13 jam) dan HNK-20 (5 jam) ke Hans; HNK-06.T1 (2 jam) pindah dari Dex ke Hans. HNK-02.T3 (1 jam) tetap Dex sampai perbandingan DEV-09 selesai; porsi diperbarui setelahnya.

| Orang | Jam | Porsi | Target awal |
|---|---|---|---|
| Hans #hans | 84 | 48,6% | 40% |
| Dex #dex | 43 | 24,9% | 30% |
| Dave #dave | 46 | 26,6% | 30% |
| **Total** | **173** | 100% | 100% |

**Revisi 2026-10-18 (D-25, DEV-11):** task Dave tetap milik Dave (label `#dave`). 23 jam di antaranya dikerjakan sementara oleh Hans sebagai backup (label "backup sementara: Hans"); porsi di atas tetap dihitung per owner. Dave me-review hasil backup.

HNK-20 naik dari 5 ke 7 jam (DEV-10). HNK-10.T7 (`jitsuin-wasm`, 3 jam) ditambahkan untuk Hans atas persetujuan user 2026-10-17 ("lanjut jitsuin-wasm"); push disetujui 2026-10-17 ("Gas push").

Porsi Hans naik di atas 40% karena keputusan user D-22.

Stretch HNK-15 (hanya kalau go): Hans 3 jam, Dex 3 jam, Dave 2 jam.
Estimasi kasar; diperbarui di Exec Summary dengan jam aktual.

## Daftar item

| ID | Item | Fase | Lead | Tim | Dependency | AC | Test | ES |
|---|---|---|---|---|---|---|---|---|
| HNK-01 | Format invoice kanonik dan tanda tangan buyer | F1 | Hans #hans | #hans #dex #dave | SPK-06 | [[AC-HNK-01 - Format invoice kanonik dan tanda tangan buyer\|AC]] | [[TEST-HNK-01 - Format invoice kanonik dan tanda tangan buyer\|Test]] | [[ES-HNK-01 - Format invoice kanonik dan tanda tangan buyer\|ES]] |
| HNK-02 | Nullifier dan entri papan registry | F1 | Hans #hans | #hans #dex | HNK-01 | [[AC-HNK-02 - Nullifier dan entri papan registry\|AC]] | [[TEST-HNK-02 - Nullifier dan entri papan registry\|Test]] | [[ES-HNK-02 - Nullifier dan entri papan registry\|ES]] |
| HNK-03 | Wallet backend kirim dan terima memo di mainnet | F2 | Hans #hans | #hans #dex | SPK-01, SPK-02, SPK-03, SPK-10 | [[AC-HNK-03 - Wallet backend kirim dan terima memo di mainnet\|AC]] | [[TEST-HNK-03 - Wallet backend kirim dan terima memo di mainnet\|Test]] | [[ES-HNK-03 - Wallet backend kirim dan terima memo di mainnet\|ES]] |
| HNK-04 | Pemindai papan registry | F2 | Hans #hans | #hans #dex | HNK-02, HNK-03, SPK-05, SPK-08 | [[AC-HNK-04 - Pemindai papan registry\|AC]] | [[TEST-HNK-04 - Pemindai papan registry\|Test]] | [[ES-HNK-04 - Pemindai papan registry\|ES]] |
| HNK-05 | Alur financier cek registrasi bayar di muka | F3 | Hans #hans | #hans #dex #dave | HNK-04 | [[AC-HNK-05 - Alur financier cek registrasi bayar di muka\|AC]] | [[TEST-HNK-05 - Alur financier cek registrasi bayar di muka\|Test]] | [[ES-HNK-05 - Alur financier cek registrasi bayar di muka\|ES]] |
| HNK-06 | Pengalihan hak tagih dan pelunasan | F3 | Hans #hans | #dex #hans #dave | HNK-05 | [[AC-HNK-06 - Pengalihan hak tagih dan pelunasan\|AC]] | [[TEST-HNK-06 - Pengalihan hak tagih dan pelunasan\|Test]] | [[ES-HNK-06 - Pengalihan hak tagih dan pelunasan\|ES]] |
| HNK-07 | Deteksi pembiayaan ganda dan bukti tanda tangan ganda | F3 | Hans #hans | #hans #dave #dex | HNK-05 | [[AC-HNK-07 - Deteksi pembiayaan ganda dan bukti tanda tangan ganda\|AC]] | [[TEST-HNK-07 - Deteksi pembiayaan ganda dan bukti tanda tangan ganda\|Test]] | [[ES-HNK-07 - Deteksi pembiayaan ganda dan bukti tanda tangan ganda\|ES]] |
| HNK-08 | Indeks suku bunga publik | F4 | Dex #dex | #dex #dave | HNK-04 | [[AC-HNK-08 - Indeks suku bunga publik\|AC]] | [[TEST-HNK-08 - Indeks suku bunga publik\|Test]] | [[ES-HNK-08 - Indeks suku bunga publik\|ES]] |
| HNK-09 | Verifier CLI hanko verify | F4 | Dex #dex | #dex #dave | HNK-04, HNK-07, SPK-11 | [[AC-HNK-09 - Verifier CLI hanko verify\|AC]] | [[TEST-HNK-09 - Verifier CLI hanko verify\|Test]] | [[ES-HNK-09 - Verifier CLI hanko verify\|ES]] |
| HNK-10 | Web app per peran | F5 | Dave #dave | #dave #hans #dex | HNK-05, HNK-06, SPK-09 | [[AC-HNK-10 - Web app per peran\|AC]] | [[TEST-HNK-10 - Web app per peran\|Test]] | [[ES-HNK-10 - Web app per peran\|ES]] |
| HNK-11 | Threat model dan halaman orang luar | F5 | Dave #dave | #dave #hans | HNK-07 | [[AC-HNK-11 - Threat model dan halaman orang luar\|AC]] | [[TEST-HNK-11 - Threat model dan halaman orang luar\|Test]] | [[ES-HNK-11 - Threat model dan halaman orang luar\|ES]] |
| HNK-12 | Spesifikasi gaya ZIP Shielded Receivable Registry | F4 | Dave #dave | #dave #dex #hans | HNK-02, HNK-07 | [[AC-HNK-12 - Spesifikasi gaya ZIP Shielded Receivable Registry\|AC]] | [[TEST-HNK-12 - Spesifikasi gaya ZIP Shielded Receivable Registry\|Test]] | [[ES-HNK-12 - Spesifikasi gaya ZIP Shielded Receivable Registry\|ES]] |
| HNK-13 | Uji dengan pengguna sungguhan | F6 | Dave #dave | #dave #hans | HNK-05, HNK-06, HNK-07, HNK-10 | [[AC-HNK-13 - Uji dengan pengguna sungguhan\|AC]] | [[TEST-HNK-13 - Uji dengan pengguna sungguhan\|Test]] | [[ES-HNK-13 - Uji dengan pengguna sungguhan\|ES]] |
| HNK-14 | Submission video deskripsi dan demo URL | F6 | Dave #dave | #dave #dex #hans | HNK-13, SPK-12, SPK-15 | [[AC-HNK-14 - Submission video deskripsi dan demo URL\|AC]] | [[TEST-HNK-14 - Submission video deskripsi dan demo URL\|Test]] | [[ES-HNK-14 - Submission video deskripsi dan demo URL\|ES]] |
| HNK-15 | Stretch JitsuinFi Vault | F7 | Hans #hans | #dex #hans #dave | HNK-07, SPK-05 | [[AC-HNK-15 - Stretch JitsuinFi Vault\|AC]] | [[TEST-HNK-15 - Stretch JitsuinFi Vault\|Test]] | [[ES-HNK-15 - Stretch JitsuinFi Vault\|ES]] |
| HNK-16 | CI dan quality gate | F1 | Dex #dex | #dex | SPK-01, SPK-14 | [[AC-HNK-16 - CI dan quality gate\|AC]] | [[TEST-HNK-16 - CI dan quality gate\|Test]] | [[ES-HNK-16 - CI dan quality gate\|ES]] |
| HNK-17 | QA E2E lintas item | F6 | Dave #dave | #dave | HNK-05 – HNK-11 | [[AC-HNK-17 - QA E2E lintas item\|AC]] | [[TEST-HNK-17 - QA E2E lintas item\|Test]] | [[ES-HNK-17 - QA E2E lintas item\|ES]] |
| HNK-18 | Materi pitch dan visual | F5 | Dave #dave | #dave | HNK-07, HNK-11 | [[AC-HNK-18 - Materi pitch dan visual\|AC]] | [[TEST-HNK-18 - Materi pitch dan visual\|Test]] | [[ES-HNK-18 - Materi pitch dan visual\|ES]] |
| HNK-19 | Jitsuin Seal tanda tangan berantai dan Sign-to-Pay | F3 | Hans #hans | #hans | HNK-05, HNK-06 | [[AC-HNK-19 - Jitsuin Seal tanda tangan berantai dan Sign-to-Pay\|AC]] | [[TEST-HNK-19 - Jitsuin Seal tanda tangan berantai dan Sign-to-Pay\|Test]] | [[ES-HNK-19 - Jitsuin Seal tanda tangan berantai dan Sign-to-Pay\|ES]] |
| HNK-20 | Riwayat pembayaran buyer standar minimal | F3 | Hans #hans | #hans | HNK-19 | [[AC-HNK-20 - Riwayat pembayaran buyer standar minimal\|AC]] | [[TEST-HNK-20 - Riwayat pembayaran buyer standar minimal\|Test]] | [[ES-HNK-20 - Riwayat pembayaran buyer standar minimal\|ES]] |

## Spike (F0)

| ID | Spike | Owner | Jam | Kritis |
|---|---|---|---|---|
| SPK-01 | [[SPK-01 - Toolchain Rust dan crate Zcash stabil\|Toolchain Rust dan crate Zcash stabil]] | Dex #dex | 2 | Ya |
| SPK-02 | [[SPK-02 - Endpoint lightwalletd mainnet\|Endpoint lightwalletd mainnet]] | Dex #dex | 1 | Ya |
| SPK-03 | [[SPK-03 - Kirim dan terima shielded dengan memo di mainnet\|Kirim dan terima shielded dengan memo di mainnet]] | Hans #hans | 3 | Ya |
| SPK-04 | [[SPK-04 - Pembayaran Zodl lewat URI ZIP-321 dengan memo\|Pembayaran Zodl lewat URI ZIP-321 dengan memo]] | Hans #hans | 1 | — |
| SPK-05 | [[SPK-05 - Pemindaian watch-only dengan viewing key\|Pemindaian watch-only dengan viewing key]] | Hans #hans | 2 | Ya |
| SPK-06 | [[SPK-06 - Kripto inti Ed25519 hash dan layout memo\|Kripto inti Ed25519 hash dan layout memo]] | Hans #hans | 2 | Ya |
| SPK-07 | [[SPK-07 - Transaksi multi-output dan fee ZIP-317\|Transaksi multi-output dan fee ZIP-317]] | Hans #hans | 1 | — |
| SPK-08 | [[SPK-08 - Latensi konfirmasi dan urutan entri\|Latensi konfirmasi dan urutan entri]] | Hans #hans | 1 | — |
| SPK-09 | [[SPK-09 - Hosting Railway dan hardening web\|Hosting Railway dan hardening web]] | Dex #dex | 2 | — |
| SPK-10 | [[SPK-10 - Dana mainnet dan keamanan seed\|Dana mainnet dan keamanan seed]] | Hans #hans | 1 | — |
| SPK-11 | [[SPK-11 - Distribusi verifier CLI di mesin bersih\|Distribusi verifier CLI di mesin bersih]] | Dex #dex | 1 | — |
| SPK-12 | [[SPK-12 - Kepastian aturan dan form ZECATHON\|Kepastian aturan dan form ZECATHON]] | Dave #dave | 1 | — |
| SPK-13 | [[SPK-13 - Dampak NU7 dan versi crate\|Dampak NU7 dan versi crate]] | Dex #dex | 1 | — |
| SPK-14 | [[SPK-14 - Repo baru lisensi dan originalitas\|Repo baru lisensi dan originalitas]] | Dex #dex | 1 | — |
| SPK-15 | [[SPK-15 - Tooling produksi video\|Tooling produksi video]] | Dave #dave | 1 | — |
| SPK-16 | [[SPK-16 - Block explorer untuk demo\|Block explorer untuk demo]] | Dave #dave | 1 | — |
| SPK-17 | [[SPK-17 - Toolchain frontend dan aset offline\|Toolchain frontend dan aset offline]] | Dave #dave | 1 | — |
| SPK-18 | [[SPK-18 - Akses tim dan kesamaan environment\|Akses tim dan kesamaan environment]] | Dex #dex | 1 | — |
| SPK-19 | [[SPK-19 - Testnet NU7 untuk development\|Testnet NU7 untuk development]] | Hans #hans | 2 | — |

## Rincian task per item

### Fase F1

**HNK-01 — Format invoice kanonik dan tanda tangan buyer** · Lead Hans #hans · [[AC-HNK-01 - Format invoice kanonik dan tanda tangan buyer|AC]]

| Task | Deskripsi | Owner | Jam | Status |
|---|---|---|---|---|
| HNK-01.T1 | Desain struct invoice dan encoding kanonik deterministik | Hans #hans | 3 | DONE (`c0d6981`) |
| HNK-01.T2 | Implementasi sign/verify Ed25519 (core) | Hans #hans | 2 | DONE (`c0d6981`) |
| HNK-01.T3 | Unit test + file test vector | Dex #dex | 2 | TODO |
| HNK-01.T4 | Sinkronkan [[Format Data]] dengan implementasi | Dave #dave (backup sementara: Hans #hans, DEV-11) | 1 | DONE: [[Format Data]] disinkronkan per item (HNK-01 – HNK-20) |

**HNK-02 — Nullifier dan entri papan registry** · Lead Hans #hans · [[AC-HNK-02 - Nullifier dan entri papan registry|AC]]

| Task | Deskripsi | Owner | Jam | Status |
|---|---|---|---|---|
| HNK-02.T1 | Nullifier BLAKE2b-256 berpersonalisasi dari byte kanonik invoice (DEV-04) | Hans #hans | 1 | DONE (`40d7656`) |
| HNK-02.T2 | Encode/decode entri papan + tanda tangan supplier (key sementara) | Hans #hans | 3 | DONE (`c0d6981`) |
| HNK-02.T3 | Commitment financier + manajemen salt | Dex #dex | 1 | TODO — dikerjakan Dex secara independen, lalu dibandingkan dengan `6b5c343` (DEV-09) |
| HNK-02.T4 | Unit test: roundtrip, ukuran ≤ 512, entri invalid | Dex #dex | 2 | TODO |

**HNK-16 — CI dan quality gate** · Lead Dex #dex · [[AC-HNK-16 - CI dan quality gate|AC]]

| Task | Deskripsi | Owner | Jam | Status |
|---|---|---|---|---|
| HNK-16.T1 | Script cek lokal satu perintah | Dex #dex | 1 | TODO |
| HNK-16.T2 | Workflow GitHub Actions | Dex #dex | 2 | TODO |
| HNK-16.T3 | Secret scanning (gitleaks) + `.gitignore` seed/key/.env/DB wallet | Dex #dex | 1 | TODO |

### Fase F2

**HNK-03 — Wallet backend kirim dan terima memo di mainnet** · Lead Hans #hans · [[AC-HNK-03 - Wallet backend kirim dan terima memo di mainnet|AC]]

| Task | Deskripsi | Owner | Jam | Status |
|---|---|---|---|---|
| HNK-03.T1 | Inisialisasi wallet dan sync via lightwalletd (Zcash) | Hans #hans | 4 | DONE (`7fd8202`) |
| HNK-03.T2 | Kirim output shielded Ironwood dengan memo biner (Zcash) | Hans #hans | 4 | DONE (`7fd8202`) |
| HNK-03.T3 | Terima dan dekode memo masuk (Zcash) | Hans #hans | 2 | DONE (`7fd8202`) |
| HNK-03.T4 | Tolak input transparan, catat fee ZIP-317 (Zcash) | Hans #hans | 1 | DONE (`7fd8202`) |
| HNK-03.T5 | Script uji integrasi `TES-` + bukti pembersihan DB uji | Dex #dex | 2 | TODO |

**HNK-04 — Pemindai papan registry** · Lead Hans #hans · [[AC-HNK-04 - Pemindai papan registry|AC]]

| Task | Deskripsi | Owner | Jam | Status |
|---|---|---|---|---|
| HNK-04.T1 | Impor viewing key watch-only dan scan papan (Zcash) | Hans #hans | 3 | DONE (`ef55987`) |
| HNK-04.T2 | Urutan entri, deteksi N ganda, filter entri invalid | Hans #hans | 2 | DONE (`ef55987`) |
| HNK-04.T3 | Perintah CLI `jitsuin board scan` + format tabel | Dex #dex | 2 | TODO |
| HNK-04.T4 | Uji integrasi 3 entri (1 invalid) | Dex #dex | 1 | TODO |

### Fase F3

**HNK-05 — Alur financier cek registrasi bayar di muka** · Lead Hans #hans · [[AC-HNK-05 - Alur financier cek registrasi bayar di muka|AC]]

| Task | Deskripsi | Owner | Jam | Status |
|---|---|---|---|---|
| HNK-05.T1 | State machine financier: cek → daftar → tunggu konfirmasi → bayar (Zcash) | Hans #hans | 4 | DONE (`6b5c343`) |
| HNK-05.T2 | Format dan verifikasi memo kuitansi | Hans #hans | 2 | DONE (`6b5c343`) |
| HNK-05.T3 | Endpoint API alur financier | Dex #dex | 3 | TODO |
| HNK-05.T4 | Integrasi layar financier ↔ backend/wallet (status txid, konfirmasi) — FE krusial | Hans #hans | 2 | PARSIAL: layar financier siap; status txid/konfirmasi butuh API backend (HNK-05.T3, Dex) |
| HNK-05.T5 | Layout dan komponen layar financier | Dave #dave (backup sementara: Hans #hans, DEV-11) | 1 | DONE (`cdcba0d`, `98466b2` (`jitsuinfi-frontend`, lokal)) |
| HNK-05.T6 | Panduan E2E financier | Dave #dave (backup sementara: Hans #hans, DEV-11) | 1 | DONE: panduan E2E di TEST-HNK-05 |

**HNK-06 — Pengalihan hak tagih dan pelunasan** · Lead Hans #hans · [[AC-HNK-06 - Pengalihan hak tagih dan pelunasan|AC]]

| Task | Deskripsi | Owner | Jam | Status |
|---|---|---|---|---|
| HNK-06.T1 | Format surat pengalihan + tanda tangan supplier dan buyer | Hans #hans | 2 | Dipindah ke HNK-19.T2 (DEV-06) |
| HNK-06.T2 | Pembuatan URI/QR ZIP-321 untuk pembayaran buyer (Zcash) | Hans #hans | 2 | DONE (`aff284d`) |
| HNK-06.T3 | Deteksi pelunasan dan pencocokan ke N (Zcash) | Hans #hans | 2 | DONE (`aff284d`) |
| HNK-06.T4 | Entri `settled` opsional di papan (Zcash) | Hans #hans | 1 | DONE (`aff284d`); diganti dua tanda tangan di HNK-19.T4 (`f07787b`, DEV-08) |
| HNK-06.T5 | Layar pembayaran buyer (menampilkan QR) | Dave #dave (backup sementara: Hans #hans, DEV-11) | 2 | DONE (`cdcba0d`, `98466b2` (`jitsuinfi-frontend`, lokal)): QR di layar buyer |
| HNK-06.T6 | Dokumentasi mode confidential + risikonya | Dave #dave (backup sementara: Hans #hans, DEV-11) | 1 | DONE: [[Mode Confidential]] |

**HNK-07 — Deteksi pembiayaan ganda dan bukti tanda tangan ganda** · Lead Hans #hans · [[AC-HNK-07 - Deteksi pembiayaan ganda dan bukti tanda tangan ganda|AC]]

| Task | Deskripsi | Owner | Jam | Status |
|---|---|---|---|---|
| HNK-07.T1 | Deteksi pembiayaan ganda + build/verify bundel bukti (core) | Hans #hans | 3 | DONE (`8e523f0`) |
| HNK-07.T2 | Integrasi data bukti di FE (verifikasi di sisi klien) — FE krusial | Hans #hans | 1 | DONE: layar Verify (`cdcba0d`, `98466b2` (`jitsuinfi-frontend`, lokal)) + `jitsuin-wasm` |
| HNK-07.T3 | Tampilan layar "tertangkap" + unduh bukti | Dave #dave (backup sementara: Hans #hans, DEV-11) | 1 | DONE (`cdcba0d`, `98466b2` (`jitsuinfi-frontend`, lokal)): tampilan "Caught" + unduh bukti |
| HNK-07.T4 | Uji integrasi `TES-INV-0003` di mainnet | Dex #dex | 1 | TODO |
| HNK-07.T5 | Naskah skenario demo pembiayaan ganda | Dave #dave (backup sementara: Hans #hans, DEV-11) | 1 | DONE: [[VID-06 - Skenario Demo Pembiayaan Ganda]] |

**HNK-19 — Jitsuin Seal tanda tangan berantai dan Sign-to-Pay** · Lead Hans #hans · [[AC-HNK-19 - Jitsuin Seal tanda tangan berantai dan Sign-to-Pay|AC]] · Desain: [[Desain Jitsuin Seal]]

| Task | Deskripsi | Owner | Jam | Status |
|---|---|---|---|---|
| HNK-19.T1 | Format seal, rantai hash, policy per dokumen, verifier (core) | Hans #hans | 3 | DONE (`b007a26`) |
| HNK-19.T2 | Surat pengalihan kanonik + seal Supplier dan Buyer (mengambil alih HNK-06.T1, DEV-06) | Hans #hans | 2 | DONE (`fdc399e`) |
| HNK-19.T3 | Gerbang `AwaitAssignment` di alur financier + memo advance dua item (kuitansi + seal Financier) (DEV-07) | Hans #hans | 2 | DONE (`f9fee3e`) |
| HNK-19.T4 | Entri `settled` dua tanda tangan + memo pelunasan dua item + watchdog dan status sengketa (DEV-08) | Hans #hans | 3 | DONE (`f07787b`) |
| HNK-19.T5 | Uji integrasi testnet siklus penuh `TES-INV-0003` | Hans #hans | 2 | DONE (`testnet`) |
| HNK-19.T6 | Bundel verifikasi seal (ekspor/impor) untuk `jitsuin verify` | Hans #hans | 1 | DONE (`dd23864`) |

**HNK-20 — Riwayat pembayaran buyer standar minimal** · Lead Hans #hans · [[AC-HNK-20 - Riwayat pembayaran buyer standar minimal|AC]] · Desain: [[Desain Jitsuin Seal]]

| Task | Deskripsi | Owner | Jam | Status |
|---|---|---|---|---|
| HNK-20.T1 | Key buyer per invoice + sertifikat riwayat berantai + entri register bertag (core, DEV-10) | Hans #hans | 3 | DONE (`f03cfb1`) |
| HNK-20.T2 | Verifier riwayat terhadap papan (jangkar, equivocation, penerus tersembunyi) + allowlist financier | Hans #hans | 3 | DONE (`687f2b4`) |
| HNK-20.T3 | Policy standar minimal di alur financier sebelum registrasi | Hans #hans | 1 | DONE (`e53ce12`) |

### Fase F4

**HNK-08 — Indeks suku bunga publik** · Lead Dex #dex · [[AC-HNK-08 - Indeks suku bunga publik|AC]]

| Task | Deskripsi | Owner | Jam | Status |
|---|---|---|---|---|
| HNK-08.T1 | Definisi dan validasi bucket diskon/tenor | Dex #dex | 2 | TODO |
| HNK-08.T2 | Agregasi indeks + ambang k | Dex #dex | 2 | TODO |
| HNK-08.T3 | Halaman indeks suku bunga di web | Dave #dave | 3 | TODO |

**HNK-09 — Verifier CLI hanko verify** · Lead Dex #dex · [[AC-HNK-09 - Verifier CLI hanko verify|AC]]

| Task | Deskripsi | Owner | Jam | Status |
|---|---|---|---|---|
| HNK-09.T1 | Perintah `jitsuin verify` (memakai ulang scanner) | Dex #dex | 3 | TODO |
| HNK-09.T2 | Image Docker + instruksi `cargo install` | Dex #dex | 2 | TODO |
| HNK-09.T3 | README: perintah persis + output yang diharapkan | Dave #dave | 1 | TODO |

**HNK-12 — Spesifikasi gaya ZIP Shielded Receivable Registry** · Lead Dave #dave · [[AC-HNK-12 - Spesifikasi gaya ZIP Shielded Receivable Registry|AC]]

| Task | Deskripsi | Owner | Jam | Status |
|---|---|---|---|---|
| HNK-12.T1 | Tulis spesifikasi gaya ZIP | Dave #dave (backup sementara: Hans #hans, DEV-11) | 3 | DONE (`c42af3e`): `docs/zip-shielded-receivable-registry.md` |
| HNK-12.T2 | Test vector dari spesifikasi dijalankan sebagai test | Dex #dex | 1 | TODO |
| HNK-12.T3 | Review teknis spesifikasi | Hans #hans | 1 | TODO — review oleh Hans sendiri: spesifikasi ditulis agent (DEV-11) |

### Fase F5

**HNK-10 — Web app per peran** · Lead Dave #dave · [[AC-HNK-10 - Web app per peran|AC]]

| Task | Deskripsi | Owner | Jam | Status |
|---|---|---|---|---|
| HNK-10.T1 | Scaffold FE, routing, design system (tanpa CDN, CSP-ready) | Dave #dave (backup sementara: Hans #hans, DEV-11) | 3 | DONE (`cdcba0d`, `98466b2` (`jitsuinfi-frontend`, lokal)) |
| HNK-10.T2 | Layar supplier: buat invoice, minta tanda tangan buyer | Dave #dave (backup sementara: Hans #hans, DEV-11) | 3 | DONE (`cdcba0d`, `98466b2` (`jitsuinfi-frontend`, lokal)) |
| HNK-10.T3 | Layar tanda tangan buyer di browser (key di sisi klien) — FE krusial | Hans #hans | 2 | DONE: layar buyer (`cdcba0d`, `98466b2` (`jitsuinfi-frontend`, lokal)) + `jitsuin-wasm` |
| HNK-10.T4 | Skeleton backend API | Dex #dex | 3 | TODO |
| HNK-10.T5 | Deploy Railway + header CSP (setelah persetujuan user) | Dex #dex | 2 | TODO |
| HNK-10.T6 | Review keamanan penanganan key di FE | Hans #hans | 1 | DONE: review dicatat di TEST-HNK-10 (U-HNK-10.3) |
| HNK-10.T7 | Paket browser `jitsuin-wasm`: key buyer dari passkey PRF, tanda tangan invoice dan surat pengalihan, QR pelunasan, sertifikat riwayat, verifikasi bundel/bukti/riwayat di sisi klien — FE krusial | Hans #hans | 3 | DONE (`2438a82`) |

**HNK-11 — Threat model dan halaman orang luar** · Lead Dave #dave · [[AC-HNK-11 - Threat model dan halaman orang luar|AC]]

| Task | Deskripsi | Owner | Jam | Status |
|---|---|---|---|---|
| HNK-11.T1 | Finalisasi [[Threat Model]] | Dave #dave (backup sementara: Hans #hans, DEV-11) | 2 | DONE: [[Threat Model]] final |
| HNK-11.T2 | Halaman "apa yang bisa dilihat orang luar" | Dave #dave (backup sementara: Hans #hans, DEV-11) | 2 | DONE (`cdcba0d`, `98466b2` (`jitsuinfi-frontend`, lokal)): halaman orang luar + kartu explorer |
| HNK-11.T3 | Review kebenaran kebocoran Zcash | Hans #hans | 1 | TODO — review oleh Hans sendiri: threat model ditulis agent (DEV-11) |

**HNK-18 — Materi pitch dan visual** · Lead Dave #dave · [[AC-HNK-18 - Materi pitch dan visual|AC]]

| Task | Deskripsi | Owner | Jam | Status |
|---|---|---|---|---|
| HNK-18.T1 | Logo dan identitas visual JitsuinFi | Dave #dave | 1 | TODO |
| HNK-18.T2 | Tiga slide video (masalah, threat model, penutup) | Dave #dave | 1 | TODO |
| HNK-18.T3 | Diagram arsitektur untuk README | Dave #dave (backup sementara: Hans #hans, DEV-11) | 1 | DONE (`d99680b`): diagram mermaid di README |
| HNK-18.T4 | Landing page immersive (visual 65% / caption 35%, tanpa UI kartu kotak), setara PortoWeb | Dave #dave (backup sementara: Hans #hans, DEV-11) | 4 | IN PROGRESS: 6 bab + toggle EN/中文 selesai dan di-push (frontend `389b9d3`, 2026-10-19); bab 1–4 divalidasi user, bab 5–6 disetujui ("Mantap lanjut"); bab 5 butuh zcash PR#3 (wasm riwayat). Live di https://jitsuinfi.vercel.app (Vercel, deploy prebuilt 2026-10-19, header CSP + `frame-ancestors 'none'`). Lihat [[Landing Page - Brief]] |

### Fase F6

**HNK-13 — Uji dengan pengguna sungguhan** · Lead Dave #dave · [[AC-HNK-13 - Uji dengan pengguna sungguhan|AC]]

| Task | Deskripsi | Owner | Jam | Status |
|---|---|---|---|---|
| HNK-13.T1 | Rekrut dan jadwalkan 2–3 peserta | Dave #dave | 1 | TODO |
| HNK-13.T2 | Jalankan sesi uji + kumpulkan kutipan (dengan izin) | Dave #dave | 2 | TODO |
| HNK-13.T3 | Dukungan masalah on-chain selama sesi | Hans #hans | 1 | TODO |

**HNK-14 — Submission video deskripsi dan demo URL** · Lead Dave #dave · [[AC-HNK-14 - Submission video deskripsi dan demo URL|AC]]

| Task | Deskripsi | Owner | Jam | Status |
|---|---|---|---|---|
| HNK-14.T1 | Rekam dan edit video 2 menit | Dave #dave | 4 | TODO |
| HNK-14.T2 | Deskripsi ≤ 2.000 karakter + pengungkapan AVAL | Dave #dave (backup sementara: Hans #hans, DEV-11) | 1 | PARSIAL: draf di [[Submission - Deskripsi]] (1.801 karakter), menunggu review Dave dan Hans |
| HNK-14.T3 | Checklist publikasi repo (lisensi, README, txid) | Dex #dex | 1 | TODO |
| HNK-14.T4 | Submit final dari akun pendaftar | Hans #hans | 1 | TODO |

**HNK-17 — QA E2E lintas item** · Lead Dave #dave · [[AC-HNK-17 - QA E2E lintas item|AC]]

| Task | Deskripsi | Owner | Jam | Status |
|---|---|---|---|---|
| HNK-17.T1 | E2E putaran 1 (HNK-01 – HNK-07) | Dave #dave | 3 | TODO |
| HNK-17.T2 | E2E putaran 2 (HNK-08 – HNK-11) | Dave #dave | 2 | TODO |
| HNK-17.T3 | Retest bug yang sudah diperbaiki | Dave #dave | 1 | TODO |

### Fase F7

**HNK-15 — Stretch JitsuinFi Vault** · Lead Hans #hans · [[AC-HNK-15 - Stretch JitsuinFi Vault|AC]]

| Task | Deskripsi | Owner | Jam | Status |
|---|---|---|---|---|
| HNK-15.T1 | Merkle sum tree kewajiban | Dex #dex | 3 | TODO |
| HNK-15.T2 | Uji solvabilitas lewat FVK akun operasional (Zcash) | Hans #hans | 3 | DONE (`e54ea36`) |
| HNK-15.T3 | Halaman verifikasi anggota | Dave #dave | 2 | TODO |

## Status (auto)
```dataview
TABLE WITHOUT ID file.link AS "AC", phase AS "Fase", lead AS "Lead", status AS "Status"
FROM "04-Acceptance-Criteria"
WHERE type = "ac"
SORT id ASC
```

## Log Deviasi

| ID | Tanggal | Item | Rencana/keputusan awal | Yang berubah | Alasan | Disetujui user |
|---|---|---|---|---|---|---|
| DEV-01 | 2026-10-16 | Semua uji integrasi | Workflow langkah 3: artefak `TES-` wajib dibersihkan, bukti sisa = 0 | Pembersihan penuh hanya untuk artefak off-chain; transaksi mainnet tidak bisa dihapus, jadi dicatat txid-nya dan memakai akun/papan `TES-` dengan nominal sekecil mungkin | Sifat blockchain append-only | _Menunggu konfirmasi user_ |
| DEV-02 | 2026-10-16 | F1 (HNK-01, HNK-02, HNK-16) | [[Rencana Fase]]: spike kritis wajib PASS sebelum F1/F2 | F1 (logika murni, tanpa chain) mulai begitu SPK-01 PASS, sementara spike Zcash lain berjalan paralel. F2 tetap menunggu spike kritis | Rust baru terpasang dan TAZ/ZEC belum tersedia; F1 tidak menyentuh chain | **Disetujui user 2026-10-16** ("yang bisa dimulai sekarang gas mulai") |
| DEV-03 | 2026-10-16 | HNK-03 – HNK-07, SPK-03, SPK-07, SPK-08 | D-04/D-10: mainnet dengan crate stabil | Jaringan development = **testnet**; crate = set **pre-release** yang di-pin (D-13). Mainnet hanya demo akhir. Kriteria "di mainnet" pada AC dibaca sebagai "di testnet" selama development; uji ulang di mainnet bila ZEC tersedia | Keputusan user (opsi B); ZEC mainnet belum tersedia | **Disetujui user 2026-10-16** |
| DEV-04 | 2026-10-16 | HNK-02 (AC-HNK-02.1), HNK-07, [[Format Data]] | N = BLAKE2b-256("JitsuinNullifier", **tanda tangan buyer**) | **Usulan:** N = BLAKE2b-256("JitsuinNullifier", **byte kanonik invoice**). Tanda tangan buyer tetap wajib sebagai bukti persetujuan | Ed25519 deterministik hanya konvensi RFC 8032. Signer buyer dengan nonce acak bisa menghasilkan dua tanda tangan valid untuk invoice yang **sama** → dua N → pembiayaan ganda lolos. Byte kanonik memuat `supplier_ephemeral_pk` acak 256 bit, jadi N tetap tidak bisa ditebak dan unik per invoice | **Disetujui user 2026-10-17** ("N nya gas sesuaikan"); diimplementasikan `40d7656` |
| DEV-06 | 2026-10-17 | HNK-06.T1 | Owner Dex | Owner **Hans**, dikerjakan sebagai bagian HNK-19.T2 | Keputusan user D-22 | **Disetujui user 2026-10-17** |
| DEV-07 | 2026-10-17 | HNK-05 (state machine financier) | Alur cek → daftar → konfirmasi → bayar (`6b5c343`) | State baru `AwaitAssignment` antara konfirmasi dan bayar: advance hanya cair setelah surat pengalihan tersegel Supplier dan Buyer; memo advance membawa kuitansi + seal Financier (HNK-19.T3) | Keputusan user D-21 (adopsi SignBaliola, Sign-to-Pay) | **Disetujui user 2026-10-17** |
| DEV-08 | 2026-10-17 | HNK-06.T4, [[Format Data]] | Entri `settled` satu tanda tangan financier, commitment nol (`aff284d`) | Entri `settled` dua tanda tangan (buyer + financier) dan flag tepat waktu; AC-HNK-06.3 diuji ulang setelah HNK-19.T4 | Keputusan user D-19 | **Disetujui user 2026-10-17** |
| DEV-09 | 2026-10-17 | HNK-02.T3 | Owner Dex | `financier_commitment` diimplementasikan Hans di `6b5c343` sebagai bagian HNK-05 dan **sudah ter-push** sebelum keputusan ini. Keputusan user: Dex tetap mengerjakan HNK-02.T3 secara independen; hasilnya dibandingkan dengan implementasi Hans dan test vector `c72255e7…2b3a`. Sama → dipakai; beda → diberi komentar; masih salah → diperbaiki. Porsi backlog diperbarui setelahnya | Dibutuhkan lebih dulu oleh HNK-05; seharusnya dicatat saat itu | **Keputusan user 2026-10-17**: tunggu Dex, bandingkan |
| DEV-10 | 2026-10-17 | HNK-20, HNK-02 ([[Format Data]]) | Riwayat berantai dengan sertifikat yang hanya ditandatangani buyer | Rantai **dijangkarkan ke papan**: entri register jenis baru `0x03` (168 byte) membawa tag penerus, dan sertifikat memuat key supplier. Tanpa jangkar, buyer bisa membuat rantai cabang yang dinomori ulang untuk menyembunyikan gagal bayar. Entri `0x01` tetap valid. Estimasi HNK-20 naik dari 5 ke 7 jam | Celah ditemukan saat implementasi; jangkar dibutuhkan agar janji "riwayat buruk tidak bisa disembunyikan" benar | Dilaporkan ke user 2026-10-17 sebelum implementasi ("Oke gas riwayat berantai") |
| DEV-11 | 2026-10-18 | HNK-01.T4, HNK-05.T5–T6, HNK-06.T5–T6, HNK-07.T3, HNK-07.T5, HNK-10.T1–T2, HNK-11.T1–T2, HNK-12.T1, HNK-15.T3, HNK-18.T3 | Owner Dave | Owner tetap Dave; dikerjakan sementara oleh Hans (agent) sebagai backup, lokal; Dave me-review. Status tiap task diperbarui saat selesai; porsi beban kerja dihitung ulang setelahnya | Keputusan user D-25, supaya alur bisa jalan | **Disetujui user 2026-10-18** |
| DEV-05 | 2026-10-16 | SPK-04 | [[Rencana Fase]]: SPK-04 spike kritis | SPK-04 tidak lagi kritis; gerbang F0 dihitung tanpa SPK-04 | D-15: Zodl opsional (keputusan user) | **Mengikuti keputusan user 2026-10-16** |
