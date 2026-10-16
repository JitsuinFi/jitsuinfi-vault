---
tags: [template]
---

# Template - Test

> Satu file per item, tiga lapis. Struktur:

```markdown
---
tags: [test, "HNK-xx"]
type: test
id: HNK-xx
unit: TODO
integrasi: TODO
e2e: TODO
---

# TEST-HNK-xx - <Judul>

> **Peta link:** [[Testing Hub]] · [[Backlog]] · [[AC-HNK-xx - <Judul>|AC]] · **Test** · [[ES-HNK-xx - <Judul>|Exec Summary]]

## 1. Unit           (logika murni, tanpa DB/chain)
## 2. Integrasi      (vs DB/chain sungguhan, artefak TES-, bukti pembersihan)
## 3. E2E            (checkbox + tabel hasil untuk user)
```
