def find(A):
    """Returns how many times number n in str A. First symbol is n, then space,
    then list."""
    count = 0
    n = A[0]
    for i in A[2:]:
        if i == n:
            count += 1
    return count

print(find(str(input())))