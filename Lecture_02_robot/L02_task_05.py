#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_2():
    """
    Task 05: Reach the end of the wall. The distance is not known.
    """

    # Moves right while a wall is beneath.
    while wall_is_beneath():
        move_right()

if __name__ == '__main__':
    run_tasks()