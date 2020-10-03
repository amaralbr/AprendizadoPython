# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

import math

def a(x, y):
    r = (x * 2) * (y / 2)
    return r

def b(x, z):
    r = (x * 3) + z
    return r

def c(z):
    r = math.pow(z, 3)
    return r

n1 = int(input('entre com o primeiro número (int): '))
n2 = int(input('entre com o segundo número (int): '))
n3 = float(input('entre com o terceiro número (real): '))

print(f'a.{a(n1, n2)}')
print(f'b.{b(n1, n3)}')
print(f'c.{c(n3)}')