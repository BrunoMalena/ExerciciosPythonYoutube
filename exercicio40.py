nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) /2

if media < 3:
    print(f'A media do aluno foi {media} e está reprovado!')
elif media >= 3 and media <= 6:
    print(f'A media do aluno foi {media} e o aluno está de recuperação!')
else:
    print(f'A media do aluno foi {media} e o aluno esta aprovado!')
    