#Faça um programa que calcule o número médio de alunos por turma.
# Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

try:
    turmas = int(input('Número de turmas: '))
    if turmas > 0:
        alunos = []
        valid = 1
        while valid <= turmas:
            quant = 0
            while True:
                try:
                    quant = int(input(f'Entre com o número de alunos da Turma {valid}: '))
                    if quant > 0 and quant <= 40:
                        alunos.append(quant)
                        break
                    else:
                        continue
                except:
                    continue
            valid += 1
        media = sum(alunos) / len(alunos)
        print('')
        print(f'Média de aluno/turma: {media:.0f}')
    else:
        print('-- Número negativo inválido! --')
except:
    print('------ Entrada Inválida! ------')