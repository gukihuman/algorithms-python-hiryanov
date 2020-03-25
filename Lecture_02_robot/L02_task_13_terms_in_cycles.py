#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_10():
	"""
	Task 13: Go to the wall on the right. The distance to
	the wall is not known. Paint over the cell above if no wall
	is above. Paint over the cell beneath if no wall is beneath.
	"""

	def check():
		"""
		Checks the cells above and beneath. Fill the cell above if
		no wall is above. Fill the cell beneath if no wall is beneath.
		"""

		# Fill the cell above if there is no wall above.
		if not wall_is_above():
			move_up()
			fill_cell()
			move_down()

		# Fill the cell beneath if there is no wall beneath.
		if not wall_is_beneath():
			move_down()
			fill_cell()
			move_up()

	# Moves right while there is no wall on the right.
	while not wall_is_on_the_right():

		# Checks the cells above and beneath and fills them by the terms.
		check()

		move_right()

	# Checks the last position by the terms.
	check()

if __name__ == '__main__':
	run_tasks()