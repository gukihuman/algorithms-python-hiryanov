"""
Draws a square spiral.
"""

import turtle

# Makes the cursor looks like turtle.
turtle.shape('turtle')

# Set a length of starting line.
lenght = 5

# Initializes a cycle with 40 iterations.
for i in range(40):

	# Draws a line using the new length
	# and turn to the left by 90 degrees.
	turtle.forward(lenght)
	turtle.left(90)

	# Increases the length of a line each iteration.
	lenght += 5

# Stops the turtle so you can see the result.
turtle.mainloop()