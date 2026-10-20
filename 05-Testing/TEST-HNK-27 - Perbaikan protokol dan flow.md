---
tags: [test, "HNK-27"]
type: test
id: HNK-27
phase: F3
unit: TODO
integrasi: TODO
e2e: TODO
updated: 2026-10-20
---

# TEST-HNK-27 - Perbaikan protokol dan flow

> **Peta link:** [[Testing Hub]] · [[Backlog]] · [[AC-HNK-27 - Perbaikan protokol dan flow|AC]] · **Test** · [[ES-HNK-27 - Perbaikan protokol dan flow|Exec Summary]]

## 1. Unit
Logika murni, cepat, tanpa DB dan tanpa chain.

| ID | Kasus | Hasil | Tanggal | Bukti |
|---|---|---|---|---|
| U-HNK-27.1 | Komitmen deterministik saat retry | TODO | — | — |
| U-HNK-27.2 | Entri dengan kelas lain ditolak `EntryMismatch` | TODO | — | — |
| U-HNK-27.3 | `assignmentDecode` roundtrip | TODO | — | — |
| U-HNK-27.4 | Konfirmasi dihitung ulang setelah posisi berubah | TODO | — | — |

## 2. Integrasi
Skrip vs DB/chain sungguhan. Semua artefak memakai prefix `TES-` (invoice, akun, label, order).

| ID | Skenario | Hasil | Tanggal | Bukti (txid/log) |
|---|---|---|---|---|
| I-HNK-27.1 | Registrasi dengan kelas di testnet | TODO | — | — |
| I-HNK-27.2 | Crash dan restart sesudah posting | TODO | — | — |

**Bukti pembersihan:** sisa artefak off-chain `TES-` = _TODO_ (target **0**). Artefak on-chain tidak bisa dihapus; catat txid-nya di tabel di atas. Data produksi tidak boleh tersentuh.

## 3. E2E
Panduan langkah demi langkah untuk user.

- [ ] Jalankan `jitsuin index` atas papan uji

| Langkah | Hasil diharapkan | Hasil aktual | Status |
|---|---|---|---|
| 1 | _TODO_ | — | TODO |
