---
tags: [test, "HNK-01"]
type: test
id: HNK-01
phase: F1
lead: Hans
owners: [Hans, Dex, Dave]
unit: TODO
integrasi: TODO
e2e: TODO
updated: 2026-10-16
---

# TEST-HNK-01 - Format invoice kanonik dan tanda tangan buyer

> **Peta link:** [[Testing Hub]] · [[Backlog]] · [[AC-HNK-01 - Format invoice kanonik dan tanda tangan buyer|AC]] · **Test** · [[ES-HNK-01 - Format invoice kanonik dan tanda tangan buyer|Exec Summary]]

**Lead:** Hans #hans · **Tim:** Hans #hans, Dex #dex, Dave #dave

## 1. Unit
Logika murni, cepat, tanpa DB dan tanpa chain.

> **Verifikasi sementara (2026-10-16, Hans):** verifikasi sementara Hans: program di scratchpad memakai `jitsuin-core` lewat path dependency, 21/21 pemeriksaan lulus (bukan unit test resmi). Hasil: encoding deterministik dan roundtrip, sign 2× identik, verify OK, amount diubah ditolak, key salah ditolak, id kosong/amount 0/tanggal salah ditolak, trailing dan truncated ditolak. Unit test resmi tetap task Dex; tabel di bawah diisi saat test resmi ada.

| ID | Kasus | Hasil | Tanggal | Bukti |
|---|---|---|---|---|
| U-HNK-01.1 | Encode lalu decode menghasilkan invoice yang sama | TODO | — | — |
| U-HNK-01.2 | Dua kali encode menghasilkan byte identik | TODO | — | — |
| U-HNK-01.3 | Dua kali sign menghasilkan tanda tangan identik | TODO | — | — |
| U-HNK-01.4 | Ubah satu field → verifikasi gagal | TODO | — | — |
| U-HNK-01.5 | Field kosong atau tidak valid ditolak | TODO | — | — |

## 2. Integrasi
Skrip vs DB/chain sungguhan. Semua artefak memakai prefix `TES-` (invoice, akun, label, order).

| ID | Skenario | Hasil | Tanggal | Bukti (txid/log) |
|---|---|---|---|---|
| I-HNK-01.1 | N/A — item ini logika murni atau dokumen; tidak menyentuh DB/chain (dicatat, bukan dilewati) | TODO | — | — |

**Bukti pembersihan:** sisa artefak off-chain `TES-` = _TODO_ (target **0**). Artefak on-chain tidak bisa dihapus; catat txid-nya di tabel di atas. Data produksi tidak boleh tersentuh.

## 3. E2E
Panduan langkah demi langkah untuk user.

- [ ] Jalankan `jitsuin invoice new` dengan data contoh `TES-INV-0001`.
- [ ] Buyer menandatangani; tampilkan byte hex dan tanda tangan.
- [ ] Ulangi → hasilnya sama persis.

| Langkah | Hasil diharapkan | Hasil aktual | Status |
|---|---|---|---|
| 1 | _TODO_ | — | TODO |
