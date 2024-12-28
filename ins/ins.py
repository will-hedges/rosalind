def insertionSort(file):
    f = open(file)
    n = int(f.readline())
    arr = [int(i) for i in f.readline().split(" ")]
    f.close()

    swaps = 0
    while arr != sorted(arr):
        for i, v in enumerate(arr):
            try:
                if arr[i] > arr[i + 1]:
                    m = arr.pop(i)
                    arr.insert(i + 1, m)
                    swaps += 1
            except IndexError:
                pass

    return swaps


print(insertionSort("rosalind_ins.txt"))
