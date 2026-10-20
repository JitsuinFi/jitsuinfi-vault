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

Target pembagian: **Hans 40% · Dex 30% · Dave 30%**. Sejak 2026-10-20 semua task Dave dipegang Hans (D-35, DEV-20); lihat revisi di bawah. Hans wajib memegang seluruh integrasi Zcash serta bagian backend dan FE yang krusial.

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

**Revisi 2026-10-20 (D-30; D-29 dijalankan):** item HNK-22 – HNK-29 dibuat dari [[FD-01 - Keputusan Usulan dan Gelombang Kerja]] dan [[FD-02 - Penelusuran Business Flow ke Backlog]] (132 task `BL-…` di file `-backlogs` tiap diagram, semuanya dipetakan ke task di bawah). HNK-21 (14 jam) dan HNK-05.T4 (2 jam) pindah dari Hans ke Dex (DEV-12); HNK-10.T4 dan HNK-10.T5 diserap HNK-23 (DEV-13, jam tidak dihitung dua kali). Kerja baru 106,5 jam: Hans 36,5, Dex 33, Dave 37. Angka "Sebelum" dihitung ulang dari tabel task di bawah (174 jam); D-29 menulis 176 karena HNK-06.T1 (2 jam, dipindah ke HNK-19.T2) ikut terhitung dua kali.

| Orang | Sebelum | Kerja baru | Total | Porsi | Target |
|---|---|---|---|---|---|
| Hans #hans | 73 | 36,5 | 109,5 | 39,0% | 40% |
| Dex #dex | 53 | 33 | 86 | 30,7% | 30% |
| Dave #dave | 48 | 37 | 85 | 30,3% | 30% |
| **Total** | **174** | **106,5** | **280,5** | 100% | 100% |

**Revisi 2026-10-20 (D-35, DEV-20):** semua task Dave dipindah ke Hans atas keputusan user. Label task: "Hans #hans (dari Dave, D-35)". Dasar tabel di atas:

| Orang | Jam | Porsi |
|---|---|---|
| Hans #hans | 194,5 | 69,3% |
| Dex #dex | 86 | 30,7% |
| Dave #dave | 0 | 0% |
| **Total** | **280,5** | 100% |

**Revisi 2026-10-20 (D-38, DEV-22):** task backend Dex dipindah ke Hans (label "Hans #hans (dari Dex, D-38)"). Dihitung ulang dari tabel task (tanpa task yang dipindah ke item lain):

| Orang | Jam | Porsi |
|---|---|---|
| Hans #hans | 240,5 | 85,7% |
| Dex #dex | 40 | 14,3% |
| **Total** | **280,5** | 100% |

Urutan kerja mengikuti gelombang FD-01: fondasi (HNK-27, HNK-22, HNK-24.T1, HNK-24.T3) 21–23 Okt, antarpihak (HNK-23, HNK-26, HNK-21) 23–26 Okt, lengkapi (HNK-25, HNK-28, HNK-29, HNK-17.T4) 26–27 Okt.

## Daftar item

| ID | Item | Fase | Lead | Tim | Dependency | AC | Test | ES |
|---|---|---|---|---|---|---|---|---|
| HNK-01 | Format invoice kanonik dan tanda tangan buyer | F1 | Hans #hans | #hans #dex | SPK-06 | [[AC-HNK-01 - Format invoice kanonik dan tanda tangan buyer\|AC]] | [[TEST-HNK-01 - Format invoice kanonik dan tanda tangan buyer\|Test]] | [[ES-HNK-01 - Format invoice kanonik dan tanda tangan buyer\|ES]] |
| HNK-02 | Nullifier dan entri papan registry | F1 | Hans #hans | #hans #dex | HNK-01 | [[AC-HNK-02 - Nullifier dan entri papan registry\|AC]] | [[TEST-HNK-02 - Nullifier dan entri papan registry\|Test]] | [[ES-HNK-02 - Nullifier dan entri papan registry\|ES]] |
| HNK-03 | Wallet backend kirim dan terima memo di mainnet | F2 | Hans #hans | #hans #dex | SPK-01, SPK-02, SPK-03, SPK-10 | [[AC-HNK-03 - Wallet backend kirim dan terima memo di mainnet\|AC]] | [[TEST-HNK-03 - Wallet backend kirim dan terima memo di mainnet\|Test]] | [[ES-HNK-03 - Wallet backend kirim dan terima memo di mainnet\|ES]] |
| HNK-04 | Pemindai papan registry | F2 | Hans #hans | #hans #dex | HNK-02, HNK-03, SPK-05, SPK-08 | [[AC-HNK-04 - Pemindai papan registry\|AC]] | [[TEST-HNK-04 - Pemindai papan registry\|Test]] | [[ES-HNK-04 - Pemindai papan registry\|ES]] |
| HNK-05 | Alur financier cek registrasi bayar di muka | F3 | Hans #hans | #hans | HNK-04 | [[AC-HNK-05 - Alur financier cek registrasi bayar di muka\|AC]] | [[TEST-HNK-05 - Alur financier cek registrasi bayar di muka\|Test]] | [[ES-HNK-05 - Alur financier cek registrasi bayar di muka\|ES]] |
| HNK-06 | Pengalihan hak tagih dan pelunasan | F3 | Hans #hans | #hans | HNK-05 | [[AC-HNK-06 - Pengalihan hak tagih dan pelunasan\|AC]] | [[TEST-HNK-06 - Pengalihan hak tagih dan pelunasan\|Test]] | [[ES-HNK-06 - Pengalihan hak tagih dan pelunasan\|ES]] |
| HNK-07 | Deteksi pembiayaan ganda dan bukti tanda tangan ganda | F3 | Hans #hans | #hans #dex | HNK-05 | [[AC-HNK-07 - Deteksi pembiayaan ganda dan bukti tanda tangan ganda\|AC]] | [[TEST-HNK-07 - Deteksi pembiayaan ganda dan bukti tanda tangan ganda\|Test]] | [[ES-HNK-07 - Deteksi pembiayaan ganda dan bukti tanda tangan ganda\|ES]] |
| HNK-08 | Indeks suku bunga publik | F4 | Dex #dex | #dex #hans | HNK-04 | [[AC-HNK-08 - Indeks suku bunga publik\|AC]] | [[TEST-HNK-08 - Indeks suku bunga publik\|Test]] | [[ES-HNK-08 - Indeks suku bunga publik\|ES]] |
| HNK-09 | Verifier CLI hanko verify | F4 | Dex #dex | #dex #hans | HNK-04, HNK-07, SPK-11 | [[AC-HNK-09 - Verifier CLI hanko verify\|AC]] | [[TEST-HNK-09 - Verifier CLI hanko verify\|Test]] | [[ES-HNK-09 - Verifier CLI hanko verify\|ES]] |
| HNK-10 | Web app per peran | F5 | Hans #hans | #hans #dex | HNK-05, HNK-06, SPK-09 | [[AC-HNK-10 - Web app per peran\|AC]] | [[TEST-HNK-10 - Web app per peran\|Test]] | [[ES-HNK-10 - Web app per peran\|ES]] |
| HNK-11 | Threat model dan halaman orang luar | F5 | Hans #hans | #hans | HNK-07 | [[AC-HNK-11 - Threat model dan halaman orang luar\|AC]] | [[TEST-HNK-11 - Threat model dan halaman orang luar\|Test]] | [[ES-HNK-11 - Threat model dan halaman orang luar\|ES]] |
| HNK-12 | Spesifikasi gaya ZIP Shielded Receivable Registry | F4 | Hans #hans | #hans #dex | HNK-02, HNK-07 | [[AC-HNK-12 - Spesifikasi gaya ZIP Shielded Receivable Registry\|AC]] | [[TEST-HNK-12 - Spesifikasi gaya ZIP Shielded Receivable Registry\|Test]] | [[ES-HNK-12 - Spesifikasi gaya ZIP Shielded Receivable Registry\|ES]] |
| HNK-13 | Uji dengan pengguna sungguhan | F6 | Hans #hans | #hans | HNK-05, HNK-06, HNK-07, HNK-10 | [[AC-HNK-13 - Uji dengan pengguna sungguhan\|AC]] | [[TEST-HNK-13 - Uji dengan pengguna sungguhan\|Test]] | [[ES-HNK-13 - Uji dengan pengguna sungguhan\|ES]] |
| HNK-14 | Submission video deskripsi dan demo URL | F6 | Hans #hans | #hans #dex | HNK-13, SPK-12, SPK-15 | [[AC-HNK-14 - Submission video deskripsi dan demo URL\|AC]] | [[TEST-HNK-14 - Submission video deskripsi dan demo URL\|Test]] | [[ES-HNK-14 - Submission video deskripsi dan demo URL\|ES]] |
| HNK-15 | Stretch JitsuinFi Vault | F7 | Hans #hans | #hans | HNK-07, SPK-05 | [[AC-HNK-15 - Stretch JitsuinFi Vault\|AC]] | [[TEST-HNK-15 - Stretch JitsuinFi Vault\|Test]] | [[ES-HNK-15 - Stretch JitsuinFi Vault\|ES]] |
| HNK-16 | CI dan quality gate | F1 | Dex #dex | #dex | SPK-01, SPK-14 | [[AC-HNK-16 - CI dan quality gate\|AC]] | [[TEST-HNK-16 - CI dan quality gate\|Test]] | [[ES-HNK-16 - CI dan quality gate\|ES]] |
| HNK-17 | QA E2E lintas item | F6 | Hans #hans | #hans | HNK-05 – HNK-11 | [[AC-HNK-17 - QA E2E lintas item\|AC]] | [[TEST-HNK-17 - QA E2E lintas item\|Test]] | [[ES-HNK-17 - QA E2E lintas item\|ES]] |
| HNK-18 | Materi pitch dan visual | F5 | Hans #hans | #hans | HNK-07, HNK-11 | [[AC-HNK-18 - Materi pitch dan visual\|AC]] | [[TEST-HNK-18 - Materi pitch dan visual\|Test]] | [[ES-HNK-18 - Materi pitch dan visual\|ES]] |
| HNK-19 | Jitsuin Seal tanda tangan berantai dan Sign-to-Pay | F3 | Hans #hans | #hans | HNK-05, HNK-06 | [[AC-HNK-19 - Jitsuin Seal tanda tangan berantai dan Sign-to-Pay\|AC]] | [[TEST-HNK-19 - Jitsuin Seal tanda tangan berantai dan Sign-to-Pay\|Test]] | [[ES-HNK-19 - Jitsuin Seal tanda tangan berantai dan Sign-to-Pay\|ES]] |
| HNK-20 | Riwayat pembayaran buyer standar minimal | F3 | Hans #hans | #hans | HNK-19 | [[AC-HNK-20 - Riwayat pembayaran buyer standar minimal\|AC]] | [[TEST-HNK-20 - Riwayat pembayaran buyer standar minimal\|Test]] | [[ES-HNK-20 - Riwayat pembayaran buyer standar minimal\|ES]] |
| HNK-21 | Polish halaman internal web app | F5 | Dex #dex | #dex #hans (dari Hans, D-29, DEV-12) | HNK-10, HNK-18.T4 | [[AC-HNK-21 - Polish halaman internal web app\|AC]] | [[TEST-HNK-21 - Polish halaman internal web app\|Test]] | [[ES-HNK-21 - Polish halaman internal web app\|ES]] |
| HNK-22 | Akun passkey peran dan kontak | F5 | Hans #hans | #hans | HNK-10 | [[AC-HNK-22 - Akun passkey peran dan kontak\|AC]] | [[TEST-HNK-22 - Akun passkey peran dan kontak\|Test]] | [[ES-HNK-22 - Akun passkey peran dan kontak\|ES]] |
| HNK-23 | Relay kotak surat end to end | F5 | Hans #hans | #hans | HNK-22 | [[AC-HNK-23 - Relay kotak surat end to end\|AC]] | [[TEST-HNK-23 - Relay kotak surat end to end\|Test]] | [[ES-HNK-23 - Relay kotak surat end to end\|ES]] |
| HNK-24 | Alur deal di layar supplier | F5 | Hans #hans | #hans | HNK-22, HNK-23, HNK-27 | [[AC-HNK-24 - Alur deal di layar supplier\|AC]] | [[TEST-HNK-24 - Alur deal di layar supplier\|Test]] | [[ES-HNK-24 - Alur deal di layar supplier\|ES]] |
| HNK-25 | Alur deal di layar buyer | F5 | Hans #hans | #hans | HNK-22, HNK-23, HNK-27 | [[AC-HNK-25 - Alur deal di layar buyer\|AC]] | [[TEST-HNK-25 - Alur deal di layar buyer\|Test]] | [[ES-HNK-25 - Alur deal di layar buyer\|ES]] |
| HNK-26 | Konsol dan API node financier | F5 | Hans #hans | #hans | HNK-05.T3, HNK-23, HNK-27 | [[AC-HNK-26 - Konsol dan API node financier\|AC]] | [[TEST-HNK-26 - Konsol dan API node financier\|Test]] | [[ES-HNK-26 - Konsol dan API node financier\|ES]] |
| HNK-27 | Perbaikan protokol dan flow | F3 | Hans #hans | #hans | HNK-05, HNK-19, HNK-20 | [[AC-HNK-27 - Perbaikan protokol dan flow\|AC]] | [[TEST-HNK-27 - Perbaikan protokol dan flow\|Test]] | [[ES-HNK-27 - Perbaikan protokol dan flow\|ES]] |
| HNK-28 | Verifikasi publik lengkap | F4 | Hans #hans | #hans | HNK-08, HNK-09, HNK-23 | [[AC-HNK-28 - Verifikasi publik lengkap\|AC]] | [[TEST-HNK-28 - Verifikasi publik lengkap\|Test]] | [[ES-HNK-28 - Verifikasi publik lengkap\|ES]] |
| HNK-29 | Alur dana anggota | F7 | Hans #hans | #hans | HNK-15, HNK-23 | [[AC-HNK-29 - Alur dana anggota\|AC]] | [[TEST-HNK-29 - Alur dana anggota\|Test]] | [[ES-HNK-29 - Alur dana anggota\|ES]] |

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
| SPK-12 | [[SPK-12 - Kepastian aturan dan form ZECATHON\|Kepastian aturan dan form ZECATHON]] | Hans #hans | 1 | — |
| SPK-13 | [[SPK-13 - Dampak NU7 dan versi crate\|Dampak NU7 dan versi crate]] | Dex #dex | 1 | — |
| SPK-14 | [[SPK-14 - Repo baru lisensi dan originalitas\|Repo baru lisensi dan originalitas]] | Dex #dex | 1 | — |
| SPK-15 | [[SPK-15 - Tooling produksi video\|Tooling produksi video]] | Hans #hans | 1 | — |
| SPK-16 | [[SPK-16 - Block explorer untuk demo\|Block explorer untuk demo]] | Hans #hans | 1 | — |
| SPK-17 | [[SPK-17 - Toolchain frontend dan aset offline\|Toolchain frontend dan aset offline]] | Hans #hans | 1 | — |
| SPK-18 | [[SPK-18 - Akses tim dan kesamaan environment\|Akses tim dan kesamaan environment]] | Dex #dex | 1 | — |
| SPK-19 | [[SPK-19 - Testnet NU7 untuk development\|Testnet NU7 untuk development]] | Hans #hans | 2 | — |

## Rincian task per item

### Fase F1

**HNK-01 — Format invoice kanonik dan tanda tangan buyer** · Lead Hans #hans · [[AC-HNK-01 - Format invoice kanonik dan tanda tangan buyer|AC]]

| Task | Deskripsi | Owner | Jam | Status |
|---|---|---|---|---|
| HNK-01.T1 | Desain struct invoice dan encoding kanonik deterministik | Hans #hans | 3 | DONE (`c0d6981`) |
| HNK-01.T2 | Implementasi sign/verify Ed25519 (core) | Hans #hans | 2 | DONE (`c0d6981`) |
| HNK-01.T3 | Unit test + file test vector | Dex #dex | 2 | DONE (`aeaae96`, jitsuinfi-zcash PR #2 di-merge 19 Okt): 9 tes + vector independen |
| HNK-01.T4 | Sinkronkan [[Format Data]] dengan implementasi | Hans #hans (dari Dave, D-35) | 1 | DONE: [[Format Data]] disinkronkan per item (HNK-01 – HNK-20) |

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
| HNK-16.T1 | Script cek lokal satu perintah | Dex #dex | 1 | DONE (`317d59b`, PR #1 di-merge): `scripts/check.sh`; lulus lokal 38 dtk, gagal benar saat merah |
| HNK-16.T2 | Workflow GitHub Actions | Dex #dex | 2 | DONE (`317d59b`): hijau di PR #1 dan di `main` (run 39215984762); branch protection menunggu repo publik (AC-HNK-16.4) |
| HNK-16.T3 | Secret scanning (gitleaks) + `.gitignore` seed/key/.env/DB wallet | Dex #dex | 1 | DONE (`317d59b`): 0 temuan seluruh riwayat |

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
| HNK-05.T3 | Endpoint API alur financier | Hans #hans (dari Dex, D-38) | 3 | TODO |
| HNK-05.T4 | Integrasi layar financier ↔ backend/wallet (status txid, konfirmasi) — FE krusial | Hans #hans (dari Dex, D-38) | 2 | PARSIAL: layar financier siap; status txid/konfirmasi butuh API backend (HNK-05.T3, Dex) |
| HNK-05.T5 | Layout dan komponen layar financier | Hans #hans (dari Dave, D-35) | 1 | DONE (`cdcba0d`, `98466b2` (`jitsuinfi-frontend`, lokal)) |
| HNK-05.T6 | Panduan E2E financier | Hans #hans (dari Dave, D-35) | 1 | DONE: panduan E2E di TEST-HNK-05 |

**HNK-06 — Pengalihan hak tagih dan pelunasan** · Lead Hans #hans · [[AC-HNK-06 - Pengalihan hak tagih dan pelunasan|AC]]

| Task | Deskripsi | Owner | Jam | Status |
|---|---|---|---|---|
| HNK-06.T1 | Format surat pengalihan + tanda tangan supplier dan buyer | Hans #hans | 2 | Dipindah ke HNK-19.T2 (DEV-06) |
| HNK-06.T2 | Pembuatan URI/QR ZIP-321 untuk pembayaran buyer (Zcash) | Hans #hans | 2 | DONE (`aff284d`) |
| HNK-06.T3 | Deteksi pelunasan dan pencocokan ke N (Zcash) | Hans #hans | 2 | DONE (`aff284d`) |
| HNK-06.T4 | Entri `settled` opsional di papan (Zcash) | Hans #hans | 1 | DONE (`aff284d`); diganti dua tanda tangan di HNK-19.T4 (`f07787b`, DEV-08) |
| HNK-06.T5 | Layar pembayaran buyer (menampilkan QR) | Hans #hans (dari Dave, D-35) | 2 | DONE (`cdcba0d`, `98466b2` (`jitsuinfi-frontend`, lokal)): QR di layar buyer |
| HNK-06.T6 | Dokumentasi mode confidential + risikonya | Hans #hans (dari Dave, D-35) | 1 | DONE: [[Mode Confidential]] |

**HNK-07 — Deteksi pembiayaan ganda dan bukti tanda tangan ganda** · Lead Hans #hans · [[AC-HNK-07 - Deteksi pembiayaan ganda dan bukti tanda tangan ganda|AC]]

| Task | Deskripsi | Owner | Jam | Status |
|---|---|---|---|---|
| HNK-07.T1 | Deteksi pembiayaan ganda + build/verify bundel bukti (core) | Hans #hans | 3 | DONE (`8e523f0`) |
| HNK-07.T2 | Integrasi data bukti di FE (verifikasi di sisi klien) — FE krusial | Hans #hans | 1 | DONE: layar Verify (`cdcba0d`, `98466b2` (`jitsuinfi-frontend`, lokal)) + `jitsuin-wasm` |
| HNK-07.T3 | Tampilan layar "tertangkap" + unduh bukti | Hans #hans (dari Dave, D-35) | 1 | DONE (`cdcba0d`, `98466b2` (`jitsuinfi-frontend`, lokal)): tampilan "Caught" + unduh bukti |
| HNK-07.T4 | Uji integrasi `TES-INV-0003` di mainnet | Dex #dex | 1 | TODO |
| HNK-07.T5 | Naskah skenario demo pembiayaan ganda | Hans #hans (dari Dave, D-35) | 1 | DONE: [[VID-06 - Skenario Demo Pembiayaan Ganda]] |

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

**HNK-27 — Perbaikan protokol dan flow** · Lead Hans #hans · [[AC-HNK-27 - Perbaikan protokol dan flow|AC]] · Dibuat 2026-10-20 (D-30)

| Task | Deskripsi | Owner | Jam | Status |
|---|---|---|---|---|
| HNK-27.T1 | Salt komitmen dari library (CSPRNG), disimpan per (invoice, financier), dipakai ulang saat retry. Rincian: `BL-D23-04` | Hans #hans | 1 | DONE (`748d451`, jitsuinfi-zcash PR #7, di-merge `69807f3`) |
| HNK-27.T2 | Kelas: `classes_for` di 3.2, parameter kelas di API entri wasm, cek di `check_entry`. Rincian: `BL-D23-05` | Hans #hans | 3 | PARSIAL (`d5f98d0`, `59cd762`, jitsuinfi-zcash PR #7, di-merge `69807f3`): kode selesai; bukti indeks berkelas I-HNK-27.1 menunggu HNK-24.T6 dan HNK-26 (GAGAL AUDIT BL-D23-05, 2026-10-20) |
| HNK-27.T3 | `assignmentDecode` di `jitsuin-wasm`. Rincian: `BL-D24-04` | Hans #hans | 1 | DONE (`948133a`, jitsuinfi-zcash PR #7, di-merge `69807f3`) |
| HNK-27.T4 | `doubleSignProof` di wasm menerima posisi papan. Rincian: `BL-D27-03` | Hans #hans | 1 | DONE (`14803af`, jitsuinfi-zcash PR #7, di-merge `69807f3`) |
| HNK-27.T5 | `register()`: terima `BoardChecked` di `Register`, cari entri terkirim sebelum posting ulang. Rincian: `BL-D23-12` | Hans #hans | 3 | DONE (`fef1d15`, jitsuinfi-zcash PR #7, di-merge `69807f3`) |
| HNK-27.T6 | Hitung ulang konfirmasi entri yang ditambang ulang; `Done` setelah advance terkonfirmasi. Rincian: `BL-D24-08`, `BL-D24-10` | Hans #hans | 2 | DONE (`b6f33d5`, jitsuinfi-zcash PR #7, di-merge `69807f3`) |
| HNK-27.T7 | Bandingkan advance yang diterima dengan advance yang disepakati. Rincian: `BL-D24-12` | Hans #hans | 1 | DONE (`a10185f`, jitsuinfi-zcash PR #7, di-merge `69807f3`) |
| HNK-27.T8 | Varian entri bertag yang hanya menerima `history_tag`. Rincian: `BL-D23-10` | Hans #hans | 1 | DONE (`8897517`, jitsuinfi-zcash PR #7, di-merge `69807f3`) |
| HNK-27.T9 | API `jitsuin-wasm` menerima key sebagai byte. Rincian: `BL-D21-13` | Hans #hans | 1 | DONE (`1ac7057`, jitsuinfi-zcash PR #7, di-merge `69807f3`) |
| HNK-27.T10 | Perintah CLI solvabilitas anggota; `SolvencyPolicy.grace_days` dihapus atau dipakai. Rincian: `BL-D29-06` | Hans #hans | 1 | DONE (`9826b09`, jitsuinfi-zcash PR #7, di-merge `69807f3`) |

### Fase F4

**HNK-08 — Indeks suku bunga publik** · Lead Dex #dex · [[AC-HNK-08 - Indeks suku bunga publik|AC]]

| Task | Deskripsi | Owner | Jam | Status |
|---|---|---|---|---|
| HNK-08.T1 | Definisi dan validasi bucket diskon/tenor | Dex #dex | 2 | DONE (`61ca636`: PR #5 masuk ke `main` lewat PR #6, karena #5 ditumpuk di branch #4): tabel kelas, `classes_for`, `validate_classes`; tabel di [[Format Data]] |
| HNK-08.T2 | Agregasi indeks + ambang k | Dex #dex | 2 | DONE (`61ca636`, PR #5 + #6): `RateIndex`, `rate_index`, `jitsuin index`, k = 5 (usulan D-27) |
| HNK-08.T3 | Halaman indeks suku bunga di web | Hans #hans (dari Dave, D-35) | 3 | DONE (jitsuinfi-frontend `e9f5afb` (PR #7, di-merge `8b83506`; disesuaikan ke gaya app D-37 di `4998be7`)): halaman publik `#/index` menghitung ulang indeks dari snapshot papan di browser (wasm `rateIndex`), tabel per kelas tenor dengan kata-kata yang sama seperti CLI, k bisa dinaikkan (min 5), legenda kelas; tes `rate-index` mencocokkan baris dengan tabel CLI papan contoh. Diuji di build produksi: papan contoh dan papan testnet sama dengan `jitsuin index`, mobile 375 px tanpa scroll horizontal |

**HNK-09 — Verifier CLI hanko verify** · Lead Dex #dex · [[AC-HNK-09 - Verifier CLI hanko verify|AC]]

| Task | Deskripsi | Owner | Jam | Status |
|---|---|---|---|---|
| HNK-09.T1 | Perintah `jitsuin verify` (memakai ulang scanner) | Dex #dex | 3 | DONE (`8859598`, jitsuinfi-zcash PR #4 di-merge 19 Okt): crate `jitsuin-cli`, scan live via UFVK atau snapshot, cek bukti + bundel; 13 tes |
| HNK-09.T2 | Image Docker + instruksi `cargo install` | Dex #dex | 2 | DONE (`8859598`, PR #4): `Dockerfile`, workflow `verifier-image.yml`, README. Build dari sumber 9–15 mnt, jadi AC-HNK-09.1 + SPK-11 FAIL; fallback image jadi = usulan D-28. 2026-10-20: filter `paths` workflow ditambah `crates/jitsuin-flow/**` (dependensi `jitsuin-cli`) dan `examples/testnet/**` (ikut di-`COPY` ke image), karena PR #11 yang hanya mengubah `jitsuin-flow` tidak memicu job (`c5cb50c`, branch `hans/ci-verifier-image-paths`, lokal) |
| HNK-09.T3 | README: perintah persis + output yang diharapkan | Hans #hans (dari Dave, D-35) | 1 | DONE (jitsuinfi-zcash `27b46c6` (PR #14, di-merge `7f0653e`, CI hijau termasuk docker)): bagian "For judges" (HNK-28.T6) berisi perintah persis untuk papan testnet sungguhan; ditambah output `jitsuin index` yang diharapkan (`examples/testnet/expected-index.txt`, dicek byte per byte oleh tes `samples`) dan perintah Docker offline. Kedua perintah Docker offline mencetak persis file yang di-commit |

**HNK-12 — Spesifikasi gaya ZIP Shielded Receivable Registry** · Lead Hans #hans · [[AC-HNK-12 - Spesifikasi gaya ZIP Shielded Receivable Registry|AC]]

| Task | Deskripsi | Owner | Jam | Status |
|---|---|---|---|---|
| HNK-12.T1 | Tulis spesifikasi gaya ZIP | Hans #hans (dari Dave, D-35) | 3 | DONE (`c42af3e`): `docs/zip-shielded-receivable-registry.md` |
| HNK-12.T2 | Test vector dari spesifikasi dijalankan sebagai test | Dex #dex | 1 | TODO |
| HNK-12.T3 | Review teknis spesifikasi | Hans #hans | 1 | TODO — review oleh Hans sendiri: spesifikasi ditulis agent (DEV-11). Pra-review siap: [[Pra-review Spesifikasi dan Threat Model]]; checklist: [[Checklist Review HNK-11.T3 dan HNK-12.T3]] (24 temuan, 1 salah: griefing riwayat) |

**HNK-28 — Verifikasi publik lengkap** · Lead Hans #hans · [[AC-HNK-28 - Verifikasi publik lengkap|AC]] · Dibuat 2026-10-20 (D-30)

| Task | Deskripsi | Owner | Jam | Status |
|---|---|---|---|---|
| HNK-28.T1 | Layanan snapshot papan di relay (JSON same-origin). Rincian: `BL-D28-06` | Hans #hans (dari Dex, D-38) | 3 | TODO |
| HNK-28.T2 | `verifyProofOnBoard(proof, snapshot)` di wasm; layar Verify memakainya. Rincian: `BL-D27-05` | Hans #hans | 2 | DONE (jitsuinfi-zcash `32a3977`, `53016fe` (PR #9, di-merge `87424e7`); jitsuinfi-frontend `d13321e` (jitsuinfi-frontend PR #6, di-merge `5104a7d`)): web dan CLI memakai `proof_on_board` yang sama |
| HNK-28.T3 | `rateIndex(snapshot, k)` di wasm untuk halaman indeks HNK-08.T3. Rincian: `BL-D28-05` | Hans #hans | 1 | DONE (jitsuinfi-zcash `32a3977`, `53016fe` (PR #9, di-merge `87424e7`)): `rateIndex` sama dengan `jitsuin index --json` (fungsi `rate_index_json` bersama); halaman `#/index` milik HNK-08.T3 |
| HNK-28.T4 | Teks verdict bundel di layar Verify sesuai status surat dan settled. Rincian: `BL-D28-04` | Hans #hans (dari Dave, D-35) | 0,5 | DONE (jitsuinfi-frontend `1dcedf3` (PR #9, di-merge `36da302`)): verdict bundel mengikuti status surat: tanpa surat = invoice asli saja; surat menunggu seal = peringatan yang menyebut seal yang kurang dan "does not prove a financed deal yet"; "every seal checks out" hanya untuk surat yang disegel supplier, buyer, dan financier. Status settled tetap dari data papan |
| HNK-28.T5 | Teks dan tabel halaman orang luar sesuai TM #13 – #14. Rincian: `BL-D28-07` | Hans #hans (dari Dave, D-35) | 0,5 | DONE (jitsuinfi-frontend `604964a` (PR #10, di-merge `c3f7db7`)): halaman orang luar tidak lagi menyebut "hanya hash dan tanda tangan"; tabel memuat yang terlihat pemegang UFVK papan (sekarang siapa pun): waktu registrasi, kelas diskon dan tenor tiap entri, jenis entri (dengan/tanpa tag riwayat), settled dengan flag tepat waktu; yang tersembunyi diberi catatan jujur (tautan settled–register bagi pemegang N, pemberi pinjaman yang diberi riwayat bisa mengikuti invoice berikutnya). Diuji dengan memo papan testnet asli (register `89af294e…` RegisterWithHistory, settled `dcba74c6…` on_time) |
| HNK-28.T6 | Publikasi UFVK + birthday papan dan README juri (publikasi setelah izin user). Rincian: `BL-D28-01`, `BL-D0-05` | Hans #hans | 0,5 | DONE (jitsuinfi-zcash `5fdb4e3` (PR #10, di-merge `c73009b`, CI hijau termasuk gitleaks dan docker)): publikasi disetujui user 2026-10-20. `examples/testnet/` berisi UFVK papan, snapshot papan live (entri sampai blok 4511024) dan bukti balapan `TES-INV-0003` yang dibangun ulang dari papan; birthday 4508703. Bagian README "For judges": scan live, indeks, cek offline, layar Verify. Tes `published_testnet_board_and_proof_still_verify`. UFVK baru benar-benar publik saat repo dibuka (DEV-19) |

### Fase F5

**HNK-10 — Web app per peran** · Lead Hans #hans · [[AC-HNK-10 - Web app per peran|AC]]

| Task | Deskripsi | Owner | Jam | Status |
|---|---|---|---|---|
| HNK-10.T1 | Scaffold FE, routing, design system (tanpa CDN, CSP-ready) | Hans #hans (dari Dave, D-35) | 3 | DONE (`cdcba0d`, `98466b2` (`jitsuinfi-frontend`, lokal)) |
| HNK-10.T2 | Layar supplier: buat invoice, minta tanda tangan buyer | Hans #hans (dari Dave, D-35) | 3 | DONE (`cdcba0d`, `98466b2` (`jitsuinfi-frontend`, lokal)) |
| HNK-10.T3 | Layar tanda tangan buyer di browser (key di sisi klien) — FE krusial | Hans #hans | 2 | DONE: layar buyer (`cdcba0d`, `98466b2` (`jitsuinfi-frontend`, lokal)) + `jitsuin-wasm` |
| HNK-10.T4 | Skeleton backend API | Dex #dex | 3 | Dipindah ke HNK-23.T3 (DEV-13) |
| HNK-10.T5 | Deploy Railway + header CSP (setelah persetujuan user) | Dex #dex | 2 | Dipindah ke HNK-23.T5 (DEV-13) |
| HNK-10.T6 | Review keamanan penanganan key di FE | Hans #hans | 1 | DONE: review dicatat di TEST-HNK-10 (U-HNK-10.3) |
| HNK-10.T7 | Paket browser `jitsuin-wasm`: key buyer dari passkey PRF, tanda tangan invoice dan surat pengalihan, QR pelunasan, sertifikat riwayat, verifikasi bundel/bukti/riwayat di sisi klien — FE krusial | Hans #hans | 3 | DONE (`2438a82`) |

**HNK-11 — Threat model dan halaman orang luar** · Lead Hans #hans · [[AC-HNK-11 - Threat model dan halaman orang luar|AC]]

| Task | Deskripsi | Owner | Jam | Status |
|---|---|---|---|---|
| HNK-11.T1 | Finalisasi [[Threat Model]] | Hans #hans (dari Dave, D-35) | 2 | DONE: [[Threat Model]] final |
| HNK-11.T2 | Halaman "apa yang bisa dilihat orang luar" | Hans #hans (dari Dave, D-35) | 2 | DONE (`cdcba0d`, `98466b2` (`jitsuinfi-frontend`, lokal)): halaman orang luar + kartu explorer |
| HNK-11.T3 | Review kebenaran kebocoran Zcash | Hans #hans | 1 | TODO — review oleh Hans sendiri: threat model ditulis agent (DEV-11). Pra-review siap: [[Pra-review Spesifikasi dan Threat Model]]; checklist: [[Checklist Review HNK-11.T3 dan HNK-12.T3]] (16 temuan) |

**HNK-18 — Materi pitch dan visual** · Lead Hans #hans · [[AC-HNK-18 - Materi pitch dan visual|AC]]

| Task | Deskripsi | Owner | Jam | Status |
|---|---|---|---|---|
| HNK-18.T1 | Logo dan identitas visual JitsuinFi | Hans #hans (dari Dave, D-35) | 1 | TODO |
| HNK-18.T2 | Tiga slide video (masalah, threat model, penutup) | Hans #hans (dari Dave, D-35) | 1 | TODO |
| HNK-18.T3 | Diagram arsitektur untuk README | Hans #hans (dari Dave, D-35) | 1 | DONE (`d99680b`): diagram mermaid di README |
| HNK-18.T4 | Landing page immersive (visual 65% / caption 35%, tanpa UI kartu kotak), setara PortoWeb | Hans #hans (dari Dave, D-35) | 4 | IN PROGRESS: 6 bab + toggle EN/中文 selesai dan di-push (frontend `389b9d3`, 2026-10-19); bab 1–4 divalidasi user, bab 5–6 disetujui ("Mantap lanjut"); bab 5 butuh zcash PR#3 (wasm riwayat). Live di https://jitsuinfi.vercel.app (Vercel, deploy prebuilt 2026-10-19, header CSP + `frame-ancestors 'none'`). Lihat [[Landing Page - Brief]] |

**HNK-21 — Polish halaman internal web app** · Lead Dex #dex (dari Hans, D-29, DEV-12) · [[AC-HNK-21 - Polish halaman internal web app|AC]] · Dicatat 2026-10-19 (D-26), dikerjakan setelah backlog terbuka yang ada

| Task | Deskripsi | Owner | Jam | Status |
|---|---|---|---|---|
| HNK-21.T1 | Shell dan beranda `app.html`: nav, toggle EN/中文, pilihan peran sebagai adegan (bukan kartu) | Dex #dex (dari Hans, DEV-12) | 2 | TODO |
| HNK-21.T2 | Layar supplier: buat invoice sebagai lembar kertas, minta tanda tangan buyer | Dex #dex (dari Hans, DEV-12) | 2 | TODO |
| HNK-21.T3 | Layar buyer: tanda tangan, segel, QR pelunasan ZIP-321 | Dex #dex (dari Hans, DEV-12) | 2 | TODO |
| HNK-21.T4 | Layar financier: cek papan, rantai segel Sign-to-Pay, status advance | Dex #dex (dari Hans, DEV-12) | 2 | TODO |
| HNK-21.T5 | Layar verify: bukti dan bundel, verdict sebagai stempel | Dex #dex (dari Hans, DEV-12) | 2 | TODO |
| HNK-21.T6 | Layar orang luar: publik vs tersembunyi sebagai ilustrasi | Dex #dex (dari Hans, DEV-12) | 1 | TODO |
| HNK-21.T7 | i18n semua teks app, responsif 390 px, a11y, reduced motion | Dex #dex (dari Hans, DEV-12) | 2 | TODO |
| HNK-21.T8 | Regresi alur fungsional (siklus TES- sebelum vs sesudah) + deploy ulang Vercel | Dex #dex (dari Hans, DEV-12) | 1 | TODO |
| HNK-21.T9 | Pesan error yang terbaca untuk semua penolakan (riwayat, `EntryMismatch`, seal salah, settle tanpa klaim). Rincian: `BL-D23-11`, `BL-D24-07`, `BL-D25-05`, `BL-D26-07` | Hans #hans (dari Dave, D-35) | 1 | TODO |

**HNK-22 — Akun passkey peran dan kontak** · Lead Hans #hans · [[AC-HNK-22 - Akun passkey peran dan kontak|AC]] · Dibuat 2026-10-20 (D-30)

| Task | Deskripsi | Owner | Jam | Status |
|---|---|---|---|---|
| HNK-22.T1 | Satu passkey per orang: `create()` sekali, `excludeCredentials`, nama netral peran, profil lokal dengan `try/catch`, tolak authenticator tanpa PRF, mode demo test secret, `rp.id` eksplisit. Rincian: `BL-D21-01`, `BL-D21-02`, `BL-D21-03`, `BL-D21-18`, `BL-S00-01` | Hans #hans (dari Dave, D-35) | 2 | DONE (jitsuinfi-frontend `7814fbc` (PR #4, di-merge `a68f075`)) |
| HNK-22.T2 | Salt per peran dan salt inbox, turunan key per peran, sidik jari key publik, peran anggota tanpa key tanda tangan. Rincian: `BL-D21-04`, `BL-D21-05`, `BL-D21-06` | Hans #hans (dari Dave, D-35) | 2 | DONE (jitsuinfi-frontend `7814fbc` (PR #4, di-merge `a68f075`)); sidik jari dari HMAC master peran (DEV-18, disetujui) |
| HNK-22.T3 | Tambah atau ganti peran dan router `app.html` per peran (konsol financier tidak lagi di web app). Rincian: `BL-S00-03`, `BL-PG-01` | Hans #hans (dari Dave, D-35) | 1 | DONE (jitsuinfi-frontend `7814fbc` (PR #4, di-merge `a68f075`)); rute `/financier` masih bisa dibuka lewat alamat sampai konsol node ada (HNK-26) |
| HNK-22.T4 | Stempel: PRF baru per tanda tangan, key `Uint8Array` dinolkan, kunci sesi 15 menit. Rincian: `BL-D21-12` | Hans #hans (dari Dave, D-35) | 3 | DONE (jitsuinfi-frontend `7814fbc` (PR #4, di-merge `a68f075`)) |
| HNK-22.T5 | Kartu kontak (QR dan teks), impor kontak rekan, cocokkan sidik jari. Rincian: `BL-D21-11` | Hans #hans (dari Dave, D-35) | 2 | PARSIAL (jitsuinfi-frontend `f67e44e` (PR #13, di-merge `fe0d03a`)): kode kartu kontak `jitsuin-contact-v1:` (peran, `mailbox_pk`, sidik jari key) di bagian Mailbox, salin; kartu rekan ditempel dan disimpan di store terenkripsi. Sisa: QR, daftar kontak per peran, layar pencocokan sidik jari |
| HNK-22.T6 | Kotak masuk per peran: ambil pesan setelah masuk dan berkala, tampilkan sebagai tindakan. Rincian: `BL-S00-02`, `BL-S02-01` | Hans #hans (dari Dave, D-35) | 1 | PARSIAL (jitsuinfi-frontend `f67e44e` (PR #13, di-merge `fe0d03a`)): "Check inbox" di layar supplier dan buyer membuka, mengecek, dan menawarkan pesan sebagai tindakan; pesan palsu ditampilkan dan diabaikan. Sisa: ambil otomatis setelah masuk dan berkala, jenis pesan lain |
| HNK-22.T7 | Uji PRF dengan authenticator nyata, dua perangkat tersinkron, uji stateless; tabel dukungan authenticator. Rincian: `BL-D21-19`, `BL-D0-03` | Hans #hans (dari Dave, D-35) | 1 | TODO: butuh authenticator nyata dan dua perangkat (uji oleh user) |

**HNK-23 — Relay kotak surat end to end** · Lead Hans #hans · [[AC-HNK-23 - Relay kotak surat end to end|AC]] · Dibuat 2026-10-20 (D-30)

| Task | Deskripsi | Owner | Jam | Status |
|---|---|---|---|---|
| HNK-23.T1 | Skema pesan relay (jenis, versi, pengirim, batas ukuran PDF) dan tinjau ulang baris relay di [[Threat Model]]. Rincian: `BL-D1-01`, `BL-D22-05`, `BL-D0-08` | Hans #hans | 2 | DONE (jitsuinfi-frontend `d015312` (PR #5, di-merge `48caa3a`)): skema 15 jenis pesan, framing `JTSM`, batas PDF 2 MiB, tanda tangan Ed25519; baris relay Threat Model ditinjau terhadap skema (tinjau lagi setelah relay dibangun) |
| HNK-23.T2 | X25519 + AEAD dan `mailbox_id` = BLAKE2b(`mailbox_pk`) di `jitsuin-wasm` (dependensi disetujui Hans dulu). Rincian: `BL-D21-07` | Hans #hans (dari Dex, D-38) | 2 | DONE (jitsuinfi-zcash `370fa2a`, `ff411eb` (PR #15, di-merge `5c4e702`); jitsuinfi-backend `5143a65`): `jitsuin-core::mailbox`: key X25519 dari output PRF kedua, `mailbox_id` dan bukti kepemilikan sama dengan relay (vektor bersama, dicek silang dengan crypto Node), pesan tersegel konstruksi `crypto_box_seal` (overhead 48 byte), key low-order ditolak; export wasm `mailboxKeysBytes`, `mailboxProofBytes`, `mailboxOpenBytes`, `mailboxSeal` (PRF dan secret ephemeral dihapus setelah dipakai). Dependensi `x25519-dalek` 2.0.1 dan `crypto_box` 0.9.1 disetujui user 2026-10-20 |
| HNK-23.T3 | Skeleton backend API (dari HNK-10.T4). Basis data: Postgres Supabase (D-33). Rincian: `BL-D0-01` | Hans #hans (dari Dex, D-38) | 3 (dari HNK-10.T4) | DONE (jitsuinfi-backend `2d987dd` (PR #1, di-merge `0b41be5`)): repo private `JitsuinFi/jitsuinfi-backend` dibuat (persetujuan user 2026-10-20); TypeScript Node + Hono + `postgres` (pilihan user); Postgres Supabase lewat `DATABASE_URL` di `.env` (di-ignore git) atau variabel Railway, memory store bila kosong; migrasi `db/001_relay.sql` (RLS aktif, tanpa akses API Supabase); `.env.example` tanpa nilai |
| HNK-23.T4 | Endpoint kotak surat: daftar `mailbox_pk` + bukti kepemilikan, baca dengan challenge terenkripsi, masa simpan. Disimpan di Postgres Supabase (D-33). Rincian: `BL-D21-08`, `BL-D21-09` | Hans #hans (dari Dex, D-38) | 3 | DONE (jitsuinfi-backend `2d987dd` (PR #1, di-merge `0b41be5`)): `POST /api/mailbox/challenge`, `POST /api/mailbox` (bukti kepemilikan), `POST /api/mailbox/:id/read` (token baca 10 menit, hanya hash disimpan), kirim/daftar/ambil/hapus pesan tersegel, masa simpan 30 hari, maks 200 pesan per kotak; 6 tes memory store lulus, tes Postgres menunggu `TEST_DATABASE_URL` |
| HNK-23.T5 | Deploy Railway + header CSP (dari HNK-10.T5, setelah persetujuan user). Variabel lingkungan Supabase hanya di Railway (D-33). Rincian: `BL-D0-01` | Hans #hans (dari Dex, D-38) | 2 (dari HNK-10.T5) | DONE (2026-10-20, izin user "deploy Railway", "Merge #1, pindahin ke main"): project Railway `jitsuinfi-relay`, service `relay`, tersambung ke repo `JitsuinFi/jitsuinfi-backend` branch `main` (PR #1 di-merge `0b41be5`, deploy `391d7ba0` SUCCESS); `DATABASE_URL` (Session pooler) diisi lewat stdin CLI tanpa dicetak; deploy `74f4d522` SUCCESS, mode postgres; domain `https://relay-production-27dc.up.railway.app`: `/api/health` ok, challenge tersimpan, header `no-store` dan `nosniff`. Sisa: rewrite Vercel (HNK-23.T6, PR #14) |
| HNK-23.T6 | Rewrite Vercel `/api/*` ke relay, CSP tetap `connect-src 'self'`; konsol financier di origin node. Rincian: `BL-PG-01` | Hans #hans (dari Dave, D-35) | 2 | DONE (jitsuinfi-frontend PR #14, di-merge `b05d8e6`; produksi `https://jitsuinfi.vercel.app/api/health` = `{"ok":true}`, challenge lewat rewrite tersimpan): `vercel.json` rewrite `/api/:path*` ke `https://relay-production-27dc.up.railway.app/api/:path*`; diuji di preview Vercel (`vercel curl`): `/api/health` 200 `{"ok":true}` dengan CSP `connect-src 'self'`, challenge POST lewat rewrite tersimpan |
| HNK-23.T7 | Dokumen deal di web app lewat relay: invoice + PDF syarat, tanda tangan buyer, seal, sertifikat atau tag. Rincian: `BL-D22-05`, `BL-D22-08`, `BL-D26-04` | Hans #hans (dari Dex, D-38) | 3 | PARSIAL (jitsuinfi-frontend `f67e44e` (PR #13, di-merge `fe0d03a`)): kaki pertama tanpa salin-tempel: supplier mengirim invoice + PDF syarat (`invoice.sign_request`, ditandatangani key per invoice di wasm, disegel ke kotak surat buyer); buyer membuka dari kotak masuk, PDF dan invoice terisi di langkah 2, tanda tangan dikirim balik (`invoice.signature`); supplier "Check and keep" mencocokkan dengan deal. Diuji end to end (build produksi, dua sesi test data, relay lokal). Sisa: seal surat, sertifikat atau tag riwayat (BL-D26-04) |
| HNK-23.T8 | Pesan dari node bertanda tangan `financier_pk`: pembuka komitmen, surat + PDF surat, permintaan riwayat, s2, txid. Rincian: `BL-D23-06`, `BL-D24-03`, `BL-D24-11`, `BL-D26-01` | Hans #hans (dari Dex, D-38) | 2 | PARSIAL (2026-10-21, jitsuinfi-node PR #3 `e5c9185`): codec JTSM dan tanda tangan header Ed25519 dengan `financier_pk` di Rust (`src/message.rs`), cocok byte-per-byte dengan `relay-message.ts` (vektor `tests/vectors/jtsm-deal-letter.hex`, dua arah). Sisa: pesan per tipe (pembuka komitmen, surat + PDF, permintaan riwayat, s2, txid) dari deal API HNK-26.T5+ |

**HNK-24 — Alur deal di layar supplier** · Lead Hans #hans · [[AC-HNK-24 - Alur deal di layar supplier|AC]] · Dibuat 2026-10-20 (D-30)

| Task | Deskripsi | Owner | Jam | Status |
|---|---|---|---|---|
| HNK-24.T1 | Key per invoice dari master supplier di `jitsuin-core` + `jitsuin-wasm` (personalisasi sendiri, input unik), test vector. Rincian: `BL-D22-02` | Hans #hans | 2 | DONE (`a252568`, jitsuinfi-zcash `a252568` (jitsuinfi-zcash PR #8, di-merge `dbfc422`)) |
| HNK-24.T2 | Layar supplier memakai key turunan; unduh JSON plaintext dihapus; `invoice_id` dipakai ulang ditolak. Rincian: `BL-D22-03` | Hans #hans (dari Dave, D-35) | 1 | DONE (jitsuinfi-frontend `17a01ea` (PR #2, di-merge `2180881`)) |
| HNK-24.T3 | Penyimpanan dokumen deal lintas sesi di perangkat supplier dan buyer (IndexedDB terenkripsi dengan key dari PRF). Rincian: `BL-D1-02`, `BL-D22-07`, `BL-D22-10` | Hans #hans | 3 | DONE (`c7d4b1b`, jitsuinfi-frontend PR #1, di-merge `7fa4fae`; dipakai layar supplier `17a01ea`). Penyimpanan di layar buyer: HNK-25.T1 (DEV-16) |
| HNK-24.T4 | Kartu cek tanda tangan buyer (`bundleBuild`). Rincian: `BL-D22-09` | Hans #hans (dari Dave, D-35) | 1 | DONE (jitsuinfi-frontend `17a01ea` (PR #2, di-merge `2180881`)) |
| HNK-24.T5 | Tawarkan ke financier: pilih kontak, advance, alamat shielded baru per deal. Rincian: `BL-D23-01` | Hans #hans (dari Dave, D-35) | 2 | PARSIAL (jitsuinfi-frontend `17a01ea` (PR #2, di-merge `2180881`)): kode penawaran salin-tempel; kirim ke kotak surat financier menunggu relay HNK-23 (GAGAL AUDIT BL-D23-01) |
| HNK-24.T6 | Kartu tanda tangani entri papan (0x01 / 0x03) dengan kelas. Rincian: `BL-D23-09` | Hans #hans (dari Dave, D-35) | 1 | DONE (jitsuinfi-frontend `17a01ea` (PR #2, di-merge `2180881`); menunggu permintaan entri: jitsuinfi-frontend `7a0b911` (jitsuinfi-frontend PR #3, di-merge `7fe0118`)) |
| HNK-24.T7 | Segel surat dengan isi terbaca (`assignmentDecode`) dan cek PDF surat. Rincian: `BL-D24-05` | Hans #hans (dari Dave, D-35) | 0,5 | DONE (jitsuinfi-frontend `17a01ea` (PR #2, di-merge `2180881`)) |
| HNK-24.T8 | Status advance: txid, nominal, kecocokan dengan advance yang disepakati. Rincian: `BL-D24-13` | Hans #hans (dari Dave, D-35) | 1 | DONE (jitsuinfi-frontend `17a01ea` (PR #2, di-merge `2180881`)) |
| HNK-24.T9 | Halaman daftar deal: timeline per N, urutan pesan mengikuti SEQ-03. Rincian: `BL-S01-01`, `BL-S01-02` | Hans #hans (dari Dave, D-35) | 2 | PARSIAL (jitsuinfi-frontend `17a01ea` (PR #2, di-merge `2180881`); jitsuinfi-frontend `7a0b911` (jitsuinfi-frontend PR #3, di-merge `7fe0118`)): daftar deal dan timeline ADA; kartu entri menunggu kode permintaan entri dari financier (urutan SEQ-03, BL-S01-02 lulus audit ulang). Sisa: langkah pelunasan di timeline, butuh `settled` lewat relay (BL-S01-01) |

**HNK-25 — Alur deal di layar buyer** · Lead Hans #hans · [[AC-HNK-25 - Alur deal di layar buyer|AC]] · Dibuat 2026-10-20 (D-30)

| Task | Deskripsi | Owner | Jam | Status |
|---|---|---|---|---|
| HNK-25.T1 | Input PDF syarat, cek hash, tampilkan apakah `buyer_pk` = `invoice_pk(k)`. Rincian: `BL-D22-06` | Hans #hans (dari Dave, D-35) | 1 | DONE (jitsuinfi-frontend `cc9abb1` (PR #11, di-merge `dd63246`), `53f5e6a` (PR #12, di-merge `56b337a`); sempat GAGAL AUDIT BL-D22-07 dan BL-D1-02 2026-10-20; perbaikan: jitsuinfi-frontend `53f5e6a` (PR #12): invoice yang diterima disimpan di store terenkripsi buyer, daftar "Your invoices", Open mengisi semua langkah): langkah 2 buyer menerima PDF syarat; "Check invoice" (satu sentuhan passkey) mencocokkan hash PDF dengan `terms_hash` dan mencari key buyer yang dituju (#k); "Sign invoice" mati sampai keduanya lolos dan terkunci lagi bila invoice atau file berubah. Diuji di build produksi dengan sesi buyer test data dan invoice `TES-INV-T25`: tanpa PDF, PDF lain, key lain, keduanya benar (tanda tangan jadi), invoice diedit |
| HNK-25.T2 | Nomor `k` otomatis dari rantai yang tertambat, kepala rantai bertanda tangan, bagikan `invoice_pk(k)`, layar permintaan riwayat. Rincian: `BL-D26-03`, `BL-D22-01`, `BL-D26-02` | Hans #hans | 3 | PARSIAL (jitsuinfi-zcash `88af897` (PR #9, di-merge `87424e7`); jitsuinfi-frontend `0e59952` (jitsuinfi-frontend PR #6, di-merge `5104a7d`)): `k` otomatis dari rantai tertambat, sertifikat tak tertambat dibuang, sertifikat terakhir yang hilang terdeteksi lewat tag penerus di papan. Sisa: bagikan `invoice_pk(k)` dan permintaan riwayat lewat relay, kepala rantai di relay (HNK-23) |
| HNK-25.T3 | Segel surat buyer dengan isi terbaca dan cek PDF surat. Rincian: `BL-D24-06` | Hans #hans (dari Dave, D-35) | 0,5 | TODO |
| HNK-25.T4 | QR hanya untuk surat `Sealed`, menunggu s2, alamat bayar ditampilkan. Rincian: `BL-D25-01`, `BL-S02-02` | Hans #hans (dari Dave, D-35) | 1 | TODO |
| HNK-25.T5 | Pengingat jatuh tempo lokal. Rincian: `BL-D25-02` | Hans #hans (dari Dave, D-35) | 1 | TODO |
| HNK-25.T6 | Kartu riwayat saya (`verifyHistory` + snapshot). Rincian: `BL-D26-09` | Hans #hans (dari Dave, D-35) | 1 | TODO |
| HNK-25.T7 | Status pelunasan di layar buyer dan supplier (`bundleOnBoard` + snapshot). Rincian: `BL-D25-09` | Hans #hans (dari Dave, D-35) | 1 | TODO |
| HNK-25.T8 | Bayar QR di testnet (Zodl atau `zcash-devtool`) dan dana testnet untuk peserta uji. Rincian: `BL-D25-10` | Hans #hans (dari Dave, D-35) | 1 | TODO |

**HNK-26 — Konsol dan API node financier** · Lead Hans #hans · [[AC-HNK-26 - Konsol dan API node financier|AC]] · Dibuat 2026-10-20 (D-30)

| Task | Deskripsi | Owner | Jam | Status |
|---|---|---|---|---|
| HNK-26.T1 | Skrip setup node testnet: seed di node, key financier, key kotak surat, UFVK papan. Rincian: `BL-D21-14`, `BL-D0-02` | Hans #hans (dari Dex, D-38) | 1 | DONE (2026-10-21, jitsuinfi-node PR #1 di-merge `9aa7f07`; deploy CI diperbaiki PR #2 `0acece0`): `jitsuin-node setup` membuat `node.key` (0600), key financier dan key kotak surat turunan, wallet zcash-devtool (seed terenkripsi ke identitas age 0600) dan watch wallet UFVK papan; idempoten; stdout devtool dibuang. Service Railway `financier-node` + volume `/data` di project relay; biner dibangun di GitHub CI lalu `railway up` |
| HNK-26.T2 | Pairing passkey konsol (kode sekali pakai, attestation, D9) + halaman pairing. Rincian: `BL-D21-15`, `BL-D21-16` | Hans #hans (dari Dex, D-38) | 2 | DONE (2026-10-21, jitsuinfi-node `1ae2ef4`, PR #4 di-merge `05be50d`; domain `https://financier-node-production.up.railway.app` dan variabel `NODE_ORIGIN` di-set atas izin user "domain juga boleh"): `jitsuin-node pair` (kode sekali pakai 15 menit, hanya hash disimpan, gugur setelah 5 salah), registrasi passkey webauthn-rs untuk `rp.id` = host `NODE_ORIGIN` dengan UV wajib, credential di D9 `console-credentials.json` (0600), halaman `/console/pair` (lembar sign-in app, DS-PAL, hanko 認), CSP same-origin dan cek `Origin`. Diuji lokal di browser pane: pairing berhasil, kode lama ditolak, authenticator yang sama ditolak `excludeCredentials` |
| HNK-26.T3 | Sesi konsol: challenge sekali pakai, origin, `rpIdHash`, UV, cookie `__Host-`. Rincian: `BL-D21-17` | Hans #hans (dari Dex, D-38) | 1 | DONE (2026-10-21, jitsuinfi-node `9ee845a`, lokal, belum PR): challenge sekali pakai 2 menit, assertion dicek webauthn-rs (origin, `rpIdHash`, UV, signature, counter), sesi 8 jam di cookie `__Host-jitsuin_console` (`Secure`, `HttpOnly`, `SameSite=Strict`), token disimpan sebagai SHA-256 di memori; halaman `/console/`. Diuji lokal: assertion yang sama dikirim ulang ditolak (410), assertion lama untuk challenge baru ditolak (403), cookie tidak terbaca JS, logout menutup sesi |
| HNK-26.T4 | Key kotak surat financier di node dan proxy `/node/mail/*`. Rincian: `BL-D21-10` | Hans #hans (dari Dex, D-38) | 1 | PARSIAL (2026-10-21, jitsuinfi-node PR #3 `e5c9185`): key kotak surat dari `node.key`, registrasi ke relay saat `serve` (dengan backoff), klien relay Rust (token baca, list/ambil/hapus, kirim tersegel), kartu kontak financier di `/node/info`, perintah `inbox`; diuji ke relay produksi. Sisa: proxy `/node/mail/*` untuk konsol (setelah sesi konsol HNK-26.T3) |
| HNK-26.T5 | Penawaran masuk: cek tanda tangan buyer sebelum `Deal`, tetapkan advance dan konfirmasi. Rincian: `BL-D23-02` | Hans #hans (dari Dex, D-38) | 2 | TODO |
| HNK-26.T6 | Tolak atau kedaluwarsa penawaran. Rincian: `BL-D23-03` | Hans #hans (dari Dex, D-38) | 1 | TODO |
| HNK-26.T7 | Registri `identity_pk` buyer hasil KYC. Rincian: `BL-D26-05` | Hans #hans (dari Dex, D-38) | 1 | TODO |
| HNK-26.T8 | API `check_buyer` dengan `MinimumStandard`, simpan laporan dan `history_tag`. Rincian: `BL-D26-06` | Hans #hans | 1 | TODO: fungsi `check_buyer` (laporan + tag) sudah ada di `jitsuin-flow` sejak HNK-20.T3; sisa endpoint `POST /node/history/check` dan penyimpanan tag menunggu node (HNK-26.T1) |
| HNK-26.T9 | Pengaturan policy di konsol: allowlist, standar minimal, tenggang. Rincian: `BL-D26-08` | Hans #hans (dari Dave, D-35) | 2 | TODO |
| HNK-26.T10 | Persistensi state deal dan dokumen deal di node (lanjut setelah restart). Rincian: `BL-D23-13`, `BL-D1-03` | Hans #hans | 3 | PARSIAL (jitsuinfi-zcash `23be34a` (PR #12, di-merge `1792397`)): snapshot deal `Flow::to_bytes` / `Flow::from_bytes` (format `JTSF` v1, tanpa dependency baru); pemuatan mengecek ulang deal, entri kita, dan segel surat, jadi snapshot rusak atau diedit ditolak. Sisa: penyimpanan di node dan dokumen deal (PDF) di disk node (HNK-26.T1) |
| HNK-26.T11 | Penjadwal pelunasan berkala (tenggang dan tanggal dari konfigurasi). Rincian: `BL-D25-03` | Hans #hans (dari Dex, D-38) | 2 | TODO |
| HNK-26.T12 | Penjadwal mengingat txid `settled` yang sudah dikirim. Rincian: `BL-D25-06` | Hans #hans (dari Dex, D-38) | 1 | TODO |
| HNK-26.T13 | Status pelunasan dan sengketa di konsol, ekspor bukti (klaim buyer + txid). Rincian: `BL-D25-04` | Hans #hans | 2 | PARSIAL (jitsuinfi-zcash `2fd155e` (PR #13, di-merge `bda24bc`)): file bukti pelunasan `settlement::Evidence` (format `JTSE` v1): dokumen pelunasan, klaim buyer bertanda tangan, setiap output pelunasan untuk N (txid, tinggi, nilai, receipt buyer); `Evidence::check` mengecek ulang tanda tangan dan menghitung ulang status (`Claimed` / `Disputed` / `Overdue`). Nilai dan tinggi output tidak bertanda tangan, hanya viewing key financier yang mengonfirmasi. Sisa: kartu status dan unduhan di konsol (HNK-26.T2 – T3) |
| HNK-26.T14 | Bukti `DoubleFinanced`: `proof_from_lookup` di node + kartu bukti ganda. Rincian: `BL-D27-02`, `BL-D27-04` | Hans #hans | 2 | PARSIAL (jitsuinfi-zcash `0ee55c6` (PR #11, di-merge `01ecdc3`)): `Flow::double_sign_proof(buyer_signature)` membangun bukti dari `Stopped(DoubleFinanced)` lewat `proof_from_lookup`, tanda tangan buyer dicek dulu; bukti lolos aturan `jitsuin verify` terhadap papan. Sisa: simpan bukti di deal (node, HNK-26.T1/T10) dan kartu unduh di konsol (HNK-26.T2 – T3) |
| HNK-26.T15 | Persetujuan operator per deal (assertion passkey) sebelum `Pay`. Rincian: `BL-D24-09` | Hans #hans (dari Dex, D-38) | 1 | TODO |
| HNK-26.T16 | Pipeline deal per state dan detail deal di konsol. Rincian: `BL-S03-01`, `BL-D23-08`, `BL-D23-14`, `BL-D27-01` | Hans #hans (dari Dex, D-38) | 2 | TODO |
| HNK-26.T17 | Alamat shielded diversified baru per deal dari wallet node. Rincian: `BL-D24-01` | Hans #hans (dari Dex, D-38) | 1 | TODO |
| HNK-26.T18 | Kirim bundel JTSB ke buyer dan supplier setelah settled. Rincian: `BL-D25-08` | Hans #hans (dari Dex, D-38) | 1 | TODO |
| HNK-26.T19 | Konfigurasi jaringan satu tempat (testnet / mainnet) di web app, node, CLI. Rincian: `BL-D0-04` | Hans #hans (dari Dex, D-38) | 1 | TODO |

### Fase F6

**HNK-13 — Uji dengan pengguna sungguhan** · Lead Hans #hans · [[AC-HNK-13 - Uji dengan pengguna sungguhan|AC]]

| Task | Deskripsi | Owner | Jam | Status |
|---|---|---|---|---|
| HNK-13.T1 | Rekrut dan jadwalkan 2–3 peserta | Hans #hans (dari Dave, D-35) | 1 | TODO |
| HNK-13.T2 | Jalankan sesi uji + kumpulkan kutipan (dengan izin) | Hans #hans (dari Dave, D-35) | 2 | TODO |
| HNK-13.T3 | Dukungan masalah on-chain selama sesi | Hans #hans | 1 | TODO |

**HNK-14 — Submission video deskripsi dan demo URL** · Lead Hans #hans · [[AC-HNK-14 - Submission video deskripsi dan demo URL|AC]]

| Task | Deskripsi | Owner | Jam | Status |
|---|---|---|---|---|
| HNK-14.T1 | Rekam dan edit video 2 menit | Hans #hans (dari Dave, D-35) | 4 | TODO |
| HNK-14.T2 | Deskripsi ≤ 2.000 karakter + pengungkapan AVAL | Hans #hans (dari Dave, D-35) | 1 | PARSIAL: draf di [[Submission - Deskripsi]] (1.801 karakter), menunggu review Hans (D-35) |
| HNK-14.T3 | Checklist publikasi repo (lisensi, README, txid) | Dex #dex | 1 | TODO |
| HNK-14.T4 | Submit final dari akun pendaftar | Hans #hans | 1 | TODO |

**HNK-17 — QA E2E lintas item** · Lead Hans #hans · [[AC-HNK-17 - QA E2E lintas item|AC]]

| Task | Deskripsi | Owner | Jam | Status |
|---|---|---|---|---|
| HNK-17.T1 | E2E putaran 1 (HNK-01 – HNK-07) | Hans #hans (dari Dave, D-35) | 3 | TODO |
| HNK-17.T2 | E2E putaran 2 (HNK-08 – HNK-11) | Hans #hans (dari Dave, D-35) | 2 | TODO |
| HNK-17.T3 | Retest bug yang sudah diperbaiki | Hans #hans (dari Dave, D-35) | 1 | TODO |
| HNK-17.T4 | E2E arsitektur target per business flow (BF-01 – BF-12, [[FD-02 - Penelusuran Business Flow ke Backlog]]) lewat relay dan node testnet. Rincian: `BL-D0-07`, `BL-D22-11`, `BL-D23-15`, `BL-D24-14`, `BL-D26-10`, `BL-D29-08`, `BL-S00-04`, `BL-S01-03`, `BL-S02-03`, `BL-S03-03`, `BL-S04-01`, `BL-S05-02` | Hans #hans (dari Dave, D-35) | 3 | TODO |

### Fase F7

**HNK-15 — Stretch JitsuinFi Vault** · Lead Hans #hans · [[AC-HNK-15 - Stretch JitsuinFi Vault|AC]]

| Task | Deskripsi | Owner | Jam | Status |
|---|---|---|---|---|
| HNK-15.T1 | Merkle sum tree kewajiban | Hans #hans (dari Dex, D-38) | 3 | TODO |
| HNK-15.T2 | Uji solvabilitas lewat FVK akun operasional (Zcash) | Hans #hans | 3 | DONE (`e54ea36`) |
| HNK-15.T3 | Halaman verifikasi anggota | Hans #hans (dari Dave, D-35) | 2 | TODO |

**HNK-29 — Alur dana anggota** · Lead Hans #hans · [[AC-HNK-29 - Alur dana anggota|AC]] · Dibuat 2026-10-20 (D-30)

| Task | Deskripsi | Owner | Jam | Status |
|---|---|---|---|---|
| HNK-29.T1 | Pencatatan setoran di node manajer: id anggota acak, kuitansi ke kotak surat anggota. Rincian: `BL-D29-02` | Hans #hans (dari Dex, D-38) | 1 | TODO |
| HNK-29.T2 | Jalur Merkle per periode lewat relay dan verifikasi inklusi terhadap root + total JTLR. Rincian: `BL-D29-04`, `BL-D29-05` | Hans #hans (dari Dex, D-38) | 1 | TODO |
| HNK-29.T3 | Batas uji solvabilitas dan kebocoran (nominal setoran, alamat supplier) di halaman anggota; panduan UFVK lewat saluran privat. Rincian: `BL-S05-01`, `BL-D0-06` | Hans #hans (dari Dave, D-35) | 1 | TODO |

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
| DEV-12 | 2026-10-20 | HNK-21 (T1 – T8), HNK-05.T4 | Owner Hans | Owner **Dex** (D-29 Opsi B dijalankan); HNK-21.T9 baru untuk Dave | Porsi 40/30/30 | **Disetujui user 2026-10-19** (D-29) dan 2026-10-20 ("Setuju semua sesuai rekomendasi, gas bikin HNK-nya") |
| DEV-13 | 2026-10-20 | HNK-10.T4, HNK-10.T5 | Bagian HNK-10 | Diserap HNK-23 (relay) sebagai HNK-23.T3 dan HNK-23.T5, owner tetap Dex | Relay butuh skeleton backend dan deploy yang sama | **Disetujui user 2026-10-20** |
| DEV-14 | 2026-10-20 | HNK-27.T1, [[Format Data]] | P-08: salt komitmen CSPRNG 32 byte, disimpan per (invoice, financier), dipakai ulang saat retry | Salt **diturunkan**: `BLAKE2b-256(key = secret key financier, personalisasi "JitsuinCommSalt_", "salt" ‖ N)`. Retry tetap memberi komitmen yang sama, tanpa penyimpanan dan tanpa dependensi CSPRNG baru; tetap tidak bisa ditebak tanpa key financier | Tujuan P-08 (tidak pernah dua komitmen per financier) tercapai lebih sederhana | **Disetujui user 2026-10-20** ("Setuju DEV-14, gas push dan buka PR") |
| DEV-15 | 2026-10-20 | HNK-24.T2, HNK-24.T4 – T9 | Owner Dave | Owner tetap Dave; dikerjakan Hans (agent) sebagai backup, seperti DEV-11; Dave me-review | Permintaan user ("Lanjut kerjain HNK-24.T4 sampai T9", "sekalian kerjain T2") | **Disetujui user 2026-10-20** |
| DEV-16 | 2026-10-20 | BL-D22-07, BL-D1-02 (`-backlogs`, baseline D-32) | BL-D22-07 (buyer menyimpan invoice yang diterima) dan BL-D1-02 (semua aliran D4) hanya merujuk HNK-24.T3 | BL-D22-07 merujuk HNK-25.T1 (layar buyer, yang memang menulisnya); BL-D1-02 merujuk HNK-24.T3 dan HNK-25.T1. HNK-24.T3 (store + pemakaian di layar supplier) menjadi DONE | Penyimpanan di sisi buyer adalah pekerjaan layar buyer, bukan pekerjaan store | **Disetujui user 2026-10-20** |
| DEV-17 | 2026-10-20 | HNK-22 (T1 – T7) | Owner Dave | Owner tetap Dave; dikerjakan Hans (agent) sebagai backup, hanya lokal sampai user mengecek | Permintaan user ("HNK-22 km kerjain sebagai backup tp stay local dulu aja") | **Disetujui user 2026-10-20** |
| DEV-18 | 2026-10-20 | HNK-22.T2, BL-D21-05 | "Tampilkan sidik jari key publik" | Sidik jari = HMAC-SHA-256(key = master peran, `jitsuin-fingerprint-v1:<peran>`), 10 byte pertama, base32 `XXXX-XXXX-XXXX-XXXX` | Supplier tidak punya satu key publik peran (key per invoice, P-03) dan anggota tanpa key tanda tangan; HMAC master memberi sidik jari yang sama untuk semua peran tanpa membuka master. Kartu kontak (HNK-22.T5) nanti memakai sidik jari `mailbox_pk` | **Disetujui user 2026-10-20** |
| DEV-19 | 2026-10-20 | D-17 (repo privat sampai menjelang submit) | Semua repo `JitsuinFi` privat | `jitsuinfi-frontend` ditemukan **public** di GitHub saat dicek 2026-10-20 (`jitsuinfi-vault` dan `jitsuinfi-zcash` privat) | Belum diketahui disengaja atau tidak. Perbaikan bila tidak disengaja: Settings → Danger Zone → Change visibility (oleh user). Lihat [[Rencana Akun Server]] | _Menunggu keputusan user_ |
| DEV-20 | 2026-10-20 | Semua task Dave | Target 40/30/30; task Dave tetap milik Dave, Hans hanya backup (D-25, DEV-11) | Semua task Dave, lead item Dave, SPK Dave, dan owner `BL-…` Dave dipindah ke Hans (D-35) | Keputusan user | **Disetujui user 2026-10-20** ("semua tasks Dave di migrate ke saya aja (Hans)") |
| DEV-21 | 2026-10-20 | HNK-21 (Dex) | Penyelarasan app ke palet utama dan gaya tanpa kartu bagian dari HNK-21 (Dex) | Hans mengerjakan fondasinya lebih dulu (D-36, D-37; PR #8 di-merge `e0f0a66`): token DS-PAL, gaya iOS dari `09-Design` (lembar kertas, panel kolam, nav pill / tab bar, daftar berkelompok, stepper segel), verdict cap hanko, di `src/style.css` dan `ui.ts` (jitsuinfi-frontend `ba9383a`, PR #8). HNK-21.T1 – T8 tetap milik Dex untuk adegan per layar, ilustrasi, i18n, dan regresi | Permintaan user: palet diselaraskan sekarang | **Disetujui user 2026-10-20** ("Ya, selaraskan sekarang") |
| DEV-22 | 2026-10-20 | Task backend Dex | Relay, node, snapshot, node dana, API financier milik Dex (D-29, DEV-12) | 26 task dipindah ke Hans (D-38); lead HNK-23, HNK-26, HNK-28, HNK-29 jadi Hans | Keputusan user, supaya app production-ready | **Disetujui user 2026-10-20** ("Pindahin task backend Dex ke saya, mulai relay") |
| DEV-23 | 2026-10-21 | HNK-26.T4, kartu kontak financier | Sidik jari kartu kontak = HMAC atas master peran (DEV-18) | Node: SHA-256(`jitsuin-fingerprint-v1:financier:` ‖ `financier_pk`), 10 byte pertama, base32 grup 4 (format tampilan sama) | Node punya satu key publik financier; rekan bisa menghitung ulang dari `financier_pk` yang ia terima | **Disetujui user 2026-10-21** ("DEV-23 disetujui") |
| DEV-05 | 2026-10-16 | SPK-04 | [[Rencana Fase]]: SPK-04 spike kritis | SPK-04 tidak lagi kritis; gerbang F0 dihitung tanpa SPK-04 | D-15: Zodl opsional (keputusan user) | **Mengikuti keputusan user 2026-10-16** |
