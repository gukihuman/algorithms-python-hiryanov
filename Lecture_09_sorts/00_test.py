x = int('0f', 16)
y = int('f0', 16)
c = x ^ y
#x = f'{x:08b}'
#y = f'{y:08b}'
c = hex(c)

print(c)
