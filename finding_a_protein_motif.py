#! python3
# finding_a_protein_motif.py - http://rosalind.info/problems/mprt/
import logging
import os
from pathlib import Path
logging.basicConfig(level=logging.DEBUG, format=' %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
os.chdir(Path(__file__).parent)


import re
import requests

with open('rosalind_mprt.txt', 'r') as infile:
    proteins = [line.strip() for line in infile.readlines()]

with open('mprt_ans.txt', 'w') as outfile:
    for protein in proteins:
        res = requests.get(f'https://www.uniprot.org/uniprot/{protein}.fasta')
        res.raise_for_status()

        if not res.text:
            print(f'Redirected at URL: https://www.uniprot.org/uniprot/{protein}')
            url = input('Enter the new URL: ')
            res = requests.get(url)
            res.raise_for_status()

        seq = ''.join(res.text.split('\n')[1:])
        mo = re.finditer(r'(?=N[^P][ST][^P])', seq)
        idxs = [str(match.start() + 1) for match in mo]

        if idxs:
            outfile.write(protein + '\n')
            outfile.write(' '.join(idxs) + '\n')

print('Done.')
