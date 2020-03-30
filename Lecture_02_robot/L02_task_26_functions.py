#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():
	"""
	Task 26: Draw 5 lines of 10 crosses in horizontal line each.
	There is one cell between crosses and lines also.
	"""

	# Using the 4 different function of crosses in this task gives
	# the effective speed of the whole movement. Though the task could be
	# solved a little bit faster, the code would be mach harder to read.
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

	def cross_top_right():
		"""
		Draws a cross by two crossing lines, 3 cell each.
		Starts from the top right.
		"""

		move_down()
		fill_cell()
		move_down()
		move_left()
		for i in range(2):
			fill_cell()
			move_up()
		fill_cell()
		move_left()
		move_down()
		fill_cell()
		move_down()

	def cross_bottom_right():
		"""
		Draws a cross by two crossing lines, 3 cell each.
		Starts from the bottom right.
		"""

		move_up()
		fill_cell()
		move_up()
		move_left()
		for i in range(2):
			fill_cell()
			move_down()
		fill_cell()
		move_left()
		move_up()
		fill_cell()
		move_up()

	# Draws 2 couple of lines by the optimized way.
	for i in range(2):

		# Draws a line of 8 crosses to the right.
		for k in range(4):
			cross_top_left()
			move_right(2)
			cross_bottom_left()
			move_right(2)

		# Draws the last 2 crosses without moving to the right at the end.
		cross_top_left()
		move_right(2)
		cross_bottom_left()

		# Moves to the position of moving to the left.
		move_down(4)

		# Draws a line of 8 crosses to the left.
		for k in range(4):
			cross_top_right()
			move_left(2)
			cross_bottom_right()
			move_left(2)

		# Draws the last 2 crosses without moving to the left at the end.
		cross_top_right()
		move_left(2)
		cross_bottom_right()

		# Moves to the position of the next moving to the right.
		move_down(4)

	# Draws the last line of 8 crosses to the right.
	for k in range(4):
		cross_top_left()
		move_right(2)
		cross_bottom_left()
		move_right(2)

	# Draws the last 2 crosses without moving to the right at the end.
	cross_top_left()
	move_right(2)
	cross_bottom_left()

	# Moves to the end position.
	move_left(38)

if __name__ == '__main__':
	run_tasks()