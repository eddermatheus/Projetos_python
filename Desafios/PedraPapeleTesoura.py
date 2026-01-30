import time
import random
print('Suas opções:\n[0] PEDRA\n[1] PAPEL\n[2] TESOURA')
itens = ['PEDRA', 'PAPEL', 'TESOURA']
opções = int(input('Qual sua jogada?'))
computador = random.randint(0,2)
if (computador == 2) and (opções== 1):
    Vencedor = 'COMPUTADOR VENCE'
elif (computador == 0) and (opções == 1):
    Vencedor = 'JOGADOR VENCE'
elif computador == 1 and opções == 2:
    Vencedor = 'JOGADOR VENCE'
elif computador == 0 and opções  == 2:
   Vencedor = 'COMPUTADOR VENCE'
elif computador == 2 and opções == 0:
   Vencedor = 'JOGADOR VENCE'
elif computador==opções:
    Vencedor = 'EMPATE'
else:
    print('JOGADA INVÁLIDA!')
    exit()

print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('POW')
print('-='*12)
print(f'Computador jogou {itens[computador]}\nJogador jogou {itens[opções]}')
print('-='*12)
print(Vencedor)
   
