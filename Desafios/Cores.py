a = 3
b = 4

print('\033[33mOlá mundo\033[0m')          # amarelo
print('\033[1;33mOlá mundo\033[0m')        # amarelo em negrito
print('\033[1;33;41mOlá mundo\033[0m')     # amarelo em negrito com fundo vermelho
print('\033[1;33;41mOlá mundo\033[0m')     # só esse texto com efeito
print(f'\033[1;33mOs valores são {a} e {b}\033[m') 
