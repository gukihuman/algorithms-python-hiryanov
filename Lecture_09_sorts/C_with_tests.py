def change(n):
    """Change 1 to 0 and 0 to 1."""
    if n == 0:
        n = 1
        return n
    n = 0
    return n

def get_list(input_string):
    """Removes spaces from input string with numbers."""
    A_list = []
    for i in range(len(input_string)):
        if input_string[i] != ' ':
            A_list.append(int(input_string[i]))
    return A_list

def how_many_knights(my_list):
    """Returns the amount of knights on an island."""
    A = [0]
    B = [1]
    for i in range(len(my_list)-1):
        if my_list[i] == 0:
            A.append(change(A[i]))
            B.append(change(B[i]))
            continue
        A.append(A[i])
        B.append(B[i])
    A_sum = B_sum = 0
    for i in range(len(A)):
        A_sum += A[i]
        B_sum += B[i]
    return A_sum if A_sum < B_sum else B_sum




def test_change(func):
    print('Test change: ', end='')
    print('OK' if func(1) == 0 else 'Fail')

def test_get_list(func):
    print('Test get_list: ', end='')
    input_string = '0 1 0 1'
    print('OK' if func(input_string) == [0, 1, 0, 1] else 'Fail')

def test_how_many_knights_1(func):
    print('Test how_many_knights 1: ', end='')
    my_list = [0, 1, 0, 1]
    print('OK' if func(my_list) == 2 else 'Fail')

def test_how_many_knights_2(func):
    print('Test how_many_knights 2: ', end='')
    my_list = [0, 1, 1, 0, 0, 0, 1, 0, 0]
    print('OK' if func(my_list) == 4 else 'Fail')

test_change(change)
test_get_list(get_list)
test_how_many_knights_1(how_many_knights)
test_how_many_knights_2(how_many_knights)