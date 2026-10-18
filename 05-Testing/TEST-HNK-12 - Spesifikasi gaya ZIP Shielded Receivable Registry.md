---
tags: [test, "HNK-12"]
type: test
id: HNK-12
phase: F4
lead: Dave
owners: [Dave, Dex, Hans]
unit: TODO
integrasi: TODO
e2e: TODO
updated: 2026-10-18
---

# TEST-HNK-12 - Spesifikasi gaya ZIP Shielded Receivable Registry

> **Peta link:** [[Testing Hub]] · [[Backlog]] · [[AC-HNK-12 - Spesifikasi gaya ZIP Shielded Receivable Registry|AC]] · **Test** · [[ES-HNK-12 - Spesifikasi gaya ZIP Shielded Receivable Registry|Exec Summary]]

**Lead:** Dave #dave · **Tim:** Dave #dave, Dex #dex, Hans #hans

## 1. Unit
Logika murni, cepat, tanpa DB dan tanpa chain.

| ID | Kasus | Hasil | Tanggal | Bukti |
|---|---|---|---|---|
| U-HNK-12.1 | Test vector dari dokumen dijalankan sebagai test | PARSIAL | 2026-10-18 | Nilai yang sama di-assert di unit test core (lihat AC-HNK-12.2); parser yang membaca dokumen = HNK-12.T2 (Dex) |

## 2. Integrasi
Skrip vs DB/chain sungguhan. Semua artefak memakai prefix `TES-` (invoice, akun, label, order).

| ID | Skenario | Hasil | Tanggal | Bukti (txid/log) |
|---|---|---|---|---|
| I-HNK-12.1 | N/A — item ini logika murni atau dokumen; tidak menyentuh DB/chain (dicatat, bukan dilewati) | TODO | — | — |

**Bukti pembersihan:** sisa artefak off-chain `TES-` = _TODO_ (target **0**). Artefak on-chain tidak bisa dihapus; catat txid-nya di tabel di atas. Data produksi tidak boleh tersentuh.

## 3. E2E
Panduan langkah demi langkah untuk user.

- [ ] Pembaca teknis bisa mengimplementasikan ulang encoding hanya dari dokumen.

| Langkah | Hasil diharapkan | Hasil aktual | Status |
|---|---|---|---|
| 1 | _TODO_ | — | TODO |
