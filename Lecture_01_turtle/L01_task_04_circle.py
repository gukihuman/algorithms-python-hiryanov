"""
Draws a circle.
"""

import turtle

# Makes the cursor looks like turtle.
turtle.shape('turtle')

# Initializes a cycle with 360 iterations.
for i in range(360):

	# Draws a mini-line and turn to the left by one degree.
	turtle.forward(1)
	turtle.left(1)

# Stops the turtle so you can see the result.
turtle.mainloop()