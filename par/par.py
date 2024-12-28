import pyperclip

# must be done in a single scan
def twoWayPartition(arr):
    q = arr.pop(0)
    B = [q]
    while arr:
        a = a.pop(0)
        if a <= q:
            B.insert(0, a)
        else:
            B += [a]

    return B


f = open("rosalind_par.txt")
n = int(f.readline().strip())
A = [int(i) for i in f.readline().split(" ")]
f.close()

B = twoWayPartition(A)


### copy answer
pyperclip.copy(" ".join([str(i) for i in B]))
print("B copied to clipboard")
