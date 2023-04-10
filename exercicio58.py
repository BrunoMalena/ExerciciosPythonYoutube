from random import randint 

y = randint(0, 10)
acertou = False 
palpites = 0 
while not acertou:
    x = int(input('Em que numero eu pensei? '))
    palpites += 1
    if x == y:
        acertou = True
    else:
        if x < y:
            print('Mais ... Tente mais uma vez')
        elif x > y:
            print('Menos ... Tente mais uma vez')
print(f'Acertou em {palpites} tentativas!!')
        