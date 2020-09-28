# Faça um Programa que converta metros para centímetros.

def convert(m):
    r = m * 100
    return r

x = float(input('Digite a distância em metros: '))
print(f'{x} m equivale a {convert(x)} cm.')