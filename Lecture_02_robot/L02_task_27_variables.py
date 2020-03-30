#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
	"""
	Task 27: Move right and fill cells with increasing interval.
	The interval starts from 0 and gets bigger by 1 each cell that
	needs to be filled. Stop in the last right cell near the right wall.
	The distance to the wall is not known. There is no need to fill
	the last cell in any case.
	"""

	# Sets the steps between the cells to be filled.
	# Steps are greater then interval by 1.
	# 1 step is for 0 interval.
	steps = 1

	# Moves to the starting position.
	move_right()

	# While there is no wall on the right, fills the cell
	# and starts moving to the right.
	while not wall_is_on_the_right():
		fill_cell()

		# Moves to the right by the amount of steps.
		# Checks the wall on the right each move.
		for i in range(steps):
			move_right()

			# If there is a wall on the right, breaks the cycle.
			if wall_is_on_the_right():
				break

		# Increases the steps for the next moving.
		steps += 1

if __name__ == '__main__':
	run_tasks()