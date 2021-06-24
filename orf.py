#!/usr/bin/env python3
# orf.py

import re

from roz import *

data = load_fasta_dict('rosalind_orf.txt')
strandf = list(data.values()).pop()
strandr = reverse_complement(strandf)

def orf(strand):
    stop_codons = ['TAA', 'TAG', 'TGA']
    ### ALGORITHM ###
    start_idx = strand.idx('ATG')
    # split into codons from ATG forward
    split_strand = split_into_codons(strand[start_idx:])
    # look for any stop codon
    # recombine into string
    # repeat
"""
MLLGSFRLIPKETLIQVAGSSPCNLS
M
MGMTPRLGLESLLE
MTPRLGLESLLE
"""