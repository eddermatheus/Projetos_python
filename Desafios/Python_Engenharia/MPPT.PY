import matplotlib.pyplot as plt
import numpy as np
tolerancia = 1e-6
for c in range(4):
  I_Curva1 = []
  I_Curva1 = list(map(lambda x: float(x), input("Lista com os valores da corrente para aprimeira curva I-V:").split(",")))
  V_curva1 = []
  V_curva1 = list(map(lambda x: float(x), input("Lista com os valores da tensão para aprimeira curva I-V:").split(",")))
  P_curva1 = [V_curva1[i] *  I_Curva1[i] for i in range(len(I_Curva1))]
  Pmax = max(P_curva1)
  indice = P_curva1.index(Pmax)
  Vmp = V_curva1[indice]
  Imp = I_Curva1[indice]
  plt.figure(1)
  plt.plot(I_Curva1, V_curva1)
  plt.scatter(Imp, Vmp)
  plt.text(Imp, Vmp, f"MPP")
  plt.figure(2)
  plt.plot(V_curva1, P_curva1)
  plt.scatter(Vmp, Pmax)
  plt.text(Vmp, Pmax, f"MPP")
  for i in range(len(I_Curva1)):
     if abs(V_curva1[i]) < tolerancia:
        Isc = I_Curva1[i]
     if abs(I_Curva1[i]) < tolerancia:
        voc = V_curva1[i]

     print(f"\nCurva {c+1}:")
     print(f"MPP = {Pmax} W")
     print(f"Vmp = {Vmp} V")
     print(f"Isc = {Isc} A")
     print(f"Voc = {voc} V")
plt.figure(1)
plt.ylabel("Tensão [V]")
plt.xlabel("Corrente [A]")
plt.show()
plt.figure(2)
plt.ylabel("Potência [W]")
plt.xlabel("Tensão [V]")
plt.show()