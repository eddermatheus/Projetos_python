import random #importação da biblioteca random
n1 = str(input(''))
n2 = str(input(''))
n3 = str(input(''))
n4 = str(input(''))
lista=[n1,n2,n3,n4] #lista em python
escolhido = random.choice(lista) #escolhendo alguem da lista
print(f'o aluno sorteado foi {escolhido}')