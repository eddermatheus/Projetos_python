import time
lugares_vagos = [10,2,1,3,0]
salas=[1,2,3,4,5]
x = 0
while True:
 numero_sala = int(input("Qual nummero da sala? "))
 quant_lugar = int(input("Quantidade de lugar? "))
 if numero_sala == 0: #condição sair do lop
  break
 indice = numero_sala - 1 #indice da sala exemplo se for 1 seria: 1 - 1 = 0 indice 0  que é 10 lugares [10]
 if quant_lugar<= lugares_vagos[indice]: #verifica a quantidade de lugar se é menor ou igual ao lugares_vagos os indices
  lugares_vagos[indice]-= quant_lugar #subtrai os lugares vagos da quantidade de lugar que eu solicitei
  print("-=-=-="*8)
  time.sleep(0.5)
  print("Lugares vendidos com sucesso")
  print(f"Restam agora {lugares_vagos[indice]}")
  print("-=-=-="*8)
 else:
  print("-=-=-="*8)
  time.sleep(0.5)
  print("Não há lugares suficientes")
  print("-=-=-="*8)   