"""
Draws a square.
"""

import turtle

# Makes the cursor looks like turtle.
turtle.shape('turtle')

# Initializes a cycle with 4 iterations.
for i in range(4):

	# Draws a line and turn to the left by 90 degrees.
	turtle.forward(80)
	turtle.left(90)

# Stops the turtle so you can see the result.
turtle.mainloop()