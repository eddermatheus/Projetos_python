import time
# A criação de uma classe chamada "ContaBancaria"
class ContaBancaria:
  def __init__(self,nomeCliente):
    self._saldo = 0
    self.nomeCliente = nomeCliente
  @property
  def saldo(self):
    return self._saldo
  @saldo.setter
  def saldo(self,valor):
    if valor >= 0:
      self._saldo = valor
  
  def consultar_saldo(self):
     return self._saldo

  def sacar(self,valor):
    if (valor > 0 and valor <= self._saldo):
      self._saldo-= valor
    else:
      print(f"Não é possível sacar!")
  
  def depositar(self,valor):
    if valor > 0:
     self._saldo += valor
    else:
      print(f"Valor inválido!")
   
class ContaCorrente(ContaBancaria):
  def __init__ (self,nomeCliente,chavepix):
    super().__init__(nomeCliente)
    self.chavepix = chavepix

  def pagar_pix(self,destino,valor):
   if destino in contas:
      destino = contas[destino]

      if (valor > 0 and self._saldo >= valor ):
       self.sacar(valor)
       destino.receber_pix(valor)
      else:
       print("Saldo insuficiente!")
   else:
      print("Chave Pix não encontrada !")

  def receber_pix(self,valor):
    if valor > 0:
     self.depositar(valor)
    else:
     print(f"Valor inválido!")
contas = {}
#Registro de contas um mini banco de dados:
conta1 = ContaCorrente("Edder", "4627262")
conta2 = ContaCorrente("Asdrubal", "381912823")

#Registrando no sistema do mini banco de dados
contas["4627262"] = conta1
contas["381912823"] = conta2

while True:
    print("=-=-= MENU =-=-=")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Fazer PIX")
    print("4 - Consultar saldo")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        chave = input("Digite sua chave pix: ")
        try:
         valor = float(input("Valor: "))
        except:
           print("Valor inválido!")
           continue
        if chave in contas:
            contas[chave].depositar(valor)
        else:
            print("Conta não encontrada!")

    elif opcao == "2":
        chave = input("Digite sua chave pix: ")
        valor = float(input("Valor: "))
        if chave in contas:
            contas[chave].sacar(valor)
        else:
            print("Conta não encontrada!")

    elif opcao == "3":
        origem = input("Sua chave pix: ")
        destino = input("Chave pix destino: ")
        try:
         valor = float(input("Valor: "))
        except:
           print("Valor inválido!")
           continue

        if origem in contas:
            contas[origem].pagar_pix(destino, valor)
        else:
            print("Conta de origem não encontrada!")

    elif opcao == "4":
        chave = input("Digite sua chave pix: ")
        if chave in contas:
            print("Saldo:", contas[chave].consultar_saldo())
        else:
            print("Conta não encontrada!")

    elif opcao == "0":
        print("Saindo...")
        time.sleep(1)
        break

    else:
        print("Opção inválida!")
  