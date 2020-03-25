#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_28():
	"""
	Task 18: You are in the horizontal linear tunnel.
	Where the exit is not known. It is known that the exit above.
	Get out of the trap and then into the top left corner.
	"""

	def way_out():
		"""
		Checks the cell above. If there is a wall, does nothing.
		If there is no wall, moves up while no wall above.
		Then moves left while no wall on the left.
		Also sets the task solving to True.
		"""
		if not wall_is_above():
			while not wall_is_above():
				move_up()
			while not wall_is_on_the_left():
				move_left()

			# Sets flag to global variable inside the way_out function.
			global flag

			# Sets the task solving to True.
			flag = True

	# Sets flag to global variable inside the main task function.
	global flag

	# Sets the task solving to False at the beginning.
	flag = False

	# Sets a variable for memorizing the size of the right side of the wall.
	# It's not necessary, but in this case there is no need to recheck
	# the right side of the tunnel while going back.
	size = 0

	# Checks the right side of the tunnel first.
	# Moves right while there is no wall on the right.
	while not wall_is_on_the_right():

		# Checks the cell above and moves out if there is no wall above.
		way_out()

		# Breaks the cycle, if the task is already solved.
		if flag:
			break

		move_right()

		# Memorizes the size of the right side of the wall.
		size += 1

	# If the task is not solved, the position is in the last right cell.
	# Checks the cell above and moves out if there is no wall above.
	if not flag:
		way_out()

		# If the task is not solved, the last right cell is not a way out.
		# Moves to the staring position included without checking.
		# Then checks the left side of the tunnel.
		if not flag:
			move_left(size + 1)

			# Moves left while there is no wall on the left.
			while not wall_is_on_the_left():

				# Checks the cell above and moves out if there is
				# no wall above.
				way_out()

				# Breaks the cycle, if the task is already solved.
				if flag:
					break

				move_left()

			# If the task is not solved yet, the position is in the last
			# left cell and it is 100% the way out. Moves out.
			if not flag:
				way_out()

if __name__ == '__main__':
	run_tasks()