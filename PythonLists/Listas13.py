# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
# Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e
# em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).


########## P R O G R A M A ##########
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
temperaturas = []
while len(temperaturas) < 12:
    temp = float(input(f'Temperatura média de {meses[len(temperaturas)]}: '))
    temperaturas.append(temp)
x=1
y=0
for i in temperaturas:
    if i >= (sum(temperaturas) / len(temperaturas)):
        if temperaturas.index(i) < 11:
            print(f'{x} - {meses[y]}', end = ', ')
            x += 1
        elif temperaturas.index(i) == 11:
            print(f'{x} - {meses[y]}.')
    y += 1
    