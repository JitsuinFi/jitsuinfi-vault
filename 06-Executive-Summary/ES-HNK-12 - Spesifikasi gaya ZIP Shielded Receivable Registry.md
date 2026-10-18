---
tags: [es, "HNK-12"]
type: es
id: HNK-12
phase: F4
lead: Dave
owners: [Dave, Dex, Hans]
status: PARSIAL
updated: 2026-10-18
---

# ES-HNK-12 - Spesifikasi gaya ZIP Shielded Receivable Registry

> **Peta link:** [[Exec Summary Hub]] · [[Backlog]] · [[AC-HNK-12 - Spesifikasi gaya ZIP Shielded Receivable Registry|AC]] · [[TEST-HNK-12 - Spesifikasi gaya ZIP Shielded Receivable Registry|Test]] · **Exec Summary**

**Lead:** Dave #dave · **Tim:** Dave #dave, Dex #dex, Hans #hans

## Apa diubah
- `docs/zip-shielded-receivable-registry.md` (`c42af3e`): spesifikasi gaya ZIP lengkap dengan test vector.
- Unit test baru untuk vector invoice kanonik dan tanda tangan buyer, sehingga semua vector di dokumen di-assert.

_Dikerjakan Hans (agent) atas keputusan user D-25 / DEV-11; Dave me-review._

## Hasil vs KPI (angka riil)
| KPI | Target | Aktual |
|---|---|---|
| Test vector yang cocok | 100% | — |

## Status
**PARSIAL**.

## Risiko tersisa
- Parser vector dari dokumen (HNK-12.T2, Dex) dan review teknis Hans (HNK-12.T3) belum.
- Tautan dari deskripsi submission (HNK-14.T2) belum.

## Bukti
- Commit: lihat Apa diubah (lokal)
- ID tes: _TODO_
- Persetujuan user untuk push/deploy: _belum_
