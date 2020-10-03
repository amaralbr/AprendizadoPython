# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
# Imprima a idade e a altura na ordem inversa a ordem lida.


########## P R O G R A M A ##########
idades = []
alturas = []
while len(idades) < 5:
    print('-----')
    idade = int(input(f'Entre com a idade da pessoa {len(idades) + 1}: '))
    altura = float(input(f'Entre com a altura da pessoa {len(alturas) + 1}: '))
    idades.append(idade)
    alturas.append(altura)
x = 5
while x > 0:
    print('-----')
    print(f'Idade {x}: {idades[x-1]}')
    print(f'Altura {x}: {alturas[x-1]}')
    x -= 1