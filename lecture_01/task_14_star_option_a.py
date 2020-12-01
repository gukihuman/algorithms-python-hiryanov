"""
Draw a star with 5 tips.
"""

import turtle

# Make a cursor look like a turtle.
turtle.shape('turtle')

line = 200

# The number of tips must be odd (3, 5, 7, 9, etc.).
tips_number = 5

angle_tip = 180 / tips_number

# Get start position.
turtle.penup()
turtle.left(angle_tip / 2)
turtle.forward(line / 2)
turtle.left(180 - angle_tip / 2)
turtle.pendown()

for i in range(tips_number):
	turtle.forward(line)
	turtle.left(180 - angle_tip)


# Prevent window from closing so you can see the result.
turtle.mainloop()
