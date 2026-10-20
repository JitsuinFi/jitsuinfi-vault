---
tags: [es, "HNK-22"]
type: es
id: HNK-22
phase: F5
status: PARSIAL
updated: 2026-10-20
---

# ES-HNK-22 - Akun passkey peran dan kontak

> **Peta link:** [[Exec Summary Hub]] · [[Backlog]] · [[AC-HNK-22 - Akun passkey peran dan kontak|AC]] · [[TEST-HNK-22 - Akun passkey peran dan kontak|Test]] · **Exec Summary**

## Apa diubah
- **T1 – T4 (Dave, backup Hans, DEV-17), PR #4:** layar Account: daftar satu passkey (`excludeCredentials`, nama netral, `rp.id` eksplisit untuk produksi), masuk, tambah atau ganti peran dengan passkey yang sama, sidik jari key, kunci. Authenticator tanpa PRF ditolak; test secret hanya bila passkey tidak bisa memberi key. Salt master dan inbox per peran (supplier, buyer, anggota); salt buyer tetap. Sesi hanya memegang key kotak surat; setiap tanda tangan = satu stempel (`Uint8Array` dinolkan); kunci setelah 15 menit idle. Router: layar peran hanya setelah masuk, Financier keluar dari navigasi. Layar supplier dan buyer memakai stempel.
- **Desain ulang layar akun (lokal, `c9784b8` → `703bac4` → `e42ac5d`):** gaya aplikasi consumer. Sign up: email, username, peran → passkey (sidik jari, wajah, atau password/PIN perangkat) → onboarding tiga bagian dengan indikator langkah. Log in: username → passkey → peran terakhir. Email dan username di profil perangkat sampai server akun ada (D-34).
- Belum: T5 kartu kontak dan T6 kotak masuk (butuh HNK-23), T7 uji authenticator nyata (user).

## Hasil vs KPI (angka riil)
| KPI | Target | Aktual |
|---|---|---|
| Credential per orang | 1 | 1 (authenticator palsu; nyata menunggu T7) |
| Authenticator yang diuji | ≥ 2 | 0 nyata (T7) |

## Status
**PARSIAL.** T1 – T4 DONE (PR #4). T5, T6 menunggu HNK-23; T7 menunggu uji user. AC 22.3, 22.4 PASS; 22.1, 22.2 lulus simulasi; 22.5 BLOCKED.

## Risiko tersisa
- PRF nyata per authenticator belum diuji (T7).
- Stempel adalah cek niat, bukan kontrol keamanan: skrip di tab yang sama tetap bisa meminta PRF.
- Belum ada pemulihan passkey (P-01).

## Bukti
- Commit: jitsuinfi-frontend `7814fbc` (branch `hans/hnk-22-passkey-account`, PR #4, belum di-merge)
- ID tes: U-HNK-22.1 – .2 PASS, I-HNK-22.2 PASS, I-HNK-22.1 TODO
- Persetujuan user untuk push/deploy: _belum_
