from datetime import date
x = int(input('Digite o ano em que nasceu: '))
a = date.today().year
i = a - x


if x == i:
    print('Deverá se alistar imediatamente')
elif x > i:
    s = i - 18
    print(f'Deveria ter feito o alistamento em {s} ano')
else:
    s = 18 - i
    print(f'Irá se alistar em {s} ano')