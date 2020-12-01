def dot_product(N, v1, v2):
    """Return the dot product of two vectors in N sizes."""
    amount = 0
    for i in range(N):
        amount += v1[i] * v2[i]
    return amount

def test_1(func):
    print('Test 1: ', end='')
    print('OK' if func(3, [1, 2, 3], [1, 2, 3]) == 14 else 'Fail')

def test_2(func):
    print('Test 2: ', end='')
    print('OK' if func(3, [1, 2, 3], [4, 5, 6]) == 32 else 'Fail')

test_1(dot_product)
test_2(dot_product)