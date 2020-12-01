"""
Draw 10 polygons. One inside the other with the same center point.
Every next one has 1 more sides_number.
"""

import turtle
import math

def polygon(sides_number, radius):
	"""
	Draw a polygon to the left side.
	"""

	angle = 360 / sides_number

	# Find a length of a side.
	angle_radians = math.radians(angle / 2)
	sinus = math.sin(angle_radians)
	side = (radius * sinus) * 2

	# Get start position.
	turtle.left(angle / 2)

	for i in range(sides_number):
		turtle.forward(side)
		turtle.left(angle)

	# Make an alignment.
	turtle.right(angle / 2)

# Make a cursor look like a turtle.
turtle.shape('turtle')

# Set the first polygon.
sides_number = 3
radius = 30

offset = 20

for y in range(10):
	turtle.left(90)
	polygon(sides_number, radius)
	turtle.right(90)

	# Move forward without drawing a line.
	turtle.penup()
	turtle.forward(offset)
	turtle.pendown()

	sides_number += 1
	radius += offset

# Prevent window from closing so you can see the result.
turtle.mainloop()
