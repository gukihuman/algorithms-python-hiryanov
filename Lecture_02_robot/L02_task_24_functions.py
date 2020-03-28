#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_1():
    """
    Task 24: Draw a cross. Starting position is one cell above and left.
    """

    # It is not necessary to use a function in this task. But it will be
    # used in the next 2 tasks, so it's created in advance. Though it's
    # possible to save a few moves here without the function, it will be
    # effective in the future.
    def cross_top_left():
        """
        Draws a cross by two crossing lines, 3 cell each.
        Starts from the top left.
        """

        move_down()
        fill_cell()
        move_down()
        move_right()
        for i in range(2):
            fill_cell()
            move_up()
        fill_cell()
        move_right()
        move_down()
        fill_cell()
        move_down()

    # Moves to the starting position.
    move_right()
    move_down()

    # Moves as the cross.
    cross_top_left()

    # Moves to the end position.
    move_left(2)
    move_up(2)

if __name__ == '__main__':
    run_tasks()