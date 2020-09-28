# Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se
# seu argumento for zero ou negativo.


########## P R O G R A M A ##########
def posOrNeg(x):
    if x > 0:
        return 'P'
    else:
        return 'N'

print(posOrNeg(3))
print(posOrNeg(0))
print(posOrNeg(-3))