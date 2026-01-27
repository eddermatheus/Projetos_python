a = int(input(''))
b = int(input(''))
c = int(input(''))
#Verificando o menor número aqui embaixo:
if (b < c and b < a):
    print(f'O menor número é : {b}')
elif (c < b and c < a):
    print(f'O menor número é ; {c}')
else:
   print(f'O menor número é {a}')
 #Verificando o maior número aqui embaixo:  
if (b > c and b > a):
   print(f'O maior número é : {b}')
elif (c > b and c > a ):
   print(f'O maior número é: {c}')
else:
  print(f'O maior número é {a}')
  