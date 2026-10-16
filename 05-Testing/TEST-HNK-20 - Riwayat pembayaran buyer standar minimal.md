---
tags: [test, "HNK-20"]
type: test
id: HNK-20
phase: F3
lead: Hans
owners: [Hans]
unit: TODO
integrasi: TODO
e2e: TODO
updated: 2026-10-17
---

# TEST-HNK-20 - Riwayat pembayaran buyer standar minimal

> **Peta link:** [[Testing Hub]] · [[Backlog]] · [[AC-HNK-20 - Riwayat pembayaran buyer standar minimal|AC]] · **Test** · [[ES-HNK-20 - Riwayat pembayaran buyer standar minimal|Exec Summary]]

**Lead:** Hans #hans · **Tim:** Hans #hans

## 1. Unit
Logika murni, cepat, tanpa DB dan tanpa chain.

| ID | Kasus | Hasil | Tanggal | Bukti |
|---|---|---|---|---|
| U-HNK-20.1 | Derivasi key per invoice dan sertifikat delegasi | TODO | — | — |
| U-HNK-20.2 | Verifier bukti riwayat (valid, allowlist, palsu) | TODO | — | — |
| U-HNK-20.3 | Policy standar minimal di alur financier | TODO | — | — |

## 2. Integrasi
Skrip vs DB/chain sungguhan. Semua artefak memakai prefix `TES-` (invoice, akun, label, order).

| ID | Skenario | Hasil | Tanggal | Bukti (txid/log) |
|---|---|---|---|---|
| I-HNK-20.1 | Bukti riwayat dari entri `settled` hasil HNK-19.T5 diverifikasi terhadap papan testnet | TODO | — | — |

**Bukti pembersihan:** sisa artefak off-chain `TES-` = _TODO_ (target **0**). Artefak on-chain tidak bisa dihapus; catat txid-nya di tabel di atas. Data produksi tidak boleh tersentuh.

## 3. E2E
Panduan langkah demi langkah untuk user.

- [ ] _TODO langkah E2E_

| Langkah | Hasil diharapkan | Hasil aktual | Status |
|---|---|---|---|
| 1 | _TODO_ | — | TODO |
