pt = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão : '))
decimo_termo = pt + (10 - 1)*razao
cont  = 0
for c in range (pt,decimo_termo + razao,razao):
    print(c,end=' -> ')
print('ACABOU')