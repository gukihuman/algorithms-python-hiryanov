"""
Draws the letter S.
"""

import turtle

# Makes the cursor looks like turtle.
turtle.shape('turtle')

# Draws a line and turn to the left by 90 degrees.
turtle.forward(50)
turtle.left(90)

# Draws a line and turn to the left by 90 degrees.
turtle.forward(50)
turtle.left(90)

# Draws a line and turn to the right by 90 degrees.
turtle.forward(50)
turtle.right(90)

# Draws a line and turn to the right by 90 degrees.
turtle.forward(50)
turtle.right(90)

# Draws a final line
turtle.forward(50)

# Stops the turtle so you can see the result.
turtle.mainloop()