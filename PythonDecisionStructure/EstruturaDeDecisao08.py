# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato.

prod = []

prod.append(float(input('Qual o preço do primeiro produto: ')))
prod.append(float(input('Qual o preço do segundo produto: ')))
prod.append(float(input('Qual o preço do terceiro produto: ')))

print(f'Você deve comprar o {prod.index(min(prod)) + 1}º produto.')