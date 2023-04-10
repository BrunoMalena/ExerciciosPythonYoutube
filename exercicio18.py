import math

x = int(input('Digite o ângulo desejado: '))
s = math.sin(math.radians(x))
c = math.cos(math.radians(x))
t = math.tan(math.radians(x))
print(f'O seno é {s:.2f}, o cosseno é {c:.2f} e a tangente é {t:.2f}')