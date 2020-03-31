#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_8_30():
	"""
	Task 31: There is the levels of grounds. Each level has one way to
	the bottom level except the last. The distance between the levels and
	the walls is not known. Reach the bottom level and stop near the left wall.
	"""

	# Introduces the variable of the progress of the task.
	done = False

	# Introduces the variable of the wall hits.
	wall_hit = 0

	# Works while the task is not finished.
	while not done:

		# Moves to the left while there is no wall on the left.
		while not wall_is_on_the_left():
			move_left()

			# Moves down if there is no wall beneath.
			# Continues to move while there is no wall beneath.
			while not wall_is_beneath():
				move_down()

				# Resets the amount of wall hits for the next level.
				wall_hit = 0

		# Cycle of moving to the left is over. It means the position is near
		# the left wall. Increases the amount of wall hits.
		wall_hit += 1

		# The task is finished. Both walls is hit. And wall is on the left
		# because the cycle of moving to the left is just finished.
		if wall_hit >= 2:
			done = True

			# Breaks the big cycle to not moving to the right again and
			# to stop near the left wall.
			break

		# Moves to the right while there is no wall on the right.
		while not wall_is_on_the_right():
			move_right()

			# Moves down while there is no wall beneath.
			# Continues to move while there is no wall beneath.
			while not wall_is_beneath():
				move_down()

				# Resets the amount of wall hits for the next level.
				wall_hit = 0

		# Cycle of moving to the right is over. It means the position is near
		# the right wall. Increases the amount of wall hits.
		wall_hit += 1

if __name__ == '__main__':
	run_tasks()