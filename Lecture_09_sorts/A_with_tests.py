def get_num(A):
    """Getting the two numbers from a string with space in the middle."""
    n1 = str()
    n2 = str()
    for i in range(len(A)):
        if A[i] != ' ':
            n1 += A[i]
        else:
            break
    n2 += A[len(n1)+1:]
    return n1, n2

def xor(n1, n2):
    """Finding the XOR from two numbers. Input and output is hexadecimal"""
    x = int(n1, 16)
    y = int(n2, 16)
    c = x ^ y
    c = hex(c)
    c = c[2:]
    return c

def test_xor_1(xor):
    print('Test xor 1: ', end='')
    print('OK' if xor('f0', '0f') == 'ff' else 'Fail')

def test_xor_2(xor):
    print('Test xor 2: ', end='')
    print('OK' if xor('1', '23') == '22' else 'Fail')

def test_get_num(xor):
    print('Test get_num: ', end='')
    print('OK' if get_num('1 23') == ('1', '23') else 'Fail')

test_xor_1(xor)
test_xor_2(xor)
test_get_num(xor)