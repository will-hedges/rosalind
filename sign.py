#! python3
# sign.py - http://rosalind.info/problems/sign/


import itertools
import logging
import os
from pathlib import Path


logging.basicConfig(level=logging.DEBUG, format=" %(levelname)s - %(message)s")
# logging.disable(logging.CRITICAL)

os.chdir(Path(__file__).parent)


def sign(n):

    lst = []
    for i in range(1, n + 1):
        lst.append(i)
        lst.append(-i)

    perms = [perm for perm in itertools.permutations(lst, 2)]
    for perm in perms:
        a, b = perm[0], perm[1]
        if abs(a) == abs(b):
            perms.remove(perm)

    with open("sign_ans.txt", "w") as outfile:
        outfile.write(f"{len(perms)}\n")
        for perm in perms:
            perm = map(str, perm)
            outfile.write(f'{" ".join(perm)}\n')

    print("Done.")
    return


sign(2)
