# see saradoesbioinformatics blogspot

import math

import pyperclip


def binomial(idx, successes, populationTotal):
    p = (
        math.factorial(P)
        / (math.factorial(i) * math.factorial(P - i))
        * (0.25 ** i)
        * (0.75 ** (P - i))
    )
    return p


f = open("rosalind_lia.txt")
k, N = map(int, f.readline().split(" "))
f.close()

P = 2 ** k  # population total

ans = "{:.3f}".format(
    sum([binomial(i, N, P) for i in range(N, P + 1)])
)  # need to round off to 3 dec

pyperclip.copy(ans)
print(f"{ans} copied to clipboard")
