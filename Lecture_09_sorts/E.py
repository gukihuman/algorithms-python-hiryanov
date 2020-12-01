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

input_string = str(input())
print(parenthesis(input_string))