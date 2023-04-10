sexo = str(input('Informe o seu sexo:  [M/F]'))
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: [M/F]')).strip()
print(f'Sexo {sexo} regitrado com sucesso')