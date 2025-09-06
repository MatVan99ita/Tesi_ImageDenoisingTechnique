#!/bin/bash
# Script per stampare nome, dimensioni e peso (MB) di tutte le immagini
# in tutte le sottocartelle, ordinate per peso decrescente

find . -type f \( -iname "*.jpg" -o -iname "*.png" \) | while read -r f; do
    size_bytes=$(stat -c%s "$f")                       # dimensione in byte
    size_mb=$(echo "scale=2; $size_bytes/1048576" | bc)  # converte in MB con 2 decimali
    dims=$(identify -format "%wx%h" "$f")             # larghezza x altezza
    echo "$size_mb MB $f - $dims"
done | sort -nr

