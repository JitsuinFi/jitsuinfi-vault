---
tags: [fe-tool, "FE-07"]
type: fe-tool
id: FE-07
layer: library-3d
status: AKTIF
updated: 2026-10-20
---

# FE-07 - three.js

> **Peta link:** [[FE-00 - Peta Tools FE|Peta tools]] · [[10 - FE Vault|Hub modul]] · [[FE-01 - Batasan Platform FE|Batasan platform]]

Mesin 3D untuk hero landing "Kota Piutang" (diorama cel-shaded, Amendment 3 di `MASTER.md`).

## Akar
| | |
|---|---|
| Paket | `three` 0.186.1 (MIT, https://threejs.org), tipe `@types/three` 0.186.0 (devDependency) |
| Dipasang | Untuk HNK-18.T4 (landing), dibundel, tanpa CDN |
| Dokumen desain | `jitsuinfi-frontend/MASTER.md` §1 Amendment 3, §5 (WebGL: DPR ≤ 2, 1 di ponsel; 30 fps idle, 60 saat scroll; berhenti di luar layar dan tab tersembunyi) |

## Dipakai di
- `src/landing/city.ts` (±57 KB): `THREE.WebGLRenderer`, kamera, `MeshToonMaterial` (ramp 3 langkah) dan `MeshBasicMaterial`, geometri primitif (Cylinder, Icosahedron, Sphere, Plane, Circle, Cone, Capsule, Extrude, BufferGeometry), tekstur dari canvas 2D (fasad, papan publik N `TES-INV-0001..0007`, kalender).
- Post-processing dari `three/examples/jsm/postprocessing/`: `EffectComposer`, `RenderPass`, `ShaderPass` (garis tinta dari normal dan depth), `OutputPass`.
- `renderer.setPixelRatio(dpr)` dan `composer.setPixelRatio(dpr)` mengikuti batas DPR.

## Batasan
- Bagian terbesar bundle `landing-*.js` (796 KB total); peringatan chunk Vite belum ditangani.
- Tidak boleh memuat model atau tekstur dari URL luar; semua tekstur dilukis di canvas.
- Sub-skill panduan: `threejs-r3f` di genjutsu ([[FE-13 - genjutsu]]).

## Status
AKTIF (landing). App (`app.html`) tidak memakai three.js.
