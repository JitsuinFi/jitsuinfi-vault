---
tags: [hub, dashboard]
---

# Dashboard

Status semua artefak, otomatis lewat Dataview (jalan di Obsidian GUI). Sumber kebenaran tetap file per item.

Kembali: [[START-HERE]] · [[Rencana Fase]]

## Spikes (gerbang F0)
```dataview
TABLE WITHOUT ID file.link AS "Spike", owner AS "Owner", area AS "Area", status AS "Status", updated AS "Update"
FROM "02-Spikes"
WHERE type = "spike"
SORT id ASC
```

## Acceptance criteria per item
```dataview
TABLE WITHOUT ID file.link AS "AC", phase AS "Fase", lead AS "Lead", status AS "Status", updated AS "Update"
FROM "04-Acceptance-Criteria"
WHERE type = "ac"
SORT id ASC
```

## Per orang
Rincian task dan jam ada di [[Backlog]]. Filter cepat lewat tag: `#hans`, `#dex`, `#dave` (panel Tags atau Search).

```dataview
TABLE WITHOUT ID lead AS "Lead", length(rows) AS "Jumlah item", rows.file.link AS "Item"
FROM "04-Acceptance-Criteria"
WHERE type = "ac"
GROUP BY lead
```

```dataview
TABLE WITHOUT ID file.link AS "Spike", status AS "Status"
FROM "02-Spikes"
WHERE type = "spike" AND owner = "Hans"
SORT id ASC
```

## Testing per item
```dataview
TABLE WITHOUT ID file.link AS "Test", unit AS "Unit", integrasi AS "Integrasi", e2e AS "E2E"
FROM "05-Testing"
WHERE type = "test"
SORT id ASC
```

## Executive summary per item
```dataview
TABLE WITHOUT ID file.link AS "Exec Summary", phase AS "Fase", status AS "Status"
FROM "06-Executive-Summary"
WHERE type = "es"
SORT id ASC
```

## Item yang belum lulus
```dataview
TABLE WITHOUT ID file.link AS "AC", phase AS "Fase", status AS "Status"
FROM "04-Acceptance-Criteria"
WHERE type = "ac" AND status != "PASS"
SORT id ASC
```

## Spike yang gagal atau terblokir
```dataview
TABLE WITHOUT ID file.link AS "Spike", status AS "Status"
FROM "02-Spikes"
WHERE type = "spike" AND (status = "FAIL" OR status = "BLOCKED")
SORT id ASC
```
