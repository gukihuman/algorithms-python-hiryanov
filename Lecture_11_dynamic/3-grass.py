def grasshopter(n, price):
    """Returns the minimal price of the way to k-position on a road
    if grasshopper is able to jump only on 1 or 2 steps per move.
    Starting from 1-st position."""
    C = [None] * (n + 1)
    C[0], C[1], C[2] = price[0], price[1], price[2]
    for i in range(3, n + 1):
        C[i] = min(C[i-2], C[i-1]) + price[i]
    return C[n]

n = 6
price = [0, 0, 3, 5, 7, 9, 11]
print(grasshopter(n, price)) # 21