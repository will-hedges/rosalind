#! python3
# tran.py - http://rosalind.info/problems/tran/


import os
from pathlib import Path


os.chdir(Path(__file__).parent)


with open("rosalind_tran.txt", "r") as infile:
    data = [line[13:].replace("\n", "") for line in infile.read().split(">") if line != ""]

s1, s2 = data[0], data[1]
transitions, transversions = 0, 0

for i, x in enumerate(s1):
    y = s2[i]
    if x != y:
        if x in "AG" and y in "AG" or x in "CT" and y in "CT":
            transitions += 1
        elif x in "AG" and y in "CT" or x in "CT" and y in "AG":
            transversions += 1

print(transitions / transversions)
