import operator

def sort_by_two_elements(A):
    """Sorting a list where each element is a list with two parts.
    Main list is sorting by second part and then by first
    if second is the same."""
    A.sort(key=lambda x: (x[1], -x[0]))

n = int(input())
A = list()
for i in range(n):
    input_string = str(input())
    element = input_string.split()
    for k in range(len(element)):
        element[k] = float(element[k])
    A.append(element)
sort_by_two_elements(A)
for i in range(n):
    print('{0:.2f}'.format(A[i][0]), '{0:.3f}'.format(A[i][1]))