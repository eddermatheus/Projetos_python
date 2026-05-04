class Carro:
    def __init__(self, nome, cor, portas):
        self.nome = nome 
        self.cor = cor
        self.portas = portas
    def acelerar(self):
     acelerou = f"O carro {self.nome} está acelerado ! a 4km/h"
     return acelerou
# criando o objeto
carro1 = Carro("carro1","vermelho", 4)
print(f"O carro1 da cor {carro1.cor} e de {carro1.portas} portas")
print(carro1.acelerar())
