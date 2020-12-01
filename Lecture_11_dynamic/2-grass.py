def grasshopper(k):
    """Returns the amount of ways to k-position on a road
    if grasshopper is able to jump only on 1, 2 or 3 steps per move."""
    if k <= 1:
        return None
    road = [None] * (k - 1)
    road[0], road[1] = 1, 2
    for i in range(2, k - 1):
        if (i + 2) % 3 == 0:
            road[i] = road[((i + 2) // 3) - 2] + road[i-2] + road[i-1]
        else:
            road[i] = road[i-2] + road[i-1]
    return road[k - 2]

print(grasshopper(9)) #39