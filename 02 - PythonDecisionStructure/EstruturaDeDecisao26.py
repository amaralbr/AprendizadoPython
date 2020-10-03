# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
# calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

# função de cálculo
def calc(l, comb):
    if l >= 20 and comb == 'A':
        result = l * 1.9
        result -= result * 0.05
        return result
    elif l < 20 and comb == 'A':
        result = l * 1.9
        result -= result * 0.03
        return result
    if l >= 20 and comb == 'G':
        result = l * 2.5
        result -= result * 0.06
        return result
    elif l < 20 and comb == 'G':
        result = l * 2.5
        result -= result * 0.04
        return result

########## P R O G R A M A ##########
try:
    litros = float(input('Litros: '))
    combustivel = input('Combustível (A-álcoo, G-gosolina): ').upper()
    if combustivel == 'A' or combustivel == 'G':
        print('------------------------')
        print(f'Valor: R${calc(litros, combustivel):.2f}')
except:
    print('>>>>> Entrada Inválida! <<<<<')