x = float(input('Digite o salário em R$: '))

if x<1250:
    a = x + (x * 15/100)
    print(f'O novo salario é {a}')
else:
    b = x + (x * 10/100)
    print(f'O novo salario é {b}')