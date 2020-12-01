"""
Draw a spider.
"""

import turtle

# Make a cursor look like a turtle.
turtle.shape('turtle')

legs_number = 12
angle = 360 / legs_number

for i in range(legs_number):
	turtle.right(angle)
	turtle.forward(100)

	# Imprint.
	turtle.stamp()	

	turtle.right(180)
	turtle.forward(100)
	turtle.right(180)

# Prevent window from closing so you can see the result.
turtle.mainloop()
