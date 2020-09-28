# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

num1 = int(input('Entre com um número inteiro: '))
num2 = int(input('Entre com outro número inteiro:'))
x = min(num1, num2) + 1
while x < max(num1, num2):
    print(x)
    x += 1

