# Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões.
# O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor
# que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470.
# Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
# $200 - $299
# $300 - $399
# $400 - $499
# $500 - $599
# $600 - $699
# $700 - $799
# $800 - $899
# $900 - $999
# $1000 em diante
# Desafio: Crie uma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.


########## P R O G R A M A ##########
faixas = [[200, 299], [300, 399], [400, 499], [500, 599], [600, 699], [700, 799], [800, 899], [900, 999], [1000]]
contadores = [0, 0, 0, 0, 0, 0, 0, 0, 0]
while True:
    try:
        vendas = float(input('Entre com o valor das vendas:'))
        if vendas == 0.0:
            break
        else:
            salario = 200 + (vendas * 0.09)
            for i in faixas:
                if faixas.index(i) < len(faixas) - 1:
                    if salario >= i[0] and salario <= i[1]:
                        contadores[faixas.index(i)] = contadores[faixas.index(i)] + 1
                elif faixas.index(i) == len(faixas) - 1:
                    if salario >= i[0]:
                        contadores[faixas.index(i)] = contadores[faixas.index(i)] + 1
    except:
        print('-- Entrada Inválida! --')
print('---')
for i in faixas:
    if faixas.index(i) < len(faixas) -1:
        print(f'Entre ${i[0]} e ${i[1]}: {contadores[faixas.index(i)]} vendedores.')
    elif faixas.index(i) == len(faixas) - 1:
        print(f'Acima de ${i[0]}: {contadores[faixas.index(i)]} vendedores.')