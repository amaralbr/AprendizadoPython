# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120.
# A saída deve ser conforme o exemplo abaixo:
# Fatorial de: 5
# 5! =  5 . 4 . 3 . 2 . 1 = 120



########## P R O G R A M A ##########
import math
try:
    numb = int(input('Entre com um número inteiro: '))
    calc = numb
    print(f'Fatorial de: {numb}')
    print(f'{numb}! = ', end = '')
    while calc >= 1:
        if calc != 1:
            print(calc, end = ' . ')
        else:
            print(calc, end = ' ')
        calc -= 1
    print(f'= {math.factorial(numb)}')
except:
    print('Inválido!')