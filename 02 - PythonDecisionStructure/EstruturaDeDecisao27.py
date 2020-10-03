# # Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                       Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
# receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e
# a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

#função de cáclulo
def calc(mor, mac):
    total = mor + mac
    valorMor = 0
    valorMac = 0
    if mor >= 5:
        valorMor = mor * 2.2
    else:
        valorMor = mor * 2.5
    if mac >= 5:
        valorMac = mor * 1.5
    else:
        valorMac = mor * 1.8
    valor = valorMor + valorMac
    if total >= 8:
        valor -= valor * 0.1
        return valor
    else:
        return valor

########## P R O G R A M A ##########
morango = float(input('Entre com a quantidade de morangos (kg): '))
maca = float(input('Entre com a quantidade de maças (kg): '))
print(f'Total: $ {calc(morango, maca):.2f}')
