# Numa eleição existem três candidatos.
# Faça um programa que peça o número total de eleitores.
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

candidato1 = '1 - Enéas Carneiro'
candidato2 = '2 - Marina Silva'
candidato3 = '3 - Henrique Meirelles'

votosC1 = []
votosC2 = []
votosC3 = []
try:
    totalEleitores = int(input('Quantas pessoas vão votar: '))
    if totalEleitores > 1:
        valid = 1
        while valid <= totalEleitores:
            voto = 0
            while True:
                voto = int(input(f'{valid}- Entre com o número do candidato: '))
                if voto == 1 or voto == 2 or voto == 3:
                    break
                else:
                    print('<<<<< Número do candidato inválido >>>>>')
                    continue
            if voto == 1:
                votosC1.append(voto)
            elif voto == 2:
                votosC2.append(voto)
            elif voto == 3:
                votosC3.append(voto)
            valid += 1
        print('')
        print(f'Total de votos: {totalEleitores}')
        print('')
        print(f'{candidato1}: {len(votosC1)} votos.')
        print(f'{candidato2}: {len(votosC2)} votos.')
        print(f'{candidato3}: {len(votosC3)} votos.')
        print('')
    else:
        print('--- Número negativo inválido! ---')
except:
    print('Entrada Inválida!')


# import random
# candidato1 = '1 - Enéas Carneiro'
# candidato2 = '2 - Marina Silva'
# candidato3 = '3 - Henrique Meirelles'
# votosC1 = []
# votosC2 = []
# votosC3 = []
# try:
#     totalEleitores = random.randint(1, 1000000)
#     if totalEleitores > 1:
#         valid = 1
#         while valid <= totalEleitores:
#             voto = 0
#             while True:
#                 voto = random.randint(1, 3)
#                 if voto == 1 or voto == 2 or voto == 3:
#                     break
#                 else:
#                     print('<<<<< Número do candidato inválido >>>>>')
#                     continue
#             if voto == 1:
#                 votosC1.append(voto)
#             elif voto == 2:
#                 votosC2.append(voto)
#             elif voto == 3:
#                 votosC3.append(voto)
#             valid += 1
#         print('')
#         print(f'{candidato1}: {len(votosC1)} votos.')
#         print(f'{candidato2}: {len(votosC2)} votos.')
#         print(f'{candidato3}: {len(votosC3)} votos.')
#         print('')
#     else:
#         print('--- Número negativo inválido! ---')
# except:
#     print('Entrada inválida!')