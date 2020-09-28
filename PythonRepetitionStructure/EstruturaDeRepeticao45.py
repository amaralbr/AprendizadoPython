# Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
# Exemplo:
#   12376489
#   => 98467321


########## P R O G R A M A ##########
numero = int(input('Entre com um número inteiro: '))
numero = str(numero)
operacao = len(numero)

while operacao > 0:
    print(numero[operacao - 1], end = "")
    operacao -= 1