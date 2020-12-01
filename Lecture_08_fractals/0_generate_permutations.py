def find(number, A):
    """Find number in A and return True if number is found and False if it's not"""
    flag = False
    for x in A:
        if number == x:
            flag = True
            break
    return flag

def generate_purmutations(N:int, M:int=-1, prefix=None):
    """Generate all the permutations of N numbers in M positions."""
    M = N if M == -1 else M # default is N numbers in N positions
    prefix = prefix or []
    if M == 0:
        print(*prefix)
        return
    for number in range(1, N+1):
        if find(number, prefix):
            continue
        prefix.append(number)
        generate_purmutations(N, M-1, prefix)
        prefix.pop()

generate_purmutations(3)