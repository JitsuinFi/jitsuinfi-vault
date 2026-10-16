---
tags: [test, "HNK-19"]
type: test
id: HNK-19
phase: F3
lead: Hans
owners: [Hans]
unit: TODO
integrasi: TODO
e2e: TODO
updated: 2026-10-17
---

# TEST-HNK-19 - Jitsuin Seal tanda tangan berantai dan Sign-to-Pay

> **Peta link:** [[Testing Hub]] · [[Backlog]] · [[AC-HNK-19 - Jitsuin Seal tanda tangan berantai dan Sign-to-Pay|AC]] · **Test** · [[ES-HNK-19 - Jitsuin Seal tanda tangan berantai dan Sign-to-Pay|Exec Summary]]

**Lead:** Hans #hans · **Tim:** Hans #hans

## 1. Unit
Logika murni, cepat, tanpa DB dan tanpa chain.

| ID | Kasus | Hasil | Tanggal | Bukti |
|---|---|---|---|---|
| U-HNK-19.1 | Rantai seal: urutan, role, key ganda, tamper | TODO | — | — |
| U-HNK-19.2 | Surat pengalihan kanonik roundtrip dan decoder ketat | TODO | — | — |
| U-HNK-19.3 | Gerbang `AwaitAssignment` di state machine | TODO | — | — |
| U-HNK-19.4 | Memo dua item (kuitansi + seal) encode/decode | TODO | — | — |
| U-HNK-19.5 | Status pelunasan: Unpaid, Claimed, Settled, Disputed, Overdue | TODO | — | — |

## 2. Integrasi
Skrip vs DB/chain sungguhan. Semua artefak memakai prefix `TES-` (invoice, akun, label, order).

| ID | Skenario | Hasil | Tanggal | Bukti (txid/log) |
|---|---|---|---|---|
| I-HNK-19.1 | Siklus penuh `TES-INV-0003` di testnet: registrasi, surat pengalihan, advance Sign-to-Pay, pelunasan dua tanda tangan | TODO | — | — |

**Bukti pembersihan:** sisa artefak off-chain `TES-` = _TODO_ (target **0**). Artefak on-chain tidak bisa dihapus; catat txid-nya di tabel di atas. Data produksi tidak boleh tersentuh.

## 3. E2E
Panduan langkah demi langkah untuk user.

- [ ] _TODO langkah E2E_

| Langkah | Hasil diharapkan | Hasil aktual | Status |
|---|---|---|---|
| 1 | _TODO_ | — | TODO |
