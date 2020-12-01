def convert(A):
    """Deletes symbols in a list after dot including dot"""
    B = []
    for i in A:
        if i == '.':
            break
        B.append(i)
    C = ''.join(B)
    return C

def sort(A, least=True):
    """Sorting the list"""
    result = list(A)
    result.sort()
    result = ''.join(result)
    result += '.'
    return result

A = str(input())
A = convert(A)
A = sort(A)
print(A)