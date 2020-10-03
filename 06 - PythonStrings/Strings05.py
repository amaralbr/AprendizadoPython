# Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.

# FULANO
# FULAN
# FULA
# FUL
# FU
# F


########## P R O G R A M A ##########
nome = input('Entre com um nome: ').upper()
cont = len(nome)
for i in range(len(nome)):
    print(nome[0:cont])
    cont -= 1