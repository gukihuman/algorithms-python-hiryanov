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

A = get_list_for_H()
sort_from_units(A)
for i in range(len(A)):
    A[i] = str(A[i])
print(' '.join(A))