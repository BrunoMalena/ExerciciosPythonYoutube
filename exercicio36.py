x1 = float(input('Digite o valor da casa em R$: '))
x2 = float(input('Digite do seu salário em R$: '))
x3 = float(input('Digite em quantos anos irá financiar: '))
parcelas = x1 / (x3*12)
minimo = x2 * 30/100

if parcelas<=minimo:
    print(f'O emprestimo foi aceito, as parcelas iriam ficar {parcelas:.2f}')
else:
    print(f'O emprestimo foi negado, as parcelas vão ser de {parcelas:.2f}')