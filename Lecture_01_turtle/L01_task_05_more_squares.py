"""
Draws 10 squares. Each inside the another.
"""

import turtle

# Makes the cursor looks like turtle.
turtle.shape('turtle')

# Sets starting coordinates.
x = 0
y = 0

# Sets a length of a side of the first square.
length = 25

# Sets a difference of lengths between squares.
# Better to keep it even, because it will be used
# for new coordinates as a half. And the drawn
# lines could be not flat.
difference = 20

# Initializes a cycle with 10 iterations for each square.
for i in range(10):

	# Disables drawing and moves to the coordinates.
	# Then enable drawing again.
	turtle.penup()
	turtle.goto(x, y)
	turtle.pendown()

	# Draws a square using a new length each iteration.
	for k in range(4):
		turtle.forward(length)
		turtle.left(90)

	# Sets new coordinates for a bottom left corner
	# of the square. Subtract a half of the difference
	# between sides, keeping the same center.
	x -= difference / 2
	y -= difference / 2

	# Sets a new length by adding the difference.
	length += difference

# Stops the turtle so you can see the result.
turtle.mainloop()