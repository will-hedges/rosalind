def mergeArrays(file):
    f = open(file)
    lines = [line.strip().split(" ") for line in f.readlines()]
    lines = [line for line in lines if len(line) > 1]
    f.close()

    a = [int(i) for i in lines[0]]
    b = [int(i) for i in lines[1]]

    return " ".join([str(i) for i in sorted(a + b)])
    # so this will give you the correct answer
    #   but the idea is you 'sort as you go' (i.e. 'linear time')
    #       meaning running sorted() is 'inefficient' although more eloquent


# looking at the top answer, the intent is really to 'fill' the list as you go
def mergeArrays(a, b):
    c = []
    # keep removing and adding smallest 0th element to c until either input list is []
    while a and b:
        if a[0] < b[0]:
            c += [a.pop(0)]
        else:
            c += [b.pop(0)]
    # then, add the leftovers
    c += a + b

    return c


# probably better to do my file handling outside of the function as well
f = open("rosalind_mer.txt")
lines = [line.strip().split(" ") for line in f.readlines()]
lines = [line for line in lines if len(line) > 1]
f.close()

a = [int(i) for i in lines[0]]
b = [int(i) for i in lines[1]]

c = mergeArrays(a, b)  # format answer etc.
