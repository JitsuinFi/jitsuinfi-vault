---
tags: [test, "HNK-28"]
type: test
id: HNK-28
phase: F4
unit: PASS
integrasi: PARSIAL
e2e: TODO
updated: 2026-10-20
---

# TEST-HNK-28 - Verifikasi publik lengkap

> **Peta link:** [[Testing Hub]] · [[Backlog]] · [[AC-HNK-28 - Verifikasi publik lengkap|AC]] · **Test** · [[ES-HNK-28 - Verifikasi publik lengkap|Exec Summary]]

## 1. Unit
Logika murni, cepat, tanpa DB dan tanpa chain.

| ID | Kasus | Hasil | Tanggal | Bukti |
|---|---|---|---|---|
| U-HNK-28.1 | `verifyProofOnBoard` menolak posisi palsu | PASS | 2026-10-20 | `jitsuin-wasm` tes `proofs_and_the_rate_index_are_checked_against_board_data_as_in_the_cli`: posisi di papan, entri kedua hilang, tanpa posisi pertama, posisi geser, tanda tangan palsu (`32a3977`) |
| U-HNK-28.2 | `rateIndex` sama dengan `rate_index` | PASS | 2026-10-20 | Tes yang sama: k = 1, 5, 9 sama persis dengan `rate_index_json` (`32a3977`) |
| U-HNK-28.3 | Snapshot dan bukti testnet yang dipublikasikan tetap terverifikasi | PASS | 2026-10-20 | `jitsuin-cli` tes `published_testnet_board_and_proof_still_verify`: output sama persis dengan `examples/testnet/expected-output.txt`, entri di 4509299/2/0 dan 4509521/3/0, UFVK berawalan testnet (`5fdb4e3`) |
| U-HNK-28.4 | Verdict bundel sesuai status surat | PASS | 2026-10-20 | jitsuinfi-frontend `tests/bundle-verdict.test.ts` (3 tes): "every seal" hanya untuk `Sealed`; `AwaitingSeal:Supplier/Buyer/Financier` = peringatan yang menyebut seal yang kurang; tanpa surat = "Invoice is genuine"; status tak dikenal ditolak (`1dcedf3`) |

## 2. Integrasi
Skrip vs DB/chain sungguhan. Semua artefak memakai prefix `TES-` (invoice, akun, label, order).

| ID | Skenario | Hasil | Tanggal | Bukti (txid/log) |
|---|---|---|---|---|
| I-HNK-28.1 | Snapshot relay dibandingkan dengan `jitsuin verify --save-board` | TODO | — | Menunggu snapshot otomatis (P-06) |
| I-HNK-28.2 | Web vs CLI pada data TES- yang sama (invoice `TES-INV-P28`, dua entri, snapshot JSON): `verifyProofOnBoard` dan `jitsuin verify --board` memberi verdict dan hasil per klaim yang sama untuk bukti lengkap (PROVEN), papan tanpa entri kedua (DOES NOT HOLD), dan bukti tanpa posisi pertama (DOES NOT HOLD); `rateIndex` sama dengan `jitsuin index --json` tanpa `version` dan `board`. Layar Verify di browser menampilkan verdict yang sama dan label "claimed, not checked" tanpa data papan | PASS | 2026-10-20 | File uji di scratchpad sesi, tidak di repo |
| I-HNK-28.3 | Juri hanya dengan README: `jitsuin verify --ufvk <examples/testnet/board-ufvk.txt> --birthday 4508703` dengan wallet watch-only baru, lalu `--proof examples/testnet/proof-tes-inv-0003.txt` dan `jitsuin index` | PASS | 2026-10-20 | Wallet dibuat 19 dtk, 13 tx mined, 9 register + 2 settled + 5 memo ditolak; bukti: entri A `33b8f3b0aa754e790e9c7fac0ae7dc08ce8612a8c26620d551d790e1ea390a56` (4509299/2/0), entri B `05d5aa7a02a33c14d460922468745fb4d6d814daa83989eed22b21c0540c79eb` (4509521/3/0), DOUBLE FINANCING PROVEN, exit 0; indeks: 6 invoice, semua kelas di bawah k = 5. Bukti dibangun ulang dengan `proof_from_lookup` dari invoice + tanda tangan buyer di bukti tawaran lama dan entri papan |
| I-HNK-28.4 | Layar Verify live https://jitsuinfi.vercel.app/app.html#/verify dengan bukti dan snapshot `examples/testnet/` | PASS | 2026-10-20 | "Double financing proven", entri pertama 4509299/2/0, entri kedua 4509521/3/0, 9 entri register dibaca: sama dengan CLI |

**Bukti pembersihan:** sisa artefak off-chain `TES-` = _TODO_ (target **0**). Artefak on-chain tidak bisa dihapus; catat txid-nya di tabel di atas. Data produksi tidak boleh tersentuh.

## 3. E2E
Panduan langkah demi langkah untuk user.

- [ ] Buka Verify, tempel bundel contoh
- [ ] Buka halaman indeks
- [ ] Buka halaman orang luar

| Langkah | Hasil diharapkan | Hasil aktual | Status |
|---|---|---|---|
| 1 | Ikuti README "For judges" langkah 1 (Docker) | Daftar entri dan `DOUBLE FINANCING PROVEN`, `Result PASS (4 check(s), 0 failed)` | Sama: image dibangun 247 dtk (OrbStack arm64), volume baru, wallet dibuat, 17,4 dtk scan, PASS 4/4, exit 0; langkah 2 (`jitsuin index`) memakai wallet yang sama, 6 invoice, exit 0 | PASS |
| 2 | Layar Verify: tempel `examples/testnet/proof-tes-inv-0003.txt`, pilih `board-snapshot.json` | "Double financing proven" | Sama (I-HNK-28.4) | PASS |
