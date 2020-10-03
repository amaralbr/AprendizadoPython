# Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos:
# [0-25], [26-50], [51-75] e [76-100].
# A entrada de dados deverá terminar quando for lido um número negativo.


########## P R O G R A M A ##########
list = []
while True:
    print('<<< >>>')
    try:
        numb = int(input('Entre com um número positivo:'))
        if numb >= 0:
            list.append(numb)
            continue
        else:
            break
    except:
        print('Entrada Inválida!')
cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
for i in list:
    if i >=0 and i <= 25:
        cont1 += 1
    elif i >= 26 and i <= 50:
        cont2 += 1
    elif i >= 51 and i <= 75:
        cont3 += 1
    elif i >= 76 and i <= 100:
        cont4 += 1
print('<<< >>>')
print(f'Há {cont1} números entre 00 e 25.')
print(f'Há {cont2} números entre 26 e 50.')
print(f'Há {cont3} números entre 51 e 75.')
print(f'Há {cont4} números entre 76 e 100.')