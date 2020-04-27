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

# Input format:
# A string with three digits and space between them. A first digit is
# a "x" coordinate of a point. A second digit is a "y" coordinate of a point.
# A third digit is a radius.

# Output format:
# 'YES' or 'NO' for an affiliation of a point.


# Catches the values from input.
input_string = str(input()).split()
coord_x = int(input_string[0])
coord_y = int(input_string[1])
radius = int(input_string[2])

# Uses the function to find if a point belongs to a circle or not.
answer = circle_affiliation(coord_x, coord_y, radius)

# Print the answer.
print(answer)
