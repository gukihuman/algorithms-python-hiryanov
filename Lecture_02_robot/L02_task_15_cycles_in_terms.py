#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
	"""
	Task 15: There is a field with 10 units side. At the initial moment,
	the robot is in the corner, but it is not known which one.
	Go into the opposite corner.
	"""

	# Checks the cell above.
	if wall_is_above():

		# It is the top of the field. Checks the cell on the left.
		if wall_is_on_the_left():

			# It is the top left corner. Moves into the bottom right corner.
			for i in range(9):
				move_right()
				move_down()

		else:  # wall_is_on_the_right()

			# It is the top right corner. Moves into the bottom left corner.
			for i in range(9):
				move_left()
				move_down()

	else:  # wall_is_beneath()

		# It is the bottom of the field. Checks the cell on the left.
		if wall_is_on_the_left():

			# It is the bottom left corner. Moves into the top right corner.
			for i in range(9):
				move_right()
				move_up()

		else:  # wall_is_on_the_right()

			# It is the bottom right corner. Moves into the top left corner.
			for i in range(9):
				move_left()
				move_up()

if __name__ == '__main__':
	run_tasks()