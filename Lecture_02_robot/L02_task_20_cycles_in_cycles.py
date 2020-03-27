#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
	"""
	Task 20: Fill the rectangle with the size of 27 cells length
	and 12 cells width.
	"""

	# Moves to the starting position.
	move_right()

	# Moves right and then back. Fills the cells all the time.
	for i in range(6):

		# Moves to the right filling cells.
		for k in range(26):
			fill_cell()
			move_right()

		# Fills the last cell and moves down.
		fill_cell()
		move_down()

		# Moves to the left filling cells.
		for k in range(26):
			fill_cell()
			move_left()

		# Fills the last cell and moves down.
		fill_cell()
		move_down()

if __name__ == '__main__':
	run_tasks()
