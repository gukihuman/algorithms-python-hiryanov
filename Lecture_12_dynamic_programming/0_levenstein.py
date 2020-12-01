def levenstein(A, B):
    T = ([[i + j if i * j == 0 else 0 for j in range(len(B) + 1)]
        for i in range(len(A) + 1)])
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                T[i][j] = T[i - 1][j - 1]
            else:
                T[i][j] = 1 + min(T[i - 1][j], T[i][j - 1], T[i - 1][j - 1])
    LA = [] # List of A-changes
    LB = [] # List of B-changes
    while i >= 0 and j >= 0:
        if T[i][j - 1] < T[i][j]:
            LA.append(['add', B[j - 1], 'after', i])
            LB.append(['delete', B[j - 1], 'after', j - 1])
            j -= 1
        elif T[i - 1][j] < T[i][j]:
            LA.append(['delete', A[i - 1], 'after', i - 1])
            LB.append(['add', A[i - 1], 'after', j])
            i -= 1
        elif T[i - 1][j - 1] < T[i][j]:
            LA.append(['change to', B[j - 1], 'in', i])
            LB.append(['change to', A[i - 1], 'in', j])
            i, j = i - 1, j - 1
        else:
            i, j = i - 1, j - 1

    LA, LB = LA[::-1], LB[::-1]

    for i in range(len(LA)):
        if LA[i][0] is 'add':
            for k in LA[i + 1:]:
                k[3] = int(k[3]) + 1
    for i in range(len(LB)):
        if LB[i][0] is 'add':
            for k in LB[i + 1:]:
                k[3] = int(k[3]) + 1

    for i in range(len(LA)):
        if LA[i][0] is 'delete':
            for k in LA[i + 1:]:
                k[3] = int(k[3]) - 1
    for i in range(len(LB)):
        if LB[i][0] is 'delete':
            for k in LB[i + 1:]:
                k[3] = int(k[3]) - 1


    return LA, LB

A = 'gfohgdsaohksfb;lsflgf;lk'
B = 'dsflkngda;ljkdl;jksd;lhk'

LA, LB = levenstein(A, B)

print('A:')
for i in range(len(LA)):
    print(*LA[i], end='')
    print('')

print('B:')
for i in range(len(LB)):
    print(*LB[i], end='')
    print('')