resp = 'S'
soma = cont = media = maior =  0 
while resp in 'Ss' :
        num = int(input('Digite um numero: '))
        soma += num
        cont += 1
        if cont == 1:
            maior = menor = num
        else:
            if num > maior:
                maior = num
            if num < menor:
                menor = num
        resp = str(input('Quer continuar? (s/n): '))
media = soma / cont
print(f'A média é de {media} e o maior numero é {maior}')