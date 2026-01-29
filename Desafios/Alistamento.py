ano = int(input('Ano de nascimento: '))
idade = 2026 - ano
Resta = 18 - idade
ano_de_alistamento = ano + 18
if (idade < 18):
 print(f'Ainda faltam {Resta} anos para o alistamento') 
 print(f'Seu alistamento será em {ano_de_alistamento}.')
elif (idade > 18):
 diferenca = idade  - 18 
 print(f'Quem nasceu em {ano} tem {idade} em 2026')
 print(f'Você deveria se alistado há {diferenca} anos e seu alistamento foi em {ano_de_alistamento}. ')
else :
 print(f'Você nasceu em {ano} tem {idade} anos em {ano_de_alistamento}')
 print('Você tem que se alistar IMEDIATAMENTE!')


