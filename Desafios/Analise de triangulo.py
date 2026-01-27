lado_1=int(input(""))
lado_2=int(input(""))
lado_3=int(input(""))
teste1 = lado_1 + lado_2
teste2 = lado_2 + lado_3
teste3 = lado_3 + lado_1
if(teste1 > lado_3 and teste2 > lado_1 and teste3> lado_2):  #verificar se é um triangulo primeiro
    if(lado_1 == lado_2 and lado_2 == lado_3):  #verificar se é um triangulo equilátero
      print("Triangulinho com todos os lados iguais: é equilátero!!")
    elif(lado_1 == lado_2 or lado_2 == lado_3 or lado_3 == lado_1):
       print("Triangulinho com dois lados iguais: é isósceles!!")
    else:
       print("Tem os três lados diferentes mas ainda continua sendo um triangulinho: é escaleno!!")
else:
   print("Esses segmentos de reta não formam um triângulo. Tchau!!!!")
       
