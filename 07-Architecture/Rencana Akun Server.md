---
tags: [architecture, account, relay]
status: USULAN
updated: 2026-10-20
---

# Rencana Akun Server

> **Peta link:** [[07 - Architecture]] · [[Decision Log]] (D-33, D-34) · [[Threat Model]] · [[Backlog]] (HNK-23) · [[SEQ-00 - Autentikasi dan Onboarding]]

Status per 2026-10-20 dan rencana untuk akun di server (sign up, log in, email). **USULAN**, belum disetujui kecuali yang ditandai.

## Status sekarang
| Hal | Keadaan |
|---|---|
| Repo backend `jitsuinfi-backend` | **Ada** sejak 2026-10-20: private di GitHub (`JitsuinFi/jitsuinfi-backend`), TypeScript Node + Hono + `postgres` (pilihan user), dikerjakan Hans (D-38). Relay kotak surat dulu (HNK-23.T3, T4); API akun menyusul |
| Basis data | Belum tersambung. Email, username, peran terakhir ada di `localStorage` perangkat (`jitsuinfi-profile`, D-34); dokumen deal di IndexedDB terenkripsi (`jitsuinfi-deals`) |
| Project Supabase dan Railway | Dibuat oleh **user** (jawaban user 2026-10-20: "Aku"); user mengisi `DATABASE_URL` (Session pooler) sendiri di `jitsuinfi-backend/.env`; migrasi relay diterapkan 2026-10-20. API key Supabase tidak dipakai relay. Insiden 2026-10-20: perintah pengecekan agent mencetak `SUPABASE_SECRET_KEY` dan anon key ke transkrip sesi; user diminta merotasi dan menghapusnya dari `.env` |
| Repo `jitsuinfi-frontend` | **Public** di GitHub, padahal D-17 menetapkan privat sampai menjelang submit. Lihat DEV-19 di [[Backlog]] |

## Di mana credential Supabase disimpan
- **Tidak di `jitsuinfi-frontend`.** Variabel `VITE_*` ikut dibundel ke JS publik, dan D-33 melarang browser bicara langsung ke Supabase. `.env.local` frontend hanya berisi `VERCEL_OIDC_TOKEN` (dibuat Vercel CLI, di-ignore git).
- **Di backend:** `jitsuinfi-backend/.env` (lokal, di-ignore git) dan variabel lingkungan Railway (produksi). Isi: `DATABASE_URL` (connection string Postgres Supabase) atau `SUPABASE_URL` + `SUPABASE_SERVICE_ROLE_KEY`. Service role key hanya di server.
- Repo backend menyertakan `.env.example` tanpa nilai.
- Credential tidak ditempel di chat, vault, atau log.

## Usulan API akun (rekomendasi)
Server memverifikasi passkey (WebAuthn assertion), bukan hanya menyimpan data. Username jadi unik global, log in jalan di perangkat mana pun, email hanya keluar setelah passkey terbukti. Satu `navigator.credentials.get()` memberi assertion untuk server dan output PRF untuk key di browser; key tidak pernah keluar dari browser.

| Endpoint | Isi |
|---|---|
| `POST /api/auth/register/options` | `{username, email, role}` → challenge + `user.id` |
| `POST /api/auth/register/verify` | Attestation → simpan public key passkey + akun |
| `POST /api/auth/login/options` | `{username}` → challenge + `allowCredentials` |
| `POST /api/auth/login/verify` | Assertion → cookie sesi `__Host-`, `HttpOnly`, `Secure`, `SameSite=Strict` |
| `GET /api/account` | `{username, email, roles}`, hanya dengan sesi |

Tabel Postgres:
| Tabel | Kolom |
|---|---|
| `accounts` | `id` (uuid), `username` (unik, huruf kecil), `email`, `roles`, `created_at` |
| `credentials` | `id` (credential id), `account_id`, `public_key`, `sign_count`, `transports`, `created_at` |

Browser memanggil lewat rewrite Vercel `/api/*` ke relay (HNK-23.T6), CSP tetap `connect-src 'self'`.

Dependensi baru (perlu izin user): `@simplewebauthn/server` di backend.

## Wallet dari passkey (permintaan user, menunggu keputusan)
User ingin alamat wallet dibuat dari passkey.
- **Bisa:** output PRF → seed ZIP-32 → Unified Address Zcash (Orchard/Sapling) di `jitsuin-wasm`.
- **Menerima dana** (alamat saja): ringan.
- **Mengirim dana dari browser:** berat (sinkron lightwalletd, pembuatan proof di wasm).
- **Risiko:** passkey hilang = dana hilang; pemulihan belum ada (P-01). Mengubah D-31 untuk supplier dan buyer (sekarang wallet sendiri, misalnya Zodl).
- Pertanyaan terbuka: cukup alamat penerima dulu, atau sampai bisa mengirim?

## Keputusan yang ditunggu
1. Setujui desain API di atas (verifikasi passkey di server).
2. Siapa membuat `jitsuinfi-backend` sekarang: Dex (HNK-23.T3) atau Hans sebagai backup.
3. Izin dependensi `@simplewebauthn/server`.
4. Ruang lingkup wallet dari passkey.
5. Visibilitas repo `jitsuinfi-frontend` (DEV-19).

## Key penyedia node (2026-10-21, HNK-26.T25)
Key penyedia (`provider.key`, 32 byte) ada di `~/.jitsuin-provider` di Mac Hans, mode 0600, dibuat `jitsuin-node provider init`. Dari key ini diturunkan kotak surat penyedia (pengajuan financier) dan key tanda tangan undangan; kunci publiknya ada di jitsuinfi-frontend `src/lib/provider.ts`. Perlu backup terenkripsi; hilang = pengajuan tidak terbaca dan undangan baru butuh key baru (ganti kunci publik di app). Tidak pernah masuk repo, vault, log, atau chat.
