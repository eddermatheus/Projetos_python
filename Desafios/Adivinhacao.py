import random #importar a biblioteca random é essencial 
print('Sou seu computador...\nAcabei de pensar num numero de 0 a 10')
palpite = 1
cont = 0
computador = random.randint(0,10) #computador gera um numero aleatório de 1 a 10 
while palpite!=computador: #Verificar se meu palpite é igual ao que o computador pensou
 palpite  = int(input('Qual é seu palpite?'))
 if palpite < computador : #Caso meu palpite for menor que o computador pensou print isso
  print('Mais... Tente mais uma vez')
 else:                #caso ao contrário seria menos
  print("Menos... Tente mais uma vez")
 cont+=1         #Flag pra contar o quanto o while "rodou"
print(f'Acertou com {cont} tentativa .Parabéns!')