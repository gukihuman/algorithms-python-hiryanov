#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_1():
    """
    Task 03: Reach the wall. The distance to the wall is not known.
    """

    # Moves right while there is no wall on the right.
    while not wall_is_on_the_right():
        move_right()

if __name__ == '__main__':
    run_tasks()