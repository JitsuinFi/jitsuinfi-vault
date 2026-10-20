---
tags: [ac, "HNK-03"]
type: ac
id: HNK-03
phase: F2
lead: Hans
owners: [Hans, Dex]
status: PASS
updated: 2026-10-17
---

# AC-HNK-03 - Wallet backend kirim dan terima memo di mainnet

> **Peta link:** [[AC Hub]] · [[Backlog]] · **AC** · [[TEST-HNK-03 - Wallet backend kirim dan terima memo di mainnet|Test]] · [[ES-HNK-03 - Wallet backend kirim dan terima memo di mainnet|Exec Summary]]

**Item:** HNK-03 · **Fase:** F2 · **Dependency:** SPK-01, SPK-02, SPK-03, SPK-10

**Lead:** Hans #hans · **Tim:** Hans #hans, Dex #dex 

## Deskripsi
Modul wallet backend (crate stabil, atau zcash-devtool/Zally) yang bisa sync, mengirim output shielded Ironwood dengan memo biner, dan mendekode memo masuk.

## Acceptance criteria
Status per kriteria: `TODO` / `PASS` / `FAIL` / `BLOCKED`, wajib dengan tanggal dan bukti (commit, txid, log, id tes).

| ID | Kriteria | Status | Tanggal | Bukti |
|---|---|---|---|---|
| AC-HNK-03.1 | Wallet `TES-` sync dari birthday height lewat lightwalletd publik. | PASS | 2026-10-17 | commit `7fd8202` (repo lokal `jitsuinfi-zcash/`); testnet (DEV-03): `Devtool::sync` via `testnet.zec.rocks` OK |
| AC-HNK-03.2 | Kirim transaksi shielded dengan memo entri ke alamat lain; txid tercatat. | PASS | 2026-10-17 | commit `7fd8202` (repo lokal `jitsuinfi-zcash/`); tx `8d8835f72129468ee06486458318355ebe98388594ae8f962ab814f99be887bc`, blok 4.508.981, 2 payment (entri ke papan + teks ke `TES-wallet-b`), mined 29 dtk setelah broadcast |
| AC-HNK-03.3 | Penerima mendekode memo identik byte per byte. | PASS | 2026-10-17 | Memo papan di-decode `jitsuin-core` identik dengan entri yang dikirim, signature valid; `wallet-b` membaca `Text("TES-HNK03 wallet-it")` |
| AC-HNK-03.4 | Input transparan ditolak atau ditandai. | PASS | 2026-10-17 | `WalletTx::touches_transparent()` menandai output transparan; tx uji: false. Unit test parser lulus |
| AC-HNK-03.5 | Fee tercatat dan sesuai ZIP-317. | PASS | 2026-10-17 | Fee 15.000 zat = 3 action × 5.000 (ZIP-317), terbaca dari `list-tx` |
| AC-HNK-03.6 | Seed dan spending key tidak pernah ditulis ke log atau repo. | PASS | 2026-10-17 | Crate hanya meneruskan path identity ke devtool; error hanya membawa baris `Error` terakhir; seed di `~/.hanko-tes/` (izin 600), `.gitignore` menolak `*.age`/DB wallet |

## Deviasi
_Kosong._ Kalau implementasi menyimpang dari keputusan, tulis di sini **dan** di [[Backlog]] bagian Log Deviasi. Tidak ada perubahan diam-diam.
