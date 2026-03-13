print("Gerador de PA")
print("-=-"*8)
primeiro  = int(input("Primeiro termo: "))
razão = int(input("Razão PA: "))
termo = primeiro 
cont = 1 
while cont<=10:
 print(f"{termo}")
 termo+=razão  #5 8 11 14
 cont+=1
print("fim")
