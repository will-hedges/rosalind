def expectedOffspring(file):
    f = open(file)
    nums = [int(i) for i in f.readline().split(' ')]
    f.close()

    p = [1, 1, 1, 0.75, 0.5, 0]
    dom = 0
    for n in nums:
        dom += (n * 2 * p.pop(0))

    return dom

print(expectedOffspring('rosalind_iev.txt'))
