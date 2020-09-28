# Faça um programa para imprimir:
#     1
#     1   2
#     1   2   3
#     .....
#     1   2   3   ...  n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.


########## P R O G R A M A ##########
def imprimir_escada(n):
    for i in range(n):
        i += 1
        for j in range(i):
            j += 1
            print(str(j), end = ' ')
        print('')

imprimir_escada(5)