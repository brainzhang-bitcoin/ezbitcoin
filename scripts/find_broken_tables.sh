#!/bin/bash
# Find files in docs/technical/ containing patterns of broken tables
mkdir -p scratch
grep -lE "(^0$|0 secs|随机示例|0 bytes|128 Bit \(12 words\))" -r docs/technical/ > scratch/broken_tables.txt
echo "Found $(wc -l < scratch/broken_tables.txt) files."
