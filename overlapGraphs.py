import re

id_re = re.compile(r'(>Rosalind_\d{4})([ATGC]+)')


def digraph(file, k):
    f = open(file)
    lines = ''.join(f.readlines()).replace('\n', '')
    f.close()
    lines = re.findall(id_re, lines)
    ids = [line[0][1:] for line in lines]
    strings = [line[1] for line in lines]

    prefixes = [string[:k] for string in strings]

    for index, string in enumerate(strings):
        id = ids[index]
        suffix = string[-k:]
        matches = [index for index, prefix in enumerate(prefixes) if prefix == suffix]
        for m in matches:
            if id != ids[m]:
                print(f'{id} {ids[m]}')


digraph('rosalind_grph.txt', 3)
