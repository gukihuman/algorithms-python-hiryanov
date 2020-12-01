"""
Draw a spring.
"""

import turtle

def half_circle(step):
	"""
	Draw half a circle to the right side.
	"""

	# The more steps, the smoother the half a circle.
	steps_number = 20

	angle = 180 / steps_number

	# Get start position.
	turtle.right(angle / 2)

	for i in range(steps_number):
		turtle.forward(step)
		turtle.right(angle)

	# Make an alignment.
	turtle.left(angle / 2)

# Make a cursor look like a turtle.
turtle.shape('turtle')

step_big = 6
step_small = 1.2

turtle.left(90)

for i in range(5):
	half_circle(step_big)
	half_circle(step_small)

# Prevent window from closing so you can see the result.
turtle.mainloop()
