# Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
# 1 , 2, 3, 4  - Votos para os respectivos candidatos 
# (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
# 5 - Voto Nulo
# 6 - Voto em Branco
# Faça um programa que calcule e mostre:
# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# A percentagem de votos nulos sobre o total de votos;
# A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.


########## P R O G R A M A ##########
lista = [[1, 'José'], [2, 'João'], [3, 'Maria'], [4, 'Nelsa'], [5, 'Nulo'], [6, 'Branco']]
votacao = []
while True:
    try:
        print('<<<< >>>>')
        voto = int(input('Entre com o número: '))
        if voto > 0 and voto < 7:
            for i in lista:
                if voto == i[0]:
                    print(f'Seu voto é: {i[1]}')
            question = input('Você confirma seu voto (S/N)? ').upper()
            if question == 'S':
                votacao.append(voto)
            else:
                continue
        elif voto == 0:
            break
        else:
            print('Voto Inválido!')
    except:
        print('Erro')
totalvotos = len(votacao)
print('---------------')
for i in lista:
    contador = 0
    for j in votacao:
        if j == i[0]:
            contador += 1
    if i[0] <= 4:
        print(f'{i[0]} - {i[1]}: {contador} votos.')
    else:
        print(f'{i[0]} - {i[1]}: {contador} votos. {((100 * contador) / totalvotos):.2f}% sobre o total.')