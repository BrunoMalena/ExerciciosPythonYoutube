tot18 = totH = totM20 = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        tot18 +=1 
    if sexo == 'M':
        totH +=1 
    if sexo == 'F' and idade < 20: 
        totM20 +=1 
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? (S/N): ')).strip().upper()
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos é de {tot18}')
print(f'Total de homens cadastrados  é {totH}')
print(f'Total de mulheres com menos de 20 anos é{totM20}')