from datetime import date
ano_atual = date.today().year
cont_M = 0
cont_N = 0 
for c in range (1,8):
 ano = int(input(f'Em que ano a {c}º pessoa nasceu : '))
 idade = ano_atual - ano
 if idade>=18:
  cont_M+= 1
  
 else:
  cont_N+= 1 

print(f'Ao todo tivemos {cont_M} pessoas maiores de idade ')
print(f'E também tivemos {cont_N} pessoas menores de idade')
