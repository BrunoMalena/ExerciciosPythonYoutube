import random 

y = random.randint(0, 5)
x = int(input('Em que numero eu pensei? '))
if y == x:
    print('Parabens você acertou!!')
else:
    print(f'Errou! o numero era {y}')
