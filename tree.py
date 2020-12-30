#! python3
# tree.py - http://rosalind.info/problems/tree/

import os
from pathlib import Path


os.chdir(Path(__file__).parent)

data = []
with open('rosalind_tree.txt', 'r') as infile:
    for line in infile.readlines():
        data.append([int(x) for x in line.split()])

nodes = data.pop(0).pop()
total_edges = nodes - 1
present_edges = len(data)

missing_edges = total_edges - present_edges
print(missing_edges)
