# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
# Caso contrário, ele será classificado como "Inocente".


########## P R O G R A M A ##########
respostas = []
quest1 = int(input('1- Telefonou para a vítima (1 - SIM/ 0 - NÃO)? '))
respostas.append(quest1)
quest2 = int(input('2- Esteve no local do crime (1 - SIM/ 0 - NÃO)? '))
respostas.append(quest2)
quest3 = int(input('3- Mora perto da vítma (1 - SIM/ 0 - NÃO)? '))
respostas.append(quest3)
quest4 = int(input('4- Devia para a vítima (1 - SIM/ 0 - NÃO)? '))
respostas.append(quest4)
quest5 = int(input('5- Já trabalhou com a vítima (1 - SIM/ 0 - NÃO)? '))
respostas.append(quest5)

if sum(respostas) < 2:
    print('Inocente')
elif sum(respostas) == 2:
    print('Suspeito')
elif sum(respostas) == 3 or sum(respostas) == 4:
    print('Cúmplice')
elif sum(respostas) == 5:
    print('Assassino')