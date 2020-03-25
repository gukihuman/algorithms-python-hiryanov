#!/usr/bin/python3

from pyrob.api import *


@task
def task_1_1():
    """
    Task 01: reach the end point.
    """

    # Moves right by 2 cells.
    move_right(2)

    # Moves down by 1 cell.
    move_down()

if __name__ == '__main__':
    run_tasks()