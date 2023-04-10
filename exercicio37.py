numero = int(input('Digite um numero: '))

print('''Escolha: 
        1 - Binario
        2 - octal
        3 - hexadecimal''')
opção = int(input('Opção: '))

if opção ==1:
    print(f'A conversão é de {bin(numero)[2:]}')
elif opção ==2:
    print(f'A conversão é de {oct(numero)[2:]}')
elif opção==3:
    print(f'A conversão é de {hex(numero)[2:]}')
else:
    print('Nenhuma opção com este numero, tente novamente!')
