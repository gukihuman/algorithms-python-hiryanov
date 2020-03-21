import lecture_12_task_B_energy_game as task_B

print('\n', 'Testing the tasks of Lecture 12:', '\n', sep='')


print('Task B. Energy Game:')
print('Test 1: ', end='')
platforms = [1]
result = 0
print('OK' if task_B.energy_game(platforms) == result else 'Fail', end='   ')

print('Test 2: ', end='')
platforms = [1, 2]
result = 1
print('OK' if task_B.energy_game(platforms) == result else 'Fail', end='   ')

print('Test 3: ', end='')
platforms = [1, 5, 10]
result = 9
print('OK' if task_B.energy_game(platforms, 3) == result else 'Fail', end='   ')

print('Test 4: ', end='')
platforms = [7, 4, 18, 34, 3, 46, 49, 34, 10, 5, 11]
result = 114
print('OK' if task_B.energy_game(platforms) == result else 'Fail', end='   ')

print('Test 5: ', end='')
platforms = [5, 22, 10]
result = 15
print('OK' if task_B.energy_game(platforms) == result else 'Fail')
print('')