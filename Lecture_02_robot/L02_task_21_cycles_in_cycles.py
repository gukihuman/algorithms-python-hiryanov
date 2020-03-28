#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
	"""
	Task 21: Fill the triangle with the legs of 13 cells length each.
	"""

	# Moves to the starting position.
	move_down()
	move_right()

	# Sets the steps for the first line. The length here is 2.
	steps = 1

	# Moves right and then back 6 times. The length is getting
	# bigger each time. Fills the cells all the time, except
	# the last cell on going to the right.
	for i in range(6):

		# Moves right filling cells. Uses steps variable for
		# the amount of iterations.
		for k in range(steps):
			fill_cell()
			move_right()

		# Moves down not filling the last cell.
		move_down()

		# Moves left filling cells. Uses steps variable for
		# the amount of iterations.
		for k in range(steps):
			fill_cell()
			move_left()

		# Moves down filling the last cell.
		fill_cell()
		move_down()

		# Sets the steps for the next iteration.
		steps += 2

	# Moves right filling the last line of the cells.
	for i in range(12):
		fill_cell()
		move_right()

	# Moves down filling the last cell.
	fill_cell()
	move_down()

	# Moves to the end position.
	move_left(12)

if __name__ == '__main__':
	run_tasks()