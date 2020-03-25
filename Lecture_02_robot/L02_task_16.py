#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_22():
	"""
	Task 16. Reach the impasse of the tunnel. The tunnel has
	the shape of the 90 degrees angle. It turns from bottom to
	the left or to the right. The sizes of the tunnel are not known.
	"""

	# Moves up while there is no wall above.
	while not wall_is_above():
		move_up()

	# Checks if there is a wall on the left or on the right.
	if wall_is_on_the_right():

		# The wall is on the right. Moves to the left while
		# there is no wall on the left.
		while not wall_is_on_the_left():
			move_left()

	else:  # wall_is_on_the_left()

		# The wall is on the left. Moves to the right while
		# there is no wall on the right.
		while not wall_is_on_the_right():
			move_right()

if __name__ == '__main__':
	run_tasks()