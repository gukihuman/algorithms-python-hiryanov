"""
Draws a circle.
"""

import turtle

# Makes the cursor looks like turtle.
turtle.shape('turtle')

# Moves to draw a circle.
for i in range(360):
	turtle.forward(1)
	turtle.left(1)

# Stops the turtle so you can see the result.
turtle.mainloop()