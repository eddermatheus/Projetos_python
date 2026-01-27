Distancia = float(input(''))
print('--==--'*8)
print(f'Você está prestes a começar a viagem')
print('--==--'*8)
if (Distancia <= 200): 
   Preço = 0.50 * Distancia
   print(f'Você está prestes a começar uma viagem de {Distancia}Km')
   print(f'E o preço da passagem será: R${Preço:.2f}')
else:
   Preço = 0.45 * Distancia
   print(f'Você está prestes a começar uma viagem de {Distancia}Km')
   print(f'E o preço da passagem será: R${Preço:.2f}')