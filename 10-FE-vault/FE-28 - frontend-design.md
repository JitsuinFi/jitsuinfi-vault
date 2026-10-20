---
tags: [fe-tool, "FE-28"]
type: fe-tool
id: FE-28
layer: skill
status: AKTIF
updated: 2026-10-20
---

# FE-28 - frontend-design

> **Peta link:** [[FE-00 - Peta Tools FE|Peta tools]] · [[10 - FE Vault|Hub modul]] · [[FE-01 - Batasan Platform FE|Batasan platform]]

Skill resmi Anthropic untuk desain antarmuka yang punya karakter dan tidak terasa templated.

## Akar
| | |
|---|---|
| Plugin | `frontend-design@claude-plugins-official` (penulis Anthropic, lisensi Apache 2.0) |
| Dipasang | 2026-10-20 oleh user: `claude plugin install frontend-design@claude-plugins-official`, scope **user** (semua proyek) |
| Lokasi | `~/.claude/plugins/cache/claude-plugins-official/frontend-design/a0b04d9ddcca/skills/frontend-design/SKILL.md` (71 baris) |
| Isi plugin | 1 skill; tanpa agent, hook, atau server MCP |
| Biaya token | ±80 token selalu aktif per sesi, ±2.7k token setiap dipanggil |
| Tersedia | Aktif di sesi sejak 2026-10-20 sebagai `frontend-design:frontend-design` |

## Isi skill
- **Berpijak pada subjek**: pilihan visual datang dari industri, bahan, dan kosakata subjeknya; konten nyata, bukan placeholder.
- **Prinsip**: hero = hal paling khas dari dunia subjek; satu atau dua keluarga huruf dengan skala tipografi tegas; baris < 80 karakter; struktur (garis, nomor, label) harus membawa informasi; gerak tanpa pemicu dipakai hemat, satu momen terorkestrasi lebih baik daripada efek di mana-mana.
- **Daftar "tell" desain buatan AI** yang dihindari kecuali brief memintanya:
  1. latar krem hangat (±`#F4F1EA`) + serif kontras tinggi + aksen terakota (±`#D97757`);
  2. latar hampir hitam + satu aksen hijau asam atau vermilion;
  3. tata letak koran: garis tipis, radius 0, kolom rapat;
  4. paket kartu SaaS: kartu bulat seragam, bayangan abu sama, gradasi dekoratif;
  5. ornamen template: eyebrow KAPITAL di atas setiap judul, string meta dengan titik tengah, `WORD — fragment`, hitam bernada (`#0B0B0B`, `#111`), font mono untuk label data kecil, `→` di setiap tombol.
- **Proses dua tahap**: rencana token (4 – 6 warna bernama, peran huruf, konsep layout dengan wireframe ASCII, prinsip), tinjau terhadap brief dan revisi bagian yang generik, baru menulis kode; lalu kritik diri dengan screenshot.
- **Menahan diri**: keberanian di satu tempat; batas kualitas (responsif, fokus keyboard, reduced motion, aksesibel).
- **Menulis**: dari sudut pandang pengguna, kalimat aktif, nama aksi konsisten ("Publish" → "Published"), error menjelaskan cara memperbaiki.

## Hubungan dengan JitsuinFi
- **Brief menang**: `MASTER.md` dan [[DS-PAL - Palet Utama JitsuinFi]] sudah menetapkan arah; skill ini dipakai untuk menguji keputusan baru, bukan menggantinya.
- Beberapa referensi di `09-Design` persis "tell" di atas: DS-03, DS-04 (gelap + lime, tell 2 dan 4), DS-09 (hitam bernada `#0F0F0F`, label nomor `01 – 03`, tell 5). Ambil polanya, hindari ciri generiknya ([[DS-00 - Peta Visual Design]]).
- App sebelum 2026-10-20 (`src/style.css`: krem `#f7f5f0`, merah `#b3261e`, kartu radius 10 px) dekat dengan tell 1 dan 4. Restyle pertama D-36 (garis tipis, radius 0) jatuh ke tell 3 dan dikoreksi D-37 (gaya iOS dari `09-Design`, palet DS-PAL, `ba9383a`).
- Landing memakai Geist Mono untuk data nyata (N, txid): pengecualian yang disengaja di `MASTER.md`, bukan label dekoratif.

## Dibanding skill lain
| Skill | Fokus |
|---|---|
| frontend-design | Arah estetika dan anti-template, proses rencana → tinjau → bangun → kritik |
| [[FE-14 - impeccable]] | Command per tugas (critique, audit, polish, harden), mode permukaan, agent |
| [[FE-13 - genjutsu]] | Gerak dan sistem visual, sub-skill teknis (three.js, Motion, CSS) |

## Status
AKTIF (terpasang 2026-10-20).
