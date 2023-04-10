n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opção = 0 
while opção !=5:
    print(''' [1]Somar
        [2]Multiplicar
        [3]Maior
        [4]Novos numeros
        [5]Sair do programa''')
    opção = int(input('Qual a sua opção: '))
    if opção == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é {soma}')
    elif opção == 2:
        multiplicação = n1 * n2
        print(f'A multiplicação {n1} e {n2} é {multiplicação}')
    elif opção == 3:
        if n1 > n2:
            print(f'O maior é {n1}')
        elif n2 > n1:
            print(f'O maior é {n2}')
    elif opção == 4:
        print('Informe os numeros novamentes: ')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opção == 5:
        print('Finalizando ...')
    else:
        print('Invalid opção')
    

