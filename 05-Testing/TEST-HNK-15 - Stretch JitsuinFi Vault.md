---
tags: [test, "HNK-15"]
type: test
id: HNK-15
phase: F7
lead: Hans
owners: [Dex, Hans, Dave]
unit: TODO
integrasi: TODO
e2e: TODO
updated: 2026-10-16
---

# TEST-HNK-15 - Stretch JitsuinFi Vault

> **Peta link:** [[Testing Hub]] · [[Backlog]] · [[AC-HNK-15 - Stretch JitsuinFi Vault|AC]] · **Test** · [[ES-HNK-15 - Stretch JitsuinFi Vault|Exec Summary]]

**Lead:** Hans #hans · **Tim:** Dex #dex, Hans #hans, Dave #dave

## 1. Unit
Logika murni, cepat, tanpa DB dan tanpa chain.

| ID | Kasus | Hasil | Tanggal | Bukti |
|---|---|---|---|---|
| U-HNK-15.1 | Merkle sum tree: inklusi dan jumlah | TODO | — | — |
| U-HNK-15.2 | Aturan solvabilitas | TODO | — | — |

## 2. Integrasi
Skrip vs DB/chain sungguhan. Semua artefak memakai prefix `TES-` (invoice, akun, label, order).

| ID | Skenario | Hasil | Tanggal | Bukti (txid/log) |
|---|---|---|---|---|
| I-HNK-15.1 | Setoran `TES-` dan root di mainnet | TODO | — | — |

**Bukti pembersihan:** sisa artefak off-chain `TES-` = _TODO_ (target **0**). Artefak on-chain tidak bisa dihapus; catat txid-nya di tabel di atas. Data produksi tidak boleh tersentuh.

## 3. E2E
Panduan langkah demi langkah untuk user.

- [ ] Anggota memverifikasi simpanannya ikut terhitung.

| Langkah | Hasil diharapkan | Hasil aktual | Status |
|---|---|---|---|
| 1 | _TODO_ | — | TODO |
