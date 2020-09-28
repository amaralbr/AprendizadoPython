# Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.


########## P R O G R A M A ##########
import math
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 0
for i in numeros:
    i = math.pow(i, 2)
    numeros[x] = i
    x += 1
print(sum(numeros))