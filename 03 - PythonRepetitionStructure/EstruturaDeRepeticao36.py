# Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a
# sua altura em centímetros.
# Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

#### Função para encontrar valor mais alto
def higher(list):
    i = 0
    listmax = []
    for i in list:
        height = i[1]
        listmax.append(height)
    result = listmax.index(max(listmax))
    return result
    
#### Função para encontrar valor mais baixo
def lower(list):
    i = 0
    listmin = []
    for i in list:
        height = i[1]
        listmin.append(height)
    result = listmin.index(min(listmin))
    return result

########## P R O G R A M A ##########
list = []
valid = 1

while valid <= 4:
    app = []
    app.append(int(input('Entre com o número do aluno: ')))
    app.append(float(input('Entre com a altura do aluno: ')))
    list.append(app)
    valid += 1

max = higher(list)
min = lower(list)
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
print(f'O aluno {list[max][0]} é o mais alto com {list[max][1]}m.')
print(f'O aluno {list[min][0]} é o mais baixo com {list[min][1]}m.')
