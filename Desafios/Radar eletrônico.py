import time
Velocidade_Atual = int(input(''))
if (Velocidade_Atual > 80):
    print(f'MULTADO! Você excedeu 80km/h')
    Multa = (Velocidade_Atual - 80) * 7
    print('Processando sua Multa...')
    time.sleep(1.5)
    print(f'Você deve pagar uma multa de: {Multa:.2f}')
print(f'tenha um bom dia e dirija com segurança')
