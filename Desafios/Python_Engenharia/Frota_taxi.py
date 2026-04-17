import sqlite3
import time 
conexao = sqlite3.connect("frota_taxi.db")
cursor = conexao.cursor()
#CRIAÇÃO DA TABELA CLIENTE
cursor.execute("""
create table if not exists CLIENTE(
    clid integer primary key,
    nome text,
    cpf text
)
""")

cursor.executemany("""
insert or ignore into CLIENTE (clid, nome, cpf) values (?, ?, ?)
""", [
    [1532,"Asdrúbal","448.754.253-65"],
    [1755,"Doriana","567.387.387-44"],
    [1780,"Quincas","546.373.762-03"],
    [2001,"Lívia","432.111.888-99"],
    [2002,"Bruno","123.456.789-00"],
    [2003,"Marina","234.567.890-10"],
    [2004,"Tiago","321.654.987-77"],
    [2005,"Camila","789.456.123-33"],
    [2006,"Renato","890.321.678-11"],
    [2007,"Juliana","111.222.333-44"]
] )
#CRIAÇÃO DA TABELA DE TAXI
cursor.execute("""
create table if not exists TAXI(
    placa text primary key,
    marca text,
    modelo text,
    ano_fab integer           
)
""")

cursor.executemany("""
insert or ignore into TAXI (placa, marca, modelo,ano_fab) values (?, ?, ?, ?)
""",[
    ["BRA1234", "Toyota", "Corolla", 2023],
    ["XYZ9876", "Hyundai", "HB20S", 2024],
    ["WYP8765", "Fiat", "Mobi", 2021],
    ["PYZ3456", "Fiat", "Argo", 2022],
    ["GHI1234", "Renault", "Logan", 2023],
    ["KLM5678", "Fiat", "Pulse", 2024],
    ["NOP4321", "Nissan", "Versa", 2023],
    ["QRS8765", "Chevrolet", "Onix Plus", 2024],
    ["TUV9999", "Volkswagen", "Virtus", 2023],
    ["BXC1234", "Honda", "City", 2024],
    ["ZXC5678", "Caoa Chery", "Arrizo 6", 2024],
    ["LMN8765", "Peugeot", "208", 2023]
])

#CRIAÇÃO DA TABELA CORRIDA
cursor.execute("""
create table if not exists CORRIDA(
    clid integer,
    placa text,
    DataPedido text,
    FOREIGN KEY (clid) REFERENCES CLIENTE(clid),
    FOREIGN KEY (placa) REFERENCES TAXI(placa)    
)
""")

cursor.executemany("""
insert or ignore into CORRIDA (clid, placa, DataPedido) values (?, ?, ?)
""",[
    [1755, "BRA1234", "10/06/2024"],
    [2001, "GHI1234", "12/06/2024"],
    [2002, "KLM5678", "13/06/2024"],
    [2003, "NOP4321", "14/06/2024"],
    [2004, "QRS8765", "15/06/2024"],
    [2005, "TUV9999", "16/06/2024"],
    [2006, "BXC1234", "17/06/2024"],
    [2007, "ZXC5678", "18/06/2024"],
    [1780, "LMN8765", "19/06/2024"]
])
conexao.commit()
while True:
    try:
        print("Carregando Opções...")
        time.sleep(1.5)
        print("Opções abaixo:")
        print("\n1 - Listar clientes")
        print("2 - Listar todos os taxi da marca Fiat")
        print("3 - Exibir as corridas realizadas com data e o nome do cliente.")
        print("4 - Mostrar os nomes dos clientes que usaram táxis do modelo Corolla.")
        print("5 - Quantas corridas cada táxi realizou?")
        print("6 - Quais táxis foram fabricados antes de 2024?")
        print("7 - Sair")

        opcao = int(input("Escolha uma opção: "))

    except ValueError:
        print("Digite um número válido.")
        continue

    if opcao == 1:
        cursor.execute("SELECT nome, cpf FROM CLIENTE")
        resultados = cursor.fetchall()

        for nome, cpf in resultados:
            print(f"Nome: {nome}, CPF: {cpf}")

    elif opcao == 2:
        cursor.execute("SELECT placa, marca ,modelo, ano_fab FROM TAXI where marca = 'Fiat'  ")
        resultados = cursor.fetchall()
        for placa, marca , modelo, ano_fab in resultados:
         print(f"{placa} ,{marca}, {modelo}, {ano_fab}")

    elif opcao == 3:
        cursor.execute("SELECT CORRIDA.DataPedido, CLIENTE.nome FROM CORRIDA JOIN CLIENTE ON CORRIDA.clid = CLIENTE.clid")
        resultados = cursor.fetchall()
        for data, nome in resultados:
         print(f"Data: {data} Nome: {nome}")

    elif opcao == 4:
        cursor.execute("SELECT DISTINCT CLIENTE.nome FROM CLIENTE JOIN CORRIDA ON CLIENTE.clid = CORRIDA.clid " \
               "JOIN TAXI ON CORRIDA.placa = TAXI.placa WHERE TAXI.modelo = 'Corolla'")
        resultados = cursor.fetchall()
        for nome in resultados:
           print(f"Nome: {nome}")
    elif opcao == 5:
        cursor.execute("""
       SELECT TAXI.placa, TAXI.modelo, COUNT(*) as total_corridas
      FROM CORRIDA
      JOIN TAXI ON CORRIDA.placa = TAXI.placa
      GROUP BY TAXI.placa, TAXI.modelo
        """)
        for placa, modelo, total in cursor.fetchall():
         print(f"{placa} ({modelo}) - {total} corridas")

    elif opcao == 6:
        cursor.execute("""
        SELECT placa, modelo, ano_fab
        FROM TAXI
        WHERE ano_fab < 2024
        """)

        for placa, modelo, ano in cursor.fetchall():
         print(f"{placa} - {modelo} ({ano})")

    elif opcao == 7:
        print("Sistema encerrado com sucesso! :)")
        break

    else:
        print("Opção inválida!")

cursor.close()
conexao.close()
