def get_list(input_string):
    """Removes spaces from input string with numbers."""
    A_list = []
    temp_str = ''
    for i in range(len(input_string)):
        if input_string[i] != ' ':
            temp_str += (input_string[i])
        else:
            A_list.append(int(temp_str))
            temp_str = ''
    A_list.append(int(temp_str))
    A_list[0] = str(A_list[0])
    A_list[1] = str(A_list[1])
    A_list = tuple(A_list)
    return A_list

def find(n:str, A:str):
    """Returns how many times number n in str A"""
    count = 0
    for i in A:
        if i == n:
            count += 1
    return count

def test_find(func):
    print('Test: ', end='')
    print('OK' if func('2', '2256') == 2 else 'Fail')

def test_get_list(func):
    print('Test get_list: ', end='')
    input_string = '2 2256'
    print('OK' if func(input_string) == ('2', '2256') else 'Fail')

test_get_list(get_list)
test_find(find)