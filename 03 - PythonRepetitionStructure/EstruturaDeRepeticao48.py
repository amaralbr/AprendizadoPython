# Faça um programa que mostre os n termos da Série a seguir:
#   S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
# Imprima no final a soma da série.


########## P R O G R A M A ##########
numero = int(input('Entre com o número te termos: '))
termos = []
soma = []
x = 1
y = 1
while numero > 0:
    termo = str(x) + '/' + str(y)
    op = x / y
    termos.append(termo)
    soma.append(op)
    x += 1
    y += 2
    numero -= 1
print('S = ', end = "")
for i in termos:
    if termos.index(i) < len(termos) - 1:
        print(f'{i} + ', end = "")
    elif termos.index(i) == len(termos) - 1:
        print(f'{i} = {sum(soma):.2f}')