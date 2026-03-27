with open("nomes.txt", "w",encoding="utf-8") as arq:
    arq.write("Luan\nEric Mendonça\nJoão")

with open("nomes.txt", "r") as arq:
    for linha in arq:
        print(linha.strip())