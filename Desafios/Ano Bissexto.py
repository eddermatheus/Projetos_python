from datetime import datetime

Ano = int(input('Que ano quer analisar? Coloque 0 pra analisar o ano atual: '))
ano_atual = datetime.now().year

if Ano == 0: #Colocando 0 pra analisar o ano atual
    if ano_atual % 4 == 0:
        print('O ano atual é um ano bissexto')
    else:
        print('O ano atual não é bissexto')
else:
    if Ano % 4 == 0:
        print(f'O ano {Ano} é bissexto')
    else:
        print(f'O ano {Ano} não é bissexto')