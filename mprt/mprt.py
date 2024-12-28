# http://rosalind.info/problems/mprt/


import re
import requests


with open("rosalind_mprt.txt", "r") as infile:
    proteins = [line.strip() for line in infile.readlines()]

ans = []


for protein in proteins:
    res = requests.get(f"https://www.uniprot.org/uniprot/{protein}.fasta")
    res.raise_for_status()

    if not res.text:
        print(f"Redirected at URL: https://www.uniprot.org/uniprot/{protein}")
        url = input("Enter the new URL: ")
        res = requests.get(url)
        res.raise_for_status()

    seq = "".join(res.text.split("\n")[1:])
    mo = re.finditer(r"(?=N[^P][ST][^P])", seq)
    idxs = [str(match.start() + 1) for match in mo]

    if idxs:
        ans.append(protein)
        ans.append(" ".join(idxs))

with open("answer.txt", "w") as outfile:
    for x in ans:
        outfile.write(x + "\n")

print("Done.")
