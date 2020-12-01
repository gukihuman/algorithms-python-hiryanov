def sort_from_units(A):
    """Sorting a list of numbers by units first,
    then decades and so on. Only if: number > 0, number <= 1000. """
    for i in range(len(A)):
        A[i] = str(A[i])
        A[i] = list(A[i])
        A[i].reverse()
        A[i] = ''.join(A[i])
        for k in range(4 - len(A[i])):
            A[i] += '0'
    A.sort()
    for i in range(len(A)):
        for k in range(len(A[i]) - 1, 0, -1):
            if A[i][k] == '0':
                A[i] = A[i][:-1]
            else:
                break
    for i in range(len(A)):
        A[i] = list(A[i])
        A[i].reverse()
        A[i] = ''.join(A[i])
        A[i] = int(A[i])

def get_list_for_H():
    """Getting an input number of elements on the first line of input.
    Then a string of numbers divided by space.
    Return the list of this numbers."""
    n = int(input())
    input_string = str(input())
    input_string += ' '
    A = []
    temp_str = ''
    for i in range(len(input_string)):
        if input_string[i] != ' ':
            temp_str += input_string[i]
            continue
        temp_str = int(temp_str)
        A.append(temp_str)
        temp_str = ''
    return A


def test_sort_from_units(func):
    print('Test sort_from_units: ', end='')
    A = [1, 6, 47, 32, 705, 12]
    A_sorted = [1, 12, 32, 705, 6, 47]
    func(A)
    passed = A == A_sorted
    print('OK' if passed else 'Fail')

def test_get_list_for_H(func):
    print('Test get_list_for_H:\nPlease enter:\n6\n1 6 47 32 705 12')
    passed = func() == [1, 6, 47, 32, 705, 12]
    print('OK' if passed else 'Fail')


test_sort_from_units(sort_from_units)
test_get_list_for_H(get_list_for_H)