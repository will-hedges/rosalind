#! python3
# sseq.py - http://rosalind.info/problems/sseq/

import os
from pathlib import Path


def sseq(dna, substr):
    lst = list(substr)

    i = 0
    idxs = []

    while lst:
        base = lst.pop(0)
        while dna[i] != base:
            i += 1
        idxs.append(i + 1)
        i += len(lst)

    return " ".join(map(str, idxs))


os.chdir(Path(__file__).parent)

with open("rosalind_sseq.txt", "r") as infile:
    raw_data = infile.read().replace("\n", "").split(">")
    data = [line[13:] for line in raw_data if line != ""]

s = data[0]
t = data[1]

print(sseq(s, t))
