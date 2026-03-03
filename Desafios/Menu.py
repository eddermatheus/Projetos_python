import time
n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))

while True:
    time.sleep(0.5)
    op = int(input('[1] [somar]\n'
                   '[2] [multiplicar]\n'
                   '[3] [maior]\n'
                   '[4] [novos números]\n'
                   '[5] [sair do programa]\n'
                   '>>>> Qual é a sua opção? '))

    if op == 5:
        break

    if op == 1:
        soma = n1 + n2
        print(f'A soma dos números é: {soma}')
        print('-==-'*8)

    elif op == 2:
        multiplicar = n1 * n2
        print(f'A multiplicação de {n1} X {n2} = {multiplicar}')
        print('-==-'*8)

    elif op == 3:
        if n1 > n2:
            print(f'Entre {n1} e {n2} o maior é {n1}')
        elif n2 > n1:
            print(f'Entre {n1} e {n2} o maior é {n2}')
        else:
            print('Os dois números são iguais')
        print('-==-'*8)

    elif op == 4:
        n1 = float(input('Primeiro valor: '))
        n2 = float(input('Segundo valor: '))

    else:
        print('Opção inválida!')

print('Programa encerrado.')