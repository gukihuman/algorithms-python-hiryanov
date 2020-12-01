def reverse_word(A):
    """Takes a list of words <= 15 symbols. Returns a list where
    each item contains three subitems. First item is the same as in
    input list. Second is a reversed word from the first. Third is
    the length of the word."""
    for i in range(len(A)):
        A[i] = [A[i], A[i][::-1], len(A[i])]

def comp_sort(A):
    """Takes a list where each item contains three subitems.
    Sorting the list by third item at first. Then by second."""
    A.sort(key=lambda x: (x[2], x[1]))

### Testing

def test_reverse_word(func):
    print('Test reverse_word: ', end='')
    A = ['eucharis', 'fittonia', 'tagetes']
    A_out = [['eucharis', 'sirahcue', 8],
             ['fittonia', 'ainottif', 8],
             ['tagetes', 'setegat', 7]]
    func(A)
    passed = A == A_out
    print('OK' if passed else 'Fail')

def test_comp_sort(func):
    print('Test comp_sort: ', end='')
    A = [['eucharis', 'sirahcue', 8],
         ['fittonia', 'ainottif', 8],
         ['tagetes', 'setegat', 7]]
    A_out = [['tagetes', 'setegat', 7],
             ['fittonia', 'ainottif', 8],
             ['eucharis', 'sirahcue', 8]]
    func(A)
    passed = A == A_out
    print('OK' if passed else 'Fail')

test_reverse_word(reverse_word)
test_comp_sort(comp_sort)