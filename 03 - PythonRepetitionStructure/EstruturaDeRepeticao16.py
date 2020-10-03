# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

nFatorial = int(input('Entre com um número inteiro: '))
valid = nFatorial
y = nFatorial - 1
while valid >= 2:
    nFatorial *= y
    y -= 1
    valid -= 1
print(nFatorial)