---
tags: [test, "HNK-15"]
type: test
id: HNK-15
phase: F7
lead: Hans
owners: [Hans]
unit: PARSIAL
integrasi: PARSIAL
e2e: TODO
updated: 2026-10-17
---

# TEST-HNK-15 - Stretch JitsuinFi Vault

> **Peta link:** [[Testing Hub]] · [[Backlog]] · [[AC-HNK-15 - Stretch JitsuinFi Vault|AC]] · **Test** · [[ES-HNK-15 - Stretch JitsuinFi Vault|Exec Summary]]

**Lead:** Hans #hans · **Tim:** Hans #hans 

## 1. Unit
Logika murni, cepat, tanpa DB dan tanpa chain.

| ID | Kasus | Hasil | Tanggal | Bukti |
|---|---|---|---|---|
| U-HNK-15.1 | Merkle sum tree: inklusi dan jumlah | TODO | — | — |
| U-HNK-15.2 | Aturan solvabilitas | PASS | 2026-10-17 | `fund::tests` (2): piutang berjalan/lunas/lewat jatuh tempo, root terbaru, root pihak luar dan advance bukan dari manajer diabaikan, potongan 100%/50%, tanpa root tanpa vonis; `fund::tests` core (catatan dan root roundtrip, root palsu ditolak); `parses_balance_of_every_pool` (`e54ea36`) |

## 2. Integrasi
Skrip vs DB/chain sungguhan. Semua artefak memakai prefix `TES-` (invoice, akun, label, order).

| ID | Skenario | Hasil | Tanggal | Bukti (txid/log) |
|---|---|---|---|---|
| I-HNK-15.1 | Setoran `TES-` dan root di mainnet | PARSIAL (testnet, DEV-03) | 2026-10-17 | Scratchpad `fund-it` (230 dtk): deal dana `TES-INV-0006-1792222928` (entri `72d0e3ed66c757cdb44e570f25ed77191b3e0f8aa111f4757ef65cc29f999083`, advance `7b5687991a8df84cdb334d910f5d08850b98d5d02c7df09cd1bff4f2c167dbd9` dengan catatan piutang), root periode 1 `d8c207554d7975a28213a7cac45405ecc7bc4ed536929683481ae630d642a03c`, root palsu `4692b8f092dcc0379d881bba1318a237ffd97aee9c8abf12318a70435498a815` diabaikan, solvabilitas dihitung dari wallet watch-only `fund-watch`. Setoran anggota + Merkle sum tree = T1 (Dex), belum |

**Bukti pembersihan:** sisa artefak off-chain `TES-` = **0** di repo dan vault. Wallet watch-only uji `TES-fund-watch` disimpan di `~/.hanko-tes/testnet/fund-watch` (di luar repo, izin 700), sama seperti `board-watch`. Artefak on-chain tidak bisa dihapus; catat txid-nya di tabel di atas. Data produksi tidak boleh tersentuh.

## 3. E2E
Panduan langkah demi langkah untuk user.

- [ ] Anggota memverifikasi simpanannya ikut terhitung.

| Langkah | Hasil diharapkan | Hasil aktual | Status |
|---|---|---|---|
| 1 | _TODO_ | — | TODO |
