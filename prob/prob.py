import logging
import math
import os
from pathlib import Path


logging.basicConfig(level=logging.DEBUG, format=" %(levelname)s - %(message)s")
# logging.disable(logging.CRITICAL)


os.chdir(Path(__file__).parent)


# with open('prob_test.txt', 'r') as infile:
with open("rosalind_prob.txt", "r") as infile:
    dna = infile.readline().strip()
    probs = [float(p) for p in infile.readline().split(" ")]


def prob(dna_str, p_arr):

    rand_chances = []

    for p in p_arr:
        p_dna = 1
        p_cg = p / 2
        p_at = (1 - p) / 2

        for base in dna_str:
            if base in "CG":
                p_dna *= p_cg
            elif base in "AT":
                p_dna *= p_at

        rand_chances.append(math.log10(p_dna))

    return rand_chances


with open("prob_ans.txt", "w") as outfile:
    for x in prob(dna, probs):
        outfile.write("{:0.3f} ".format(x))

print("Done.")
