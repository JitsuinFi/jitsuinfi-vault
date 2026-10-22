---
tags: [test, "HNK-31"]
type: test
id: HNK-31
phase: F6
unit: TODO
integrasi: TODO
e2e: TODO
updated: 2026-10-22
---

# TEST-HNK-31 - Migrasi FE ke React dan TanStack Router

> **Peta link:** [[Testing Hub]] · [[Backlog]] · [[AC-HNK-31 - Migrasi FE ke React dan TanStack Router|AC]] · **Test** · [[ES-HNK-31 - Migrasi FE ke React dan TanStack Router|Exec Summary]]

## 1. Unit
Logika murni, cepat, tanpa DB dan tanpa chain.

| ID | Kasus | Hasil | Tanggal | Bukti |
|---|---|---|---|---|
| U-HNK-31.1 | `npm test` 78 test `src/lib/*` lulus setelah tiap task | PASS | 2026-10-22 | 80 test lulus setelah setiap task T2 – T12 (`npm test`) |
| U-HNK-31.2 | Pengalihan tautan lama: `#/supplier`, `app.html#/verify`, `/console.html` ke route baru (test unit fungsi redirect) | PASS | 2026-10-22 | `tests/legacy-url.test.ts`: `app.html`, `#/x`, `#/index` ke `/rates`, `console.html?view=pair`, kode pairing di hash tidak dibaca sebagai route |

## 2. Integrasi
Skrip vs DB/chain sungguhan. Semua artefak memakai prefix `TES-` (invoice, akun, label, order).

| ID | Skenario | Hasil | Tanggal | Bukti (txid/log) |
|---|---|---|---|---|
| I-HNK-31.1 | Paritas visual per halaman: tangkapan layar 1440 × 900 dan 390 × 844 dibandingkan berdampingan dengan `assets/hnk31-baseline/`, dicatat per task T3 – T10 | PASS | 2026-10-22 | Harness CDP (`scripts/fe-cdp-shots.mjs`) + `scripts/fe-diff.py`: build lama (main `155eaf7`, port 4175) vs build baru (port 4173, untuk konsol bergantian di 5173), 1440 × 900 dan 390 × 844, reduced motion: 0,00 % per halaman/bab kecuali data live, kota 3D beranimasi, sidik jari passkey virtual, port host |
| I-HNK-31.2 | Nol pelanggaran CSP dan nol error console di semua route (`vite preview` dengan header produksi) | PASS | 2026-10-22 | 18 route build baru: nol pelanggaran CSP (`securitypolicyviolation`) dan nol error/rejection tak tertangkap |
| I-HNK-31.3 | E2E lokal testnet di FE baru: siklus penuh sampai settled | TODO | — | — |

**Bukti pembersihan:** sisa artefak off-chain `TES-` = _TODO_ (target **0**). Artefak on-chain tidak bisa dihapus; catat txid-nya di tabel di atas. Data produksi tidak boleh tersentuh.

## 3. E2E
Panduan langkah demi langkah untuk user.

- [ ] Buka tiap URL bersih di production setelah deploy, bandingkan dengan patokan
- [ ] Jalankan E2E lokal (relay, node, web app). Passkey: authenticator virtual Chrome lewat CDP (`WebAuthn.addVirtualAuthenticator`, `hasPrf: true`, `scripts/fe-cdp-shots.mjs` job `webauthn`), terbukti di T7 untuk daftar dan masuk; sentuhan passkey user tidak lagi wajib

| Langkah | Hasil diharapkan | Hasil aktual | Status |
|---|---|---|---|
| 1 | _TODO_ | — | TODO |
