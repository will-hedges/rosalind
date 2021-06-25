#! python3
# lexv.py - http://rosalind.info/problems/lexv/

import os
from pathlib import Path


os.chdir(Path(__file__).parent)


import itertools


with open("rosalind_lexv.txt", "r") as infile:
    sym = "".join(infile.readline().split())
    n = int(infile.readline())

ans = []
for i in range(1, n + 1):
    ans += ["".join(t) for t in itertools.product(sym, repeat=i)]

with open("lexv_ans.txt", "w") as outfile:
    for a in sorted(ans, key=lambda word: [sym.index(x) for x in word]):
        outfile.write(f"{a}\n")
