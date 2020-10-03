# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles.
# O usuário deverá informar a quantidade de CDs e o valor pago em cada um.

try:
    quant = int(input('Quantos CDs foram comprados: '))
    if quant > 0:
        valid = 1
        totalValue = []
        while valid <= quant:
            while True:
                valueCD = 0
                try:
                    valueCD = float(input(f'Valor do CD {valid}: $'))
                    if valueCD > 0:
                        totalValue.append(valueCD)
                        break
                    else:
                        continue
                except:
                    continue
            valid += 1
        print('')
        print(f'Valor total investido: ${sum(totalValue):.2f}')
        print(f'Valor médio/CD: ${sum(totalValue) / len(totalValue):.2f}')
    else:
        print('-- Null --')
except:
    print('-- Inválido! --')