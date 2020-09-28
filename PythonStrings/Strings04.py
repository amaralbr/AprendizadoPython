# Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

# F
# FU
# FUL
# FULA
# FULAN
# FULANO


########## P R O G R A M A ##########
nome = input('Entre com um nome: ').upper()
for i in range(len(nome)):
    print(nome[0:i+1])