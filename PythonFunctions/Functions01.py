# Faça um programa para imprimir:
#     1
#     2   2
#     3   3   3
#     .....
#     n   n   n   n   n   n  ... n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.


########## P R O G R A M A ##########
def imprimir_escada(n):
    for i in range(n):
        i += 1
        print(f'{str(i)} ' * i)

imprimir_escada(5)
