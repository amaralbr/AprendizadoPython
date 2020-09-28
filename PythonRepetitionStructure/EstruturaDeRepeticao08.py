# Faça um programa que leia 5 números e informe a soma e a média dos números.

listNumber = []
while len(listNumber) <= 4:
    listNumber.append(int(input('Entre com um número: ')))
media = (sum(listNumber) / len(listNumber))
print(f'Média: {media}')