# Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de
# cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa).
# Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
# Maior e Menor Acerto;
# Total de Alunos que utilizaram o sistema;
# A Média das Notas da Turma.
# Gabarito da Prova:

# 01 - A
# 02 - B
# 03 - C
# 04 - D
# 05 - E
# 06 - E
# 07 - D
# 08 - C
# 09 - B
# 10 - A
# Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.


########## P R O G R A M A ##########
gabarito = []
while True:
    app = input(f'Resposta da questão {len(gabarito) + 1}: ').upper()
    gabarito.append(app)
    questaoprof = input('Deseja registrar outra questão no gabarito (S/N)? ').upper()
    if questaoprof == 'S':
        continue
    else:
        break
notas = []
while True:
    nota = 0
    repet = len(gabarito)
    valid = 0
    print('<<< >>>')
    while valid < repet:
        questao = input(f'Entre com a resposta da questão {valid + 1}: ').upper()
        if questao == gabarito[valid]:
            nota += 1
            valid +=1
            continue
        else:
            valid += 1
    notas.append(nota)
    print('------')
    question = input('Outro aluno vai utilizar o sistema (S/N)? ').upper()
    if question == 'S':
        continue
    else:
        break
print('---------------------------------------------')
print(f'Maior n\' acerto: {max(notas)}     Menor n\' acerto: {min(notas)}')
print(f'Utilizaram o sistema: {len(notas)} alunos')
print(f'A média de notas da turma é {(sum(notas) / len(notas)):.1f}.')
print('---------------------------------------------')