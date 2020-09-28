# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
# O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário
# nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e
# o programa não deve fazer pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

import math

def delta(a, b, c):
    d = math.pow(b, 2) - (4 * a * c)
    if d < 0:
        print(f'O valor de delta é {d}. A equação não possui raizes reais.')
    elif d == 0:
        print(f'O valor de delta é {d}. A equação possui uma raiz real.')
    elif d > 0:
        d = math.sqrt(d)
        print(f'O valor de delta é {d:.2f}. A equação possui duas raizes reais.')


a = int(input('Entre com o valor de A: '))
if a != 0:
    b = int(input('Entre com o valor de B: '))
    c = int(input('Entre com o valor de C: '))
else:
    print('A = 0. Equação não é do 2º Grau.')
delta(a, b, c)


