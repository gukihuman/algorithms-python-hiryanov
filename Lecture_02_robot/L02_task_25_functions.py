#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():
	"""
	Task 25: Draw a 5 crosses in horizontal line with one cell between them.
	Starting position is one cell above the first cross.
	"""

	# Using the 2 different function of crosses in this task gives
	# the effective speed of the whole movement.
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

	def cross_bottom_left():
		"""
		Draws a cross by two crossing lines, 3 cell each.
		Starts from the bottom left.
		"""

		move_up()
		fill_cell()
		move_up()
		move_right()
		for i in range(2):
			fill_cell()
			move_down()
		fill_cell()
		move_right()
		move_up()
		fill_cell()
		move_up()

	# Moves to the starting position.
	move_down()

	# Draws 4 crosses by the optimized way.
	for i in range(2):
		cross_top_left()
		move_right(2)
		cross_bottom_left()
		move_right(2)

	# Draws the last 5th cross.
	cross_top_left()

	# Moves to the end position.
	move_left(2)
	move_up(2)

if __name__ == '__main__':
	run_tasks()