# Faça um Programa que peça os 3 lados de um triângulo.
# O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

def validacaoTriangulo(x, y, z):
    if x < (y + z) and y < (z + x) and z < (x + y):
        return 1
    else:
        return 0

def classificacao(x, y ,z):
    if x == y == z:
        c = 'equilátero'
        return c
    elif x == z or x == y or y == z:
        c = 'isósceles'
        return c
    elif x != y != z:
        c = 'escaleno'
        return c

def tela(x, y, z):
    if validacaoTriangulo(x, y, z) == 1:
        print(f'Os valores podem formar um triangulo {classificacao(x, y, z)}.')
    elif validacaoTriangulo(x, y, z) == 0:
        print('Os valores não formam um trinângulo.')

def validNumb(x):
    try:
        x = int(x)
        return x
    except ValueError:
        return 'S'


x = True
while x is True:
    print('--------------------')
    n1 = input('Entre com o primeiro número: ')
    n2 = input('Entre com o segundo número: ')
    n3 = input('Entre com o terceiro número: ')
    print('--------------------')
    validNumb(n1)
    validNumb(n2)
    validNumb(n3)
    if validNumb(n1) == 'S' or validNumb(n2) == 'S' or validNumb(n3) == 'S':
        print('>>> Entre com um número inteiro. <<<')
        continue
    if validNumb(n1) < 0 or validNumb(n2) < 0 or validNumb(n3) < 0:
        print('>>> Entre apenas com valores positivos! <<<')
        continue
    else:
        tela(validNumb(n1), validNumb(n2), validNumb(n3))
        print('--------------------')
        question1 = input('Continue (S/N)? ').upper()
        if question1 == 'S':
            continue
        else:
            x = False