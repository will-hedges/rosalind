#!/usr/bin/env python3
# rstr.py - http://rosalind.info/problems/rstr/


def prst(N, x, s):
    p = 1               # initialize overall probability of any string
    p_cg = x / 2        # probability of either G or C (GC content)
    p_at = (1 - x) / 2  # probability of either A or T (complement of GC)

    base_dict = {base: s.count(base) for base in 'ATGC'}

    # determine the probability p of the string s forming for one string
    #   the exponent is basically 'out of all the CG/AT in this string
    #       this has to be one of them'
    for base, count in base_dict.items():
        if base in 'GC':
            p *= p_cg**count
        else:
            p *= p_at**count

    # the probability t 'not s' that there is no random string s in N strings
    t = (1 - p) ** N
    # the probability u 'not t', that a random string == s out of N strings
    u = 1 - t

    return "{:0.3f}".format(u)


def main():
    with open('rosalind_rstr.txt') as file:
        N, x, s = file.read().strip().split()
        N = int(N)
        x = float(x)
    ans = prst(N, x, s)
    print(ans)


if __name__ == '__main__':
    main()
