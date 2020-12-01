def grasshopper(k):
    """Returns the amount of ways to k-position on a road
    if grasshopper is able to jump only on 1, 2 or 3 steps per move."""
    road = [None] * (k + 2)
    road[0], road[1], road[2] = 0, 0, 1
    for i in range(3, k + 2):
        road[i] = road[i-3] + road[i-2] + road[i-1]
    return road[k + 1]
k = 6
print(grasshopper(k))