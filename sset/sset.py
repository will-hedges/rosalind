#!/usr/bin/env python3
# sset.py - https://rosalind.info/problems/sset/

import itertools


def count_subsets(s, n):
    res = 0
    for i in range(n):
        res += len(list(itertools.combinations(s, i)))
    return res


def main():
    with open("rosalind_sset.txt", "r") as infile:
        n = int(infile.read().strip())

    s = set(i for i in range(n))
    res = count_subsets(s, n)
    print(res)
    return


if __name__ == "__main__":
    main()
