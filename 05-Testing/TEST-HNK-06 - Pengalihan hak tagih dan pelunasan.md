---
tags: [test, "HNK-06"]
type: test
id: HNK-06
phase: F3
lead: Hans
owners: [Dex, Hans, Dave]
unit: TODO
integrasi: TODO
e2e: TODO
updated: 2026-10-16
---

# TEST-HNK-06 - Pengalihan hak tagih dan pelunasan

> **Peta link:** [[Testing Hub]] · [[Backlog]] · [[AC-HNK-06 - Pengalihan hak tagih dan pelunasan|AC]] · **Test** · [[ES-HNK-06 - Pengalihan hak tagih dan pelunasan|Exec Summary]]

**Lead:** Hans #hans · **Tim:** Dex #dex, Hans #hans, Dave #dave

## 1. Unit
Logika murni, cepat, tanpa DB dan tanpa chain.

| ID | Kasus | Hasil | Tanggal | Bukti |
|---|---|---|---|---|
| U-HNK-06.1 | Format surat pengalihan | TODO | — | — |
| U-HNK-06.2 | Pencocokan pembayaran ke N | TODO | — | — |

## 2. Integrasi
Skrip vs DB/chain sungguhan. Semua artefak memakai prefix `TES-` (invoice, akun, label, order).

| ID | Skenario | Hasil | Tanggal | Bukti (txid/log) |
|---|---|---|---|---|
| I-HNK-06.1 | Buyer `TES-` membayar `TES-INV-0002` ke financier `TES-`; terdeteksi | TODO | — | — |

**Bukti pembersihan:** sisa artefak off-chain `TES-` = _TODO_ (target **0**). Artefak on-chain tidak bisa dihapus; catat txid-nya di tabel di atas. Data produksi tidak boleh tersentuh.

## 3. E2E
Panduan langkah demi langkah untuk user.

- [ ] Buyer membayar dari Zodl via QR ZIP-321 (kalau SPK-04 PASS).
- [ ] Financier melihat status berubah menjadi lunas.

| Langkah | Hasil diharapkan | Hasil aktual | Status |
|---|---|---|---|
| 1 | _TODO_ | — | TODO |
