#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
	"""
	Task 22: Fill the whole field. Starting position is the top left corner.
	The size of the field is not known. Stop at the bottom left corner.
	"""

	def opposite_move():
		"""
		Moves left if wall is on the left or right if wall is on the right.
		Fills the cells all the time.
		"""

		# Checks the left cell. If there is a wall, the position is near to
		# the left side of the field. In this case, moves to the right side.
		# If there is no wall on the left, the position is near to the right
		# side of the field. In this case, moves to the left side.
		if wall_is_on_the_left():

			# Moves right while there is no wall on the right. Fills the cells.
			while not wall_is_on_the_right():
				fill_cell()
				move_right()

		else:  # not wall_is_on_the_left()

			# Moves left while there is no wall on the left. Fills the cells.
			while not wall_is_on_the_left():
				fill_cell()
				move_left()

	# Moves to the opposite side of the field while there is no wall beneath.
	# Then moves down. Fills the cells all the time.
	while not wall_is_beneath():
		opposite_move()

		# Moves down filling the last cell.
		fill_cell()
		move_down()

	# After the previous cycle, the position is in the cell, where is
	# a wall beneath. Moves to the opposite side for the last time.
	opposite_move()

	# Fill the last cell.
	fill_cell()

	# Check the position. If it is the bottom left corner, stays here.
	# Else moves to the bottom right corner.
	if wall_is_on_the_right():

		# Moves left while there is no wall on the left.
		while not wall_is_on_the_left():
			move_left()

if __name__ == '__main__':
	run_tasks()
