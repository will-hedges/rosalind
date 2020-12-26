#! python3
import re


def get_codons(base_lst):
    codon_lst = []
    while base_lst:
        codon_lst.append(''.join(base_lst[:3]))
        base_lst = base_lst[3:]
    return codon_lst


def translate_codons(codon_lst):
    rna_codon_dic = {
        'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
        'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
        'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M',
        'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
        'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
        'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'TAT': 'Y', 'TAC': 'Y', 'TAA': None, 'TAG': None,
        'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'TGT': 'C', 'TGC': 'C', 'TGA': None, 'TGG': 'W',
        'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }

    aa_str = ''
    for codon in codon_lst:
        aa = rna_codon_dic[codon]
        if aa is not None:
            aa_str += aa
        else:
            return aa_str


with open('rosalind_splc.txt', 'r') as infile:
# with open('splc_test.txt', 'r') as infile:
    data = [line.replace('\n', '')[13:] for line in infile.read().split('>') if line != '']

dna = list(data.pop(0))
exons = data

for exon in exons:
    mo = re.search(exon, ''.join(dna))
    if mo:
        del dna[mo.start():mo.end()]

codons = get_codons(dna)
print(translate_codons(codons))
