# Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.


########## P R O G R A M A ##########
numeros = []
par = []
impar = []
while len(numeros) < 20:
    numero = int(input(f'Entre com o {len(numeros) + 1}º número: '))
    numeros.append(numero)
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
print(numeros)
print(par)
print(impar)