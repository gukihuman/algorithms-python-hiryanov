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

def test_convert(func):
    print('Test convert: ', end='')
    input_line = 'qwe Rty5, yu! Mama.5hg'
    output_line = 'qwe Rty5, yu! Mama'
    print('OK' if func(input_line) == output_line else 'Fail')

def test_sort(func):
    print('Test sort: ', end='')
    input_line = 'qwe Rty5, yu! Mama'
    output_line = '   !,5MRaaemqtuwyy.'
    print('OK' if func(input_line) == output_line else 'Fail')

test_convert(convert)
test_sort(sort)