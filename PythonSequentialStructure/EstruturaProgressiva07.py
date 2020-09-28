# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

import math

def area(l):
    a = math.pow(l, 2) * 2
    return a

x = float(input('entre com o lado do quadrado: '))
print(f'O quadrado de lado {x} tem área de {area(x):.2f} .')