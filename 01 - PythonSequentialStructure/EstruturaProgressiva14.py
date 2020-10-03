# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o
# rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que
# o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve
# pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa
# que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso
# a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
# Imprima os dados do programa com as mensagens adequadas.

def excesso(kg):
    if kg > 50:
        r = kg - 50
        return r
    elif kg <=50:
        r = 0
        return r

def multa(kg):
    if kg > 50:
        r = (kg - 50) * 4.00
        return r
    else:
        r = 0
        return r

kg = int(input('Quantos kilos de peixe você pescou? '))
excesso = excesso(kg)
multa = multa(kg)
print(f'Você está excedendo {excesso}kg de peixe.')
print(f'Portanto, deve pagar ${multa:.2f} de multa.')