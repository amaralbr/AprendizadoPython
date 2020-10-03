# Tendo como dado de entrada a altura (h) de uma pessoa,
# construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

def idealH(h):
    r = (72.7 * h) - 58
    return r

def idealM(h):
    r = (62.1 * h) - 44.7
    return r

sexo = input('Entre com o sexo (m/f): ').lower()
x = float(input('Entre com a altura (metros): '))
if sexo == 'm':
    r = idealH(x)
elif sexo == 'f':
    r = idealM(x)
else:
    print('Entrada inválida!')
print(f'Peso ideal: {r:.1f} kg.')