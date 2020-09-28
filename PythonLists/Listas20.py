# Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor.
# Depois, mostre quantas vezes cada valor foi conseguido.
# Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.


########## P R O G R A M A ##########
import random

lancamentos = []
contadores = [0,0,0,0,0,0]
while len(lancamentos) < 100:
    lancamentos.append(random.randint(1, 6))
for i in lancamentos:
    contadores[i-1] += 1
cont=1
for i in contadores:
    print(f'Número {cont} repete: {i} vezes.')
    cont+=1