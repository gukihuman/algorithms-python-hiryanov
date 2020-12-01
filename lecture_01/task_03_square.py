"""
Draw a square.
"""

import turtle

# Make a cursor look like a turtle.
turtle.shape('turtle')

for i in range(4):
	turtle.forward(80)
	turtle.left(90)

# Prevent window from closing so you can see the result.
turtle.mainloop()
