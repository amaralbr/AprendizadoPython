# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do
# saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão
# as de 2, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10,
# uma nota de 5 e quatro notas de 1.

def calcNotas(x, y):
    xi = x
    notas = []
    valorNotas = [100, 50, 20, 10, y]
    _100 = int(x / 100)
    x = x % 100
    notas.append(_100)
    _50 = int(x / 50)
    x = x % 50
    notas.append(_50)
    _20 = int(x / 20)
    x = x % 20
    notas.append(_20)
    _10 = int(x / 10)
    x = x % 10
    notas.append(_10)
    _00 = int(x / y)
    x = x % y
    notas.append(_00)
    
    print('')
    print(f'Para saque de $ {xi} será fornecido:')
    z = 0
    while z <= (len(notas) - 1):
        if notas[z] != 0:
            print(f'({notas[z]}) notas de $ {valorNotas[z]}')
        z += 1
    
    print('')
    print('#################################')



valid = False
while valid is False:
    try:
        print('#################################')
        valor = int(input('Entre com o valor do Saque (Mín: $ 10 - Máx: $ 600): '))
        if valor % 2 == 0:
            calcNotas(valor, 2)
            valid = True
        elif valor % 5 == 0:
            calcNotas(valor, 5)
            valid = True
        elif valor % 2 != 0 and valor % 5 != 0:
            print('Valor inválido! O valor deve ser múltiplo de 2 ou 5.')
    except:
        print('Valor inválido! Entre com um número inteiro.')