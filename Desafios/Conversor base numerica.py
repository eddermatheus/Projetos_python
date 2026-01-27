numero = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão: \n [1] converter para BINÁRIO\n [2] converter para OCTAL\n [3] converter para HEXADECIMAL')
escolha = input('Escolha : ')
if escolha == '1' :
  print(f'\033[0;33m{numero} convertido em binário é igual {bin(numero)}\033[m') #converte pra binário
elif escolha  == '2':
  print(f'\033[0;34m{numero} convertido em octal igual {oct(numero)}\033[m]') #converte pra octal
elif escolha == '3':
    print(f'\033[0;35m{numero} convertido em hexadecimal é igual {hex(numero)}\033[m') #converte pra hexadecimal
else : 
 print('Opção invalida tente novamente')

