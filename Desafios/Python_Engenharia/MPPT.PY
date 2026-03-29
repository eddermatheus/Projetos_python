import matplotlib.pyplot as plt
import numpy as np

tolerancia = 1e-6 #tolerancia como referença o valor mais baixo possível

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

    passo = 1
    x = 1 

    # achar Isc e Voc
    for i in range(len(I_Curva1)):
        if abs(V_curva1[i]) < tolerancia:
            Isc = I_Curva1[i]
        if abs(I_Curva1[i]) < tolerancia:
            voc = V_curva1[i]

    # fallback (caso não ache zero exato)
    if Isc is None:
        idx = V_curva1.index(min(V_curva1, key=abs))
        Isc = I_Curva1[idx]

    if voc is None:
        idx = I_Curva1.index(min(I_Curva1, key=abs))
        voc = V_curva1[idx]

    # PRINT no lugar certo
    print(f"\nCurva {c+1}:")  #esse c vai de 0 a 4 , mas c +1 => curva 1 para c = 0 + 1
    print(f"MPP = {Pmax} W")
    print(f"Vmp = {Vmp} V")
    print(f"Isc = {Isc} A")
    print(f"Voc = {voc} V")

    #  PLOT dentro do loop
    plt.figure(1)
    plt.plot(I_Curva1, V_curva1)
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