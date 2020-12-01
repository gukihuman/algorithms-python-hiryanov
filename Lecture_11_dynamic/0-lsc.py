def len_lcs(A, B):
    """Finding the length of longest common subsequence from two lists.
    Returns the hole table of comparisons. Big O(A * B)."""

    # Creating table.
    T = [[0] * (len(B) + 1) for i in range(len(A) + 1)]

    # Finding equality and rising previous by diagonal
    # or choose maximum number from top or bottom in the table.
    # T - Table.
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i-1] == B[j-1]:
                T[i][j] = 1 + T[i-1][j-1]
            else:
                T[i][j] = max(T[i-1][j], T[i][j-1])
    return T

def print_table():
    """Print the hole table of len_lsc"""
    for i in range(1, len(B) + 1):
        for j in range(1, len(A) + 1):
            print(lcs(A, B)[i][j], end='')
            print(' ', end='')
        print('')

def lcs(T, A):
    """Using the len_lcs table, returns the longest common subsequence.
    Big O(T**0.5 - A)."""

    # Creating the list for longest common sequence.
    L = []

    # Saving j-position.
    J = len(T[0]) - 1

    for i in range(len(T) - 1, 0, -1):
        for j in range(J, 0, -1):
            if T[i][j] == T[i][j-1]:
                continue
            elif T[i][j-1] != T[i-1][j]:
                J = j
                break
            else: # T[i][j-1] == T[i-1][j]
                J = j-1
                L.append(A[i-1])
                break
    return L[::-1]

A = [6, 7, 1, 2, 3, 8, 9]
B = [4, 2, 6, 1, 2, 3, 4]
T = len_lcs(A, B)

print(T[-1][-1])
print(lcs(T, A))