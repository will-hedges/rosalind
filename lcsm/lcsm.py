#!/usr/bin/env python3
# lcsm.py

from itertools import combinations

from roz import load_fasta_dict

"""Brute force slow (~2 minutes), but it does work!"""

def lcsm(data):
    # generate all substrings of the first_string string
    first_string = data[0]
    substrings = [
        first_string[x:y] for x, y in combinations(
            range(len(first_string) + 1), r=2
        )
    ]

    # store all the common substrings in a dictionary by length as key
    common_substrings = {len(substring): [] for substring in substrings}
    for substring in substrings:
        if all([substring in string for string in data]):
            common_substrings[len(substring)].append(substring)

    # return any common substring, as long as it is one of the longest
    ans_length = sorted([k for k, v in common_substrings.items() if v], reverse=True)[0]
    ans = common_substrings[ans_length][0]
    return ans


def main():
    data = load_fasta_dict("rosalind_lcsm.txt")
    data = list(data.values())
    ans = lcsm(data)
    print(ans)


if __name__ == '__main__':
    main()
