"""
Draw 10 squares. One inside the other.
"""

import turtle

# Make a cursor look like a turtle.
turtle.shape('turtle')

# Start coordinates.
x = 0
y = 0

side = 25
offset = 10

for i in range(10):

	# Move to coordinates without drawing a line.
	turtle.penup()
	turtle.goto(x, y)
	turtle.pendown()

	for k in range(4):
		turtle.forward(side)
		turtle.left(90)

	# Update coordinates and a side.
	x -= offset
	y -= offset
	side += offset * 2

# Prevent window from closing so you can see the result.
turtle.mainloop()
