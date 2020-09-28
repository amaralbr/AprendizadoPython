# Tendo como dados de entrada a altura de uma pessoa,
# construa um algoritmo que calcule seu peso ideal,
# usando a seguinte fórmula: (72.7*altura) - 58

def ideal(a):
    r = (72.7 * a) - 58
    return r

x = float(input('Qual sua altura em metros? '))
print(f'Peso ideal: {ideal(x):.2f}kg.')