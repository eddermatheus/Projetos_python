
tabuada = int(input('Tabuada de que número? : '))
print(f'A tabuada do {tabuada} abaixo: ')
for c in range (1,11): #o final é 11 pois é sempre o final n - 1 , sendo n um numero inteiro
  resultado= tabuada * c
  print(resultado, end = ' ') #imprimir tudo ao lado do outro com espaço

