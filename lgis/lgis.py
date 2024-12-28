#!/usr/bin/env python3
'''
Longest Increasing Subsequence (LGIS)
http://rosalind.info/problems/lgis/

Return a longest increasing subsequence of π,
followed by a longest decreasing subsequence of π.
'''

def lgis(pi):
    for i, idx in enumerate(pi):
        inc = [i] + [j for j in pi[idx:] if j > i]
        for k, kdx in enumerate(inc[1:]):
            try:
                if inc[kdx+1] > k:
                    del inc[kdx]
            except IndexError:
                pass

        print(inc)

def main():
    with open('rosalind_lgis.txt') as infile:
        data = infile.read().splitlines()
    data = [int(x) for x in data[1].split()]
    print(lgis(data))

if __name__ == '__main__':
    main()
