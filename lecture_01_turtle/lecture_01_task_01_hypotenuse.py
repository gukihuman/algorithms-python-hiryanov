def hypotenuse(a, b):
    """
    Finds a hypotenuse from two other sides (legs) of a triangle
    using Pythagorean theorem.

    :param a: length of the first leg
    :param b: length of the second leg
    :return: length of the hypotenuse
    """
    c = (a ** 2 + b ** 2) ** 0.5

    return c