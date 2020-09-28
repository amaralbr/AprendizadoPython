# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
# Caso contrário, ele será classificado como "Inocente".

## função para calcular peso da questão
def peso(x):
    if x == 'S':
        return 1
    else:
        return 0

## função para classicar a pessoa interrogada
def classPessoa(x):
    if x <= 1:
        print('>>> Inocente <<<')
    elif x == 2:
        print('>>> Suspeito <<<')
    elif x == 3 or x == 4:
        print('>>> Cúmplice <<<')
    elif x == 5:
        print('>>> Assassino <<<')

########## P R O G R A M A ##########
print('------------------------------------')
print('Responde S (Sim) ou N (Não):')
print('')
question1 = input('Telefonou para a vítima? ').upper()
question2 = input('Esteve no local do crime? ').upper()
question3 = input('Mora perto da vítima? ').upper()
question4 = input('Devia para a vítima? ').upper()
question5 = input('Já trabalhou com a vítima? ').upper()

result = peso(question1) + peso(question2) + peso(question3) + peso(question4) + peso(question5)
classPessoa(result)