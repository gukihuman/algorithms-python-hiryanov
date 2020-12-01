import operator

def sort_by_two_elements(A):
    """Sorting a list where each element is a list with two parts.
    Main list is sorting by second part and then by first
    if second is the same."""
    A.sort(key=lambda x: (x[1], -x[0]))

def test_sort_by_two_elements(func):
    print('Test sort_by_two_elements: ', end='')
    A = [[1.8, 70], [1.75, 70], [1.8, 69.5]]
    A_sorted = [[1.8, 69.5], [1.80, 70], [1.75, 70]]
    func(A)
    passed = A == A_sorted
    print('OK' if passed else 'Fail')

test_sort_by_two_elements(sort_by_two_elements)