from random import randint 
v = 0
while True:
    jogador = int(input('Digite um numero: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI' :
        tipo = str(input('Pár ou impár? (P / I): ')).strip().upper()
    print(f'Você jogou {jogador} e o computador jogou {computador}, o total é {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!!')
            v += 1
        else:
            print('Você perdeu!!')
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!!')
            v += 1
        else:
            print('Você perdeu!!')