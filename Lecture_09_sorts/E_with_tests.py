def parenthesis(input_string):
    """Checking the structure of parenthesis."""
    if len(input_string) == 0:
        return 'NO'
    if input_string[0] == ')':
        return 'NO'
    n = 0
    for i in input_string:
        if n < 0:
            return 'NO'
        if i == '(':
            n += 1
        else:
            n -= 1
    return 'YES' if n == 0 else 'NO'

def test_1(func):
    print('Test 1: ', end='')
    print('OK' if func(')(') == 'NO' else 'Fail')

def test_2(func):
    print('Test 2: ', end='')
    print('OK' if func('(()()(()()') == 'NO' else 'Fail')

def test_3(func):
    print('Test 3: ', end='')
    print('OK' if func('(()(())()())') == 'YES' else 'Fail')

def test_4(func):
    print('Test 4: ', end='')
    print('OK' if func('') == 'NO' else 'Fail')

test_1(parenthesis)
test_2(parenthesis)
test_3(parenthesis)
test_4(parenthesis)