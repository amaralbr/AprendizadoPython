# Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados:
# valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
# Os juros e a quantidade de parcelas seguem a tabela abaixo:
# Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
# 1       0
# 3       10
# 6       15
# 9       20
# 12      25
# Exemplo de saída do programa:
# Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
# R$ 1.000,00     0               1                       R$  1.000,00
# R$ 1.100,00     100             3                       R$    366,00
# R$ 1.150,00     150             6                       R$    191,67


########## P R O G R A M A ##########
valor = float(input('Entre com o valor: $ '))

tabela = []
valid = 1
juros = 0
parcelas = 1
while valid <= 5:
    app = []
    divida = valor + (valor * (juros / 100))
    valorjuros = divida - valor
    valorparcela = divida / parcelas
    app.append(divida)
    app.append(valorjuros)
    app.append(parcelas)
    app.append(valorparcela)
    tabela.append(app)
    if valid == 1:
        juros = 10
        parcelas = 3
        valid += 1
    else:
        juros += 5
        parcelas += 3
        valid += 1

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
print(f'Valor da Dívida    Valor dos Juros    Qt Parcelas    Valor da Parcela')
for i in tabela:
    valor_divida, valor_juros, parcelas, valor_parcela = i
    print(f'{valor_divida:^15,.2f}    {valor_juros:^15,.2f}    {parcelas:^11.0f}    {valor_parcela:^16,.2f}')