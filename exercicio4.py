a = input('Digite algo: ')
print('O seu tipo primitivo é: ', type(a))
print('é um número? ', a.isnumeric())
print('tem espaço? ', a.isspace())
print('é alphanumérico? ', a.isalpha())
print('qual tamanho da palavra? ', len(a))
print('está em maiuscula? ', a.isupper())
print('está em minuscula? ', a.islower())