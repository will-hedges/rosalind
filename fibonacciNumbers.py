def fibonacciNumber(file):
    f = open(file)
    n = int(f.readline())
    f.close()

    fib = [0, 1]
    for i in range(1, n):
        fib.append(sum(fib[-2:]))

    return fib[-1]


print(fibonacciNumber('rosalind_fibo.txt'))