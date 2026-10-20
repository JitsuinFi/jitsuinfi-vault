---
tags: [test, "HNK-09"]
type: test
id: HNK-09
phase: F4
lead: Dex
owners: [Dex, Hans]
unit: PASS
integrasi: BLOCKED
e2e: TODO
updated: 2026-10-19
---

# TEST-HNK-09 - Verifier CLI hanko verify

> **Peta link:** [[Testing Hub]] · [[Backlog]] · [[AC-HNK-09 - Verifier CLI hanko verify|AC]] · **Test** · [[ES-HNK-09 - Verifier CLI hanko verify|Exec Summary]]

**Lead:** Dex #dex · **Tim:** Dex #dex, Hans #hans 

## 1. Unit
Logika murni, cepat, tanpa DB dan tanpa chain.

| ID | Kasus | Hasil | Tanggal | Bukti |
|---|---|---|---|---|
| U-HNK-09.1 | Parsing argumen | PASS | 2026-10-19 | `crates/jitsuin-cli/src/args.rs`, 5 tes (PR #4): help/versi; snapshot + `--proof`/`--bundle` berulang; default scan live per jaringan dari prefix UFVK (folder wallet, lightwalletd); override + `$JITSUIN_DEVTOOL`; 11 kombinasi salah ditolak (dua sumber, opsi live tanpa `--ufvk`, UFVK bukan unified, nilai kosong, opsi ganda, opsi tak dikenal). Plus 3 tes `board.rs`: snapshot bolak-balik, snapshot rusak, wallet baru tanpa `--birthday` dan devtool tidak ada → pesan jelas. |
| U-HNK-09.2 | Format output | PASS | 2026-10-19 | `crates/jitsuin-cli/tests/samples.rs`, 5 tes yang menjalankan biner: output teks = `examples/verify/expected-output.txt` byte demi byte; `--json` dengan vonis yang sama; papan dipotong → baris `FAIL` per klaim + exit 1; bukti diubah 1 bit → exit 1; argumen atau berkas salah → exit 2. Contoh papan/bukti/bundel dibangun ulang dari key tetap dan harus sama dengan berkas yang di-commit. |

## 2. Integrasi
Skrip vs DB/chain sungguhan. Semua artefak memakai prefix `TES-` (invoice, akun, label, order).

| ID | Skenario | Hasil | Tanggal | Bukti (txid/log) |
|---|---|---|---|---|
| I-HNK-09.1 | Verifikasi papan uji mainnet dari container bersih | BLOCKED | 2026-10-19 | Container dibangun dari nol di runner GitHub dan contoh terverifikasi di dalamnya (lihat [[SPK-11 - Distribusi verifier CLI di mesin bersih\|SPK-11]]). Scan papan sungguhan menunggu UFVK + blok pertama papan dari Hans: isi variabel repo `BOARD_UFVK` dan `BOARD_BIRTHDAY`, langkah CI-nya sudah ada di `verifier-image.yml`. |

**Bukti pembersihan:** sisa artefak off-chain `TES-` = **0** (container CI dibuang setelah run; belum ada wallet watch-only yang dibuat). Artefak on-chain tidak bisa dihapus; catat txid-nya di tabel di atas. Data produksi tidak boleh tersentuh.

## 3. E2E
Panduan langkah demi langkah untuk user.

- [ ] Salin perintah dari README dan dapatkan hasil yang sama. (Contoh: lulus. Papan sungguhan: menunggu UFVK + T3.)

| Langkah | Hasil diharapkan | Hasil aktual | Status |
|---|---|---|---|
| 1 | `docker build -t jitsuin .` lalu `docker run --rm jitsuin verify --board examples/verify/board-sample.json --proof examples/verify/proof-sample.txt --bundle examples/verify/bundle-sample.txt` → sama persis dengan `examples/verify/expected-output.txt`, akhir `Result   PASS (7 check(s), 0 failed)` | CI menjalankan perintah README ini di runner bersih dua kali (PR #4 dan #5): build 550 dtk dan 868 dtk, output = `expected-output.txt` (`diff` kosong) di keduanya, https://github.com/JitsuinFi/jitsuinfi-zcash/actions/runs/39239022151 · https://github.com/JitsuinFi/jitsuinfi-zcash/actions/runs/39239847330 | PASS |
| 2 | Perintah papan sungguhan di README (T3) → entri dan bundel yang dicantumkan terverifikasi | — | TODO |
