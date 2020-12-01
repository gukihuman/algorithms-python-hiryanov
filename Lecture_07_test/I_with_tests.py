def get_greatest():
    """Return the greatest number in a list from input. The list doesn't include
    last 5 numbers and also 0 which is the sign of the end of the list"""
    temp_list = [0] * 7
    index_list = [0] * 7
    new = None
    n = 0
    i = 0
    while new != 0:
        new = int(input())
        if n < new:
            n = new
            temp_list.pop(0)
            temp_list.append(n)
            index_list.pop(0)
            index_list.append(i)
        i += 1
    my_iter = i - 6
    final_list = []
    for i in range(len(index_list)):
        if index_list[i] < my_iter:
            final_list.append(temp_list[i])
    n = 0
    for i in range(len(final_list)):
        if n < final_list[i]:
            n = final_list[i]
    return n


def test_1(func):
    print('Test get_list 1:\nEnter 1, 2, 3, 4, 5, 6, 7, 8, 9, 6, 11, 12, 8, 1, 0:')
    print('OK' if func() == 9 else 'Fail')

test_1(get_greatest)
