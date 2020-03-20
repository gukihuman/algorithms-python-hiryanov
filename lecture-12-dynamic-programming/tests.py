import task_B_energy_game

def test_task_B_energy_game():
    print('Task B. Energy Game: ')

    print('Test 1: ', end='')
    platforms = [1]
    print('OK' if task_B_energy_game.energy_game(platforms) is 0 else 'Fail')

    print('Test 2: ', end='')
    platforms = [1, 2]
    print('OK' if task_B_energy_game.energy_game(platforms) is 1 else 'Fail')

    print('Test 3: ', end='')
    platforms = [1, 5, 10]
    print('OK' if task_B_energy_game.energy_game(platforms, 3) is 9 else 'Fail')

    print('Test 4: ', end='')
    platforms = [7, 4, 18, 34, 3, 46, 49, 34, 10, 5, 11]
    print('OK' if task_B_energy_game.energy_game(platforms) is 114 else 'Fail')

    print('Test 5: ', end='')
    platforms = [5, 22, 10]
    print('OK' if task_B_energy_game.energy_game(platforms) is 15 else 'Fail')

test_task_B_energy_game()