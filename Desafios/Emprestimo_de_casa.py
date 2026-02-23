import time
Valor_da_casa = float(input('Qual é o valor da casa: '))
Salario  = float(input('Qual o seu Salário?: '))
Anos = int(input('Quantos anos de financiamento?: '))
numero_meses = Anos * 12
Prestacao_mensal = Valor_da_casa / numero_meses
Salario_percentual = Salario * 30/100
if (Salario_percentual <= Prestacao_mensal):
    print(f'Para pegar uma casa de R${Valor_da_casa:.2f} em {Anos} a prestação será R${Prestacao_mensal:.2f}')
    print('Em analise...')
    time.sleep(1)  #timme de delay
    print('EMPRESTIMO NEGADO!')

else : 
  print(f'Para pegar uma casa de R${Valor_da_casa:.2f} em {Anos} a prestação será R${Prestacao_mensal:.2f}')
  print('Em analise...')
  time.sleep(1)
  print('EMPRESTIMO CONCEDIDO !')

