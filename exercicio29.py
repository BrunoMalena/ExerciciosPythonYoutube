x = float(input('Qual velocidade? (km/h): '))
y = (x-80) *7    #a cada 1 km/h a mais será cobrado 7 reais
 
if x < 80:
    print('Não foi multado!!')
else:
    print(f'Você foi multado em R${y:.2f}!!')