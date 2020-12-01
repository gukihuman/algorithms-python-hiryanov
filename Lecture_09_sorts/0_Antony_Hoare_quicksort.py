def hoare_sort(A):
    if len(A) <= 1:
        return
    barrier = A[0]
    L = []
    M = []
    R = []
    for x in A:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else: # x > barrier
            R.append(x)
    hoare_sort(L)
    hoare_sort(R)
    k = 0
    for x in L + M + R:
        A[k] = x
        k += 1

def test(hoare_sort):
    print('Test: ', end='')
    A = [1, 4, 6, 2, 5, 2]
    B = [1, 2, 2, 4, 5, 6]
    hoare_sort(A)
    print('OK' if A == B else 'Fail')

test(hoare_sort)