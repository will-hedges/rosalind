#!/usr/bin/env python3
# sset.py - https://rosalind.info/problems/sset/

import itertools


def count_subsets(n):
    """
    n = 3 ("buffy", "puppy", "nugget")
    1. {}
    2, 3, 4. {"buffy"}, {"puppy"}, {"nugget"}
    5. {"buffy", "puppy"}
    6. {"buffy", "nugget"}
    7. {"puppy", "nugget"}
    8. {"nugget", "puppy", "buffy"}
    """
    res = [itertools.combinations(range(n), ni) for ni in range(n + 1)]
    res = itertools.chain(*res)
    return res


def main():
    with open("rosalind_sset.txt", "r") as infile:
        data = int(infile.read().strip())
    res = count_subsets(data)
    print(res)
    return


if __name__ == "__main__":
    main()
