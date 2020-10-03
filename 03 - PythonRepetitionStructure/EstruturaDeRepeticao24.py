# Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da
# turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

try:
    numbPessoas = int(input('Quantas pessoas há na turma: '))
    if numbPessoas > 0:
        valid = 1
        idades = []
        while valid <= numbPessoas:
            n = 0
            while True:
                try:
                    n = int(input(f'Entre com idade da pessoa {valid}: '))
                    if n >= 0:
                        break
                    else:
                        continue
                except:
                    continue
            idades.append(n)
            valid += 1
        mediaIdades = sum(idades) / len(idades)
        if mediaIdades >= 0 and mediaIdades < 26:
            print('A turma é jovem!')
        elif mediaIdades >= 26 and mediaIdades < 60:
            print('A turma é adulta!')
        elif mediaIdades >= 60:
            print('A turma é idosa!')
    else:
        print('-- Número negativo inválido! --')
except:
    print('------ Inválido! ------')