x = int(input('Digite um numero: '))

u = x // 1%10
d = x // 10%10
c = x // 100%10
m = x // 1000%10

print(f'Tem {u} unidades, {d} dezenas, {c} centenas e {m} milhar')