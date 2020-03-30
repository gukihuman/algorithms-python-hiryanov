#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
	"""
	Task 28: There is the filled cells on the right side with random interval
	between them. Move right and stop in the 3th filled cell in a row.
	If there is no 3 filled cells in a row, stop near the right wall.
	"""

	# Sets the amount of the filled cells.
	filled_cell = 0

	# Moves right while there is no wall on the right or the amount of
	# filled cells doesn't equal 3.
	while not wall_is_on_the_right() and filled_cell != 3:
		move_right()

		# Checks the standing cell. If it's filled, counts it.
		# If it's not filled, zeroing it.
		if cell_is_filled():
			filled_cell += 1

		else:  # not cell_is_filled()
			filled_cell = 0

if __name__ == '__main__':
	run_tasks()