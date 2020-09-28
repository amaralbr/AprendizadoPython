# Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

# quantos espaços em branco existem na frase.
# quantas vezes aparecem as vogais a, e, i, o, u.


########## P R O G R A M A ##########
frase = input(':')
vogais = [' ','a','e','i','o','u']
contadores = [0,0,0,0,0,0]
for i in frase:
    for j in vogais:
        if i == j:
            contadores[vogais.index(i)] += 1
print(f'A frase contém {contadores[0]} espaços em branco.')
for i in range(len(contadores)):
    if i == 0:
        True
    else:
        print(f'A vogal \"{vogais[i]}\" aparece {contadores[i]} na frase.')