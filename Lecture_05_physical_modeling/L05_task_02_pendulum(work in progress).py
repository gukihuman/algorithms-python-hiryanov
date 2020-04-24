"""
Runs a simple model of pendulum.*
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
    point = gr.Point(point1.x + point2.x, point1.y + point2.y)

    # Returns the new point
    return point


def sub(point1, point2):
    """
    Subtracts a second coordinate from a first. Each point of input has
    to be "gr.Point". It has "x" and "y" parameters called by ".x" and ".y".

    :param point1: a first coordinate
    :param point2: a second coordinate
    :return: a point which is a result of subtracting
    """

    # Subtracts coordinates by "x" for x-coordinate of new point and by
    # "y" for y-coordinate of new point.
    point = gr.Point(point1.x - point2.x, point1.y - point2.y)

    # Returns the new point
    return point


def update_angle():
    """
    Calculates a new angle of ball deviation by new ball coordinates.

    :return: a new angle of ball deviation
    """

    # Calculates a new angle of ball deviation using the tricky formula.
    new_angle = math.atan(ball_deviation / -ball_height)

    # Returns a new angle of ball deviation.
    return new_angle


def update_ball_height():
    """
    Calculates a ball height  vertex point of the pendulum and
    the middle point of the pendulum by deviation on the ball_height of the ball
    """

    new_height = (cord_length ** 2 - ball_deviation ** 2) ** 0.5
    return new_height


def update_acceleration():
    """
    Return the amount of acceleration using the gravity strength and
    the angle angle for x coordinate and the substraction the ball_height from
    the new ball_height and the same but with old ball_height witch is
    ball_coords.y - vertex_coords.y
    """

    return gr.Point(G * angle, (ball_height - ball_height) - ((ball_coords.y - vertex_coords.y) - ball_height))


def create_cord(size):
    """
    Creates a cord using circles between the ball and the vertex of the pendulum.
    Global function creates unique names for each circle started by circle_0
    """

    # ball_deviation between the circles by x
    dist_x = ball_deviation/(amount+1)
    dist_y = ball_height/(amount+1)  # ball_deviation between the circles by y
    for k in range(amount):
        coords_circle = gr.Point(
            dist_x*(k+1) + vertex_coords.x, dist_y*(k+1) + vertex_coords.y)
        globals()['circle_%s' % k] = gr.Circle(coords_circle, size)
        globals()['circle_%s' % k].setFill('black')
        globals()['circle_%s' % k].draw(window)
        globals()['coords_circle_%s' % k] = coords_circle


def move_cord():
    """
    Moving the circles in the cord using just velocity of the ball.
    Global function calls the unique names for each circle to move
    """

    dist_x = velocity.x / \
        (amount+1)  # ball_deviation inside the velocity between the circles by x
    # ball_deviation inside the velocity between the circles by y
    dist_y = velocity.y/(amount+1)
    for k in range(amount):
        velocity_circle = gr.Point(dist_x*(k+1), dist_y*(k+1))
        globals()['velocity_circle_%s' % k] = velocity_circle
        globals()['circle_%s' % k].move(globals()['velocity_circle_%s' % k].x,
                                        globals()['velocity_circle_%s' % k].y)


# Opens a window with 800 cord_length and 800 width with the name.
window = gr.GraphWin("Model", 800, 800)

# Sets the gravity.
G = 0.02

# Sets starting velocity to 0.
velocity = gr.Point(0, 0)

acceleration = gr.Point(0, 0)  # acceleration

vertex_coords = gr.Point(400, 180)  # vertex pendulum point

ball_coords = gr.Point(600, 500)  # starting coordinates

# Calculates ball height. It's a distance between a horizontal axis of
# a vertex of a pendulum and horizontal axis of a ball.
# In other words, how low the ball is.
ball_height = ball_coords.y - vertex_coords.y

# ball_deviation the ball to the middle of the pendulum
ball_deviation = ball_coords.x - vertex_coords.x

# Calculates cord length by ball deviation and ball height
# using Pythagoras Theorem.
cord_length = (ball_deviation ** 2 + ball_height ** 2) ** 0.5


vertex = gr.Circle(vertex_coords, 12)  # create a vertex of the pendulum
vertex.setFill('black')  # fill the vertex of the pendulum
vertex.draw(window)  # draw the vertex of the pendulum

ball = gr.Circle(ball_coords, 28)  # create a ball
ball.setFill('black')  # fill the ball
ball.draw(window)  # draw the ball

# amount = 17  # amount of circles in the cord
# # creates cord by circles where argument is a size of the circles
# create_cord(5)


# Initializes an infinite cycle with breaking point, which is closing
# the window. Each iteration calculates the new positoins of the ball and
# the cord.
while True:

    angle = update_angle()
    acceleration = update_acceleration()

    # update velocity by adding the acceleration
    velocity = add(velocity, acceleration)

    ball.move(velocity.x, velocity.y)  # move the ball using velocity values

    ball_coords = add(ball_coords, velocity)  # update ball_coords
    ball_deviation = ball_coords.x - vertex_coords.x  # update ball_deviation
    ball_height = update_ball_height()

    # move_cord()  # move the cord (details in description of the function)

    # Sets a bit of delay for comfort watching.
    gr.time.sleep(0.005)

    # Breaks the cycle if the window is manually closed.
    if window.isClosed():
        break
