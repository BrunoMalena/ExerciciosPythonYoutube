cont = 1
pos = 1
times = ('Corinthians', 'Palmeiras', 'Santos', 'Gremio', 'Cruzeiro',
          'Flamengo', 'Vasco', 'Chapecoense', 'Atletico', 'Botafogo',
          'Atletico-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sporte Recife',
          'EC Vitoria', 'Coritiba', 'Avai', 'Ponte Preta', 'Atletico-GO')
print(f'Lista de times do Brasileirão: {times}')
print('-*-'*15)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-*-'*15)
print(f'Os 4 últimos são: {times [-4:]}')
print('-*-'*15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-*-'*15)
print(f'O Chapecoense está na {times.index("Chapecoense")+1} posição')