"""
Draw a circle.
"""

import turtle

# Make a cursor look like a turtle.
turtle.shape('turtle')

for i in range(360):
	turtle.forward(1)
	turtle.left(1)

# Prevent window from closing so you can see the result.
turtle.mainloop()
