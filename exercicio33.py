x = float(input('Digite um numero: '))
y = float(input('Digite um numero: '))
z = float(input('Digite um numero: '))

if x<y and x<z:
    print(f'O menor valor é {x}')
if y<x and y<z:
    print(f'O menor valor é {y}')
if z<x and z<y:
    print(f'O menor valor é {z}')