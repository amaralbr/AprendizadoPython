# Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta.
# O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento, que
# calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a
# execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação.
# Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia.
# O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de
# multa, mais 0,1% de juros por dia de atraso.


########## P R O G R A M A ##########
def valorPagamento (valorPrestacao, diasEmAtraso):
    if diasEmAtraso == 0:
        print(f'${valorPrestacao:.2f}')
        return valorPrestacao
    elif diasEmAtraso > 0:
        print(f'${valorPrestacao + valorPrestacao*0.03 + valorPrestacao*(0.001*diasEmAtraso):.2f}')
        return valorPrestacao + valorPrestacao*0.03 + valorPrestacao*(0.001*diasEmAtraso)

prestacoes = 0
valores = 0
while True:
    valorPrestacao = float(input('Entre com um valor: $'))
    if valorPrestacao == 0:
        break
    else:
        diasEmAtraso = int(input('Quantos dia de atraso (0 - Nenhum)? '))
        prestacoes += 1
        valores += valorPagamento(valorPrestacao, diasEmAtraso)

print('-----')
print(f'Hoje, foi recebido {prestacoes} prestações no total de ${valores:.2f}')