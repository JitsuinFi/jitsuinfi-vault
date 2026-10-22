#!/bin/sh
# Usage: shots.sh <out-dir> <base-url> <name=path>...  Viewport shots 1440x900, 390x844 and a tall 1440x4000, plus the DOM.
out=$1; base=$2; shift 2; mkdir -p "$out"
C="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
P=$(mktemp -d)
for pair in "$@"; do
  name=${pair%%=*}; path=${pair#*=}
  for size in 1440,900 390,844 1440,4000; do
    tag=$(echo $size | tr , x)
    "$C" --headless=new --use-angle=swiftshader --enable-unsafe-swiftshader --hide-scrollbars --user-data-dir="$P" --window-size=$size --virtual-time-budget=6000 --screenshot="$out/$name-$tag.png" "$base$path" >/dev/null 2>&1
    sips -s format jpeg -s formatOptions 70 "$out/$name-$tag.png" --out "$out/$name-$tag.jpg" >/dev/null 2>&1 && rm "$out/$name-$tag.png"
  done
  "$C" --headless=new --use-angle=swiftshader --enable-unsafe-swiftshader --user-data-dir="$P" --window-size=1440,900 --virtual-time-budget=6000 --dump-dom "$base$path" 2>/dev/null > "$out/$name.dom.html"
  echo "$name done"
done
rm -rf "$P"
