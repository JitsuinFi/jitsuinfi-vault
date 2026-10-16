---
tags: [test, "HNK-03"]
type: test
id: HNK-03
phase: F2
lead: Hans
owners: [Hans, Dex]
unit: PASS
integrasi: TODO
e2e: TODO
updated: 2026-10-17
---

# TEST-HNK-03 - Wallet backend kirim dan terima memo di mainnet

> **Peta link:** [[Testing Hub]] · [[Backlog]] · [[AC-HNK-03 - Wallet backend kirim dan terima memo di mainnet|AC]] · **Test** · [[ES-HNK-03 - Wallet backend kirim dan terima memo di mainnet|Exec Summary]]

**Lead:** Hans #hans · **Tim:** Hans #hans, Dex #dex

## 1. Unit
Logika murni, cepat, tanpa DB dan tanpa chain.

| ID | Kasus | Hasil | Tanggal | Bukti |
|---|---|---|---|---|
| U-HNK-03.1 | Builder memo (prefix `0xFF`, padding) | PASS | 2026-10-17 | `builds_zip321_uri`, `rejects_bad_payments` (`cargo test -p jitsuin-wallet`) |
| U-HNK-03.2 | Parser memo masuk | PASS | 2026-10-17 | `parses_list_tx` |
| U-HNK-03.3 | Perhitungan fee | PASS | 2026-10-17 | `parses_list_tx` (fee), `formats_amounts` |

## 2. Integrasi
Skrip vs DB/chain sungguhan. Semua artefak memakai prefix `TES-` (invoice, akun, label, order).

| ID | Skenario | Hasil | Tanggal | Bukti (txid/log) |
|---|---|---|---|---|
| I-HNK-03.1 | Sync `TES-wallet-a` dari birthday height | PASS | 2026-10-17 | run integrasi sementara (scratchpad `wallet-it`) |
| I-HNK-03.2 | Kirim `TES-entry` ke `TES-wallet-b` dan dekode | PASS | 2026-10-17 | tx `8d8835f72129468ee06486458318355ebe98388594ae8f962ab814f99be887bc` |
| I-HNK-03.3 | Hapus DB wallet uji setelah tes (sisa 0) | TODO | — | Run ini memakai wallet `TES-` yang sudah ada (tidak membuat DB baru). Script resmi + bukti pembersihan = HNK-03.T5 (Dex); aturan on-chain menunggu DEV-01 |

**Bukti pembersihan:** sisa artefak off-chain `TES-` = _TODO_ (target **0**). Artefak on-chain tidak bisa dihapus; catat txid-nya di tabel di atas. Data produksi tidak boleh tersentuh.

## 3. E2E
Panduan langkah demi langkah untuk user.

- [ ] Jalankan `jitsuin wallet sync`.
- [ ] Jalankan `jitsuin wallet send --memo-file <file>`.
- [ ] Buka txid di explorer: transaksi terlihat, isinya tidak.

| Langkah | Hasil diharapkan | Hasil aktual | Status |
|---|---|---|---|
| 1 | _TODO_ | — | TODO |
