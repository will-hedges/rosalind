#!/usr/bin/env python3
'''
Locating Restriction Sites (REVP)
http://rosalind.info/problems/revp/

Return the position and length of every reverse palindrome in the string
having length between 4 and 12. You may return these pairs in any order.
'''

from itertools import combinations

from roz import load_fasta_string, reverse_complement, copy_answer_to_clipboard


def revp(s):
    substrings = [
        (x+1, s[x:y]) for x, y in combinations(range(len(s) + 1), r=2) if len(s[x:y]) in range(4, 13)
    ]
    res = []
    for tup in substrings:
        idx, val = tup[0], tup[1]
        if val == reverse_complement(val):
            res.append((idx, len(val)))

    return res


def main():
    data = load_fasta_string('rosalind_revp.txt')
    ans = revp(data)
    with open('revp_answer.txt', 'w') as outfile:
        for index, palindrome in ans:
            outfile.write(f'{index} {palindrome}\n')
    copy_answer_to_clipboard('revp_answer.txt')


if __name__ == '__main__':
    main()
