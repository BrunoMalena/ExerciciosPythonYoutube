import math

x = float(input('Digite o cateto oposto: '))
y = float(input('Digite o cateto adjacente'))
h = math.hypot(x, y)
print(f'O valor da hipotenusa é {h:.2f}')