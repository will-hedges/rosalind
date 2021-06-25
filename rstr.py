#!/usr/bin/env python3
# rstr.py - http://rosalind.info/problems/rstr/


def prst(N, x, s):
    pass


def main():
    with open('rosalind_rstr.txt') as file:
        N, x = file.readline().split()
        N, x = int(N), float(x)
        s = file.readline().strip()

    prst(N, x, s)


if __name__ == '__main__':
    main()
