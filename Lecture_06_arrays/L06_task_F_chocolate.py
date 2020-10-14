"""
There is a chocolate with 3-framed width. The height of the chocolate is
getting from input. The height must be a positive even integer number.
The chocolate is divided on parts. Each part is 2-framed. Find how many
ways there is to divide the chocolate. Symmetrical ways counts as different.
If the height is not a positive even integer number, return 0.

There is an image next to this file. The image explains the dividing ways.

Input format:
A positive even integer number. The height of the chocolate.

Output format:
An integer number. The amount of dividing ways or 0.

An example of input:
6

An example of output:
41
"""


def chocolate(height):
    """
    Counting the ways of dividing a chocolate with 3-framed width and
    dynamic height. Divided parts are 2-framed. Symmetrical ways counts as
    different. The height must be a positive even integer number. If it's not,
    return 0.

    :param height: an integer number, the height of the chocolate
    :return: an integer number, the amount of dividing ways or 0
    """

    # Check the height. If it's not a positive even integer number, return 0.
    if height % 2 != 0 or height <= 0:
        return 0

    # It's going to be a cycle, where the hight grows from the 2 to
    # 4, 6, 8, 10 etc. Sets a value of all previous ways' amounts,
    # except the last one and the one before the last.
    all_previous = 0

    # Sets a value of the ways' amount before the last. 0 is subsidiary value
    # for the start of the cycle.
    before_last = 0

    # Sets a value of the last ways' amount. 1 is subsidiary value for
    # the start of the cycle.
    last = 1

    # Sets a value of the current ways' amount.
    current = 0

    # Starts the cycle, where the hight grows from the 2 to 4, 6, 8, 10 etc.,
    # while the hight is not the one from the input.
    for i in range(height//2):

        # Calculate the current ways' amount.
        current = last * 3 + before_last * 2 + all_previous

        # Add the part with the way's amount before the last to the memory
        # of all previous ways' amount.
        all_previous += before_last * 2

        # Switches the last and before the last values.
        before_last = last
        last = current

    # Return the final current value of the ways' amount of dividing
    # the cocolate with the hight from the input.
    return current


# Executes only if runs as a script.
if __name__ == '__main__':

    # Cathes height from the input.
    height = int(input())

    # Calculates the amount of ways there is to divide the chocolate with
    # the height from the input.
    ways_amount = chocolate(height)

    # Prints the answer.
    print(ways_amount)
