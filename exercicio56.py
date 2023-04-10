somaidade = 0
maioridadehomem = 0
mediaidade = 0
nomevelho = ''
totalmulheres20 = 0
for x in range(1, 5):
    nome = str(input(f'Digite o nome da pessoa {x}: '))
    idade = int(input(f'Qual a idade da {nome}?: '))
    sexo = str(input(f'Qual o sexo da {nome}? (M ou F): '))
    somaidade += idade
    if x == 0 and sexo in 'Mm':
        maioridadehomemp = idade 
        nomevelho = nome 
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade 
        nomevelho = nome
    if sexo in 'Ff' and idade < 20: 
        totalmulheres20 += 1
mediaidade = somaidade / 4
print(f'A média da idade do grupo é de {mediaidade}')
print(f'O homem mais velho tem {maioridadehomem} e se chama {nomevelho}')
print(f'Ao todo são {totalmulheres20} mulheres com menos de 20 anos')