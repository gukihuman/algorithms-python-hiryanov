from L03_task_A_digits_sum import digits_sum
from L03_task_B_queens_move import queens_move

print('\n', 'Testing the tasks of Lecture 03:', '\n', sep='')


print('Task A. Digits sum:')
print('Test 1: ', end='')
number = 123
result = 6
print('OK' if digits_sum(number) == result else 'Fail', end='    ')

print('Test 2: ', end='')
number = 768
result = 21
print('OK' if digits_sum(number) == result else 'Fail', end='    ')

print('Test 3: ', end='')
number = 179
result = 17
print('OK' if digits_sum(number) == result else 'Fail')
print('')


print('Task B. Queens move:')
print('Test 1: ', end='')
coordinates = [1, 1, 8, 8]
result = 'YES'
print('OK' if queens_move(*coordinates) == result else 'Fail', end='    ')

print('Test 2: ', end='')
coordinates = [4, 5, 7, 2]
result = 'YES'
print('OK' if queens_move(*coordinates) == result else 'Fail', end='    ')

print('Test 3: ', end='')
coordinates = [4, 3, 1, 1]
result = 'NO'
print('OK' if queens_move(*coordinates) == result else 'Fail')
print('')