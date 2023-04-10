x1 = float(input('Digite um segmento: '))
x2 = float(input('Digite um segmento: '))
x3 = float(input('Digite um segmento: '))

if x1 == x2 or x1 == x3 or x2 == x3:   
    print('É um triangulo equilátero')
elif x1 == x2 or x1 == x3:
    print('É um triangulo isósceles')
else: 
    print('É um triangulo escaleno')