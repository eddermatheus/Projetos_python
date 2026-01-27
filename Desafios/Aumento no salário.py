Salario = float(input('Digite seu salário: '))
if (Salario <= 1250):
  Aumento = (Salario * 15/100) + Salario 
  print(f'Quem ganhava R$ {Salario:.2f} passa a ganhar R$ {Aumento:.2f}')
else:
  Aumento = (Salario * 10/100) + Salario
  print(f'Quem ganhava R$ {Salario:.2f} passa a ganhar R$ {Aumento:.2f}')