---
tags: [test, "HNK-32"]
type: test
id: HNK-32
phase: F6
unit: TODO
integrasi: TODO
e2e: TODO
updated: 2026-10-22
---

# TEST-HNK-32 - Perbaikan hasil audit flow

> **Peta link:** [[Testing Hub]] · [[Backlog]] · [[AC-HNK-32 - Perbaikan hasil audit flow|AC]] · **Test** · [[ES-HNK-32 - Perbaikan hasil audit flow|Exec Summary]]

## 1. Unit
Logika murni, cepat, tanpa DB dan tanpa chain.

| ID | Kasus | Hasil | Tanggal | Bukti |
|---|---|---|---|---|
| U-HNK-32.1 | Segel buyer ditolak untuk PDF salah dan financier lain | TODO | — | — |
| U-HNK-32.2 | QR pelunasan ditolak untuk surat tanpa rantai `Sealed` atau surat yang berbeda dari surat tersimpan | TODO | — | — |
| U-HNK-32.3 | Setiap varian `Stop` dipetakan ke kode dan kalimat | TODO | — | — |
| U-HNK-32.4 | Hitungan konfirmasi dari tinggi entri dan tip | TODO | — | — |

## 2. Integrasi
Skrip vs DB/chain sungguhan. Semua artefak memakai prefix `TES-` (invoice, akun, label, order).

| ID | Skenario | Hasil | Tanggal | Bukti (txid/log) |
|---|---|---|---|---|
| I-HNK-32.1 | E2E lokal testnet diperluas (HNK-32.T6): kirim key, simpan kontak, tolak penawaran, permintaan riwayat, lalu siklus sampai settled | TODO | — | — |
| I-HNK-32.2 | File bukti yang diunduh dari konsol lolos `/verify` | TODO | — | — |

**Bukti pembersihan:** sisa artefak off-chain `TES-` = _TODO_ (target **0**). Artefak on-chain tidak bisa dihapus; catat txid-nya di tabel di atas. Data produksi tidak boleh tersentuh.
