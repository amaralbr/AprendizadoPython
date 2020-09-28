# Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.


########## P R O G R A M A ##########
def reverso(n):
    string = str(n)
    cont = 1
    for i in range(len(string)):
        print(f'{string[len(string)-cont]}', end = '')
        cont += 1

reverso(int(input('Entre com um número inteiro: ')))