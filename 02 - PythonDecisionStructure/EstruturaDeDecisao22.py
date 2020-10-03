# Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).

def validImPar(x):
    if x % 2 == 0:
        print('Número par!')
    else:
        print('Número impar!')


valid = False
while valid is False:
    try:
        print('--------------------')
        num = int(input('Entre com um número inteiro: '))
        validImPar(num)
        valid = True
    except:
        print('--------------------')
        print('>>> Entrada inválida! <<<')