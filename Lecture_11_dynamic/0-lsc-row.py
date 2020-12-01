def lcs_row(A, B):
    """Returns the longest common subsequence in a row from two lists of numbers.
    Big O(A * B)."""

    # Creating table. T - Table.
    T = [[0] * (len(B) + 1) for i in range(len(A) + 1)]

    # Finding equality and rising previous by diagonal
    # or put 0 in the cell if numbers are not the same.
    # m - maximum length of the lcs in a row. c - coordinates.
    m = 0
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i-1] == B[j-1]:
                T[i][j] = 1 + T[i-1][j-1]
                if m < T[i][j]:
                    m = T[i][j]
                    c = i
            else:
                T[i][j] = 0

    # Creating the list for the longest common sequence in a row.
    L = []

    # Appending the numbers from the table to a final list.
    for k in range(m):
        L.append(A[(c - 1) - k])

    return L[::-1]

def test_1(func):
    print('Test 1:')
    A = [16, 11, 16, 19, 12, 7, 12, 3, 8, 8, 14, 3, 11, 14, 17, 3, 7, 7, 18, 5]
    B = [15, 6, 1, 0, 6, 11, 17, 3, 7, 18, 12, 6, 6, 13, 9, 9, 5, 8, 3, 10]
    print(A, B, lcs_row(A, B), sep='\n')
    print('OK' if lcs_row(A, B) == [17, 3, 7] else 'Fail')

# This is the way you can find sorted lcs in a row. You just need to
# use sorted version of the list as the second argument of the lsc-row function.
def test_2(func):
    print('Test 2:')
    A = [16, 11, 16, 19, 12, 7, 12, 3, 8, 9, 14, 3, 11, 14, 17, 3, 7, 7, 18, 5]
    B = sorted(A)
    print(A, B, lcs_row(A, B), sep='\n')
    print('OK' if lcs_row(A, B) == [8, 9] else 'Fail')

test_1(lcs_row)
test_2(lcs_row)