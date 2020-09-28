#Altere o programa de cálculo do fatorial,
# permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

import math

valid = True
while valid is True:
    try:
        number = int(input('Entre com um número (0-16): '))
        if number >= 0 and number <= 16:
            print(f'Fatorial de {number} é {math.factorial(number):.0f}.')
        else:
            print('>>>> Número Inválido <<<<!')
            continue
        question = input('Você deseja calcular outromúmero (S - Sim / Qualque tecla - Não)?: ').upper()
        if question == 'S':
            continue
        else:
            valid = False
    except:
        print('>>>> Entrada Inválida! <<<<')
        continue