# Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M.
# A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação
# A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se
# é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.


########## P R O G R A M A ##########
def conversao(hh, mm):
    def amPm (hh):
        if hh >= 12:
            return 'P.M.'
        else:
            return 'A.M.'
    if hh == 0:
        return f'12:{mm} {amPm(hh)}'
    elif hh >= 1 and hh <= 12:
        return f'{hh}:{mm} {amPm(hh)}'
    elif hh >= 13:
        return f'{hh-12}:{mm} {amPm(hh)}'

print(conversao(12, 53))
print(conversao(0, 25))
print(conversao(9, 30))
print(conversao(17, 15))