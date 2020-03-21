import lecture_01_task_01 as task_01

def test_lecture_01_task_01():
    print('Task 01:')

    print('Test 1: ', end='')
    a, b = 179, 197
    result = 266.1766330841233
    print('OK' if task_01.hypotenuse(a, b) == result else 'Fail')

test_lecture_01_task_01()