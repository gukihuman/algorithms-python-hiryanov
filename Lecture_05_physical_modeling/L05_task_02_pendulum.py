"""
Runs a simple model of pendulum.

Most of the functions in graphics module are easy to understand.
They creates objects, changes parameters and draws objects.
"gr.Point" is a point with two parameters: "x" and "y" coordinates.
The coordinates starts from upper left corner to lower right corner.
"""

import math
import graphics as gr


def add(point1, point2):
    """
    Adds two coordinates. Each point of input has to be "gr.Point".
    It has "x" and "y" parameters called by ".x" and ".y".

    :param point1: a first coordinate
    :param point2: a second coordinate
    :return: a point which is a result of adding
    """

    # Adds coordinates by "x" for x-coordinate of new point and by
    # "y" for y-coordinate of new point.
    return gr.Point(point1.x + point2.x, point1.y + point2.y)


def update_angle():
    """
    Calculates a new angle of ball deviation by new ball coordinates.

    :return: a new angle of ball deviation
    """

    # Calculates a new angle of ball deviation by arctangent of
    # the ball deviation and a ball height.
    return math.atan(ball_deviation / ball_height)


def update_ball_acceleration():
    """
    Calculates a new acceleration of a ball.

    :return: an acceleration as a coordinate
    """

    # Calculates a new acceleration of a ball by a gravity constant multiplied
    # by a new angle as a "x" coordinate and a difference between old and
    # new height as a "y" coordinate. "x" coordinate is negative because
    # a starting point is on the right, so a ball needs to go to the left.
    # "x" coordinate needs to be decreased.
    return gr.Point(-(G * angle),
                    ball_height - (ball_coords.y - vertex_coords.y))


def update_ball_height():
    """
    Calculates new height of a ball by cord length and ball deviation
    using Pythagoras Theorem. It's a distance between a horizontal axis of
    a pendulum vertex and horizontal axis of a ball.
    In other words, how low the ball is.

    :return: ball height
    """

    return (cord_length ** 2 - ball_deviation ** 2) ** 0.5


def draw_cord():
    """
    Draws a cord by circular elements between the ball and the pendulum
    vertex. Global functions sets unique names for each ball started from
    "element_1".
    """

    # Calculates a distance between elements as "gr.Point" coordinate.
    # "x" coordinate is based on ball deviation and an amount of cord elements
    # plus 1. "y" coordinate is based on ball height and cord elements plus 1.
    # Cord length is devided by an amount of segments which is greater then
    # an amount of elements by 1. Because the elements are located between
    # line segments.
    elements_distance = gr.Point(ball_deviation / (cord_elements+1),
                                 ball_height / (cord_elements+1))

    # Initializes a cycle with an amount of iterations equals to an amount of
    # cord elements. Indexes in the cycle starts from 1.
    for i in range(1, cord_elements+1):

        # Sets element coordinates as a "gr.Point" coordinate.
        # "x" coordinate of an element is based on a "x" coordinate of
        # a distance between elements multiplied by index and "x" coordinate
        # of pendulum vertex.
        # "y" coordinate of an element is based on a "y" coordinate of
        # a distance between elements multiplied by index and "y" coordinate
        # of pendulum vertex.
        element_coords = gr.Point(elements_distance.x*i + vertex_coords.x,
                                  elements_distance.y*i + vertex_coords.y)

        # Sets a global name for an element using index started from
        # "element_1". Draws an element by it's coordinates and size.
        globals()['element_%s' % i] = gr.Circle(element_coords, element_size)
        globals()['element_%s' % i].setFill('black')
        globals()['element_%s' % i].draw(window)


def move_cord():
    """
    Moves cord elements. Global function calls unique names of each element.
    """

    # Calculates a velocity distance between elements as "gr.Point" coordinate.
    # "x" coordinate of velocity distance is based on a "x" coordinate of
    # ball velocity cord elements plus 1.
    elements_velocity_distance = gr.Point(ball_velocity.x / (cord_elements+1),
                                          ball_velocity.y / (cord_elements+1))

    # Initializes a cycle with an amount of iterations equals to an amount of
    # cord elements. Indexes in the cycle starts from 1.
    for i in range(1, cord_elements+1):

        # Moves an element with global name where a number of
        # an element equals to index.
        # A distance of "x" offset is "x" coordinate of a velocity
        # distance between elements multiplied by index.
        # A distance of "y" offset is "y" coordinate of a velocity
        # distance between elements multiplied by index.
        globals()['element_%s' % i].move(elements_velocity_distance.x * i,
                                         elements_velocity_distance.y * i)


# Opens a window with 800 cord_length and 800 width with the name.
window = gr.GraphWin("Model", 800, 800)

# Sets the gravity constant. Basically it affects only on speed of
# programm execution.
G = 0.1

# Sets starting velocity and acceleration to 0.
ball_velocity = gr.Point(0, 0)
ball_acceleration = gr.Point(0, 0)

# Sets starting coordinates of a pendulum vertex and a ball.
vertex_coords = gr.Point(400, 180)
ball_coords = gr.Point(600, 500)

# Calculates ball height by "y" coordinate of a ball and "y" coordinate of
# pendulum vertex. It's a distance between a horizontal axis of
# a pendulum vertex and horizontal axis of a ball.
# In other words, how low a ball is.
ball_height = ball_coords.y - vertex_coords.y

# Calculates ball deviation by "x" coordinate of a ball and "x" coordinate of
# pendulum vertex. It's a distance between a vertical axis of
# a pendulum vertex and vertical axis of a ball.
# In other words, how far from an equilibrium point a ball is.
ball_deviation = ball_coords.x - vertex_coords.x

# Calculates cord length by ball deviation and ball height
# using Pythagoras Theorem.
cord_length = (ball_deviation ** 2 + ball_height ** 2) ** 0.5

# Draws a pendulum vertex by it's coordinates.
vertex = gr.Circle(vertex_coords, 10)
vertex.setFill('black')
vertex.draw(window)

# Draws a ball by it's coordinates.
ball = gr.Circle(ball_coords, 30)
ball.setFill('black')
ball.draw(window)

# Sets an amount of cord elements and a size of an element.
cord_elements = 18
element_size = 5

# Draws a cord.
draw_cord()

# Initializes an infinite cycle with breaking point, which is closing
# the window. Each iteration calculates the new positoins of the ball and
# the cord.
while True:

    # Updates an angle and acceleration.
    angle = update_angle()
    ball_acceleration = update_ball_acceleration()

    # Updates velocity by an addition of velocity and acceleration.
    ball_velocity = add(ball_velocity, ball_acceleration)

    # Moves a ball by "x" coordinate and "y" coordinate of velocity.
    ball.move(ball_velocity.x, ball_velocity.y)

    # Moves a cord.
    move_cord()

    # Updates ball coordinates by an addition of old ball coordinates and
    # velocity.
    ball_coords = add(ball_coords, ball_velocity)

    # Updates ball deviation by new "x" coordinate of the ball and "x"
    # coordinate of pendulum vertex.
    ball_deviation = ball_coords.x - vertex_coords.x

    # Updates ball height.
    ball_height = update_ball_height()

    # Sets a bit of delay for comfort watching.
    gr.time.sleep(0.01)

    # Breaks the cycle if the window is manually closed.
    if window.isClosed():
        break
