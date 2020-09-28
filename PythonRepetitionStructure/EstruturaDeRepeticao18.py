# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

import random

list = []
n = int(input('Quantos entradas deve ter na lista? '))
while n >= 1:
    list.append(random.randrange(1000))
    n -= 1
print(f'Lista de números: {list}')
print(f'Máximo: {max(list)}')
print(f'Mínimo: {min(list)}')
print(f'Soma: {sum(list)}')