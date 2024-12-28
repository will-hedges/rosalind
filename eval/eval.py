#!/usr/bin/env python3
# eval.py -

from ..prob.prob2 import calculate_random_chances


def main():
    with open("./eval/rosalind_eval.txt") as fo:
        data = [line.strip() for line in fo.readlines()]

    n, s, p = data
    n = int(n)
    p = [float(x) for x in p.split(" ")]

    return


if __name__ == "__main__":
    main()
