---
tags: [template]
---

# Template - MOC

> Template untuk Map of Content (indeks navigasi). Taruh di root atau folder panduan.

```markdown
---
tags: [moc, <nama>]
---

# <Judul MOC>

Pengantar singkat: <apa yang dipetakan MOC ini.>

## Bagian A
- [[<Note 1>]
- [[<Note 2>]

## Bagian B
- [[<Note 3>]

## Auto (Dataview)
```dataview
LIST FROM #<tag> SORT file.name ASC
```
```

MOC harus link ke node penting & punya setidaknya satu query Dataview folder-based supaya konten baru otomatis muncul.
