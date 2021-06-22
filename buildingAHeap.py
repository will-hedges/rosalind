# SEE https://www.geeksforgeeks.org/building-heap-from-array/

import pyperclip

def heapify(arr, n, i):
    # will 'heapify' a subtree with root at node i, which is
    #   an index in an array arr. n is the size of the heap
    largest = i # initialize largest as root
    l = 2*i + 1 # left child
    r = 2*i + 2 # right child
    # if left child is larger than the root
    if l < n and arr[l] > arr[largest]:
        largest = l
    # if right child is larger than the root
    if r < n and arr[r] > arr[largest]:
        largest = r
    # if largest is not the root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # recursively heapify the affected subtree
        heapify(arr, n, largest)


def buildMaxHeap(arr, n):
    # Function to build a Max-Heap from the given array
    startIdx = n//2 - 1
    # go backwards by level from from last non-leaf node
    # and heapify each node
    for i in range(startIdx, -1, -1):
        heapify(arr, n, i)

    return arr


f = open('rosalind_hea.txt')
n = int(f.readline())
array = [int(i) for i in f.readline().split(' ')]
f.close()

ans = buildMaxHeap(array, n)
pyperclip.copy(' '.join([str(i) for i in ans]))
print('answer copied to clipboard')