saque = int(input('Digite o valor do saque: '))

if saque < 2 or saque == 3:
    print('Valor inválido!')

cem = int(saque/100)
saque = saque % 100
    
cinquenta = int(saque/50)
saque = saque % 50

vinte = int(saque/20)
saque = saque % 20

dez = int(saque/10)
saque = saque % 10

cinco = int(saque/5)
saque = saque % 5

dois = int(saque/2)
saque = saque % 2

print(f'{cem} Nota(s) R$ 100,00.')
print(f'{cinquenta} Notas(s) R$ 50,00.')
print(f'{vinte} Notas(s) R$ 20,00.')
print(f'{dez} Notas(s) R$ 10,00.')
print(f'{cinco} Notas(s) R$ 5,00.')
print(f'{dois} Notas(s) R$ 2,00.')