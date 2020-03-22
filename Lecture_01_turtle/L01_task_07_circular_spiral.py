"""
Draws a circular spiral.
"""

import turtle

# Makes the cursor looks like turtle.
turtle.shape('turtle')

# Set a length of starting mini-line.
lenght = 1

# Initializes a cycle with 300 iterations.
for i in range(300):

	# Draws a mini-line using the new length
	# and turn to the left by 10 degrees.
	turtle.forward(lenght)
	turtle.left(10)

	# Increases the length of the mini-line each iteration.
	lenght += 0.05

# Stops the turtle so you can see the result.
turtle.mainloop()