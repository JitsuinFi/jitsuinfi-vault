# new-note.ps1
# Generate a concept note from template into the Concepts/ folder.
# Usage:
#   powershell -ExecutionPolicy Bypass -File scripts\new-note.ps1 -Title "Flash Accounting" -Source "v4-architecture" -Module "02"
#   powershell -ExecutionPolicy Bypass -File scripts\new-note.ps1 -Title "MEV" -Related "cow","async-swaps"
# Params:
#   -Title    (required) concept name
#   -Source   (optional) source file basename to link, e.g. "v4-architecture"
#   -Module   (optional) module number "02" -> links the matching Module Guide
#   -Related  (optional) array of related note basenames
#   -Folder   (optional) target folder (default: Concepts)

param(
  [Parameter(Mandatory = $true)][string]$Title,
  [string]$Source,
  [string]$Module,
  [string[]]$Related,
  [string]$Folder = "Concepts"
)

$vault = Split-Path (Split-Path $PSScriptRoot -Parent) -Parent  # scripts\windows\ -> vault root
$nl = "`n"

# sanitize filename (strip chars invalid on Windows)
$safe = ($Title -replace '[<>:"/\\|?*]', '').Trim()
if ($safe -eq '') { Write-Host "ERROR: Title kosong setelah sanitasi." -ForegroundColor Red; exit 1 }

$dir = Join-Path $vault $Folder
if (-not (Test-Path -LiteralPath $dir)) { New-Item -ItemType Directory -Path $dir | Out-Null }

$path = Join-Path $dir ($safe + ".md")
if (Test-Path -LiteralPath $path) {
  Write-Host "SKIP: sudah ada -> $Folder/$safe.md" -ForegroundColor Yellow
  exit 0
}

# resolve module guide link if -Module given
$moduleLink = $null
if ($Module) {
  $guideDir = Join-Path $vault 'Module-Guides'
  $prefix = "^" + $Module + " "
  $g = Get-ChildItem -LiteralPath $guideDir -Filter *.md -ErrorAction SilentlyContinue | Where-Object { $_.Name -match $prefix } | Select-Object -First 1
  if ($g) { $moduleLink = $g.BaseName }
}

$c = New-Object System.Collections.Generic.List[string]
$c.Add("---")
$c.Add("tags: [concept]")
$c.Add("---")
$c.Add("")
$c.Add("# $Title")
$c.Add("")
$c.Add("**Definisi:** _TODO 1-2 kalimat._")
$c.Add("")
$c.Add("**Detail:** _TODO penjelasan._")
$c.Add("")
$refParts = @()
if ($Source)     { $refParts += "[[$Source]]" }
if ($moduleLink) { $refParts += "[[$moduleLink]]" }
if ($refParts.Count -gt 0) { $c.Add("**Referensi:** " + ($refParts -join ", ")) } else { $c.Add("**Referensi:** _TODO_") }
$c.Add("")
$relList = @()
if ($Related) { $relList = $Related | ForEach-Object { $_ -split ',' } | ForEach-Object { $_.Trim() } | Where-Object { $_ -ne '' } }
if ($relList.Count -gt 0) {
  $rel = ($relList | ForEach-Object { "[[$_]]" }) -join ", "
  $c.Add("**Related:** $rel")
} else {
  $c.Add("**Related:** _TODO_")
}

Set-Content -LiteralPath $path -Value ($c -join $nl) -Encoding UTF8
Write-Host "OK  dibuat: $Folder/$safe.md" -ForegroundColor Green

# validate links
& (Join-Path $PSScriptRoot 'check-links.ps1') | Out-Null
if ($LASTEXITCODE -eq 0) { Write-Host "OK  semua link valid." -ForegroundColor Green }
else { Write-Host "WARN cek link: ada link belum resolve (isi TODO dulu)." -ForegroundColor Yellow }
