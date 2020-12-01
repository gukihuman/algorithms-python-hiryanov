def dot_product(N, v1, v2):
    """Return the dot product of two vectors in N sizes."""
    amount = 0
    for i in range(N):
        amount += v1[i] * v2[i]
    return amount