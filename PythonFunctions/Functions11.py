# Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de
# mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.


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
            print(f'{d} de {meses[m-1]} de {a}.')

data = input('Entre com uma data no formato \'dd/mm/aaaa\': ')
dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:])
porExtenso(dia, mes, ano)
        