"""
Draw a smile.
"""

import turtle
import math

def jump(x, y):
	"""
	Move to coordinates without drawing a line.
	"""

	turtle.penup()
	turtle.goto(x, y)
	turtle.pendown()

def circle(radius, type='full'):
	"""
	Draw a circle to the left side. To draw half a circle use 'half'
	as the second parameter.
	"""

	# The more steps, the smoother the circle.
	steps_number = 60

	if type == 'half':
		degrees = 180
	else:
		degrees = 360
	
	angle = degrees / steps_number

	# Find a length of a step.
	angle_radians = math.radians(angle / 2)
	sinus = math.sin(angle_radians)
	step = (radius * sinus) * 2

	# Get start position.
	turtle.left(angle / 2)

	for i in range(steps_number):
		turtle.forward(step)
		turtle.left(angle)

	# Make an alignment.
	turtle.right(angle / 2)

def circle_colored(radius, color):
	"""
	Draw a colored circle to the left side. Use 'circle' function.
	"""

	turtle.begin_fill()
	turtle.fillcolor(color)
	circle(radius)
	turtle.end_fill()

# Make a cursor look like a turtle.
turtle.shape('turtle')

jump(75, 0)
turtle.left(90)
circle_colored(75, 'yellow')

jump(-30, 25)
turtle.right(90)
circle_colored(12, 'blue')

jump(30, 25)
circle_colored(12, 'blue')

# Make a line wide.
turtle.width(8)

jump(0, 5)
turtle.right(90)
turtle.forward(25)

jump(-55, 0)
turtle.color('red')
circle(55, 'half')

# Prevent window from closing so you can see the result.
turtle.mainloop()
