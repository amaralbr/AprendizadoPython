# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math

def area(r):
    a = math.pi * math.pow(r, 2)
    return a

x = float(input('Entre com o raio: '))
print(f'A área do círculo de raio {x} é {area(x):.2f}.')