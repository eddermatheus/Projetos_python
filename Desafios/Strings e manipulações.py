nome =  input('')
nome_div = nome.split() #Ou ele divide uma string em partes, ou seja, pega separada por espaço = Edder Matheus 
# ele deixa ["Edder" , "Matheus"]>> ou seja transforma em uma "lista"
##nome_maiusculo = nome.upper()
print(f'seu nome em maisculo é {nome.upper()}') #nome todo maiusculo
print(f'seu nome em minusculo é {nome.lower()}') #nome toddo minusculo
print(f'tamanho do nome sem o espaço: {len(nome.strip())}') #quantidade do numero de nomes sem contar os espaços no começo e fim
print(f'tamanho do nome com espaços: {len(nome)}') #tamanho do nome com espaços
print(f'seu primeiro nome é : {nome_div[1]}')
print(f"o tamanho do primeiro nome é : {len(nome_div[0])}") #conta o primeiro nome