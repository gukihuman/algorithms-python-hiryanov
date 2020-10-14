"""
There is a point and a circle. The coordinates of the point and
the radius of the circle are known. The center of the circle is
the origin of the coordinates' system. Find an affiliation of the point
to the circle. In other words, is the point inside the circle or not
(perimeter included).

Input format:
A string with three digits and space between them.
The first digit is the "x" coordinate of the point.
The second digit is the "y" coordinate of the point.
The third digit is the radius.

Output format:
A string. 'YES' or 'NO' for an affiliation of a point.

An example of input:
-4 4 5

An example of output:
NO
"""


def circle_affiliation(coord_x, coord_y, radius):
    """
    Finds an affiliation of a point to a circle. In other words,
    is the point inside the circle or not (perimeter included).
    The coordinates of the point and the radius of the circle are known.
    The center of the circle is the origin of the coordinates' system.

    :coord_x: "x" coordinate of a point
    :coord_y: "y" coordinate of a point
    :radius: a radius of a circle
    :return: a string 'YES' or 'NO'
    """

    # If an addition of coordinates at squares is lesser then a radius in
    # square, returns 'YES'. It's the Pythagoras theorem.
    if coord_x ** 2 + coord_y ** 2 < radius ** 2:
        return 'YES'

    # Else returns 'NO'.
    return 'NO'


# Executes only if runs as a script.
if __name__ == '__main__':

    # Catches the values from input.
    input_string = str(input()).split()
    coord_x = int(input_string[0])
    coord_y = int(input_string[1])
    radius = int(input_string[2])

    # Uses the function to find if a point belongs to a circle or not.
    answer = circle_affiliation(coord_x, coord_y, radius)

    # Print the answer.
    print(answer)
