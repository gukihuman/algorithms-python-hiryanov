#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_29():
	"""
	Task 19: You are in the horizontal linear tunnel.
	Where the exit is not known. It may be on the left side or
	on the right side. Also it is possible that there is no exit at all.
	Get out of the trap and then into the top left corner.
	If there is no exit, stop in the right dead end.
	"""

	def up_left():
		"""
		Moves into the top left corner.
		"""

		# Moves up while there is no wall above.
		while not wall_is_above():
			move_up()

		# Moves left while there is no wall on the left.
		while not wall_is_on_the_left():
			move_left()

	# Moves left while there is no wall on the left.
	while not wall_is_on_the_left():
		move_left()

	# Checks the cell above. If there is no wall above, the position is
	# outside the tunnel. In this case, moves into the top left corner.
	# If there is a wall above, the position still inside the tunnel.
	# In this case, moves right while there is no wall on the right.
	# Then checks the top cell again.
	if not wall_is_above():
		up_left()

	else:  # wall_is_above()
		while not wall_is_on_the_right():
			move_right()

		# Checks the cell above. If there is no wall above, the position is
		# outside the tunnel. In this case, moves into the top left corner.
		# If there is a wall above, the position still inside the tunnel.
		# In this case, there is no way out. Stays here.
		if not wall_is_above():
			up_left()

if __name__ == '__main__':
	run_tasks()
