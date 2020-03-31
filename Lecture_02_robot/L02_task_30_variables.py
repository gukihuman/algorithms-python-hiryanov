#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.1)
def task_9_3():
	"""
	Task 30: Paint over the field with triangles pointing from sides to
	the center. The size of the field is not known, but the length of
	the side is always odd. Stop in the bottom left corner.
	"""

	def check(steps, y, x):
		"""
		Checks the coordinates and fills the standing cell if
		it's not diagonal.

		:param length: the length of the field
		:param y: the "y" coordinate
		:param x: the "x" coordinate
		"""
		if y != x and y != (steps - x):
			fill_cell()

	# Introduce the amount of steps to be done for the moving to
	# the opposite side of the field.
	steps = 0

	# Moves right while there is no wall on the right.
	while not wall_is_on_the_right():
		move_right()

		# Memorize the amount of steps.
		steps += 1

	# Initializes the moving down by the length of the field.
	# The length is the amount of steps plus one.
	for y in range(steps + 1):

		# Initializes the moving to the opposite side.
		for x in range(steps + 1):

			# Checks the coordinates and fills the standing cell if
			# it's not diagonal.
			check(steps, y, x)

			# Always works except the last iteration, so
			# doesn't move left or right in this time.
			if x != steps:

				# Moves left or right in turn by using "y" coordinate.
				# If it's even, moves to the left. If it's odd, to the right.
				# It starts form 0, so first moving is go to the left.
				if y % 2 == 0:
					move_left()
				else:  # i % 2 != 0
					move_right()

		# Moves down if there is no wall beneath.
		# Basically it is always true except the last line.
		if not wall_is_beneath():
			move_down()

if __name__ == '__main__':
	run_tasks()