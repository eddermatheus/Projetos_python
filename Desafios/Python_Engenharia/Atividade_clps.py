import random
def trata_erro(nome_sensor, clp_escolhido):
    if nome_sensor not in clp_escolhido:
        print("Erro: Sensor inválido!")
        return False
    return True
 
def lersensor_temperatura(Nome_sensor):
 valor_sensor = random.randint(0,100)
 return valor_sensor
def lersensor_pressão(Nome_sensor):
  valor_sensor = random.randint(0,100)
  return valor_sensor
def lersensor_vazão(Nome_sensor):
 valor_sensor = random.randint(0,100)
 return valor_sensor

Siemens = {'Sensor_temperatura': None ,'Sensor_vazão': None, 'Sensor_pressão': None}
WEG = {'Sensor_temperatura': None,'Sensor_vazão': None, 'Sensor_pressão': None}
Rockwell = {'Sensor_temperatura': None,'Sensor_vazão': None, 'Sensor_pressão': None}
lista_clp = [Siemens , WEG , Rockwell]
while True:
    try:
        clp = int(input("Qual clp?"))
        clp_escolhido = lista_clp[clp]
    except:
         print("Erro: CLP inválido!")
         continue
  
    Sensor_nome = input("Qual sensor? ")

    if Sensor_nome == 'fim':
      break

    if not trata_erro(Sensor_nome, clp_escolhido):
      continue

    if Sensor_nome == 'Sensor_temperatura':
      valor = lersensor_temperatura(Sensor_nome)
      print(f"{Sensor_nome} -> {valor} °C")
      

    elif Sensor_nome == 'Sensor_vazão':
     valor = lersensor_vazão(Sensor_nome)
     print(f"{Sensor_nome} -> {valor} m³/s")
    

    elif Sensor_nome == 'Sensor_pressão':
     valor = lersensor_pressão(Sensor_nome)
     print(f"{Sensor_nome} -> {valor} bar")
    