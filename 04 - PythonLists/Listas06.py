# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
# imprima o número de alunos com média maior ou igual a 7.0.


########## P R O G R A M A ##########
alunos = []
while len(alunos) < 10:
    notas = []
    while len(notas) < 4:
        print('-----')
        nota = float(input(f'Entre com a {len(notas) + 1}ª do aluno {len(alunos) + 1}:'))
        notas.append(nota)
    alunos.append(sum(notas) / len(notas))
contador = 0
for i in alunos:
    if i >= 7:
        contador += 1
print('-----')
print(f'Alunos com média maior ou igual a 7.0: {contador}')