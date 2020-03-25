#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_3():
	"""
	Task 06: Reach the end of the wall. The distance is not known.
	At the beginning there is no wall for some cells.
	"""

	# Moves right while there is no wall beneath.
	while not wall_is_beneath():
		move_right()

	# Moves right while a wall is beneath.
	while wall_is_beneath():
		move_right()

if __name__ == '__main__':
	run_tasks()