# Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
# Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
# Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
# A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
# Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que
# o usuário digite o salário inicial do funcionário.


########## P R O G R A M A ##########
import datetime

salario = float(input('Entre com o valor do salário: '))
aumento = 0.0000015
salario += salario * aumento
ano_entrada = int(input('Entre com o ano da contratação: '))
ano_atual = datetime.date.today().year
aumento_variavel = ano_entrada + 2
while aumento_variavel <= ano_atual:
    aumento *= 2
    salario += salario * aumento
    aumento_variavel += 1

print(f'{salario:.2f}')