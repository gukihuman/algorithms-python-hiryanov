def reverse_word(A):
    """Takes a list of words <= 15 symbols. Returns a list where
    each item contains three subitems. First item is the same as in
    input list. Second is a reversed word from the first. Third is
    the length of the word."""
    for i in range(len(A)):
        A[i] = [A[i], A[i][::-1], len(A[i])]

def comp_sort(A):
    """Takes a list where each item contains three subitems.
    Sorting the list by third item at first. Then by second."""
    A.sort(key=lambda x: (x[2], x[1]))

# Create a list from input
N = int(input())
A = list()
for i in range(N):
    A.append(str(input()))

# Transform the list
reverse_word(A)
comp_sort(A)

# Print by groups where groups contains items with the same length
print(A[0][2])
print(A[0][1], A[0][0])
for i in range(1, N):
    if A[i][2] != A[i - 1][2]:
        print(A[i][2])
    print(A[i][1], A[i][0])