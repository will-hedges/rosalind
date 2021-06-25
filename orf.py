#!/usr/bin/env python3
# orf.py

import re

from roz import split_into_codons, translate_codons_to_amino_acids, load_fasta_dict, reverse_complement


def orf(data):
    res = []
    stop_codons = ['TAA', 'TAG', 'TGA']
    start_codon_idxs = [i for i in range(len(data)) if data.startswith('ATG', i)]
    for idx in start_codon_idxs:
        frame = data[idx:]
        frame = split_into_codons(frame)
        if any([frame.index(stop_codon) if stop_codon in frame else False for stop_codon in stop_codons]):
            res.append(translate_codons_to_amino_acids(frame)[0])
    return res


def main():
    data = load_fasta_dict('rosalind_orf.txt')
    strandf = list(data.values()).pop()
    strandr = reverse_complement(strandf)

    ans = orf(strandf) + orf(strandr)
    ans = set(ans)

    with open('orf_answer.txt', 'w') as outfile:
        for protein in ans:
            outfile.write(protein + '\n')


if __name__ == '__main__':
    main()

"""
MLLGSFRLIPKETLIQVAGSSPCNLS
M
MGMTPRLGLESLLE
MTPRLGLESLLE
"""