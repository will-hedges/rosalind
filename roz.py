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

# TODO make a nice answer writer function? maybe maybe not
def translate_to_amino_acids(strand):
    codons = load_codons()
    if 'U' in strand:
        codons = codons['rna']
    else:
        codons = codons['dna']
    ## this may or may not work, what if no U or T?
    chunks = [strand[i:i+3] for i in range(0, len(strand), 3)]
    aas = []
    for chunk in chunks:
        if len(chunk) == 3:
            aas.append(codons[chunk])
    return ''.join(aas)

print(translate_to_amino_acids('ACTGCATATA'))