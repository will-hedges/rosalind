#!/usr/bin/env python3
'''
Generalizing GC-Content (KMER)
http://rosalind.info/problems/kmer/

Given: A DNA string s in FASTA format (having length at most 100 kbp)
Return: The 4-mer composition of s
'''

from functools import partial
from io import StringIO

from roz import load_fasta_string


def kmer(s, lex):

    ans = sorted(
        [x for x in iter(partial(StringIO(s).read, 4), '')],
        key=lambda lex: [lex.index(base) for base in lex]
    )
    arr = [s.count(l) for l in ans if len(l) == 4]
    print(arr)



def main():
    s = load_fasta_string('rosalind_kmer.txt')
    lex = sorted([(s.index(base), base) for base in 'ATCG'])
    lex = ''.join([tup[1] for tup in lex])
    ans = kmer(s, lex)


if __name__ == '__main__':
    main()
