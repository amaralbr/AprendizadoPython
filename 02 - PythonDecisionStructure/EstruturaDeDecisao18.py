# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

data = input('Entre com uma data (dd/mm/aaaa):')

dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:])

if mes >= 1 and mes <= 12:
    X = True
else:
    x = False
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    if mes == 2:
        if dia >= 1 and dia <= 29:
            x = True
        else:
            x = False
else:
    if mes == 2:
        if dia >= 1 and dia <=28:
            x = True
        else:
            x = False
if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if dia >= 1 and dia <= 31:
        x = True
    else:
        x = False
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia >= 1 and dia <= 30:
        x = True
    else:
        x = False

if x is True:
    print('>>> Data válida! >>>')
else:
    print('<<< Data inválida! <<<')