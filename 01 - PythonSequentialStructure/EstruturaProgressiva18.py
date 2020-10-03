# Faça um programa que peça o tamanho de um arquivo para download (em MB)
# e a velocidade de um link de Internet (em Mbps), calcule e informe o
# tempo aproximado de download do arquivo usando este link (em minutos).

def calcV(b, v):
    t = (b / v) / 60
    return t
tamanho = float(input('Tamanho do arquivo em MB: '))
velocidade = float(input('Velocidade em Mbps: '))
tempo = calcV(tamanho, velocidade)
print(f'Tempo de download: {tempo:.1f} minutos.')