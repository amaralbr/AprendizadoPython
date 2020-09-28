# Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada atleta, o
# melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um
# programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe a média dos saltos conforme a
# descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). Faça uso de uma lista para armazenar os saltos.
# Os saltos são informados na ordem da execução, portanto não são ordenados. O programa deve ser encerrado quando não for informado o nome
# do atleta. A saída do programa deve ser conforme o exemplo abaixo:
# Atleta: Rodrigo Curvêllo

# Primeiro Salto: 6.5 m
# Segundo Salto: 6.1 m
# Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m
# Quinto Salto: 5.3 m

# Melhor salto:  6.5 m
# Pior salto: 5.3 m
# Média dos demais saltos: 5.9 m

# Resultado final:
# Rodrigo Curvêllo: 5.9 m


########## P R O G R A M A ##########
nome = input('Entre com o nome do atleta: ')
saltos = []

while len(saltos) < 5:
    salto = float(input(f'Entre com o {len(saltos) + 1}º salto: '))
    saltos.append(salto)

print(f'Atleta: {nome}')
print('')
print(f'Primeiro Salto: {saltos[0]:.1f} m')
print(f'Segundo Salto: {saltos[1]:.1f} m')
print(f'Terceiro Salto: {saltos[2]:.1f} m')
print(f'Quarto Salto: {saltos[3]:.1f} m')
print(f'Quinto Salto: {saltos[4]:.1f} m')
print('')
print(f'Melhor salto: {max(saltos):.1f} m')
print(f'Pior salto: {min(saltos):.1f} m')
del(saltos[saltos.index(max(saltos))])
del(saltos[saltos.index(min(saltos))])
media = sum(saltos) / len(saltos)
print(f'Média dos demais saltos: {media:.1f} m')
print('')
print('Resultado final:')
print(f'{nome}: {media:.1f} m')