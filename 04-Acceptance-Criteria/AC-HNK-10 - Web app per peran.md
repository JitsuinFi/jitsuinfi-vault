---
tags: [ac, "HNK-10"]
type: ac
id: HNK-10
phase: F5
lead: Hans
owners: [Hans, Dex]
status: TODO
updated: 2026-10-16
---

# AC-HNK-10 - Web app per peran

> **Peta link:** [[AC Hub]] · [[Backlog]] · **AC** · [[TEST-HNK-10 - Web app per peran|Test]] · [[ES-HNK-10 - Web app per peran|Exec Summary]]

**Item:** HNK-10 · **Fase:** F5 · **Dependency:** HNK-05, HNK-06, SPK-09

**Lead:** Hans #hans · **Tim:** Hans #hans, Dex #dex 

## Deskripsi
Antarmuka web untuk supplier, buyer, dan financier; tanpa CDN pihak ketiga, analytics, atau cookie pelacak; header CSP ketat.

## Acceptance criteria
Status per kriteria: `TODO` / `PASS` / `FAIL` / `BLOCKED`, wajib dengan tanggal dan bukti (commit, txid, log, id tes).

| ID | Kriteria | Status | Tanggal | Bukti |
|---|---|---|---|---|
| AC-HNK-10.1 | Alur supplier, buyer, dan financier bisa dijalankan dari browser. | TODO | 2026-10-18 | Bagian browser berjalan (uji klik 2026-10-18, build produksi): supplier buat invoice → buyer tanda tangan → surat → seal supplier → seal buyer → QR pelunasan → bundel → Verify "genuine"; bundel diubah ditolak. Registrasi, advance, dan watchdog lewat backend (API HNK-05.T3/HNK-10.T4, Dex) belum terhubung ke layar |
| AC-HNK-10.2 | 0 request ke domain pihak ketiga (bukti DevTools). | PASS | 2026-10-18 | DevTools (network) saat uji klik: semua request ke `localhost:4173` (HTML, JS, CSS, WASM, ikon); 0 ke domain lain. Tanpa CDN; font sistem |
| AC-HNK-10.3 | Header CSP aktif; tanpa cookie pelacak. | TODO | 2026-10-18 | CSP aktif lewat `<meta>` di `index.html` (`default-src 'self'`, `connect-src 'self'`, `'wasm-unsafe-eval'`); terbukti memblokir `fetch` ke `data:`. Tanpa cookie. Header CSP di server menunggu deploy (HNK-10.T5, Dex) |
| AC-HNK-10.4 | Diuji dalam keadaan logout dari jaringan lain. | TODO | — | — |

## Deviasi
_Kosong._ Kalau implementasi menyimpang dari keputusan, tulis di sini **dan** di [[Backlog]] bagian Log Deviasi. Tidak ada perubahan diam-diam.
