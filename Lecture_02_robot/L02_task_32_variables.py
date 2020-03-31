#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_8_18():
    """
    Task 32: There is the horizontal tunnel connected to vertical corridors
	above. The amount and the size of the corridors is not known.
	The tunnel has exit and the wall on the right just after the tunnel ends.
	Stop in this cell near the right wall. Starting position is in the
	very left cell in the tunnel. Fill the cell of the tunnel if there is no
	corridor above. Also there is already the filled cells in the corridors.
	Count this cells and save the amount in the "ax" register by the "mov"
	function. The last part is: fills the rest of the cells in the corridors.
    """

    # Introduces the amount of the already filled cells.
    amount = 0

    # Works while not have been broken by the wall on the right
    # after the tunnel ends.
    while True:

        # Moves right while there is a wall above. Fills the cell also.
        while wall_is_above():
            fill_cell()
            move_right()

        # Checks the wall on the right and breaks the whole cycle because
        # the wall means that the task is finished.
        if wall_is_on_the_right():
            break

        # If there is no wall above, moves up, counts the filled cells,
        # and fills the unfilled cells.
        while not wall_is_above():
            move_up()

            if cell_is_filled():
                amount += 1
            else:  # not cell_is_filled()
                fill_cell()

        # Moves down while there is no wall beneath. It is possible to
        # remember the size of the corridor and to use it for moving down.
        # But the code would be harder to read in this case. Let it be simple.
        while not wall_is_beneath():
            move_down()

        # Moves right after the corridor's cycles.
        move_right()

    # Saves in the "ax" register the amount of cells which were already filled.
    mov('ax', amount)

if __name__ == '__main__':
    run_tasks()