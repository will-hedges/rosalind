#!/usr/bin/env python3
# orf.py

import re

from roz import *

def orf(data):
    codons = load_codons()['dna']
    start_codon = [codon for codon, aa in codons.items() if aa == 'M'].pop()
    stop_codons = [codon for codon, aa in codons.items() if aa is None]

    res = []
    while data:
        try:
            start_idx = data.index(start_codon)
            data = data[start_idx:]
            stop_idx = sorted([data.index(stop_codon) for stop_codon in stop_codons if stop_codon in data])[0]
            strand = data[:stop_idx]
            res.append(translate_to_amino_acids(strand))
            data = data[stop_idx:]
        except ValueError:
            break
        except IndexError:
            break
    return res


data = load_fasta_dict('rosalind_orf.txt')
data1 = list(data.values()).pop()
data2 = reverse_complement(data1)

res = []
res += orf(data1)
res += orf(data2)

print(set(res))

"""
MLLGSFRLIPKETLIQVAGSSPCNLS
M
MGMTPRLGLESLLE
MTPRLGLESLLE
"""