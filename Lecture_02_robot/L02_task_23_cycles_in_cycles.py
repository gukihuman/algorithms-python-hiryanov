#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():
	"""
	Task 23: There is the horizontal tunnel connected to vertical corridors
	above. The amount and the size of the corridors is not known.
	Starting position is in the cell before the tunnel.
	Fill the all corridors and go back to the same position.
	"""

	# Sets an empty length of the tunnel.
	tunnel = 0

	# Moves right while there is no wall on the right.
	while not wall_is_on_the_right():
		move_right()

		# Memorizes the length of the tunnel each move.
		tunnel += 1

		# Checks the cell above. If there is no wall above, moves up while
		# there is no wall above. Fills the cells.
		if not wall_is_above():

			# Sets an empty length of the new corridor.
			corridor = 0

			# Moves up while there is no wall above. Fills the cells.
			while not wall_is_above():
				move_up()
				fill_cell()

				# Memorizes the length of the corridor each move.
				corridor += 1

			# Go back to the tunnel by the length of the corridor.
			move_down(corridor)

	# Go back to the starting position by the length of the tunnel.
	move_left(tunnel)


if __name__ == '__main__':
	run_tasks()