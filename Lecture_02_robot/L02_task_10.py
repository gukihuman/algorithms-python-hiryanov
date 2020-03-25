#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_3():
	"""
	Task 10: Go to the wall on the right. The distance to the wall is
	not known. Paint over the cells if a wall is above or beneath.
	"""

	# Moves right while there is no wall on the right.
	while not wall_is_on_the_right():

		# Fill the cell if there is a wall above or beneath.
		if wall_is_above() or wall_is_beneath():
			fill_cell()

		move_right()

	# Fills the last cell if there is a wall above or beneath.
	if wall_is_above() or wall_is_beneath():
		fill_cell()

if __name__ == '__main__':
	run_tasks()