# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

a = int(input('Entre com a população da cidade A: '))
taxaA = float(input('Entre com a taxa de crescimento da cidade A: '))
b = int(input('Entre com a população da cidade B: '))
taxaB = float(input('Entre com a taxa de crescimento da cidade B: '))
anos = 1

while a <= b:
    a += (a * (taxaA / 100))
    b += (b * (taxaB / 100))
    anos += 1

print(anos)