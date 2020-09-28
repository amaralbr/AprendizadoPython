# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.


########## P R O G R A M A ##########
numeros1 = [1,2,3,4,5,6,7,8,9,10]
numeros2 = [11,12,13,14,15,16,17,18,19,20]
numeros3 = [21,22,23,24,25,26,27,28,29,30]
numeros4 = []
x = 0
while len(numeros4) < 30:
    numeros4.append(numeros1[x])
    numeros4.append(numeros2[x])
    numeros4.append(numeros3[x])
    x += 1
print(numeros4)