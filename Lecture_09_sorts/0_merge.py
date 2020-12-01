def merge(A:list, B:list):
    """Merging two lists in one"""
    C = [0] * (len(A) + len(B))
    i = k = n = 0
    while i < len(A) and k < len(B):
        if A[i] <= B[k]:
            C[n] = A[i]
            i += 1
        else: # A[i] > B[k]
            C[n] = B[k]
            k += 1
        n += 1
    while i < len(A):
        C[n] = A[i]
        i += 1
        n += 1
    while k < len(B):
        C[n] = B[k]
        k += 1
        n += 1
    return C

def merge_sort(A):
    if len(A) <= 1:
        return
    middle = len(A)//2
    L = [A[i] for i in range(middle)]
    R = [A[i] for i in range(middle, len(A))]
    merge_sort(L)
    merge_sort(R)
    C = merge(L, R)
    for i in range(len(A)):
        A[i] = C[i]

def test_1(merge):
    print('Test 1: ', end='')
    print('OK' if merge([1,2,3],[4,5,6]) == [1,2,3,4,5,6] else 'Fail')

def test_2(merge):
    print('Test 2: ', end='')
    print('OK' if merge([1,6,7],[1,4,5]) == [1,1,4,5,6,7] else 'Fail')

test_1(merge)
test_2(merge)
