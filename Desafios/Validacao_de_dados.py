sexo = input("Digite seu sexo: ")
nome = ''
while sexo !='M' and sexo != 'F':
 sexo = input('Dados inválidos. Por favor, informe seu sexo: ').upper()
if sexo == 'F':
  nome = 'Feminino'
else:
   nome = 'Masculino'
print(f'Sexo {nome} Registrado com sucesso ! ')

 