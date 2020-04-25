"""
Runs a casual model of solar system.

Most of the functions in graphics module are easy to understand.
They creates objects, changes parameters and draws objects.
"gr.Point" is a point with two parameters: "x" and "y" coordinates.
The coordinates starts from upper left corner to lower right corner.
"""

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


# Opens a window with 800 length and 800 width with the name.
window = gr.GraphWin("Model", 800, 800)

# Draws a rectangle of space by diagonal-opposite points.
space = gr.Rectangle(gr.Point(0, 0), gr.Point(800, 800))
space.setFill('black')
space.draw(window)

# Sets coordinatinos of Sun and draws it.
sun_coords = gr.Point(400, 400)
sun = gr.Circle(sun_coords, 50)
sun.setFill('yellow')
sun.draw(window)

# Sets coordinatinos of Venus and draws it.
# Also sets it's starting velocity and acceleration.
venus_coords = gr.Point(500, 400)
venus = gr.Circle(venus_coords, 10)
venus.setFill('yellow')
venus.draw(window)
venus_velocity = gr.Point(0, -4.75)
venus_acceleration = gr.Point(-0.5, -0.5)

# Sets coordinatinos of Earth and draws it.
# Also sets it's starting velocity and acceleration.
earth_coords = gr.Point(670, 400)
earth = gr.Circle(earth_coords, 15)
earth.setFill('blue')
earth.draw(window)
earth_velocity = gr.Point(0, -2.75)
earth_acceleration = gr.Point(0, 0)

# Sets coordinatinos of Mars and draws it.
# Also sets it's starting velocity and acceleration.
mars_coords = gr.Point(550, 400)
mars = gr.Circle(mars_coords, 8)
mars.setFill('red')
mars.draw(window)
mars_velocity = gr.Point(0, -4.05)
mars_acceleration = gr.Point(0, 0)

# Initializes an infinite cycle with breaking point, which is closing
# the window. Each iteration calculates the new positoins of heavenly bodys.
while True:

    # Moves objects by their velocity.
    venus.move(venus_velocity.x, venus_velocity.y)
    earth.move(earth_velocity.x, earth_velocity.y)
    mars.move(mars_velocity.x, mars_velocity.y)

    # Updates acceleration by current coordinations and sun coordinations.
    venus_acceleration = update_acceleration(venus_coords, sun_coords)
    earth_acceleration = update_acceleration(earth_coords, sun_coords)
    mars_acceleration = update_acceleration(mars_coords, sun_coords)

    # Updates velocity by addition of current velocity and acceleration.
    venus_velocity = add(venus_velocity, venus_acceleration)
    earth_velocity = add(earth_velocity, earth_acceleration)
    mars_velocity = add(mars_velocity, mars_acceleration)

    # Updates coordinates by addition of current coordinations and velocity.
    venus_coords = add(venus_coords, venus_velocity)
    earth_coords = add(earth_coords, earth_velocity)
    mars_coords = add(mars_coords, mars_velocity)

    # Sets a bit of delay for comfort watching.
    gr.time.sleep(0.02)

    # Breaks the cycle if the window is manually closed.
    if window.isClosed():
        break
