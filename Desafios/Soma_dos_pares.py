s = 0 
cont  = 0
cont_N = 0
for c in range(1,7):
  n1 = int(input(f'Digite o {c} valor: '))
  cont_N= cont_N + 1 #conta todos os numeros ao total
  if n1%2 ==0:
    s = n1 + s # Soma todos os numeros
    cont= cont + 1 #Fonta quantos números pares teve
print(f'A soma dos  {cont} numeros pares: {s}\nTendo ao total {cont_N} numeros')

