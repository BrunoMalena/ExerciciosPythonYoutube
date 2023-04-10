from datetime import date
a = date.today().year
tmaior = 0
tmenor = 0
for c in range(1, 8):
    n = int(input(f'Em que ano a {c} pessoa nasceu?: '))
    i = a - n
    if i >= 18:
        tmaior += 1
    else:
        tmenor += 1
print(f'Ao todo temos {tmaior} pessoas maiores de idade')
print(f'Ao todo temos {tmenor} pessoas menores de idade')