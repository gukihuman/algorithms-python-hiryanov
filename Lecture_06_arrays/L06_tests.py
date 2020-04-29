from L06_task_A_circle_affiliation import circle_affiliation
from L06_task_B_bank_deposit import bank_deposit

print('\n', 'Testing the tasks of Lecture 06:', '\n', sep='')


print('Task A. Circle affiliation:')
print('Test 1: ', end='')
coord_x, coord_y, radius = 0, 0, 1
result = 'YES'
print('OK' if circle_affiliation(coord_x, coord_y, radius) == result
      else 'Fail', end='    ')

print('Test 1: ', end='')
coord_x, coord_y, radius = -1, 3, 1
result = 'NO'
print('OK' if circle_affiliation(coord_x, coord_y, radius) == result
      else 'Fail', end='    ')

print('Test 1: ', end='')
coord_x, coord_y, radius = -4, 4, 5
result = 'NO'
print('OK' if circle_affiliation(coord_x, coord_y, radius) == result
      else 'Fail')
print('')


print('Task B. Bank deposit:')
print('Test 1: ', end='')
deposit, percent, target = 1, 1, 2
result = 100
print('OK' if bank_deposit(deposit, percent, target) == result
      else 'Fail', end='    ')

print('Test 2: ', end='')
deposit, percent, target = 100, 10, 200
result = 8
print('OK' if bank_deposit(deposit, percent, target) == result
      else 'Fail', end='    ')

print('Test 3: ', end='')
deposit, percent, target = 1000, 10, 1000000
result = 73
print('OK' if bank_deposit(deposit, percent, target) == result
      else 'Fail')
print('')


print('There is no tests for the answers of tasks: C.')
print('Only contest online-test.')
print('')
