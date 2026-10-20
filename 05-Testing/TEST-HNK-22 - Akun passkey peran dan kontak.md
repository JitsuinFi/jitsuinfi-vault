---
tags: [test, "HNK-22"]
type: test
id: HNK-22
phase: F5
unit: TODO
integrasi: TODO
e2e: TODO
updated: 2026-10-20
---

# TEST-HNK-22 - Akun passkey peran dan kontak

> **Peta link:** [[Testing Hub]] · [[Backlog]] · [[AC-HNK-22 - Akun passkey peran dan kontak|AC]] · **Test** · [[ES-HNK-22 - Akun passkey peran dan kontak|Exec Summary]]

## 1. Unit
Logika murni, cepat, tanpa DB dan tanpa chain.

| ID | Kasus | Hasil | Tanggal | Bukti |
|---|---|---|---|---|
| U-HNK-22.1 | Salt per peran menghasilkan PRF berbeda per peran | TODO | — | — |
| U-HNK-22.2 | Profil lokal: akses localStorage yang melempar error tidak menghentikan daftar/masuk | TODO | — | — |

## 2. Integrasi
Skrip vs DB/chain sungguhan. Semua artefak memakai prefix `TES-` (invoice, akun, label, order).

| ID | Skenario | Hasil | Tanggal | Bukti (txid/log) |
|---|---|---|---|---|
| I-HNK-22.1 | Daftar, masuk di perangkat kedua, tambah peran di authenticator nyata (macOS/iOS, Android, security key) | TODO | — | — |

**Bukti pembersihan:** sisa artefak off-chain `TES-` = _TODO_ (target **0**). Artefak on-chain tidak bisa dihapus; catat txid-nya di tabel di atas. Data produksi tidak boleh tersentuh.

## 3. E2E
Panduan langkah demi langkah untuk user.

- [ ] Daftar sebagai supplier
- [ ] Tambah peran buyer
- [ ] Tukar kartu kontak dengan akun lain
- [ ] Stempel satu invoice uji `TES-`

| Langkah | Hasil diharapkan | Hasil aktual | Status |
|---|---|---|---|
| 1 | _TODO_ | — | TODO |
