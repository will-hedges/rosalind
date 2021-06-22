#!/usr/bin/env python3
# orf.py

import re

from roz import load_fasta_dict, load_codons, copy_answer_to_clipboard, translate_to_amino_acids


# choose rna codons
codons = load_codons()['dna']
start_codon = [codon for codon, aa in codons.items() if aa == 'M'].pop()
stop_codons = [codon for codon, aa in codons.items() if aa is None]

data = load_fasta_dict('rosalind_orf.txt')
data = list(data.values()).pop()

res = []

while True:
    stop_idxs = sorted([data.index(stop_codon) for stop_codon in stop_codons if stop_codon in data])
    if any(stop_idxs):
        try:
            start_idx = data.index(start_codon)
            stop_idx = stop_idxs[0]
        except ValueError:
            break
        else:
            strand = data[start_idx:stop_idx]
            data = data[stop_idx+2:]
            aa_chain = translate_to_amino_acids(strand)
            res.append(aa_chain)

print(res)