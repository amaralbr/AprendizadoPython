# Faça um Programa que leia dois vetores com 10 elementos cada.
# Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.


########## P R O G R A M A ##########
numeros1 = [1,2,3,4,5,6,7,8,9,10]
numeros2 = [11,12,13,14,15,16,17,18,19,20]
numeros3 = []
x = 0
while len(numeros3) < 20:
    numeros3.append(numeros1[x])
    numeros3.append(numeros2[x])
    x += 1
print(numeros3)