def lis(A):
    F = [0] * (len(A))
    for i in range(1, len(A)):
        m = 0
        for j in range(0, i):
            if A[i] > A[j] and F[j] > m:
                m = F[j]
        F[i] = m + 1
    return F[-1]

A = [4, 2, 1, 7, 9]

print(lis(A))