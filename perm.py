import logging
import itertools
import os
from pathlib import Path


logging.basicConfig(level=logging.DEBUG, format=' %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)


os.chdir(Path(__file__).parent)


def perm(n):
    with open('perm_ans.txt', 'w') as outfile:
        s = ''
        for i in range(1, n+1):
            s += str(i)
        lst = [i for i in itertools.permutations(s)]
        outfile.write(f'{len(lst)}\n')
        for tpl in lst:
            outfile.write(f"{' '.join(tpl)}\n")

    print('Done.')


perm(5)
