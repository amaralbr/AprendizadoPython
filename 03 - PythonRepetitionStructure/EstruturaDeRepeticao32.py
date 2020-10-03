# O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia um conjunto indeterminado de temperaturas,
# e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

########## P R O G R A M A ##########
try:
    somaTemp = []
    while True:
        try:
            temp = float(input('Temperaruta (ºC): '))
            if temp > -90 and temp < 60:
                somaTemp.append(temp)
            elif temp == 999:
                break
            else:
                print('null')
                continue
        except:
            continue
    media = sum(somaTemp) / len(somaTemp)
    print('')
    print(f'Máxima: {max(somaTemp):.1f}ºC')
    print(f'Mínima: {min(somaTemp):.1f}ºC')
    print(f'Média: {media:.1f}ºC')
    print('')
except:
    print('Inválido!')