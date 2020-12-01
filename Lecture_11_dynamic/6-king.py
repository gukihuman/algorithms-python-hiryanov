def king(N, M):
    """Two players makes a move of the king one by one. It allowed
    to move only on a cell horizontally, vertically or diagonally.
    Wins the player who reach bottom right cell. We need to find
    100% winnable starting position. Returns the table as a matrix
    with N-height and M-width, where we can see winnable positions.
    T - Table."""

    #Create table.
    T = [[None] * M for i in range(N)]
    winnable_symbol = '-'
    negative_symbol = 'O'

    # Find 'None' cells in the line.
    # If found, flag winnable cells from it.
    # Use 'i' and 'j' for vertical and horizontal indexes.
    for i in range(N - 1, -1, -1):
        for j in range(M - 1, -1, -1):
            if not T[i][j] and j != 0 and i != 0:
                T[i][j] = negative_symbol
                T[i][j - 1] = winnable_symbol
                T[i - 1][j] = winnable_symbol
                T[i - 1][j - 1] = winnable_symbol

            # Border cases.
            elif not T[i][j] and j != 0 and i == 0:
                T[i][j] = negative_symbol
                T[i][j - 1] = winnable_symbol
            elif not T[i][j] and i != 0: # j == 0
                T[i][j] = negative_symbol
                T[i - 1][j] = winnable_symbol

            # Last cell case.
            elif not T[i][j]: # i == 0 and  j == 0
                T[i][j] = negative_symbol

    return T

N = 13
M = 11

for i in king(N, M):
    print(*i, sep = '  ')