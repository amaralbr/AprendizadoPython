# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.


########## P R O G R A M A ##########
caracteres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
for i in caracteres:
    if i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u':
        print(i, end = " ")