#!/usr/bin/env python3
# pdst.py

from roz import get_fasta_dict, copy_answer_to_clipboard

data = get_fasta_dict('rosalind_pdst.txt')

ans = []
for strand1 in data.values():
    res = []
    for strand2 in data.values():
        count = 0
        for base1, base2 in zip(list(strand1), list(strand2)):
            if base1 != base2:
                count += 1
        # fill in zeros so that you have a total of 5 decimal places
        #   but clip off extra decimal places
        fmt = '{:<07}'
        res.append(fmt.format(count/len(strand1))[:7])
    ans.append(' '.join(res))

outfile = 'pdst_answer.txt'
with open(outfile, 'w') as f:
    for line in ans:
        f.write(line + '\n')

copy_answer_to_clipboard(outfile)
