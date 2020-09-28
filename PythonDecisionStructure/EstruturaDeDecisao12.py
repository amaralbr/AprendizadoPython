# Faça um programa para o cálculo de uma folha de pagamento,
# sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo)
# e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado
# (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20%
# Imprima na tela as informações, dispostas conforme o exemplo abaixo.
# No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#         Salário Bruto: (5 * 220)        : R$ 1100,00
#         (-) IR (5%)                     : R$   55,00  
#         (-) INSS ( 10%)                 : R$  110,00
#         FGTS (11%)                      : R$  121,00
#         Total de descontos              : R$  165,00
#         Salário Liquido                 : R$  935,00

def calcSalario(valorHora, horasMes):
    resultado = valorHora * horasMes
    return resultado

def ir(salario):
    if salario <= 900.00:
        return 0
    elif salario > 900.00 and salario <= 1500.00:
        return 0.05
    elif salario > 1500.00 and salario <= 2500.00:
        return 0.10
    elif salario > 2500.00:
        return 0.20

def tela(salario, valorHora, horasMes):
    y = ir(salario)
    print(f'Salário Bruto: ({valorHora} * {horasMes})'.ljust(35) + f': ${salario:.2f}')
    print(f'(-) IR ({y * 100}%)'.ljust(35) + f': ${salario * y:.2f}')
    print('(-) INSS (10%)'.ljust(35) + f': ${salario * 0.10:.2f}')
    print('(-) SINDICATO (3%)'.ljust(35) + f': ${salario * 0.03:.2f}')
    print('FGTS (11%)'.ljust(35) + f': ${salario * 0.11:.2f}')
    print('Total de desconto'.ljust(35) + f': ${(salario * y) + (salario * 0.10) + (salario * 0.03):.2f}')
    print('Salário Líquido'.ljust(35) + f': ${salario - ((salario * y) + (salario * 0.10) + (salario * 0.03)):.2f}')

valorHora = float(input('Entre com o valor da hora trabalhada: '))
horasMes = int(input('Entre com o valor das horas trabalhadas no mês: '))

ir(calcSalario(valorHora, horasMes))
tela(calcSalario(valorHora, horasMes), valorHora, horasMes)