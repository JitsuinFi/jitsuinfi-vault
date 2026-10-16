---
tags: [hub, start-here]
---

# JitsuinFi Vault — START HERE

Knowledge base proyek **JitsuinFi** untuk **ZECATHON** (hackathon privasi Zcash), track **Private Markets**.

> **JitsuinFi:** pembiayaan invoice (factoring) yang privat tanpa pembiayaan ganda.
> **"Zcash stops double-spending. JitsuinFi stops double-financing."**

Deadline submission: **28 Okt 2026 23:59 UTC** (29 Okt 06:59 WIB). Target submit final: **27 Okt**.

## Tim
| Orang | Label | Fokus | Porsi |
|---|---|---|---|
| Hans | #hans | Semua integrasi Zcash, core kripto, backend dan FE krusial, submit final | 40% |
| Dex | #dex | Backend pendukung, verifier CLI, CI, uji integrasi, DevOps | 30% |
| Dave | #dave | FE non-krusial, dokumentasi dan spesifikasi, QA E2E, uji pengguna, video, pitch | 30% |

Rincian task per orang: [[Backlog]].

## Mulai dari sini
1. [[JitsuinFi - Ringkasan Proyek]] — apa yang dibangun dan kenapa.
2. [[ZECATHON - Aturan dan Deadline]] — aturan yang mengikat (kriteria juri, form, larangan).
3. [[Workflow Development]] — 5 langkah wajib per item/fase.
4. [[Rencana Fase]] — urutan fase, gerbang verifikasi, dan tanggal.
5. [[Spikes Hub]] — uji kelayakan semua tools dan resource **sebelum** build.
6. [[Backlog]] — daftar item dengan ID stabil (HNK-xx) dan log deviasi.
7. [[AC Hub]] · [[Testing Hub]] · [[Exec Summary Hub]] — bukti per item.
8. [[Arsitektur JitsuinFi]] · [[Format Data]] · [[Threat Model]] · [[Decision Log]].
9. [[Video-Workspace]] — produksi video demo 2 menit.
10. [[Dashboard]] — status semua item (Dataview).

## Struktur vault
| Folder | Isi |
|---|---|
| `00-Project/` | Ringkasan proyek, aturan ZECATHON, sumber eksternal |
| `01-Workflow/` | Workflow development dan rencana fase |
| `02-Spikes/` | Hub + satu file per spike (SPK-xx) |
| `03-Backlog/` | Backlog item (HNK-xx) dan log deviasi |
| `04-Acceptance-Criteria/` | Hub + satu file AC per item |
| `05-Testing/` | Hub + satu file tes per item (unit, integrasi, E2E) |
| `06-Executive-Summary/` | Hub + satu exec summary per item |
| `07-Architecture/` | Arsitektur, format data, threat model, decision log |
| `Video-Workspace/` | Naskah, storyboard, checklist rekaman dan export |
| `Concepts/` | Catatan konsep atomik (`#concept`) |
| `Module-Guides/` | Ringkasan tiap modul `NN-` |
| `Templates/` | Template note |
| `Notes/` | Scratchpad |
| `scripts/` | Otomasi vault (Python) |

## Aturan emas
- Kriteria lulus = [[AC Hub]], bukan perasaan "sudah jalan".
- Push/deploy **hanya setelah user menyetujui** hasil langkah 2–4 di [[Workflow Development]].
- Deviasi dari rencana ditulis eksplisit di [[Backlog]] (Log Deviasi). Keputusan user final.
- Setelah edit vault: `python3 scripts/sync-vault.py` → harus `Broken: 0`.

## Konsep kunci (auto)
```dataview
LIST FROM #concept SORT file.name ASC
```

## Semua halaman (auto)
```dataview
LIST FROM "" WHERE file.name != "START-HERE" SORT file.folder ASC, file.name ASC
```

Indeks statis untuk AI agent: [[_Auto-Index]].
