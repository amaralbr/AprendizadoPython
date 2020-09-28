# Faça um programa que calcule o mostre a média aritmética de N notas.

try:
    numbNotas = int(input('Quantas notas serão lançadas: '))
    if numbNotas > 0:
        valid = 1
        notas = []
        while valid <= numbNotas:
            n = 0
            while True:
                try:
                    n = int(input(f'Entre com a Nota {valid}: '))
                    if n >= 0:
                        break
                    else:
                        continue
                except:
                    continue
            notas.append(n)
            valid += 1
        mediaNotas = sum(notas) / len(notas)
        print(f'Média: {mediaNotas:.1f}')
    else:
        print('-- Número negativo inválido! --')
except:
    print('------ Entrada Inválida! ------')