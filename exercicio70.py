total = tmil = pbarato = cont = 0
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço do produto: '))
    total += preço
    cont += 1
    if tmil > 1000:
        tmil += 1
    if cont == 1:
        pbarato = preço
    elif preço < pbarato:
        pbarato = preço
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
        
print(f'O total foi de R${total:.2f}')
print(f'Temos {tmil} produtos maiores que R$1000.00')
print(f'O produto mais barato custa R${pbarato:.2f}')