"""
Draws a star polygon with variable corner verticals.
This option uses 11 corner verticals.
"""

import turtle

# Makes the cursor looks like turtle.
turtle.shape('turtle')

def star(corners, length):
	"""
	Draws a star polygon using an amount of corner verticals and
	a length between two corner verticals.

	:param corners: an amount of corner verticals of a star
	:param length: a length between two corner verticals
	"""

	for i in range(corners):
		turtle.forward(length)
		turtle.left(180 - (360 / corners / 2))

# Sets an amount of corner verticals. Only odd numbers.
corners = 11

# Sets a length between two corner verticals.
length = 200

# Goes to the starting position.
# Uses 4x multiplier for the first turn special for
# 11 corner vertical.
turtle.penup()
turtle.left((360/corners / 2) * 4)
turtle.forward(length / 2)
turtle.left(180 - (360 / corners / 2))
turtle.pendown()

# Draws a star.
star(corners, length)

# Stops the turtle so you can see the result.
turtle.mainloop()