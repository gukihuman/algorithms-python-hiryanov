from L03_task_A_digits_sum import digits_sum
from L03_task_B_queens_move import queens_move
from L03_task_C_leap_year import leap_year
from L03_task_D_square_sequence import square_sequence
from L03_task_E_logarithm import logarithm

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


print('Task C. Leap year:')
print('Test 1: ', end='')
year = 1
result = 'NO'
print('OK' if leap_year(year) == result else 'Fail', end='    ')

print('Test 2: ', end='')
year = 2000
result = 'YES'
print('OK' if leap_year(year) == result else 'Fail', end='    ')

print('Test 3: ', end='')
year = 1668
result = 'YES'
print('OK' if leap_year(year) == result else 'Fail')
print('')


print('Task D. Square sequence:')
print('Test 1: ', end='')
max_square = 1
result = [1]
print('OK' if square_sequence(max_square) == result else 'Fail', end='    ')

print('Test 2: ', end='')
max_square = 16
result = [1, 4, 9, 16]
print('OK' if square_sequence(max_square) == result else 'Fail', end='    ')

print('Test 3: ', end='')
max_square = 50
result = [1, 4, 9, 16, 25, 36, 49]
print('OK' if square_sequence(max_square) == result else 'Fail')
print('')


print('Task E. Logarithm:')
print('Test 1: ', end='')
number = 2
result = 1
print('OK' if logarithm(number) == result else 'Fail', end='    ')

print('Test 2: ', end='')
number = 10
result = 4
print('OK' if logarithm(number) == result else 'Fail', end='    ')

print('Test 3: ', end='')
number = 1627
result = 11
print('OK' if logarithm(number) == result else 'Fail')
print('')