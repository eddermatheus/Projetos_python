nome = input(('Digite um nome: ')).strip()
separar = nome.split() #separando em palavras
junto = ''.join(separar)  #juntando as palavras que eu havia separado
inverso = ''
for letra in range(len(junto) - 1 , -1, -1): # esse len(junto) é um numero o tamanho total que conta decrescendo até 0
   inverso+= junto[letra] # aq o inverso vai ser somado com as letras de trás pra frente, ou seja, formar a palavra inversa
if inverso == junto:  #if pra saber se é palindromo
   print('É um palindromo')
else:
  print('não é palindromo')


