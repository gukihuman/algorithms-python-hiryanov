def queens_move(start_x, start_y, stop_x, stop_y):
    """
    Finds the answer for the question: Is it possible for a queen to reach
    the second cell from the first by only one move. The queen moves by
    chess mate's terms. The cells are always different.

    :param start_x: starting x-coordinate from 1 to 8
    :param start_y: starting y-coordinate from 1 to 8
    :param stop_x: stop x-coordinate from 1 to 8
    :param stop_y: stop x-coordinate from 1 to 8
    :return: 'YES' if it's possible and 'NO' if it's not
    """

    # Returns YES if x-coordinate is the same for both cells.
    # It means that the both cells are on the same horizontal line.
    if start_x == stop_x:
        return 'YES'

    # Returns YES if y-coordinate is the same for both cells.
    # It means that the both cells are on the same vertical line.
    if start_y == stop_y:
        return 'YES'

    # Returns YES if the subtraction from the starting x-coordinate by
    # the stop x-coordinate is the same as the subtraction from the starting
    # y-coordinate by the stop y-coordinate. It means that the both cells
    # are on the same diagonal witch increasing by both coordinates.
    if start_x - stop_x == start_y - stop_y:
        return 'YES'

    # Returns YES if the subtraction from the starting x-coordinate by
    # the stop x-coordinate is the same as the subtraction from the stop
    # y-coordinate by the starting y-coordinate. It means that the both cells
    # are on the same diagonal witch increasing by x-coordinates and
    # decreasing by y-coordinates.
    if start_x - stop_x == stop_y - start_y:
        return 'YES'

    # Returns NO if every term is not true.
    return 'NO'


# Input format:
# 4 numbers. First and second are x and y coordinates for the starting cell.
# Third and fourth x and y coordinates for the stop cell.

# Output format:
# 'YES' or 'NO' for the possibility for a queen to reach the second cell
# from the first by only one move.

# Catches the coordinates from input.
start_x = int(input())
start_y = int(input())
stop_x = int(input())
stop_y = int(input())

# Uses the function to find if it is possible for a queen to reach
# the second cell from the first by only one move.
answer = queens_move(start_x, start_y, stop_x, stop_y)

# Print the answer.
print(answer)
