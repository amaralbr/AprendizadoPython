# Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas.
# A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas dos
# sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima informada
# (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são informados ordenadas.
# Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
# Atleta: Aparecido Parente
# Nota: 9.9
# Nota: 7.5
# Nota: 9.5
# Nota: 8.5
# Nota: 9.0
# Nota: 8.5
# Nota: 9.7

# Resultado final:
# Atleta: Aparecido Parente
# Melhor nota: 9.9
# Pior nota: 7.5
# Média: 9,04


########## P R O G R A M A ##########
nome = input('Entre com o nome do atleta: ')
notas = []

while len(notas) < 7:
    nota = float(input(f'Entre com o {len(notas) + 1}º nota: '))
    notas.append(nota)

print(f'Atleta: {nome}')
print('')
for i in notas:
    print(f'Nota: {i:.1f}')

print('')
print('Resultado final:')
print(f'Atleta: {nome}')
print(f'Melhor nota: {max(notas):.1f}')
print(f'Pior nota: {min(notas):.1f}')
del(notas[notas.index(max(notas))])
del(notas[notas.index(min(notas))])
media = sum(notas) / len(notas)
print(f'Média: {media:.1f}')
print('')