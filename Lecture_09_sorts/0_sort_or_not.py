def check_sorted(A, ascending = True):
    """Checking the list if it's sorted or not. O(n)"""
    flag = True
    s = 2 * int(ascending) - 1
    for i in range(0, len(A) - 1):
        if s * A[i] > s * A[i + 1]:
            flag = False
            break
    return flag

def test_1(check_sorted):
    print('Test 1: ', end='')
    print('OK' if check_sorted([1, 5, 2, 4]) == False else 'Fail')

def test_2(check_sorted):
    print('Test 2: ', end='')
    print('OK' if check_sorted([6, 5, 2, 5], False) == False else 'Fail')

def test_3(check_sorted):
    print('Test 3: ', end='')
    print('OK' if check_sorted([6, 5, 2, 1], False) == True else 'Fail')

test_1(check_sorted)
test_2(check_sorted)
test_3(check_sorted)