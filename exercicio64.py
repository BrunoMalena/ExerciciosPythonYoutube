soma = 0
cont = 0
num = 0
num = int(input('Digite um numero (999 pra parar): '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um numero: '))
print(f'Você digitou {cont} e a soma deu {soma}')