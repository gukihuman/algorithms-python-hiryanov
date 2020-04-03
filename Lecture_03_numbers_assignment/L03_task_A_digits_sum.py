def digits_sum(number):
    """
    Finds the sum of every digit in a three-digit number.

    :param number: a three-digit number
    :return: the sum of every digit in the number
    """

    # Transforms the number from integer-type to string-type.
    number = str(number)

    # Adds every digit and returns the amount
    return int(number[0]) + int(number[1]) + int(number[2])