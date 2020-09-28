# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.

def transform(c):
    f = ((c * 9) + 160) / 5
    return f

x = float(input('Quantos ºC? '))
y = transform(x)

print(f'{y:.1f} F')