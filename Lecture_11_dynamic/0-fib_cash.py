n = 9
F = [None] * (n + 1)

def fib(n):
    if n <= 1:
        return n
    if not F[n]:
        F[n] = fib(n - 1) + fib(n - 2)
    return F[n]

print(fib(n)) #34