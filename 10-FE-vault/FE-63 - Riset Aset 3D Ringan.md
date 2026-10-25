---
tags: [fe-tool, "FE-63", monad-blitz, research]
type: fe-tool
id: FE-63
layer: referensi
status: REFERENSI
author: "Gpt 6.1 sol - agentrouter"
updated: 2026-10-23
---

# FE-63 - Riset Aset 3D Ringan

> **Peta link:** [[FE-00 - Peta Tools FE|Peta tools]] · [[10 - FE Vault|Hub modul]] · [[FE-01 - Batasan Platform FE|Batasan platform]]

Riset sumber tentang tool yang menghasilkan objek detail, tajam, dan ringan seperti Colorfigures. Disalin dari vault Monad Blitz (`/Users/Shenhan/HansProject/MOnadBlitz/vault`), catatan RS-01 (author **Gpt 6.1 sol - agentrouter**, 2026-10-22). Link ke tool memakai ID vault ini.

**Author:** Gpt 6.1 sol - agentrouter  
**Status riset:** SELESAI · **Tanggal:** 2026-10-22  


## Tujuan

Mencari skills, MCP, framework, dan tools yang menghasilkan objek detail, tajam, namun lightweight seperti [Colorfigures karya April Zhu](https://april-zhu.com/colorfigures).

## Kesimpulan utama

**Colorfigures sendiri tersedia sebagai AI skill dan menjadi pilihan paling dekat dengan referensi.** Implementasi yang diperiksa membangun geometri 3D secara prosedural, lalu memproyeksikannya ke SVG di dalam HTML interaktif. Rotasi mengubah proyeksi; beberapa figur memiliki mekanisme bergerak dan mode see-through.

Detail visual berasal dari komponen kecil yang terbaca, outline vektor, dan shading sederhana. Ini menjelaskan bagaimana figur terlihat detail tanpa mengandalkan mesh padat atau texture maps besar.

Pilihan berdasarkan kebutuhan:

- **Gaya persis referensi:** Colorfigures.
- **Komponen teknis dan cutaway presisi:** Anatomy.
- **Isometrik fine-line dan glow:** ISO-GLOW.
- **Framework prosedural untuk ilustrasi 3D sederhana:** Zdog.
- **SVG isometrik minimal:** iso-figure.
- **Mesh GLB yang dapat dipakai lintas renderer:** Blender + MCP → glTF Transform → model-viewer atau React Three Fiber.

Ranking di sini menilai kecocokan visual dan teknis. Pemilihan tools untuk batas waktu project tercatat di [[FE-00 - Peta Tools FE|Peta tools]].

## Mengapa detail tetap ringan

1. **Komponen geometris ekonomis:** box, extrusion, cylinder, dan rod untuk bodi, pipa, tombol, dan mekanisme.
2. **Pengulangan prosedural:** loop untuk kisi, sekrup, dan tick gauge.
3. **Outline yang terbaca:** garis luar tebal, garis interior tipis.
4. **Warna dan shading sederhana:** beberapa tone menggantikan material/tekstur kompleks.
5. **Proyeksi ortografis:** bentuk dan susunan komponen tetap jelas pada ukuran ilustrasi.

SVG filters untuk grain/wobble tetap menambah biaya runtime. Detail permukaan juga tidak seluruhnya murni vektor; implementasi memakai noise yang dibake lokal.

## Ukuran contoh yang diperiksa

Pengukuran pada 2026-10-22. Angka berikut merupakan ukuran body aset contoh, bukan benchmark FPS atau ukuran seluruh website.

| Aset | Ukuran | Sumber |
|---|---|---|
| Washer HTML interaktif | 127,887 bytes, sekitar 128 KB | [Live washer](https://april-zhu.com/colorfigures/live/washer) |
| Washer WebP, 480 × 360 | 12,998 bytes, sekitar 13 KB | [Preview washer](https://april-zhu.com/colorfigures/img/washer.webp) |
| Espresso WebP, 480 × 360 | 15,152 bytes, sekitar 15 KB | [Preview espresso](https://april-zhu.com/colorfigures/img/espresso.webp) |
| Galeri HTML dengan 26 figur tertanam | 2,894,995 bytes, sekitar 2.9 MB | [Galeri](https://april-zhu.com/colorfigures-demo) |

Satu figur cukup kecil; galeri lengkap jauh lebih besar. Payload kecil tidak otomatis berarti rendering murah, dan outline tajam tidak otomatis berarti presisi mesh manufaktur.

## Shortlist ilustrasi sekelas referensi

| Prioritas | Tool | Jenis dan output | Kekuatan | Batas |
|---|---|---|---|---|
| 1 | [[FE-32 - colorfigures\|Colorfigures]] | AI skill + engine JS; SVG dalam HTML interaktif | Gaya persis referensi; mesin berwarna, orbit, see-through | Occlusion kompleks dan effort authoring; exporter GLB/standalone SVG belum terverifikasi |
| 2 | [[FE-49 - Anatomy\|Anatomy]] | Agent skill + kit; SVG, HTML, React/Next.js | Komponen kecil, koneksi mekanis, cutaway presisi | Gaya lebih teknis; mode reprojected 3D masih beta |
| 3 | [[FE-31 - iso-glow\|ISO-GLOW]] | Skill; HTML isometrik dan template Three.js terpisah | Fine-line, komponen glowing, filled Lumen style | Mode 3D menambah engine/model; renderer berbeda dari Colorfigures |
| 4 | [[FE-55 - Zdog\|Zdog]] | Framework JS; SVG atau Canvas | Bentuk ilustratif bersih dan rotasi prosedural | Detail mesin, ink, shading, dan cutaway perlu kode sendiri |
| 5 | [[FE-48 - iso-figure\|iso-figure]] | AI skill; SVG murni dalam HTML | Minimal, tajam, tanpa library | Kurang turnkey untuk bodi berwarna dan mekanisme kompleks |

### Akses langsung

- Colorfigures: [halaman](https://april-zhu.com/colorfigures) · [skill ZIP](https://april-zhu.com/colorfigures/colorfigures.zip).
- Anatomy: [repository dan panduan pemasangan](https://github.com/wheresryan22/anatomy).
- ISO-GLOW: [halaman](https://isoglow.dev/) · [skill ZIP](https://isoglow.dev/iso-glow.zip).
- Zdog: [dokumentasi](https://zzz.dog/) · [repository](https://github.com/metafizzy/zdog).
- iso-figure: [repository](https://github.com/MrBongoC/ai-iso-skill).

Anatomy mendokumentasikan pemasangan untuk OpenCode:

```bash
npx skills add wheresryan22/anatomy -g -a opencode
```

## Pilihan untuk aset mesh GLB

| Tool | Peran | Temuan penting |
|---|---|---|
| [[FE-46 - Blender MCP\|Blender + Blender MCP]] | Authoring geometri presisi dan otomasi | Kontrol bevel, normals, komponen berulang, baking, dan export GLB. [MCP terverifikasi](https://github.com/ahujasid/mcp-for-blender) merupakan integrasi third-party |
| [Spline](https://spline.design/) | Editor scene interaktif | [MCP resmi](https://docs.spline.design/generate/spline-mcp-server.md) dan [skills resmi](https://github.com/splinetool/spline-skills). Export GLB tidak mempertahankan seluruh material, lighting, physics, dan interaksi |
| [[FE-38 - gltfjsx dan glTF-Transform\|glTF Transform]] | Optimasi aset | Inspect, deduplicate, simplify, quantize, kompresi geometri dan tekstur |
| [model-viewer](https://modelviewer.dev/) | Menampilkan satu model | Orbit, poster, loading, dan annotations |
| [[FE-37 - React Three Fiber dan drei\|React Three Fiber]] | Interaksi khusus dalam React | Scene komposabel, resource reuse, demand rendering |

MCP menyediakan antarmuka otomasi. Kualitas geometri, style, dan efisiensi aset tetap berasal dari proses authoring serta delivery.

[Meshy](https://docs.meshy.ai/en/api/text-to-3d) dan [Tripo](https://developers.tripo3d.ai/en/docs/generation-text-to-model/p) memiliki generasi low-poly dengan budget topology dan integrasi agent. Cocok untuk draft cepat; presisi mesin dan ukuran akhir kecil perlu diperiksa. Integrasi: [Meshy MCP](https://github.com/meshy-dev/meshy-mcp-server), [Meshy skills](https://github.com/meshy-dev/meshy-3d-agent), [Tripo CLI/MCP](https://developers.tripo3d.ai/en/docs/cli).

## Pipeline rekomendasi

### A. Ilustrasi interaktif paling dekat Colorfigures

**Colorfigures → satu HTML per figur → poster-first loading.**

Brief menyebut parts list, silhouette, palet, garis interior, kamera ortografis, orbit, dan mode see-through. Kurangi wobble bila ingin garis lebih bersih. Muat figur per kebutuhan agar payload galeri lengkap tidak ikut masuk.

### B. Ilustrasi teknis tajam

**Anatomy → SVG atau React → optimasi SVG selektif.**

Pilih SVG statis untuk ilustrasi tanpa rotasi. Pertahankan HTML/React bila kontrol diperlukan. [SVGO](https://svgo.dev/docs/introduction/) atau [SVGOMG](https://jakearchibald.github.io/svgomg/) dapat mengurangi SVG sambil menjaga IDs, filters, dan interaction hooks.

### C. Mesh 3D reusable

**Blender + MCP → GLB → glTF Transform → model-viewer atau R3F.**

Pertahankan silhouette, lubang, dan gap antarbagian sebagai geometri; gunakan bevel secukupnya dan material sederhana. Inspect hasil export sebelum simplification, deduplication, quantization, dan compression.

Untuk ilustrasi fixed-view, render ke WebP/AVIF juga dapat mempertahankan detail tanpa engine 3D di browser.

## Kriteria lightweight yang perlu dipisahkan

- **Download:** bytes HTML/model, tekstur, engine, decoder, dan environment map.
- **Runtime:** triangles, draw calls, SVG nodes/filters, CPU, GPU, dan memory.
- **Ketajaman visual:** silhouette, normals, outline, bevel, dan resolusi pada ukuran tampil.

Draco/Meshopt mengurangi transfer data; compression saja tidak mengurangi triangles atau draw calls. Decoder memiliki biaya startup. KTX2/Basis dapat mengurangi penggunaan memori tekstur GPU, dengan biaya transcoding. Normal maps mengubah shading, bukan silhouette.

## Bukti dan catatan lengkap

- Laporan: `/Users/Shenhan/HansProject/MOnadBlitz/reports/Lightweight detailed 3D tools.md`.
- Referensi dan ukuran contoh: `/Users/Shenhan/HansProject/MOnadBlitz/research_notes/Lightweight detailed 3D tools/reference.md`.
- Authoring, MCP, dan skills: `/Users/Shenhan/HansProject/MOnadBlitz/research_notes/Lightweight detailed 3D tools/creation.md`.
- Framework dan optimasi delivery: `/Users/Shenhan/HansProject/MOnadBlitz/research_notes/Lightweight detailed 3D tools/delivery.md`.

 Riset mencakup inspeksi sumber dan dokumentasi; ukuran contoh tidak membuktikan performa mobile atau kualitas hasil generasi lintas tools.
