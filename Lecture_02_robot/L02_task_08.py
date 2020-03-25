#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_7():
    """
    Task 08: Exit the corridor. There are walls above or beneath.
    """

    # Moves right while there is a wall beneath or above.
    while wall_is_beneath() or wall_is_above():
        move_right()

if __name__ == '__main__':
    run_tasks()