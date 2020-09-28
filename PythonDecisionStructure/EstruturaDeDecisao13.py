# Faça um Programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

dias = {1:'Domingo', 2:'Segunda', 3:'Terça', 4:'Quarta', 5:'Quinta', 6:'Sexta', 7:'Sábado'}

x = int(input('Entre com um número de 1 à 7: '))

if x >= 1 and x <= 7:
    print(dias[x])
else:
    print('Valor Inválido!')