n = int(input('Digite o numero para calcular o fatorial: '))
c = n
f = 1
print(f'Calculando {n}', end='')
while c > 0:
    print({c}, end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = c 
    c -= 1
print(f'{f}')
