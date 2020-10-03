# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

def mensal(v, h):
    m = v * h
    return m

x = float(input('qual valor da hora trabalhada: '))
y = int(input('quantas horas trabalhadas no mês: '))
z = mensal(x, y)

print(f'Total: R${z:.2f}')