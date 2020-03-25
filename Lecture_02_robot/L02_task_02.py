#!/usr/bin/python3

from pyrob.api import *


@task
def task_1_2():
    """
    Task 02: Reach the end point, paint over one cell.
    """

    # Moves to the cell you need to fill.
    move_down(2)
    move_right(2)

    # Fills the cell and moves to the end cell.
    fill_cell()
    move_down()
    move_right(2)

if __name__ == '__main__':
    run_tasks()