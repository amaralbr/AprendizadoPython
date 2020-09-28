# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

x = 1
while x <= 18:
    numb = int(input('Entre com um número inteiro menor do que 1000: '))
    if numb < 10:
        numb = str(numb)
        print(f'{numb} = {numb[0]} unidades.')
    elif numb >=10 and numb < 100:
        numb = str(numb)
        print(f'{numb} = {numb[0]} dezenas e {numb[1]} unidades.')
    elif numb >= 100 and numb < 1000:
        numb = str(numb)
        print(f'{numb} = {numb[0]} centenas, {numb[1]} dezenas e {numb[2]} unidades.')
    elif numb >= 1000:
        print('Entrada inválida!')
    x += 1