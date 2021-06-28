#! python3
# sign.py - http://rosalind.info/problems/sign/


import itertools


def sign(n):
    lst = []
    for i in range(1, n + 1):
        lst.append(i)
        lst.append(-i)

    # take a look at output
    #   getting repeat numbers
    #       i.e. for n = 4 --> -1, 1, 2, 3
    perms = [perm for perm in itertools.permutations(lst, n)]
    for perm in perms:
        if len(set([abs(x) for x in perm])) < n:
            perms.remove(perm)

    return perms


def main():
    with open('rosalind_sign.txt') as infile:
        n = int(infile.readline())

    ans = sign(n)

    with open('sign_ans.txt', 'w') as outfile:
        outfile.write(str(len(ans)) + '\n')
        for perm in ans:
            perm = map(str, perm)
            outfile.write(f'{" ".join(perm)}\n')


if __name__ == '__main__':
    main()
