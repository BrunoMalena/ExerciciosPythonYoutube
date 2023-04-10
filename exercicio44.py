valor = float(input('Digite o valor da compra: '))

print('''Escolha: 
        1 - A vista no pix
        2 - A vista no cartão
        3 - em até 2x no cartão
        4 - 3x ou mais no cartão''')
opção = int(input('Opção: '))

if opção ==1:
    p = valor - (valor * 10/100)
    print(f'O valor final é de {p}')
elif opção ==2:
    c1 = valor - (valor * 5/100)
    print(f'O valor final é de {c1}')
elif opção==3:
    c2 = valor / 2
    print(f'O valor final é de {valor} e as parcelas serão de {c2} ')
elif opção==4:
    p1 = int(input('Quantas parcelas serão? : '))
    c2 = valor + (valor * 20/100)
    p2 = c2 / p1
    print(f'O valor final é de {c2} e as parcelas serão de {p2}')  
else:
    print('Nenhuma opção com este numero, tente novamente!')