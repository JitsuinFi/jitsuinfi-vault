---
tags: [test, "HNK-22"]
type: test
id: HNK-22
phase: F5
unit: PASS
integrasi: PARSIAL
e2e: TODO
updated: 2026-10-20
---

# TEST-HNK-22 - Akun passkey peran dan kontak

> **Peta link:** [[Testing Hub]] · [[Backlog]] · [[AC-HNK-22 - Akun passkey peran dan kontak|AC]] · **Test** · [[ES-HNK-22 - Akun passkey peran dan kontak|Exec Summary]]

## 1. Unit
Logika murni, cepat, tanpa DB dan tanpa chain.

| ID | Kasus | Hasil | Tanggal | Bukti |
|---|---|---|---|---|
| U-HNK-22.1 | Salt per peran menghasilkan PRF berbeda per peran; `rp.id`; profil bolak-balik; sidik jari; satu passkey per orang; perangkat baru tanpa profil; tidak ada master setelah masuk atau stempel; stempel dari passkey lain ditolak; anggota tidak menandatangani; kunci idle; mode demo | PASS | 2026-10-20 | `tests/account.test.ts` dengan authenticator palsu (PRF = HMAC), `npm test` 29/29 (`7814fbc`) |
| U-HNK-22.2 | Profil lokal: akses localStorage yang melempar error tidak menghentikan daftar/masuk | PASS | 2026-10-20 | `tests/account.test.ts` (storage `blocked`) |

## 2. Integrasi
Skrip vs DB/chain sungguhan. Semua artefak memakai prefix `TES-` (invoice, akun, label, order).

| ID | Skenario | Hasil | Tanggal | Bukti (txid/log) |
|---|---|---|---|---|
| I-HNK-22.1 | Daftar, masuk di perangkat kedua, tambah peran di authenticator nyata (macOS/iOS, Android, security key) | TODO | — | HNK-22.T7, oleh user |
| I-HNK-22.2 | Browser (dev server dan build produksi) dengan `navigator.credentials` diganti authenticator palsu: `#/supplier` tanpa sesi membuka Masuk; daftar (`rp.id` localhost, nama "JitsuinFi", PRF di `create()`); daftar kedua ditolak lewat `excludeCredentials`; masuk lagi, sidik jari sama; ganti ke buyer, sidik jari beda, satu passkey; key buyer = turunan lama; stempel dari passkey lain ditolak; invoice supplier = satu prompt; anggota tanpa tombol tanda tangan; tanpa PRF: pesan + test secret; profil kosong + passkey sama: deal kembali; 375 px tanpa scroll horizontal | PASS | 2026-10-20 | Skrip di pane browser; `jitsuinfi-deals` dan profil dihapus di kedua origin (sisa 0) |

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
