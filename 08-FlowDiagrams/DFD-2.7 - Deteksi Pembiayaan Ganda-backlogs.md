---
tags: [flow, backlog]
status: DITETAPKAN
progress: 4/6 SELESAI
updated: 2026-10-20
---

# DFD-2.7 - Deteksi Pembiayaan Ganda-backlogs

**Diagram:** [[DFD-2.7 - Deteksi Pembiayaan Ganda]] · Rencana: [[FD-01 - Keputusan Usulan dan Gelombang Kerja]] · [[FD-02 - Penelusuran Business Flow ke Backlog]] · Backlog: [[Backlog]]

Task untuk proses 7.1 – 7.5. Aturan kolom sama dengan [[DFD-2.1 - Identitas dan Sesi-backlogs]].

Kolom Status mengikuti langkah 6 "Audit flow diagram" di [[Workflow Development]]: `TODO` → `DIKERJAKAN` → `AUDIT` (semua task backlog-nya DONE) → `SELESAI (tanggal, bukti)` atau `GAGAL AUDIT (tanggal, alasan)`; `DITUNDA` hanya dengan keputusan user. Antrean audit tampil di setiap `python3 scripts/sync-vault.py` (lewat `scripts/check-backlogs.py`). Backlog ini ditetapkan 2026-10-20 (D-32).

## Task

| ID | Elemen | Task | Selesai bila | Ref | Task backlog | Owner | Status |
|---|---|---|---|---|---|---|---|
| BL-D27-01 | 7.1, F7.01 – F7.02 | Konsol menampilkan `Stopped(AlreadyFinanced)` dan `Stopped(DoubleFinanced)` dan menutup deal | Deal berhenti tampil sebagai "dihentikan, tanpa transaksi" | HNK-05.T4 | HNK-26.T16, HNK-32.T3 | Hans | SELESAI (2026-10-22, audit ulang setelah HNK-32.T3: deal berhenti berbunyi "The deal stopped here: no entry was posted and no money left this node." (`stopReason`, diuji, juga untuk dump node lama)) |
| BL-D27-02 | 7.2, F7.03, F7.05 | Node memanggil `proof_from_lookup` saat `Stopped(DoubleFinanced)` dan menyimpan bukti di deal | Bukti tersimpan dan lolos `jitsuin verify` | C-23 | HNK-26.T14 | Hans | SELESAI (2026-10-22, audit: `drive` memanggil `deals::double_proof` (`main.rs:1435`) yang memakai `Flow::double_sign_proof` + `proof.verify()`; U-HNK-26.4 `a_double_financed_deal_gives_a_proof_that_holds_on_the_board`; `cargo test` node 49/49; format diterima `jitsuin verify --proof`, node `e1ac72a`) |
| BL-D27-03 | 7.3, F7.06 – F7.07 | `doubleSignProof` di `jitsuin-wasm` menerima posisi papan | Bukti dari wasm dengan posisi lolos `jitsuin verify` | K-3 | HNK-27.T4 | Hans | SELESAI (2026-10-20, `14803af`, U-HNK-27.8) |
| BL-D27-04 | 7.3, 7.5 | Kartu "Bukti ganda" di konsol: tampilkan dan unduh bukti untuk pihak berwenang | Operator mengunduh bukti dari konsol | C-23 | HNK-26.T14, HNK-32.T5 | Hans | AUDIT (2026-10-22, audit ulang setelah HNK-32.T5: tombol unduh Exhibit A dan bukti lengkap ada di kartu 重; sisa: belum tampil dengan deal `DoubleFinanced` nyata di konsol) |
| BL-D27-05 | 7.4, F7.08 – F7.10 | `verifyProofOnBoard(proof, snapshot)` di `jitsuin-wasm`; layar Verify memakai snapshot dan tidak lagi menulis posisi yang hanya diklaim sebagai fakta | Bukti tanpa posisi entri pertama FAIL di web, sama dengan CLI | K-8 | HNK-28.T2 | Hans | SELESAI (2026-10-20, `32a3977`, `d13321e`: layar Verify memakai `verifyProofOnBoard`; tanpa data papan posisi ditulis "claimed, not checked"; bukti tanpa posisi entri pertama FAIL di web dan di `jitsuin verify`, tiga kasus TES- dibandingkan langsung, U-HNK-28.1, I-HNK-28.2) |
| BL-D27-06 | Uji | Integrasi testnet: dua financier mendaftarkan N yang sama, bukti dari `proof_from_lookup` diverifikasi CLI dan web | Kasus tercatat di TEST-HNK-07 (I-HNK-07.x) | HNK-07.T4 | HNK-07.T4 | Dex | TODO |

## Sudah ada (tanpa task baru)

- 7.1 state `Stopped` (`Flow::on_board`), fungsi `proof_from_lookup` dan `proof_from_offer`, 7.4 verifikasi CLI (`check_proof`, `verify_proof_on_board`), 7.5 unduh di layar Verify.

## Roadmap

- F7.04 bukti untuk `AlreadyFinanced` dari entri yang ditawarkan (P-14): tidak aman seperti tertulis, butuh perubahan format entri.
