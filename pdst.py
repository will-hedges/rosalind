#! python3
# pdst.py - http://rosalind.info/problems/pdst/

import os
from pathlib import Path
os.chdir(Path(__file__).parent)


# with open('pdst_test.txt', 'r') as infile:
with open('rosalind_pdst.txt', 'r') as infile:
    data = [line.strip() for line in infile.readlines() if not line.startswith('>')]

ans = []
for j in data:
    lst = []
    for k in data:
        count = 0
        for b1, b2 in zip(j, k):
            if b1 != b2:
                count += 1
        lst.append('%.5f' % (count / len(j)))
    ans.append(' '.join(lst))

with open('pdst_ans.txt', 'w') as outfile:
    for a in ans:
        outfile.write(f'{a}\n')

print('Done.')
