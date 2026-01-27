from datetime import datetime

# Solicita ao usuário um ano para análise
# Se digitar 0, analisa o ano atual
ano = int(input('Que ano quer analisar? Coloque 0 pra analisar o ano atual: '))
ano_atual = datetime.now().year

# Se o usuário digitou 0, usa o ano atual
if ano == 0:
    ano = ano_atual

# Verifica se o ano é bissexto usando a regra correta:
# - Divisível por 4 E não divisível por 100, OU
# - Divisível por 400
eh_bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

# Exibe o resultado
if eh_bissexto:
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto')