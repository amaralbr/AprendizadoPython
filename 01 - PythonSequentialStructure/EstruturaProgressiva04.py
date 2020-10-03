# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

def media(x1, x2, x3, x4):
    r = (x1 + x2 + x3 + x4) / 4
    return r

x1 = float(input('nota do primeiro bimestre: '))
x2 = float(input('nota do segundo bimestre: '))
x3 = float(input('nota do terceiro bimestre: '))
x4 = float(input('nota do quarto bimestre: '))
print(f'A média dos 4 bimestre é {media(x1, x2, x3, x4)}')