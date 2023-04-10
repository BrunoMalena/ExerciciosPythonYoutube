peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('Está abaixo do peso ideal!')
elif imc >= 18.5 and imc < 25:
    print('Está no peso ideal')
elif imc >= 25 and imc <30:
    print('Está em sobrepeso')
elif imc >= 30 and imc < 40:
    print('Está em obesidade')
else:
    print('Está em obesidade morbida')