#!/usr/bin/env python3
# prob2.py - refactored prob.py

import math


def calculate_random_chances(dna_str, prob_arr):
    res = []

    for p in prob_arr:
        p_dna = 1
        p_cg = p / 2
        p_at = (1 - p) / 2

        for base in dna_str:
            if base in "CG":
                p_dna *= p_cg
            elif base in "AT":
                p_dna *= p_at

        res.append(str(round(math.log10(p_dna), 3)))

    return res


def main():
    with open("./prob/rosalind_prob.txt", "r") as fo:
        data = [line.strip() for line in fo.readlines()]
    dna, probs = data
    probs = [float(p) for p in probs.split(" ")]

    res = calculate_random_chances(dna, probs)
    print(" ".join(res))
    return


if __name__ == "__main__":
    main()
