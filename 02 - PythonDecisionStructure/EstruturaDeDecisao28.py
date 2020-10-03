# # O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                       Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
# porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um
# desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, 
# contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.


## função de cálculo do valor
def calcValor(carne, quantidade, pgto):
    valor = 0
    if carne == 1 and quantidade >= 5:
        valor = quantidade * 5.8
        return valor
    elif carne == 1 and quantidade < 5:
        valor = quantidade * 4.9
        return valor
    elif carne == 2 and quantidade >= 5:
        valor = quantidade * 6.8
        return valor
    elif carne == 2 and quantidade < 5:
        valor = quantidade * 5.9
        return valor
    elif carne == 3 and quantidade >= 5:
        valor = quantidade * 7.8
        return valor
    elif carne == 3 and quantidade < 5:
        valor = quantidade * 6.9
        return valor

## função de cálculo do desconto
def calcDesc(carne, quantidade, pgto):
    if pgto == 1:
        return 0
    elif pgto == 2:
        return 0
    elif pgto == 3:
        result = calcValor(carne, quantidade, pgto) * 0.05
        return result

## função de cálculo do pagamento final
def valorPgto(carne, quantidade, pgto):
    result = calcValor(carne, quantidade, pgto) - calcDesc(carne, quantidade, pgto)
    return result

## função de impressão do cupom fiscal
def printCF(carne, quantidade, pgto):
    print('-----------------------------')
    print('   C U P O M   F I S C A L   ')
    print('')
    cn = ''
    if carne == 1:
        cn = 'File Duplo'
    elif carne == 2:
        cn = 'Alcatra'
    elif carne == 3:
        cn = 'Picanha'
    print(f'1. {cn} : {quantidade:.1f}kg : ${calcValor(carne, quantidade, pgto):.2f}')
    pg = ''
    if pgto == 1:
        pg = 'Dinheiro'
    elif pgto == 2:
        pg = 'Cartão'
    elif pgto == 3:
       pg = 'Cartão Tabajara'
    print(f'   {pg} : Desconto: -${calcDesc(carne, quantidade, pgto):.2f}')
    print(f'   TOTAL A PAGAR  : ${valorPgto(carne, quantidade, pgto):.2f}')
    print('-----------------------------')



########## P R O G R A M A ##########
try:
    carne = int(input('Qual o tipo da carne (1-File Duplo/2-Alcatra/3-Picanha): '))
    quantidade = float(input('Quantidade de carne (kg): '))
    pgto = int(input('Forma de pagamento (1-Dinheiro/2-Cartão/3-Cartão Tabajara): '))
    printCF(carne, quantidade, pgto)
except:
    print('-----------------------------')
    print('Entrada Inválida!')