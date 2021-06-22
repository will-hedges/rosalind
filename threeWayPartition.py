import pyperclip

# should only scan once
def threeWayPartition(arr):
    q = arr.pop(0)
    B = [q]

    while arr:
        x = arr.pop(0)
        if x < q:
            B.insert(0, x)
        elif x == q: # implies r
            B.insert(B.index(q), x)
        else:
            B += [x]

    return B


f = open('rosalind_par3.txt')
n = f.readline()
A = [int(i) for i in f.readline().split(' ')]
f.close()

B = threeWayPartition(A)

### copy
B = ' '.join([str(i) for i in B])
pyperclip.copy(B)
print('B copied to clipboard')