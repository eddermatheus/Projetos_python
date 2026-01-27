import random
import time #importanto a função tempo
print('--==--'*20) #repete essa escrita 20x m                    vezes
print('Vou pensar num numero entre 0 e 5 tente advinhar...')
print('--==--' *20)
print('Em que número eu pensei')
numero = int(input(''))
print('Processando...')
time.sleep(2.5) #colocando um delay de 2.5 pra prosseguir
computador = random.randint(0,5) # o computador vai sortear um numero aleatório entre 0 e 5
if(numero == computador): # se o numero que eu entrei for igual a do computador , eu ganho
   print(f'parabéns você conseguiu me vencer') 
else:
   print(f'EU ganhei pois eu pensei no numero {computador} e não {numero}!') #caso não eu perco
  