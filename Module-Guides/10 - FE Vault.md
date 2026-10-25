---
tags: [module, "10"]
---

# 10 - FE Vault

**Tujuan:** Peta semua tool frontend JitsuinFi (library, skill, MCP, referensi) sampai ke akarnya: sumber, versi, lisensi, lokasi pasang, cara kerja, tempat dipakai, batasan, dan status. Dibuat 2026-10-20 supaya pekerjaan FE fokus pada tool yang benar dan tidak ada yang terlewat. Tidak mencakup `09-Design`.

Kembali: [[START-HERE]]

## Mulai di sini
- [[10-FE-vault/FE-M0 - Mandat FE]]: mandat user untuk FE (level PortoWeb, 65/35, tanpa kartu, semua MCP dan tool) dengan aturan yang bisa dicek.
- [[10-FE-vault/FE-00 - Peta Tools FE]]: tabel semua tool, alur end to end, temuan audit.
- [[10-FE-vault/FE-01 - Batasan Platform FE]]: CSP same-origin, tanpa CDN, izin dependensi; berlaku untuk semua tool.

## Build, tes, deploy
- [[10-FE-vault/FE-02 - Vite]] · [[10-FE-vault/FE-03 - TypeScript]] · [[10-FE-vault/FE-04 - Node Test Runner]] · [[10-FE-vault/FE-05 - jitsuin-wasm Bindings]] · [[10-FE-vault/FE-06 - Vercel Deploy dan CI]]

## Library
- [[10-FE-vault/FE-07 - three.js]] · [[10-FE-vault/FE-08 - anime.js]] · [[10-FE-vault/FE-09 - Motion]] · [[10-FE-vault/FE-10 - Lenis]] · [[10-FE-vault/FE-11 - hairline]] · [[10-FE-vault/FE-12 - Font Fontsource]]

## Skill
- [[10-FE-vault/FE-13 - genjutsu]] · [[10-FE-vault/FE-14 - impeccable]] · [[10-FE-vault/FE-15 - Skill Artifact dan dataviz]] · [[10-FE-vault/FE-28 - frontend-design]]

## MCP
- Verifikasi: [[10-FE-vault/FE-16 - Claude Browser Pane]] · [[10-FE-vault/FE-17 - Claude in Chrome]]
- Riset: [[10-FE-vault/FE-18 - Mobbin]] · [[10-FE-vault/FE-19 - ScreensDesign]] · [[10-FE-vault/FE-20 - MotionSites]] · [[10-FE-vault/FE-21 - Refero]]
- Presentasi dan media: [[10-FE-vault/FE-22 - Visualize Widget]] · [[10-FE-vault/FE-23 - Motion.so]] · [[10-FE-vault/FE-24 - Canva]]

## Belum terpasang dan referensi
- [[10-FE-vault/FE-25 - React Bits shadcn MCP]] · [[10-FE-vault/FE-26 - motionmaxxing]] · [[10-FE-vault/FE-27 - Referensi Visual Vault]] · [[10-FE-vault/FE-29 - PortoWeb Benchmark]]

## Tambahan dari vault Monad Blitz (2026-10-23)
- Skill figur isometrik: [[10-FE-vault/FE-48 - iso-figure]] · [[10-FE-vault/FE-49 - Anatomy]] · [[10-FE-vault/FE-32 - colorfigures]] · [[10-FE-vault/FE-31 - iso-glow]] · [[10-FE-vault/FE-33 - playable]] · [[10-FE-vault/FE-50 - Neon Diagrams]] · [[10-FE-vault/FE-51 - isometric-motion]] · [[10-FE-vault/FE-52 - isometric-objects (gist)]] · [[10-FE-vault/FE-53 - isometric-ops]] · [[10-FE-vault/FE-47 - game-creator (opusgamelabs)]] · [[10-FE-vault/FE-58 - Threejs Awesome Graphics Agent Skills]]
- Library ilustrasi/3D/game: [[10-FE-vault/FE-54 - heerich]] · [[10-FE-vault/FE-55 - Zdog]] · [[10-FE-vault/FE-56 - isometric (elchininet)]] · [[10-FE-vault/FE-37 - React Three Fiber dan drei]] · [[10-FE-vault/FE-38 - gltfjsx dan glTF-Transform]] · [[10-FE-vault/FE-60 - model-viewer]] · [[10-FE-vault/FE-39 - PixiJS]] · [[10-FE-vault/FE-40 - KAPLAY]] · [[10-FE-vault/FE-41 - Phaser]] · [[10-FE-vault/FE-42 - Lottie (dotLottie)]]
- Audio dan efek: [[10-FE-vault/FE-34 - ZzFX]] · [[10-FE-vault/FE-35 - canvas-confetti]] · [[10-FE-vault/FE-36 - Howler.js]] · Optimasi: [[10-FE-vault/FE-59 - SVGO]]
- Aset: [[10-FE-vault/FE-43 - Kenney]] · [[10-FE-vault/FE-44 - Quaternius]] · [[10-FE-vault/FE-45 - Poly Pizza]]
- MCP dan layanan 3D: [[10-FE-vault/FE-46 - Blender MCP]] · [[10-FE-vault/FE-61 - Spline MCP]] · [[10-FE-vault/FE-62 - Meshy dan Tripo]] · [[10-FE-vault/FE-57 - Recraft MCP]]
- Akun: [[10-FE-vault/FE-30 - Mera]] · Riset: [[10-FE-vault/FE-63 - Riset Aset 3D Ringan]]

## Konsep kunci
- Satu tool = satu file `FE-xx`; ID tidak dipakai ulang.
- Saat tool dipasang, dihapus, atau mulai dipakai: perbarui file tool-nya dan baris di FE-00.
