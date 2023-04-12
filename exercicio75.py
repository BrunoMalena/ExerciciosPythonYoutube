numeros = int(input('Digite um número: ')), \
          int(input('Digite mais um número: ')),\
          int(input('Mais um: ')),\
          int(input('E o ultimo: '))
print(f'Voce digitou os valores: {numeros}.')
print(f'O numero 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O número 3 aparece a primeira vez na posição {numeros.index(3)+1}')
else:
    print('O valor 3 não foi digitado nenhuma vez.')
print('Os números pares digitados foram:',end='')
for n in numeros:
    if n % 2 == 0:
        print(n,end=' ')