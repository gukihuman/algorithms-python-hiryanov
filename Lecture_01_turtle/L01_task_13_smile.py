"""
Draws a smile.
There is two kind of movements: drawing and changing a position.
Changing a position always disables printing.

It uses following figures:
- the big yellow circle as a whole face.
- the two small blue circles as eyes.
- the wide black straight line as a nose.
- and the wide red circular line as a mouth.
"""

import turtle
import math

# Makes the cursor looks like turtle.
turtle.shape('turtle')

# This function will be used to draw a circle by using
# a high amount of sides of a polygon. Also it uses radius
# for better positioning of all the figures.
def polygon(sides, radius, type=360):
	"""
	Draws a polygon to the left using an amount of sides and
	the radius of the circumscribed circle of the polygon.
	Default type is full (360).

	:param sides: an amount of sides
	:param radius: a radius of circumscribed circle
	:param type: a type of a polygon, 360 is full, 180 is a half
	"""

	# Calculates the main angle for other calculations.
	angle = type / sides

	# Calculates the length of the side of the polygon
	# using the tricky formula of circumscribed circle.
	angle_radians = math.radians(angle / 2)
	sinus = math.sin(angle_radians)
	length = (radius * sinus) * 2

	# Turns to the left before the drawings to take the correct
	# starting position.
	turtle.left(angle / 2)

	# Initializes a cycle with amount of iterations equals amount of sides.
	for x in range(sides):

		# Draws a line and turn to the left by the value of the main angle.
		turtle.forward(length)
		turtle.left(angle)

	# Turns to the right after the drawings to make the alignment.
	turtle.right(angle / 2)

# Goes to the starting position of the whole face.
turtle.penup()
turtle.goto(75, 0)
turtle.pendown()

# Draws the big yellow circle. It's the whole face.
turtle.left(90)
turtle.begin_fill()
turtle.fillcolor('yellow')
polygon(90, 75)
turtle.end_fill()

# Goes to the starting position of the left eye.
turtle.penup()
turtle.goto(-30, 25)
turtle.pendown()

# Draws the small blue circle. It's the left eye.
turtle.right(90)
turtle.begin_fill()
turtle.fillcolor('blue')
polygon(25, 12)
turtle.end_fill()

# Goes to the starting position of the right eye.
turtle.penup()
turtle.goto(30, 25)
turtle.pendown()

# Draws the small blue circle. It's the right eye.
turtle.begin_fill()
turtle.fillcolor('blue')
polygon(25, 12)
turtle.end_fill()

# Goes to the starting position of the wide black straight line.
turtle.penup()
turtle.goto(0, 5)
turtle.pendown()

# Draws the wide black straight line. Is's the nose.
turtle.right(90)
turtle.width(8)
turtle.forward(25)

# Goes to the starting position of the wide red circular line.
turtle.penup()
turtle.goto(-55, 0)
turtle.pendown()

# Draws the wide red circular line. Is's the mouth.
turtle.color('red')
polygon(180, 55, 180)

# Stops the turtle so you can see the result.
turtle.mainloop()