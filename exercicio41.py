from datetime import date 

a = date.today().year
d = int(input('Digite o ano de nascimento: '))
i = a - d

if i <= 9:
    print(f'Como tem {i} está na categoria mirim')
elif i > 9 and i <=14:
    print(f'Como tem {i} está na categoria infantil')
elif i > 14 and i <= 19:
    print(f'Como tem {i} está na categoria junior')
elif i > 19 and i <= 25:
    print(f'Como tem {i} está na categoria senior')
else:
    print(f'Como tem {i} está na categoria master')
