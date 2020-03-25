#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_3():
    """
    Task 04: There is three sides of the wall around the first cell.
    Get off through the free side. The exit position is not known.
    """

    # Moves up if there is no wall above.
    if not wall_is_above():
        move_up()

    # Moves down if there is no wall beneath.
    elif not wall_is_beneath():
        move_down()

    # Moves right if there is no wall on the right.
    elif not wall_is_on_the_right():
        move_right()

    # Moves left if there is no wall on the left.
    elif not wall_is_on_the_left():
        move_left()

if __name__ == '__main__':
    run_tasks()