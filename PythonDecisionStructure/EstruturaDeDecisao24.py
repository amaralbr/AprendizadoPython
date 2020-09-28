# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.


## função para validar par ou impar
def validParIm(x):
    if x % 2 == 0:
        return 'par'
    else:
        return 'impar'

## função para validar positivo ou negativo
def validPosNeg(x):
    if x >= 0:
        return 'positivo'
    else:
        return 'negativo'

## função para validar intero ou decimal
def validIntDec(x):
    if round(x) == x:
        return 'inteiro'
    else:
        return 'decimal'

## função para converter str para número
def convertNumb(x):
    try:
        x = int(x)
        return x
    except:
        x = float(x)
        return x

## função para realizar a operação definida
def opProg(op, num1, num2):
    if op == 'SOMA':
        r = num1 + num2
        print(f'>>> O resultado da {op} entre {num1} e {num2} é: {r:.1f} >>> um número {validParIm(r)}, {validPosNeg(r)} e {validIntDec(r)}.')
    elif op == 'SUB':
        r = max(num1,num2) - min(num1, num2)
        print(f'>>> O resultado da {op} entre {num1} e {num2} é: {r:.1f} >>> um número {validParIm(r)}, {validPosNeg(r)} e {validIntDec(r)}.')
    elif op == 'MULT':
        r = num1 * num2
        print(f'>>> O resultado da {op} entre {num1} e {num2} é: {r:.1f} >>> um número {validParIm(r)}, {validPosNeg(r)} e {validIntDec(r)}.')
    elif op == 'DIV':
        r = max(num1, num2) / min(num1, num2)


########## P R O G R A M A ##########
valid = True
while valid is True:
    try:
        num1 = convertNumb(input('1. Entre com um número: '))
        num2 = convertNumb(input('2. Entre com outro número: '))
        op = input('3. Qual operação você quer fazer (SOMA/SUB/MULT/DIV): ').upper()
        if op == 'SOMA' or op == 'SUB' or op == 'MULT' or op == 'DIV':
            opProg(op, num1, num2)
        else:
            op = int(op) ## comando inválido para levar ao except
        question = input('Outra entrada? (Qualquer tecla para sair ou "S" Sim): ').upper()
        if question != 'S':
            valid = False
        else:
            continue
    except:
        print('-------------------------')
        print('>>> Entrada Inválida! <<<')