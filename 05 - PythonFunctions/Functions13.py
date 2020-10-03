# Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘.
# Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e
# o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma elegante.


########## P R O G R A M A ##########
def desenhaMoldura(linhas, colunas):
    def vL(l):
        if l < 1:
            return 1
        elif l > 20:
            return 20
        else:
            return l
    def vC(c):
        if c < 1:
            return 1
        elif c > 20:
            return 20
        else:
            return c
        
    lin = range(vL(linhas))
    for i in lin:
        if i == 0:
            print('-' * vC(colunas))
        elif i > 0 and i < len(lin) - 1:
            print('|' + '+' * (vC(colunas) - 2) + '|')
        elif i == len(lin) - 1:
            print('-' * vC(colunas))

try:
    linhas = int(input('Entre com o número de linhas: '))
    colunas = int(input('Entre com o número de colunas: '))
    if linhas != colunas:
        desenhaMoldura(linhas, colunas)
except:
    print('Entrada Inválida!')