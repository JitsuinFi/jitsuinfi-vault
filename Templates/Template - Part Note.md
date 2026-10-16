---
tags: [template]
---

# Template - Part Note

> Template untuk part-note granular (satu node = satu topik). Dipakai di `Course-Maps/`, `Incubator-Maps/`.

```markdown
---
tags: [<kategori-part>, "<Identity>"]
---

# <Descriptive Title>

**Bagian dari:** [[<Hub>]]
**Sumber:** [[<folder>/<sourcefile>]]
**Terkait modul:** [[<Module Guide>]]   (omit bila sama)

**Ringkas:** <3-6 kalimat menjelaskan bagian ini.>

**Poin kunci:**
- <poin konkret>
- <4-8 poin>

**Detail sumber:**
- <excerpt / code verbatim dari sumber>
- <fakta: fungsi, parameter, nilai>
- <cross-link ke part/modul terkait>
```

Aturan:
- `<kategori-part>` mis. `course-part` / `incubator-part`.
- `<Identity>` mis. `M04` / `T09` (quote bila ada karakter khusus).
- `Sumber` wikilink ke `.md` asli; file bukan `.md` → inline code path.
- Nama file: `<Prefix>.<k> - <Title>.md`, `k` urut unik per grup.
