"""
Draw a butterfly.
"""

import turtle

# Make a cursor look like a turtle.
turtle.shape('turtle')

# Set the first circle. The more steps, the smoother the circle.
steps_number = 60
step = 5

angle = 360 / steps_number

turtle.left(90)

for i in range(10):

	# Get start position.
	turtle.left(angle / 2)

	for i in range(steps_number):
		turtle.forward(step)
		turtle.left(angle)

	# Make an alignment by turning before moving forward.
	for i in range(steps_number):
		turtle.right(angle)
		turtle.forward(step)

	# Make an alignment.
	turtle.right(angle / 2)

	step += 1

# Prevent window from closing so you can see the result.
turtle.mainloop()
