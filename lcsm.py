#!/usr/bin/env python3
# lcsm.py

from roz import get_fasta_dict, copy_answer_to_clipboard

data = get_fasta_dict("rosalind_lcsm.txt")
data = list(data.values())
first_strand = data[0]

ans = ""
# slice fwd
for i in range(1, len(data[0]) + 1):
    res = []
    sub_string = first_strand[:i]
    for strand in data:
        if sub_string in strand:
            res.append(True)
        else:
            res.append(False)
    if all(res) and len(sub_string) >= len(ans):
        ans = sub_string
# slice bkwd

print(ans)
