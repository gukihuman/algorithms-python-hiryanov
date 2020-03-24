"""
Draws a spring by repeating a half of a circle. One time big,
one time small. In fact, the half of a circle is just
a high quality half of a polygon.
"""

import turtle

# Makes the cursor looks like turtle.
turtle.shape('turtle')

# Instead of using a function which uses length and angle, it could be
# a function which uses radius. But this will use additional
# calculations (as in task 09). It's not necessary in this task.
def half_circle(length, angle):
	"""
	Draws a half of a circle to the right. In fact, the half of
	a circle is just a high quality half of a polygon.

	:param length: a length of a side of the half of the polygon
	:param angle: an angle of a turn between sides
	"""

	# Turns to the right by a half of the angle
	# Taking the starting positon.
	turtle.right(angle / 2)

	# Draws a half circle to the right using the amount of sides,
	# the length of the sides and the angle between them.
	for i in range(sides):
		turtle.forward(length)
		turtle.right(angle)

	# Turns to the left by a half of the angle.
	# Making the alignment after the drawings.
	turtle.left(angle / 2)

# Sets an amount of sides of the half of the polygon. The more sides,
# the more accurate the half of a circle will be.
sides = 20

# Sets the angle of a turn between sides.
angle = 180 / sides

# Sets lengths of sides of the halves of the polygons. The more sides,
# the less a length should be. The big length is for a big half of
# a circle, the small one is for a small half of a circle.
length_big = 6
length_small = 1.2

# Turns to the left by 90 degrees. Taking the starting positon.
turtle.left(90)

# Initializes a cycle with 5 iterations.
for i in range(5):

	# Draws a big half of a circle.
	half_circle(length_big, angle)

	# Draws a small half of a circle.
	half_circle(length_small, angle)

# Stops the turtle so you can see the result.
turtle.mainloop()