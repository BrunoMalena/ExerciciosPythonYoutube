from random import randint

itens = ['Pedra', 'Papel', 'Tesoura']
computador = randint(1, 3)
print('''Escolha: 
        1 - Pedra
        2 - Papel
        3 - Tesoura''')
jogador = int(input('Opção: '))

print(f'O computador escolheu {computador}')
print(f'O jogador escolheu {jogador}')

if computador == 1:
    if jogador == 1:
        print('Deu empate')
    elif jogador == 2:
        print('Você ganhou')
    elif jogador == 3:
        print('Você perdeu')
    else:
        print('Não valeu')
if computador == 2:
    if jogador == 1:
        print('Você perdeu')
    elif jogador == 2:
        print('Deu empate')
    elif jogador == 3:
        print('Você ganhou')
    else:
        print('Não valeu')
if computador == 3:
    if jogador == 1:
        print('Você ganhou')
    elif jogador == 2:
        print('Você perdeu')
    elif jogador == 3:
        print('Deu empate')
    else:
        print('Não valeu')