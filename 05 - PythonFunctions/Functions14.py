# Quadrado mágico. Um quadrado mágico é aquele dividido em linhas 
# e colunas, com um número em cada posição e no qual a soma das linhas,
# colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:

# 8  3  4 
# 1  5  9
# 6  7  2
# Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima.
# Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado.
# Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3.


########## P R O G R A M A ##########
def quadradoMagico():
    numeros = [1,2,3,4,5,6,7,8,9]
    combinacoes = []
    for i in range(1, 10):
        for j in numeros:
            for k in numeros:
                if i + j + k == 15 and (i != j and i != k and j != k):
                    combinacoes.append([i, j, k])
    for i in combinacoes:
        linha1 = i
        for j in combinacoes:
            linha2 = j
            for k in combinacoes:
                linha3 = k
                if (linha1[0] + linha2[0] + linha3[0] == 15) and\
                   (linha1[1] + linha2[1] + linha3[1] == 15) and\
                   (linha1[2] + linha2[2] + linha3[2] == 15) and\
                   (linha1[0] + linha2[1] + linha3[2] == 15) and\
                   (linha1[2] + linha2[1] + linha3[0] == 15):
                   if (linha1[0] not in linha2) and\
                      (linha1[1] not in linha2) and\
                      (linha1[2] not in linha2):
                        print(linha1)
                        print(linha2)
                        print(linha3)
                        print('')

quadradoMagico()