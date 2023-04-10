frase = str(input('Digite uma frase: ')).lower()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palindromo!!!')
else:
    print('Não temos um palindromo!!')