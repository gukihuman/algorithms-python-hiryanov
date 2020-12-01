def gen_bin(M, prefix=''):
    if M == 0:
        print(prefix)
    else:
        gen_bin(M-1, prefix+'0')
        gen_bin(M-1, prefix+'1')

def generate_numbers(N:int, M:int, prefix=None):
    """Generate all the numbers in N-system where N <= 10"""
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_numbers(N, M-1, prefix)
        prefix.pop()

#gen_bin(5)

generate_numbers(10, 7)