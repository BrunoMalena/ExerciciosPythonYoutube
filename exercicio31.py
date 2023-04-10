x = float(input('Digite quantos km tem a viagem: '))

y = x*0.50
z = x*0.45

if x <= 200:
    print(f'O valor da viagem é de {y} reais')
else:
    print(f'O valor da viagem é de {z} reais')