#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_27():
    """
    Task 17: There is a filled cell above. It is not known how far.
    There is another filled cell on the left or on the right from
    the first one. Go to the second filled cell.
    """

    # Moves up while a standing cell is not filled.
    while not cell_is_filled():
        move_up()

    # Moves right for a checking at least one cell.
    # Only a standing cell can be checked.
    move_right()

    # Checks the standing cell. If it is filled, stands here.
    # If it is not, moves to the left one.
    if not cell_is_filled():
        move_left(2)

if __name__ == '__main__':
    run_tasks()