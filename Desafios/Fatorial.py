from math import factorial #importando a biblioteca pra fazer fatorial
n = int(input('Digite um número que você deseja obter fatorial: '))
f = factorial(n)
c=n
while c>0:
 print(f'{c} x {n} = {f}')
 c-=1
print(f'O fatorial de {n} é {f}')