# Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for
# informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
# Mostre a quantidade de valores que foram lidos;
# Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# Calcule e mostre a soma dos valores;
# Calcule e mostre a média dos valores;
# Calcule e mostre a quantidade de valores acima da média calculada;
# Calcule e mostre a quantidade de valores abaixo de sete;
# Encerre o programa com uma mensagem;

########## P R O G R A M A ##########
notas = []
while True:
    nota = int(input('Entre com uma nota: '))
    if nota > 0:
        notas.append(nota)
    elif nota == -1:
        break
print('...')
for i in notas:
    print(i, end = " ")
print('')
for i in reversed(notas):
    print(i)
print(f'Soma: {sum(notas)}')
print(f'Média: {sum(notas) / len(notas):.1f}')
cont1 = 0
for i in notas:
    if i > (sum(notas) / len(notas)):
        cont1 += 1
print(f'Valores acima da média: {cont1}')
cont2 = 0
for i in notas:
    if i < 7:
        cont2 += 1
print(f'Valores abaixo de 7: {cont2}')
print('...')
print('PROGRAMA ENCERRADO!')