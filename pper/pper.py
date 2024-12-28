import math
import os
from pathlib import Path


os.chdir(Path(__file__).parent)


def pper(n, k):
    return math.factorial(n) // math.factorial(n - k) % 1000000


print(pper(21, 7))  # test
print(pper(90, 10))
