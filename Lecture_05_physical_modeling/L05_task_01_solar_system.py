"""
Runs a casual model of solar system.

Most of the functions in graphics module are easy to understand.
They creates objects, changes parameters and draws objects.
"gr.Point" is a point with two parameters: "x" and "y" coordinates.
The coordinates starts from upper left corner to lower right corner.
"""

import graphics as gr
import random as r


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
    return gr.Point(point1.x - point2.x, point1.y - point2.y)


def update_acceleration(planet_coords, center_coords):
    """
    Calculates a new point of a ball in casual gravity model, where
    center point is a source of gravity.

    :param planet_coords: a ball coordinates
    :param center_coords: a center coordinates
    :return: a point which is a result of calculating
    """

    # Calculates a new point of a ball in casual gravity model
    # using the tricky formula. "diff" is difference.
    diff = sub(planet_coords, center_coords)
    distance = (diff.x ** 2 + diff.y ** 2) ** (3/2)
    G = 2000
    new_point = gr.Point(-diff.x * G / distance, -diff.y * G / distance)

    # Returns a new point of a ball.
    return new_point


def planet_draw(name, size, color, coord_x, coord_y, velocity_x, velocity_y):
    """
    Draws a planet. Global functions creates unique names of a planets.

    :param name: a string of a planet name
    :param size: a planet size
    :param color: a string of a planet color
    :param coord_x: "x" coordinate of a planet
    :param coord_y: "y" coordinate of a plenet
    :param velocity_x: "x" coordinate of planet velocity
    :param velocity_y: "y" coordinate of planet velocity
    """

    # Sets planet coordinatinos and draws it.
    globals()[name + '_coords'] = gr.Point(coord_x, coord_y)
    globals()[name] = gr.Circle(globals()[name + '_coords'], size)
    globals()[name].setFill(color)
    globals()[name].draw(window)

    # Sets planet velocity and acceleration.
    globals()[name + '_velocity'] = gr.Point(velocity_x, velocity_y)
    globals()[name + '_acceleration'] = gr.Point(0, 0)


def planet_move(name):
    """
    Moves a planet. Global functions calls unique name of a planet.

    :param name: a string of a planet name
    """

    # Moves objects by their velocity.
    globals()[name].move(globals()[name + '_velocity'].x,
                         globals()[name + '_velocity'].y)

    # Updates acceleration by current coordinations and sun coordinations.
    globals()[name + '_acceleration'] = update_acceleration(
        globals()[name + '_coords'], sun_coords)

    # Updates velocity by addition of current velocity and acceleration.
    globals()[name + '_velocity'] = add(globals()[name + '_velocity'],
                                        globals()[name + '_acceleration'])

    # Updates coordinates by addition of current coordinations and velocity.
    globals()[name + '_coords'] = add(globals()[name + '_coords'],
                                      globals()[name + '_velocity'])


# Opens a window with 800 length and 800 width with the name.
window = gr.GraphWin("Model", 800, 800)

# Draws a rectangle of space by diagonal-opposite points.
space = gr.Rectangle(gr.Point(0, 0), gr.Point(800, 800))
space.setFill('black')
space.draw(window)

# Draws stars with random positions.
for i in range(50):
    star = gr.Circle(
        gr.Point(r.randrange(800), r.randrange(800)), 1)
    star.setFill('white')
    star.draw(window)

# Sets coordinatinos of Sun and draws it.
sun_coords = gr.Point(400, 400)
sun = gr.Circle(sun_coords, 20)
sun.setFill('yellow')
sun.draw(window)

# Sets coordinations of planets and draws it.
# Also sets it's starting velocity.
planet_draw('mercury', 2, '#A4868D', 400, 437, 7.2, 0)
planet_draw('venus', 5, '#499F91', 455, 400, 0, -6.1)
planet_draw('earth', 6, '#0044FF', 400, 325, -5.25, 0)
planet_draw('mars', 4, '#980A0A', 300, 400, 0, 4.42)
planet_draw('jupiter', 15, '#685020', 210, 400, 0, 3.2)
planet_draw('saturn', 13, '#8A6D32', 400, 150, -2.82, 0)
planet_draw('uranus', 9, '#0E544D', 710, 400, 0, -2.6)
planet_draw('neptune', 8, '#0E3554', 400, 770, 2.34, 0)


# Initializes an infinite cycle with breaking point, which is closing
# the window. Each iteration calculates the new positoins of heavenly bodys.
while True:

    # Moves planets.
    for i in ('mercury', 'venus', 'mars', 'earth', 'jupiter', 'saturn',
              'uranus', 'neptune'):
        planet_move(i)

    # Sets a bit of delay for comfort watching.
    gr.time.sleep(0.035)

    # Breaks the cycle if the window is manually closed.
    if window.isClosed():
        break
