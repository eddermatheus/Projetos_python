# Aqui inicia aprendizagem ultilizando while 
import time
par = impar = 0
n = 1
while n!= 0:
    n= int(input('Digite um valor: '))
    if n != 0:
     if n % 2 == 0 : 
      par+=1
     else:
      impar+=1
time.sleep(0.5)
print(f'Você digitou {par} numeros pares e digitou {impar} impares')