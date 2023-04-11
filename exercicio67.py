while True:
    n = int(input('Digite um número para saber a tabuada: '))
    if n < 0 :
        break
    for c in range(1, 11):
        print(f'{n} * {c} = {n*c}')