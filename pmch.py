#!/usr/bin/env python3
'''
Perfect Matching and RNA Secondary Structures (PMCH)
http://rosalind.info/problems/pmch/

Given:
    An RNA string s of length at most 80 bp having the same number
    of occurrences of 'A' as 'U' and the same number of occurrences
    of 'C' as 'G'.

Return:
    The total possible number of perfect matchings of basepair edges
    in the bonding graph of s.
'''

from math import factorial

from roz import load_fasta_string


def pmch(data):
    au = data.count('A')
    gc = data.count('G')
    return factorial(au) * factorial(gc)


def main():
    data = load_fasta_string('rosalind_pmch.txt')
    print(pmch(data))


if __name__ == '__main__':
    main()
