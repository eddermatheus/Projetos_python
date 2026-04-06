import matplotlib.pyplot as plt
import numpy as np

##tolerancia = 1e-6 #tolerancia como referença o valor mais baixo possível

for c in range(4):
    I_Curva1 = list(map(lambda x: float(x), input("Lista com os valores da corrente para a primeira curva I-V: ").split(",")))
    V_curva1 = list(map(lambda x: float(x), input("Lista com os valores da tensão para a primeira curva I-V: ").split(",")))
    #código criado pra fazer a curva da Potência  -> P=VxI
    P_curva1 = [V_curva1[i] * I_Curva1[i] for i in range(len(I_Curva1))]

    Isc = None   
    voc = None   

    Pmax = max(P_curva1)
    indice = P_curva1.index(Pmax)
    Vmp = V_curva1[indice]
    Imp = I_Curva1[indice]

    passo = - 1
    x =  len(P_curva1) - 1

    while 0 < x < len(P_curva1) - 1:
      Pk = P_curva1[x]
      Pk_1 = P_curva1[x-passo]

      if Pk > Pk_1:
        x += passo
      else:
        passo = -passo
        x += passo

    # achar Isc e Voc
    for i in range(len(I_Curva1)):
        if abs(V_curva1[i]) == 0:  #Para pegar o dado de ISc onde V = 0
            Isc = I_Curva1[i]
        if abs(I_Curva1[i]) == 0:  #para pegar o dado de voc onde I = 0 
            voc = V_curva1[i]

    # PRINT no lugar certo
    print(f"\nCurva {c+1}:")  #esse c vai de 0 a 4 , mas c +1 => curva 1 para c = 0 + 1
    print(f"MPP = {Pmax} W")
    print(f"Vmp = {Vmp} V")
    print(f"Isc = {Isc} A")
    print(f"Voc = {voc} V")

    #  PLOT dentro do loop
    plt.figure(1)
    plt.plot(V_curva1, I_Curva1)
    plt.scatter(Imp, Vmp)
    plt.text(Imp, Vmp, "MPP")

    plt.figure(2)
    plt.plot(V_curva1, P_curva1)
    plt.scatter(Vmp, Pmax)
    plt.text(Vmp, Pmax, "MPP")

# labels (fora do loop)
plt.figure(1)
plt.ylabel("Tensão (V)")
plt.xlabel("Corrente (A)")

plt.figure(2)
plt.ylabel("Potência (W)")
plt.xlabel("Tensão (V)")

# mostrar tudo no final
plt.show()