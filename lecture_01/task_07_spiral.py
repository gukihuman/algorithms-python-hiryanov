"""
Draw a spiral.
"""

import turtle

# Make a cursor look like a turtle.
turtle.shape('turtle')

step = 1

for i in range(300):
	turtle.forward(step)
	turtle.left(10)
	
	step += 0.05

# Prevent window from closing so you can see the result.
turtle.mainloop()
