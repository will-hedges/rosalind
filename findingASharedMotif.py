import re


motif_re = re.compile(r'([ATGC]{2,}){2,}')


def sharedMotif(file):
    f = open(file)
    lines = ' '.join([line.strip() for line in f.readlines() if '>' not in line])
    f.close()

    mo = motif_re.findall(lines)
    
    return mo


print(sharedMotif('sharedMotif.txt')) # AC