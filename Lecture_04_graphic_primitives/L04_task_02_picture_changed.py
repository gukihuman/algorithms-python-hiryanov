"""
This picture is based on previous from task 01.
It's changed by positions of objects.
It's been made to show how difficult it is to change flat-style code.

Draws a picture with a couple of objects.
Most of the functions in graphics module are easy to understand.
They creates objects, changes parameters and draws objects.
"gr.Point" is a point with two parameters: "x" and "y" coordinates.
The coordinates starts from upper left corner to lower right corner.
There is three empty lines between the blocks of the code.
Each block is one object. A first part is main and contains parameters.
Other is just additional repeated necessity.
The code was written in flat-style for an education purpose.
"""

import graphics as gr

# Opens a window with 800 length and 600 width with the name.
window = gr.GraphWin("City of Dreams", 800, 600)



# Creates a rectangle of sky by diagonal-opposite points.
sky = gr.Rectangle(gr.Point(0, 0), gr.Point(800, 300))

# Fills the sky by blue.
sky.setFill('blue')

# Makes a stroke of the sky invisible.
sky.setWidth(0)

# Draws the sky.
sky.draw(window)



# Creates a big circle of grass by a center point and a radius.
grass = gr.Circle(gr.Point(400, 12290), 12000)

# Fills the grass by green.
grass.setFill('green')

# Makes a stroke of the grass invisible.
grass.setWidth(0)

# Draws the grass.
grass.draw(window)



# Creates a circle of sun by a center point and a radius.
sun = gr.Circle(gr.Point(450, 110), 40)

# Fills the sun by yellow.
sun.setFill('yellow')

# Makes a stroke of the sun invisible.
sun.setWidth(0)

# Draws the sun.
sun.draw(window)



# Creates five circles of a cloud by a center point and a radius.
cloud_left = gr.Circle(gr.Point(600, 165), 35)
cloud_middle = gr.Circle(gr.Point(650, 150), 40)
cloud_right = gr.Circle(gr.Point(690, 170), 30)
cloud_left_mini = gr.Circle(gr.Point(630, 195), 30)
cloud_right_mini = gr.Circle(gr.Point(665, 200), 25)

# Fills the circles of the cloud by white.
cloud_left.setFill('white')
cloud_middle.setFill('white')
cloud_right.setFill('white')
cloud_left_mini.setFill('white')
cloud_right_mini.setFill('white')

# Makes a stroke of the circles of the cloud invisible.
cloud_left.setWidth(0)
cloud_middle.setWidth(0)
cloud_right.setWidth(0)
cloud_left_mini.setWidth(0)
cloud_right_mini.setWidth(0)

# Draws the circles of the cloud.
cloud_left.draw(window)
cloud_middle.draw(window)
cloud_right.draw(window)
cloud_left_mini.draw(window)
cloud_right_mini.draw(window)



# Creates a rectangle by diagonal-opposite points and
# six circles by a center point and a radius. It's a tree.
trunk = gr.Rectangle(gr.Point(163, 140), gr.Point(177, 350))
foliage_big = gr.Circle(gr.Point(170, 140), 85)
foliage_left = gr.Circle(gr.Point(140, 200), 45)
foliage_right = gr.Circle(gr.Point(200, 200), 48)
foliage_mini = gr.Circle(gr.Point(170, 230), 25)

# Fills the rectangle and the circles of the tree.
trunk.setFill('brown')
foliage_big.setFill('green')
foliage_left.setFill('green')
foliage_right.setFill('green')
foliage_mini.setFill('green')

# Makes a stroke of the rectangle and the circles of the cloud invisible.
trunk.setWidth(0)
foliage_big.setWidth(0)
foliage_left.setWidth(0)
foliage_right.setWidth(0)
foliage_mini.setWidth(0)

# Draws the rectangle and the circles of the cloud.
trunk.draw(window)
foliage_big.draw(window)
foliage_left.draw(window)
foliage_right.draw(window)
foliage_mini.draw(window)



# Creates four circles of a lake by a center point and a radius.
lake_left = gr.Circle(gr.Point(380, 420), 50)
lake_middle_left = gr.Circle(gr.Point(445, 445), 75)
lake_middle_right = gr.Circle(gr.Point(520, 445), 90)
lake_right = gr.Circle(gr.Point(580, 430), 60)

# Fills the circles of the lake by blue.
lake_left.setFill('blue')
lake_middle_left.setFill('blue')
lake_middle_right.setFill('blue')
lake_right.setFill('blue')

# Makes a stroke of the circles of the lake invisible.
lake_left.setWidth(0)
lake_middle_left.setWidth(0)
lake_middle_right.setWidth(0)
lake_right.setWidth(0)

# Draws the circles of the lake.
lake_left.draw(window)
lake_middle_left.draw(window)
lake_middle_right.draw(window)
lake_right.draw(window)


# Waits for a mouse click.
window.getMouse()

# Closes the window.
window.close()