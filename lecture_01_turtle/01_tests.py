import lecture_01_task_01_hypotenuse as task_01

print('\n', 'Testing the tasks of Lecture 01:', '\n', sep='')


print('Task 01. Hypotenuse:')
print('Test 1: ', end='')
a, b = 179, 197
result = 266.1766330841233
print('OK' if task_01.hypotenuse(a, b) == result else 'Fail')
print('')