# Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
# Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

# Compara duas strings
# String 1: Brasil Hexa 2006
# String 2: Brasil! Hexa 2006!
# Tamanho de "Brasil Hexa 2006": 16 caracteres
# Tamanho de "Brasil! Hexa 2006!": 18 caracteres
# As duas strings são de tamanhos diferentes.
# As duas strings possuem conteúdo diferente.


########## P R O G R A M A ##########
texto1 = input('String 1: ')
texto2 = input('String 2: ')

print(f'Tamanho de \"{texto1}\": {len(texto1)} caracteres')
print(f'Tamanho de \"{texto2}\": {len(texto2)} caracteres')
if len(texto1) == len(texto2):
    print('As duas strings são do mesmo tamanho.')
    cont = 0
    for i in range(len(texto1)):
        if texto1[i] == texto2[i]:
            cont += 1
    if cont == len(texto2):
        print('AS duas strings possuem o mesmo conteúdo.')
    else:
        print('As duas strings possuem conteúdos diferentes.')
else:
    print('As duas strings são de tamanhos diferentes.')
    print('As duas strings possuem conteúdos diferentes.')
