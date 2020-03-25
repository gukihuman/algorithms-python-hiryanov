#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_4():
	"""
	Task 07: Go around the wall. The size of the wall and
	the distance to it are unknown.
	"""

	# Moves down while there is no wall beneath.
	while not wall_is_beneath():
		move_down()

	# Sets variable for memorizing the size of the wall.
	size = 0

	# Moves right while there is a wall beneath.
	# Memorizes the size of the wall.
	while wall_is_beneath():
		move_right()
		size += 1

	# Moves down after the wall is ended.
	move_down()

	# Moves left by the size of the wall.
	move_left(size)

if __name__ == '__main__':
	run_tasks()