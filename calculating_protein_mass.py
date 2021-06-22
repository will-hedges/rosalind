#! python3
# calculating_p_mass.py - http://rosalind.info/problems/prtm/
import os
from pathlib import Path
os.chdir(Path(__file__).parent)


with open('monoisotopic_mass_table.txt', 'r') as ref_file:
    mass_dic = {}
    for line in ref_file.readlines():
        line = line.strip().split('   ')
        aa = line[0]
        mass = float(line[1])
        mass_dic[aa] = mass

with open('rosalind_prtm.txt', 'r') as datafile:
    p_str = datafile.readline().strip()

p_mass = sum([mass_dic[aa] for aa in p_str])

print(round(p_mass, 3))

# my answer was 96514.153
