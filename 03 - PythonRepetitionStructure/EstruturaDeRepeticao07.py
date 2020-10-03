# Faça um programa que leia 5 números e informe o maior número.

listNumb = []
while len(listNumb) <= 4:
    listNumb.append(int(input('Entre com um número: ')))
print(max(listNumb))