import itertools
import os
from pathlib import Path


def lexf():
    # with open('lexf_test.txt', 'r') as infile:
    with open('rosalind_lexf.txt', 'r') as infile:
        symbols = infile.readline().strip().replace(' ', '')
        posint = int(infile.readline())

    combo_lst = [x for x in itertools.product(symbols, repeat=posint)]

    with open('lexf_ans.txt', 'w') as outfile:
        for combo in combo_lst:
            outfile.write(f"{''.join(combo)}\n")

    print('Done.')
    return


os.chdir(Path(__file__).parent)

lexf()
