# Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.


########## P R O G R A M A ##########
numero = int(input('Entre com o número te termos: '))
termos = []
x = 1
y = 1
while numero > 0:
    termo = x / y
    termos.append(termo)
    x += 1
    y += 2
    numero -= 1
resultado = 1 + sum(termos)
print(f'H = {resultado:.2f}')