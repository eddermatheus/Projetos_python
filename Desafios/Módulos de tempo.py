#from datetime import date #importando a biblioteca date dentro da datetime
from datetime import datetime
##hoje = date.today() # a data atual a de hoje
##print(hoje)
agora = datetime.now().strftime('%d/%m/%y %H:%M') #converte em uma string o strftime
print(agora) # data e o horario de hoje 