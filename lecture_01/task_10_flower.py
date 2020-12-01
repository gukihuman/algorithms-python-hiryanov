"""
Draw a flower.
"""

import turtle

# Make a cursor look like a turtle.
turtle.shape('turtle')

# Set a circle. The more sides, the smoother the circle.
steps_number = 60
step = 6

angle = 360 / steps_number

circle_couples_number = 3

for i in range(circle_couples_number):

	for i in range(steps_number):
		turtle.forward(step)
		turtle.left(angle)

	# Make an alignment by turning before moving forward.
	for i in range(steps_number):
		turtle.right(angle)
		turtle.forward(step)

	turtle.left(180 / circle_couples_number)

# Prevent window from closing so you can see the result.
turtle.mainloop()
