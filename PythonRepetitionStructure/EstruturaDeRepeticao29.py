# O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que
# já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela de preços de
# pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:
# Preço do pão: R$ 0.18
# Panificadora Pão de Ontem - Tabela de preços
# 1 - R$ 0.18
# 2 - R$ 0.36
# ...
# 50 - R$ 9.00

try:
    valor = float(input('Valor da unidade do pão: '))
    if valor > 0:
        quant = 50
        valid = 1
        print('')
        while valid <= quant:
            print(f'{valid} - ${valid * valor:.2f}')
            valid += 1
        print('')
    else:
        print('Valor Inválido!')
except:
    print('-- Inválido! --')