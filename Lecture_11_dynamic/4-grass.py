def grasshopter(n, prices):
    """Returns the minimal price of the way to n-position on a road
    if grasshopper is able to jump only on 1 or 2 steps per move.
    Also returns the hole path of minimal price with every position in it.
    Starting from 1-st position. n > 1. Prices starts from 2-nd position."""

    # Check the correctness of n.
    if n <= 1:
        return None

    # Finding minimal summary price for each position to achieve.
    S = [None] * (n + 1)
    S[0], S[1] = float('inf'), 0
    for i in range(2, n + 1):
        S[i] = min(S[i - 2], S[i - 1]) + prices[i - 2]

    # Finding the path to n-position with minimal summary price. Backwards.
    i = n
    path = [n]
    while i > 1:
        if S[i - 1] < S[i - 2]:
            path.append(i - 1)
            i -= 1
        else:
            path.append(i - 2)
            i -= 2

    # Returning the minimal price for n-position and the path to it.
    return [S[n], path[::-1]]

n = 6
prices = [3, 5, 7, 9, 11]
print(grasshopter(n, prices)) # 21