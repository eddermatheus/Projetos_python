with open("clientes.txt", "w",encoding="utf-8") as arq:
  for  i in range (3):
   print(f"Cadastro do cliente {i+1}")
   nome = input("Nome completo: ")
   chave_pix = input("Chave pix: ")
   cpf = input("Digite o CPF: ")
   arq.write(f"{nome},{chave_pix},{cpf}\n")
   