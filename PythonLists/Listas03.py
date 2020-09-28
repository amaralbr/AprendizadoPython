# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.


########## P R O G R A M A ##########
notas = []
while len(notas) < 4:
    nota = float(input(f'Entre com a {len(notas) + 1}ª nota: '))
    notas.append(nota)
print('-----')
for i in notas:
    print(f'Nota {notas.index(i) + 1}: {i:.1f}')
print(f'Média: {sum(notas) / len(notas)}')