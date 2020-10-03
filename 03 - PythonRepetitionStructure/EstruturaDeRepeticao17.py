# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

import random

list = []
n = int(input('Quantos entradas deve ter na lista? '))
while n >= 1:
    list.append(random.randrange(100))
    n -= 1
print(f'Lista de números: {list}')
print(f'Máximo: {max(list)}')
print(f'Mínimo: {min(list)}')
print(f'Soma: {sum(list)}')