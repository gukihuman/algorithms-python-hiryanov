#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_28():
	"""
	Task 18: You are in the horizontal linear tunnel.
	Where the exit is not known. It is known that the exit above.
	Get out of the trap and then into the top left corner.
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

	# Sets a variable for memorizing the size of the right side of the wall.
	# It's not necessary, but in this case there is no need to recheck
	# the right side of the tunnel while going back.
	size = 0

	# Checks the right side of the tunnel. Moves right while
	# there is no wall on the right and wall is above.
	while not wall_is_on_the_right() and wall_is_above():
		move_right()

		# Memorizes the size of the right side of the wall.
		size += 1

	# Checks the cell above. If there is no wall above, it is the way out.
	# In this case, moves into the top left corner.
	# If there is a wall above, the position still inside the tunnel.
	# In this case, moves left to the staring position included
	# without checking. Then checks the left side of the tunnel.
	if not wall_is_above():
		up_left()

	else:  # wall_is_above()
		move_left(size + 1)

		# Moves left while there is a wall above.
		while wall_is_above():
			move_left()

		# After the previous cycle, the position is in the cell, where
		# is no wall above. It is 100% the way out. Moves out.
		up_left()

if __name__ == '__main__':
	run_tasks()