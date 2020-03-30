#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
    """
    Task 28: There is the filled cells on the right side with random
    interval between them. Move right and stop in the 5th filled cell.
    """

    # Sets the amount of the filled cells.
    filled_cells = 0

    # Moves right while there is less then 5 of filled cells.
    while filled_cells < 5:
        move_right()

        # Checks the standing cell. If it's filled, counts it.
        if cell_is_filled():
            filled_cells += 1

if __name__ == '__main__':
    run_tasks()