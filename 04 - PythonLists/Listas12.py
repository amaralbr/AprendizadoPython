# Foram anotadas as idades e alturas de 30 alunos.
# Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.


########## P R O G R A M A ##########
alturas = [1.65,1.63,1.68,1.65,1.71,1.59,1.66,1.64,1.89,1.78,1.63,1.65,1.71,1.71,1.72,1.72,1.72,1.85,1.73,1.58,1.59,1.57,1.74,1.65,1.68,1.61,1.62,1.81,1.65,1.66]
idades = [12,13,14,15,12,12,13,14,13,12,12,14,15,15,12,13,12,14,15,13,13,12,12,15,14,13,15.13,12,12]
mediaaltura = sum(alturas) / len(alturas)
contador = 0
for i in idades:
    if i >= 13:
        if alturas[idades.index(i)] < mediaaltura:
            contador += 1
print(contador)