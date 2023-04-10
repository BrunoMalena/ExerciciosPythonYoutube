import random
x1 = str(input('Digite o nome do primeiro aluno: '))
x2 = str(input('Digite o nome do segundo aluno: '))
x3 = str(input('Digite o nome do terceiro aluno: '))
x4 = str(input('Digite o nome do quarto aluno: '))

l = [x1, x2, x3, x4]
y = random.choice(l)    
print(f'O nome sorteado é {y}')