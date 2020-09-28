# Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.

# Data de Nascimento: 29/10/1973
# Você nasceu em  29 de Outubro de 1973.

########## P R O G R A M A ##########
def porExtenso(d, m, a):
    meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    if d > 31 or d < 1:
        print('--- Dia Inválido ---')
    elif m > 12 or m < 1:
        print('--- Mês Inválido ---')
    elif a > 9999 or a < 1111:
        print('--- Ano Inválido ---')
    elif d <= 31:
        if d == 31 and (m == 2 or m == 4 or m == 6 or m == 9 or m == 11):
            print('-- Mês Inválido --')
        elif d == 30 and m == 2:
            print('-- Mês Inválido --')
        elif d == 29 and m == 2 and (a % 4 != 0 or (a % 100 == 0 and a % 400 != 0)):
            print('-- Ano Inválido --')
        else:
            print(f'Você nasceu em {d} de {meses[m-1]} de {a}.')

data = input('Data de Nascimento: ')
dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:])
porExtenso(dia, mes, ano)