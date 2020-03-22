"""
Draws a spider with variable amount of legs.
"""

import turtle

# Makes the cursor looks like turtle.
turtle.shape('turtle')

# Sets a number of legs.
legs = 12

# Calculates an angle between two closest legs.
angle = 360 / legs

# Initializes a cycle with amount of iterations equals legs.
for i in range(legs):

	# This is main turn.
	# Turns to the right by angle-variable.
	turtle.right(angle)

	# Draws a line and makes a stamp.
	turtle.forward(100)
	turtle.stamp()

	# Turn by 180 degrees and go back.
	turtle.right(180)
	turtle.forward(100)

	# Turn by 180 degrees to stand on the position where turtle was
	# before going from the center but after making the main turn.
	turtle.right(180)

# Stops the turtle so you can see the result.
turtle.mainloop()