valor = int(input('Entre com um número para saber a tabuada: '))  
aux = 0   
print('Tabuada de {}'.format(valor))   
while(aux <= 10):  
  print('{0} X {1} = {2}'.format(aux, valor, (aux * valor)))  
  aux = aux + 1