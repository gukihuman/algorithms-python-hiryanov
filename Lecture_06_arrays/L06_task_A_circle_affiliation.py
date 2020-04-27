import math


def circle_affiliation(coord_x, coord_y, radius):
    """
    There is a point and a circle with the center in coordinates origin.
    The coordinates of the point and the radius of the circle is known.
    Find an affiliation of the point to the circle. In other words, is
    the point inside the circle or not (perimeter included).

    :coord_x: "x" coordinate of a point
    :coord_y: "y" coordinate of a point
    :radius: a radius of a circle
    :return: a string 'YES' or 'NO'
    """

    # If an addition of coordinates at squares is lesser then a radius in
    # square, returns 'YES'. It's the Pythagoras theorem.
    if math.fabs((coord_x ** 2) + (coord_y ** 2)) < math.fabs(radius ** 2):
        return 'YES'

        # Else returns 'NO'.
    return 'NO'
