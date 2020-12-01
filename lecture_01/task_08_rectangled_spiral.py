"""
Draw a rectangled spiral.
"""

import turtle

# Make a cursor look like a turtle.
turtle.shape('turtle')

step = 5

for i in range(40):
	turtle.forward(step)
	turtle.left(90)

	step += 5

# Prevent window from closing so you can see the result.
turtle.mainloop()
