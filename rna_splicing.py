# http://rosalind.info/problems/splc/

import os
from pathlib import Path
os.chdir(Path(__file__).parent)


#! python3
import re


with open('splc_test.txt', 'r') as infile:
    data = [line.strip() for line in infile.readlines() if not line.startswith('>')]

dna_str = list(data.pop(0))
exons = data

for exon in exons:
    mo = re.search(exon, ''.join(dna_str))
    if mo:
        del dna_str[mo.start():mo.end()]

print(''.join(dna_str))
