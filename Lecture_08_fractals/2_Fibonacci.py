def fib(n):
    """Return the number in the N index from Fibonacci Sequence."""
    if n in (1, 2):
        return 1
    return fib(n - 1) + fib(n - 2)

print(fib(8))