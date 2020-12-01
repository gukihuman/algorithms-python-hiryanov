def mark_cells(T, n, i, j, m=0):
    if m >= n:
        return

    # C - coordinates [i, j]
    for C in [[i-1, j+2], [i-1, j-2], [i-2, j+1], [i-2, j-1],
              [i+1, j+2], [i+1, j-2], [i+2, j+1], [i+2, j-1]]:
        if 0 <= C[0] < 8 and 0 <= C[1] < 8:
            if T[C[0]][C[1]] > m + 1 or T[C[0]][C[1]] is -1:
                T[C[0]][C[1]] = m + 1
            mark_cells(T, n, C[0], C[1], m + 1)
    return T

def find_moves(i, j):
    T = [[-1] * 8 for k in range(8)]
    return mark_cells(T, 2, i, j)

def print_table(func, i, j):
    for k in range(8):
        print(*func(i, j)[k], end='')
        print('')

i = int(input())
j = int(input())
I = int(input())
J = int(input())

T = find_moves(i-1, j-1)

T[i-1][j-1] = 0

print(T[I-1][J-1])