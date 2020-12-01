def flag_cells(T, i, j, symbol='-'):
    """Flag all winnable cells from the input negative cell."""
    for k in range(j, 0, -1):
        T[i][k - 1] = symbol
    for k in range(i, 0, -1):
        T[k - 1][j] = symbol
    for k in range(1, min(i, j) + 1):
        T[i - k][j - k] = symbol

def queen(N, M):
    """Two players makes a move of the queen one by one. It allowed
    to move only straight horizontally, vertically or diagonally.
    Wins the player who reach bottom right cell. We need to find
    100% winnable starting position. Returns the table as a matrix
    with N-height and M-width, where we can see winnable positions.
    T - Table."""

    #Create table.
    T = [[None] * M for i in range(N)]
    winnable_symbol = '-'
    negative_symbol = 'O'

    # Find 'None' cells in the next line.
    # If found, flag winnable cells from it.
    # Use 'i' and 'j' for vertical and horizontal indexes.
    for k in range(N):
        i = N - 1 - k
        j = M - 1
        while T[i][j] and j >= 0:
            j -= 1
        if j != -1:
            T[i][j] = negative_symbol
            flag_cells(T, i, j, winnable_symbol)

    return T

N = 15
M = 25

for i in queen(N, M):
    print(*i, sep = '  ')