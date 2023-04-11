primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro 
cont = 1
total = 0
mais = 10 
while mais != 0:
    total = mais + total
while cont <= total:
    print(f'{termo}', end = ' - ')
    termo += razão 
    cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais?: '))
print(f'a PA acabou e foram mostrados {total} termos')

           