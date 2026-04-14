CPF = input("Digite seu CPF : ").strip()

with open("clientes.txt","r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        nome, chave_pix, cpf = [dado.strip() for dado in linha.split(",")]

        if cpf == CPF:
            print(f"{nome},{chave_pix},{cpf}")
            break
    else:
        print("Cpf não encontrado")