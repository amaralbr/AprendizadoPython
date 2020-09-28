# Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o
# número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar
# o número com ou sem o traço separador.

# Valida e corrige número de telefone
# Telefone: 461-0133
# Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
# Telefone corrigido sem formatação: 34610133
# Telefone corrigido com formatação: 3461-0133


## função para classificar a modificação do número
def classificacao (telefone):
    if len(telefone) == 9 and telefone[4] == '-':
        return 'O número está correto.'
    elif len(telefone) == 8 and telefone[3] == '-':
        return 'Vou acrescenta o digito 3 na frente.'
    elif len(telefone) == 8 and telefone[3] != '-' and telefone[0] == '3':
        return 'O número está correto.'
    elif len(telefone) == 7:
        return 'Vou acrescenta o digito 3 na frente.'

## função para formatar o número
def formatacao (telefone, valid):
    if valid == 0:
        if len(telefone) == 9 and telefone[4] == '-':
            result = telefone[0:4] + telefone[5:]
            return result
        elif len(telefone) == 8 and telefone[3] == '-':
            result = '3' + telefone[0:3] + telefone[4:]
            return result
        elif len(telefone) == 8 and telefone[3] != '-' and telefone[0] == '3':
            return telefone
        elif len(telefone) == 7:
            result = '3' + telefone
            return result
    elif valid == 1:
        if len(telefone) == 9 and telefone[4] == '-':
            return telefone
        elif len(telefone) == 8 and telefone[3] == '-':
            result = '3' + telefone
            return result
        elif len(telefone) == 8 and telefone[3] != '-' and telefone[0] == '3':
            result = telefone[0:4] + '-' + telefone[4:]
            return result
        elif len(telefone) == 7:
            result = '3' + telefone[0:3] + '-' + telefone[3:]
            return result

## função para imprimir
def impressao(telefone):
    print(f'Telefone: {telefone}')
    print(f'Telefone possui {len(telefone)} dígitos. {classificacao(telefone)}')
    print(f'Telefone corrigido sem formatação: {formatacao(telefone, 0)}')
    print(f'Telefone corrigido com formatação: {formatacao(telefone, 1)}')


########## P R O G R A M A ##########
numero = input('Número de telefone: ')
impressao(numero)