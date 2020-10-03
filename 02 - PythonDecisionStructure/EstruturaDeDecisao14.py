# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
# e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO”
# se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

def media(x, y):
    m = (x + y) / 2
    return m

def conceito(x, y):
    if media(x, y) >= 9.00 and media(x, y) <= 10.00:
        c = 'A'
        return c
    elif media(x, y) >= 7.50 and media(x, y) < 9.00:
        c = 'B'
        return c
    elif media(x, y) >= 6.00 and media(x, y) < 7.50:
        c = 'C'
        return c
    elif media(x, y) >= 4.00 and media(x, y) < 6.00:
        c = 'D'
        return c
    elif media(x, y) >= 0.00 and media(x, y) < 4.00:
        c = 'E'
        return c

def tela(x, y):
    m = media(x, y)
    c = conceito(x, y)
    print('----------------------------------------')
    print(f'Primeira nota: {x} | Segunda nota: {y}')
    print(f'Média: {m:.1f}')
    print(f'Conceito: {c}')
    if c == 'A' or c == 'B' or c == 'C':
        print('>> APROVADO <<')
    elif c == 'D' or c == 'E':
        print('>> REPROVADO <<')
    print('----------------------------------------')

nota1 = int(input('Entre com a primeira nota: '))
nota2 = int(input('Entre com a segunda nota: '))

tela(nota1, nota2)