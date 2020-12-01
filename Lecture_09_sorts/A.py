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

A = str(input())
n1, n2 = get_num(A)
print(xor(n1, n2))