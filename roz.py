#!/usr/bin/env python3
# roz.py - module for Project Rosalind helper functions

import json

import pyperclip

# TODO write unit tests

def load_fasta_dict(filepath):
    fasta_dict = {}
    with open(filepath) as f:
        data = f.read().splitlines()
    strand = ''
    name = data[0]
    for line in data[1:]:
        if line.startswith('>'):
            fasta_dict[name] = strand
            strand = ''
            name = line
        else:
            strand += line
    # capture the last one built strand
    fasta_dict[name] = strand
    return fasta_dict


def copy_answer_to_clipboard(filepath):
    with open(filepath) as f:
        pyperclip.copy(f.read().strip())


def load_codons():
    with open('codons.json') as f:
        codons = json.load(f)
    return codons


def reverse_complement(strand):
    strand = list(strand)
    strand.reverse()
    res = ''
    for base in strand:
        if base == 'A':
            res += 'T'
        elif base == 'T':
            res += 'A'
        elif base == 'C':
            res += 'G'
        elif base == 'G':
            res += 'C'
    return res

def split_into_codons(strand):
    return [strand[i:i+3] for i in range(0, len(strand), 3)]

# TODO make a nice answer writer function? maybe maybe not
def translate_to_amino_acids(strand):
    codons = load_codons()
    if 'U' in strand:
        codons = codons['rna']
    else:
        codons = codons['dna']
    ## this may or may not work, what if no U or T?
    chunks = split_into_codons(strand)
    aas = []
    for chunk in chunks:
        if len(chunk) == 3 and codons[chunk] is not None:
            aas.append(codons[chunk])
    return ''.join(aas)
