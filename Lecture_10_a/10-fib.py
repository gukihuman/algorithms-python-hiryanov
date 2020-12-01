import util
import matplotlib
import random
import math
%matplotlib inline

def fib_cache(n, cache=None):
    """Recursive fibonacci numbers with cash. O(n)."""
    if n == 0:
        fib_list = [0]
    elif n == 1:
        fib_list = [0, 1]
    else:
        fib_list = fib_cache(n-1, True)
        fib_list.append(fib_list[-2] + fib_list[-1])
    if cache:
        return fib_list
    return fib_list[-1]

def recursive_fib(n):
    """Recursive fibonacci numbers without cash. O(n**2)."""
    if n == 0:
        return 0
    if n == 1:
        return 1
    return recursive_fib(n-1) + recursive_fib(n-2)

def fib(n):
    """Linear fibonacci numbers. O(n)."""
    fib_list = [None] * (n + 1)
    fib_list[0] = 0
    fib_list[1] = 1
    for i in range(2, n + 1):
        fib_list.append(fib_list[-2] + fib_list[-1])
    return fib_list[n]

def bubble_sort(a):
    for i in range(len(a)-1):
        for k in range(len(a)-1):
            if a[k] > a[k+1]:
                a[k], a[k+1] = a[k+1], a[k]

def quick_sort_first(a):
    if len(a) <= 1:
        return
    pivot = a[0]
    L = []
    M = []
    R = []
    for i in a:
        if i < pivot:
            L.append(i)
        elif i == pivot:
            M.append(i)
        else: # i > pivot
            R.append(i)
    quick_sort_first(L)
    quick_sort_first(R)
    k = 0
    for i in L + M + R:
        a[k] = i
        k += 1



print(fib_cache(9)) # 34
print(recursive_fib(9)) # 34
print(fib(9)) # 34

a = [5, 4, 3, 2, 1]
bubble_sort(a)
print(a) # [1, 2, 3, 4, 5]

a = [5, 4, 3, 2, 1]
quick_sort_first(a)
print(a) # [1, 2, 3, 4, 5]
