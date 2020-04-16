"""
Draws a picture with a couple of complex objects.
This time it uses it's own functions for easier management.
There is two parts of functions.
The first creates basic functions to draw objects from graphics module.
The second creates functions to draw complex objects.

Most of the functions in graphics module are easy to understand.
They creates objects, changes parameters and draws objects.
"gr.Point" is a point with two parameters: "x" and "y" coordinates.
The coordinates starts from upper left corner to lower right corner.
There is three empty lines between the blocks of the code.
Each block is one object. A first part is main and contains parameters.
Other is just additional repeated necessity.
"""

import math
import graphics as gr



# This part creates basic functions to draw objects from graphics module.
def rectangle(stroke, color, point1_x, point1_y, point2_x, point2_y):
	"""
	Draws a rectangle by width of stroke, color, and diagonal-opposite points.

	:param stroke: a width of stroke
	:param color: a color
	:param point1_x: "x" coordinate of first point
	:param point1_y: "y" coordinate of first point
	:param point2_x: "x" coordinate of second point
	:param point2_y: "y" coordinate of second point
	"""

	rectangle = gr.Rectangle(gr.Point(point1_x, point1_y),
							 gr.Point(point2_x, point2_y))
	rectangle.setFill(color)
	rectangle.setWidth(stroke)
	rectangle.draw(window)

def circle(stroke, color, point_x, point_y, radius):
	"""
	Draws a circle by width of stroke, color, a center point and a radius.

	:param stroke: a width of stroke
	:param color: a color
	:param point_x: "x" coordinate of the center point
	:param point_y: "y" coordinate of the center point
	:param radius: a length of a radius
	"""

	circle = gr.Circle(gr.Point(point_x, point_y), radius)
	circle.setFill(color)
	circle.setWidth(stroke)
	circle.draw(window)

def line(width, color, point1_x, point1_y, point2_x, point2_y):
	"""
	Draws a line by width, color, and two points.

	:param width: a width
	:param color: a color
	:param point1_x: "x" coordinate of the first point
	:param point1_y: "y" coordinate of the first point
	:param point2_x: "x" coordinate of the second point
	:param point2_y: "y" coordinate of the second point
	"""

	line = gr.Line(gr.Point(point1_x, point1_y), gr.Point(point2_x, point2_y))
	line.setOutline(color)
	line.setWidth(width)
	line.draw(window)



# This part creates functions to draw complex objects.
def sun(point_x, point_y, radius):
	"""
	Draws sun with rays by a center point and a radius.

	:param point_x: "x" coordinate of the center point
	:param point_y: "y" coordinate of the center point
	:param radius: a length of a radius
	"""

	# Draws a yellow circle of sun by a center point and a radius.
	circle(0, 'yellow', point_x, point_y, radius)

	# Sets abradius for a hidden inside circle of rays
	# by the radius of the sun.
	in_rad = radius * 1.2

	# Sets a radius for a hidden outside circle of rays
	# by the radius of the sun.
	out_rad = radius * 1.7

	# Sets a starting angle for rays in degrees.
	angle = 10

	# Initializes a cycle with 5 iterations. The cycle goes only in a quarter
	# of the circle. Though, the rays is drawn in each quarter of the circle
	# on each iteration. 4 rays per iteration, 5 rays in each quarter.
	for i in range(5):

		# Sets an offset for rays coordinates by radii of inside and outside
		# circles of rays multiplied by a sinus and a cosine of the angle.
		# It's an offset from the center point of the sun.
		# Degrees are changed to radians for sinus and cosine from math module.
		off_in_x = in_rad * math.cos(math.radians(angle))
		off_in_y = in_rad * math.sin(math.radians(angle))
		off_out_x = out_rad * math.cos(math.radians(angle))
		off_out_y = out_rad * math.sin(math.radians(angle))

		# Draws a yellow line of a ray by coordinates in each quarter.
		# Coordinates is found by the position of the sun and the offset.
		# The first line is a top right quarter.
		# The second line is a top left quarter.
		# The third line is a bottom left quarter.
		# The fourth line is a bottom right quarter.
		line(6, 'yellow', point_x + off_in_x, point_y - off_in_y,
			 point_x + off_out_x, point_y - off_out_y)
		line(6, 'yellow', point_x - off_in_y, point_y - off_in_x,
			 point_x - off_out_y, point_y - off_out_x)
		line(6, 'yellow', point_x - off_in_x, point_y + off_in_y,
			 point_x - off_out_x, point_y + off_out_y)
		line(6, 'yellow', point_x + off_in_y, point_y + off_in_x,
			 point_x + off_out_y, point_y + off_out_x)

		# Increases the angle for a new ray by a value of an angle of a quarter
		# of a circle in degrees. It's divided by the amount of iterations.
		angle += 90 / 5

def cloud(point_x, point_y, width):
	"""
	Draws a cloud by a top left corner and a width.
	The cloud contains five circles.

	:param point_x: "x" coordinate of a top left corner of a cloud
	:param point_y: "y" coordinate of a top left corner of a cloud
	:param width: a width of a cloud
	"""

	# Sets height based on width.
	height = width * 2/3

	# Draws circles of a cloud by a center point and a radius.
	# The radius depends on width.
	# The first circle is top left. The second circle is top right.
	# The third circle is bottom left. The fourth circle is bottom middle.
	# The fifth circle is bottom right.
	circle(0, 'white', point_x + width * 1/3, point_y + height * 1/3,
		   width * 21/100)
	circle(0, 'white', point_x + width * 2/3, point_y + height * 1/3,
		   width * 24/100)
	circle(0, 'white', point_x + width * 1/6, point_y + height * 2/3,
		   width * 16/100)
	circle(0, 'white', point_x + width * 3/6, point_y + height * 2/3,
		   width * 28/100)
	circle(0, 'white', point_x + width * 5/6, point_y + height * 2/3,
		   width * 22/100)

def building(point_x, point_y, width):
	"""
	Draws a building by a top left corner and a width.
	The building contains a rectangle of a body, 6 rectangles of windows,
	a rectangle of a threshold, a rectangle of a door and a rectangle of
	a roof above the door.

	:param point_x: "x" coordinate of a top left corner of a building
	:param point_y: "y" coordinate of a top left corner of a building
	:param width: a width of a building
	"""

	# Sets height based on width.
	height = width * 2

	# Draws a rectangle of a body by diagonal-opposite points.
	rectangle(0, 'gray', point_x, point_y, point_x + width, point_y + height)

	# Draws rectangles of windows by diagonal-opposite points.
	# A stroke depends on width.
	# The first rectangle is top left. The second rectangle is middle left.
	# The third rectangle is bottom left. The fourth rectangle is top right.
	# The fifth rectangle is middle right. The sixth rectangle is bottom right.
	rectangle(width/70, 'yellow', point_x + width * 1/7, point_y + width * 1/7,
			  point_x + width * 3/7, point_y + width * 3/7)
	rectangle(width/70, 'yellow', point_x + width * 1/7, point_y + width * 4/7,
			  point_x + width * 3/7, point_y + width * 6/7)
	rectangle(width/70, 'yellow', point_x + width * 1/7, point_y + width * 7/7,
			  point_x + width * 3/7, point_y + width * 9/7)
	rectangle(width/70, 'yellow', point_x + width * 4/7, point_y + width * 1/7,
			  point_x + width * 6/7, point_y + width * 3/7)
	rectangle(width/70, 'yellow', point_x + width * 4/7, point_y + width * 4/7,
			  point_x + width * 6/7, point_y + width * 6/7)
	rectangle(width/70, 'yellow', point_x + width * 4/7, point_y + width * 7/7,
			  point_x + width * 6/7, point_y + width * 9/7)

	# Draws a rectangle of a threshold by diagonal-opposite points.
	# A stroke depends on width.
	rectangle(width/70, 'grey',
			  point_x + width * 2.2/7, point_y + height * 9.5/10,
			  point_x + width * 4.8/7, point_y + height)

	# Draws a rectangle of a door by diagonal-opposite points.
	rectangle(0, 'black', point_x + width * 2.8/7, point_y + height * 8/10,
			  point_x + width * 4.2/7, point_y + height * 9.5/10)

	# Draws a rectangle of a roof above the door by diagonal-opposite points.
	# A stroke depends on width.
	rectangle(width/70, 'grey',
			  point_x + width * 2.2/7, point_y + height * 7.7/10,
			  point_x + width * 4.8/7, point_y + height * 8/10)

def man(point_x, point_y, width):
	"""
	Draws a man by a top left corner and a width.
	The man contains a rectangle of a body, 2 lines of pants, 2 lines of arms,
	2 circles of shoulders, circle of a hat, circle of a head, rectangle of
	a hat, circles of mustache and circles of eyes.

	:param point_x: "x" coordinate of a top left corner of a man
	:param point_y: "y" coordinate of a top left corner of a building
	:param width: a width of a building
	"""

	# Sets height based on width.
	height = width * 2

	# Draws a rectangle of a body by diagonal-opposite points.
	rectangle(0, 'brown', point_x + width * 1/4, point_y + height * 1.5/4,
			  point_x + width * 3/4, point_y + height)

	# Draws lines of pants by two points. A thickness depends on width.
	# The first line is horizontal. The second line is vertical.
	line(width/25, 'black', point_x + width * 1/4, point_y + height * 3.3/4,
		 point_x + width * 3/4, point_y + height * 3.3/4)
	line(width/25, 'black', point_x + width * 1/2, point_y + height * 3.3/4,
		 point_x + width * 1/2, point_y + height)

	# Draws lines of arms by two points. A thickness depends on width.
	# The first line is a left arm. The second line is a right arm.
	line(width/7, 'black', point_x + width * 0.8/4, point_y + height * 2.5/4,
		 point_x + width * 0.4/4, point_y + height * 3.1/4)
	line(width/7, 'black', point_x + width * 3.2/4, point_y + height * 2.5/4,
		 point_x + width * 3.6/4, point_y + height * 3.1/4)

	# Draws circles of shoulders by a center point and a radius.
	# The first circle is a left shoulder.
	# The second circle is a right shoulder.
	circle(0, 'brown', point_x + width * 1.2/4, point_y + height * 2.5/4,
		   width * 1.7/10)
	circle(0, 'brown', point_x + width * 2.8/4, point_y + height * 2.5/4,
		   width * 1.7/10)

	# Draws a circle of a hat by a center point and a radius.
	circle(0, 'black', point_x + width * 1/2, point_y + height * 0.6/4,
		   width * 25/80)

	# Draws a circle of a head by a center point and a radius.
	circle(0, 'yellow', point_x + width * 1/2, point_y + height * 1.5/4,
		   width * 40/80)

	# Draws a rectangle of a hat by diagonal-opposite points.
	rectangle(0, 'black', point_x + width * -0.5/4, point_y + height * 0.5/4,
			  point_x + width * 4.5/4, point_y + height * 1/4)

	# Draws circles of mustache by a center point and a radius.
	# The stroke depends on width. The first circle is a left mustache.
	# The second circle is a right mustache.
	circle(width/100, 'black', point_x + width * 4/10, point_y + height * 2/4,
		   width * 1/10)
	circle(width/100, 'black', point_x + width * 6/10, point_y + height * 2/4,
		   width * 1/10)

	# Draws circles of eyes by a center point and a radius.
	# The first circle is a left eye. The second circle is a right eye.
	circle(0, 'black', point_x + width * 3/10, point_y + height * 1.6/4,
		   width * 0.3/10)
	circle(0, 'black', point_x + width * 7/10, point_y + height * 1.6/4,
		   width * 0.3/10)



# Opens a window with 800 length and 600 width with the name.
window = gr.GraphWin("City of Dreams", 800, 600)

# Draws a rectangle of sky by diagonal-opposite points.
rectangle(0, 'blue', 0, 0, 800, 275)

# Draws a big circle of grass by a center point and a radius.
circle(0, 'green', 400, 12265, 12000)

# Draws complex objects. Sun is drawn by a center point and a radius.
# Other objects is drawn by a top left corner and a width.
sun(236, 135, 40)
man(538, 270, 18)  # hiding man
building(610, 180, 145)
building(470, 210, 80)
building(390, 235, 42)
cloud(80, 120, 140)
cloud(440, 50, 110)
cloud(670, 80, 85)
cloud(440, 190, 45)
man(140, 290, 210)
man(620, 450, 40)  # the kid
man(560, 400, 65)
man(452, 325, 32)
man(385, 300, 15)
man(50, 252, 12)  # the man on a field
man(703, 62, 12)  # the man on a cloud

# Waits for a mouse click.
window.getMouse()

# Closes the window.
window.close()