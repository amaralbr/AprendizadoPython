# Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
# C = (5 * (F-32) / 9).

def transform(f):
    c = (5 * (f - 32) / 9)
    return c

x = float(input('Quantos Farenheit? '))
y = transform(x)

print(f'{y:.1f}ºC')