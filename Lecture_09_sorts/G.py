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
    if len(A) < 2:
        return A
    barrier = A[0]
    A_less = [i for i in A[1:] if i <= barrier]
    A_greater = [i for i in A[1:] if i > barrier]
    result = sort(A_less, False) + [barrier] + sort(A_greater, False)
    if least:
        resul = ''.join(result)
        resul += '.'
        return resul
    return result

input_str = (convert(str(input())))
print(sort(input_str))