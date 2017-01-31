fib_table = {1:1, 2:1}
def fib(n):
    if n <= 2:
        return 1
    if n in fib_table:
        return fib_table[n]
    else:
        fib_table[n] = fib(n-1) + fib(n-2)
        print fib_table
        return fib_table[n]


print fib(15)