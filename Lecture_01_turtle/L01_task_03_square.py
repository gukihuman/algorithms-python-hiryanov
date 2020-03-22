"""
Draws a square.
"""

import turtle

# Makes the cursor looks like turtle.
turtle.shape('turtle')

# Moves to draw a square.
for i in range(4):
	turtle.forward(80)
	turtle.left(90)

# Stops the turtle so you can see the result.
turtle.mainloop()