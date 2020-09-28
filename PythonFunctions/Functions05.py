# Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais:
# taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto.
# A função “altera” o valor de custo para incluir o imposto sobre vendas.


########## P R O G R A M A ##########
def somaImposto(taxa, custo):
    return f'{(0.01*taxa)*custo + custo:.2f}'

print(somaImposto(3, 10))
print(somaImposto(5, 10))
print(somaImposto(4, 10))