import matplotlib.pyplot as plt
import numpy as np


for c in range(4):
    I_Curva1 = list(map(lambda x: float(x), input(f"Lista com os valores da  para {c + 1}º curva I-V: ").split(",")))
    V_curva1 = list(map(lambda x: float(x), input(f"Lista com os valores da tensão para a {c + 1}º curva I-V: ").split(",")))
    # código abaixo foi criado pra fazer a curva da Potência  -> P=VxI
    P_curva1 = [V_curva1[i] * I_Curva1[i] for i in range(len(I_Curva1))]

    Isc = None   
    voc = None   

    Pmax = max(P_curva1)
    indice = P_curva1.index(Pmax)
    Vmp = V_curva1[indice]
    Imp = I_Curva1[indice]

    Vref = V_curva1[-1]  # começa no Voc
    direcao = 1

    for k in range(1, len(V_curva1)):
        dP = P_curva1[k] - P_curva1[k-1]
        dV = V_curva1[k] - V_curva1[k-1]

        if dP > 0:
            if dV > 0:
              direcao = 1
            else:
              direcao = -1
        else:
            if dV > 0:
              direcao = -1
            else:
              direcao = 1

        Vref += direcao * abs(dV)
    

    # achar Isc e Voc
    for i in range(len(I_Curva1)):
        if abs(V_curva1[i]) == 0:  #Para pegar o dado de ISc onde V = 0
            Isc = I_Curva1[i]
        if abs(I_Curva1[i]) == 0:  #para pegar o dado de voc onde I = 0 
            voc = V_curva1[i]


    print(f"\nCurva {c+1}:")  #esse c vai de 0 a 4 , mas c +1 => curva 1 para c = 0 + 1
    print(f"MPP = {Pmax} W")
    print(f"Vmp = {Vmp} V")
    print(f"Isc = {Isc} A")
    print(f"Voc = {voc} V")
    print(f"Vref (MPPT) = {Vref} V")

    #  PLOT dentro do loop
    plt.figure(1)
    plt.plot(V_curva1, I_Curva1)
    plt.scatter(Vmp, Imp)
    plt.text(Vmp, Imp, "MPP")
    plt.scatter(0,Isc)
    plt.text(0,Isc,"Isc")
    plt.scatter(voc,"Voc")
    plt.text(voc,0,"Voc")

    plt.figure(2)
    plt.plot(V_curva1, P_curva1)
    plt.scatter(Vmp, Pmax)
    plt.text(Vmp, Pmax, "MPP")
    plt.scatter(voc,0)
    plt.text(voc,0,"Voc")

# labels (fora do loop)
plt.figure(1)
plt.xlabel("Tensão (V)")
plt.ylabel("Corrente (A)")

plt.figure(2)
plt.ylabel("Potência (W)")
plt.xlabel("Tensão (V)")

# mostrar tudo no final
plt.show()