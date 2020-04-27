from L06_task_A_circle_affiliation import circle_affiliation

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
coord_x, coord_y, radius = 4, 4, 5
result = 'NO'
print('OK' if circle_affiliation(coord_x, coord_y, radius) == result
      else 'Fail')
print('')
