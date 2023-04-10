x1 = float(input('Digite um segmento: '))
x2 = float(input('Digite um segmento: '))
x3 = float(input('Digite um segmento: '))

if x1<x2+x3 and x2<x1+x3 and x3<x1+x2: 
    print('É um triangulo')
else:
    print('Não é um triangulo')