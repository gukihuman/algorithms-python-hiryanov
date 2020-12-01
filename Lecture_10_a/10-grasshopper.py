def count_min_cost(N, price:list):
    C = [float('-inf'), price[1], price[1] + price[2] + [0] * (n-2)]
    for i in range(3, N+1):
        C[i] = price[i] + min(C[i-1], C[i-2])
    return C[N]