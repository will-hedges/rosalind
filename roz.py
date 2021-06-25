#!/usr/bin/env python3
# roz.py - module for Project Rosalind helper functions

import json

import pyperclip

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
        codon_dict = json.load(f)
    return codon_dict


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


def translate_codons_to_amino_acids(list_of_codons):
    codon_dict = load_codons()
    if 'U' in ''.join(list_of_codons):
        codon_dict = codon_dict['rna']
    else:
        codon_dict = codon_dict['dna']
    protein = ''
    while list_of_codons:
        codon = list_of_codons.pop(0)
        try:
            aa = codon_dict[codon]
        except KeyError:
            break
        else:
            if aa is None:
                break
            else:
                protein += aa
    return (protein, list_of_codons)


def split_into_codons(string_of_bases):
    return [string_of_bases[i:i+3] for i in range(0, len(string_of_bases), 3)]
