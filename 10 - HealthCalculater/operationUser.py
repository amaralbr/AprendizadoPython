import defModuleCalc as calcParse

print('Vamos fazer 3 teste:')
print('IMC - Índice de Massa Corporal')
print('RCQ - Relação Cintura Quadril')
print('IAC - Índice de Adiposidade Corporal')
print('')
input('Aperte ENTER para começar.')


x = False
while x is False:
    print('---------------------------------------------')
    sexo = input('Qual o seu sexo (f/m)? ').lower()
    if sexo == 'f' or sexo == 'm':
        x = True
    else:
        print('Entrada inválida. Digite f ou m.')

x = False
while x is False:
    print('---------------------------------------------')
    idade = input('Digite a sua idade:')
    try:
        idade = int(idade)
        if idade > 0:
            x = True
        else:
            print('Entrada inválida. Digite um valor positivo.')
    except:
        print('Entrada inválida. Digite um número inteiro.')

x = False
while x is False:
    print('---------------------------------------------')
    altura = input('Digite a sua altura em m(0.00): ')
    try:
        altura = float(altura)
        if altura > 0.00:
            x = True
        else:
            print('Entrada inválida. Digite um número positivo.')
    except:
        print('Entrada inválida. Digite um número separado por ponto (ex.: 0.00).')

x = False
while x is False:
    print('---------------------------------------------')
    peso = input('Digite o seu peso em kg(00.0): ')
    try:
        peso = float(peso)
        if peso > 0.00:
            x = True
        else:
            print('Entrada inválida. Digite um número positivo.')
    except:
        print('Entrada inválida. Digite um número separado por ponto (ex.: 00.0).')

x = False
while x is False:
    print('---------------------------------------------')
    cintura = input('Digite a sua circunf. da cintura em cm(00.0): ')
    try:
        cintura = float(cintura)
        if cintura > 0.00:
            x = True
        else:
            print('Entrada inválida. Digite um número positivo.')
    except:
        print('Entrada inválida. Digite um número separado por ponto (ex.: 00.0).')

x = False
while x is False:
    print('---------------------------------------------')
    quadril = input('Digite a sua circunf. do quadril em cm(00.0): ')
    try:
        quadril = float(quadril)
        if quadril > 0.00:
            x = True
        else:
            print('Entrada inválida. Digite um número positivo.')
    except:
        print('Entrada inválida. Digite um número separado por ponto (ex.: 00.0).')

imc = calcParse.calcIMC(peso, altura)
imcClas = calcParse.classIMC(sexo, peso, altura)
rcq = calcParse.calcRCQ(cintura, quadril)
rcqClas = calcParse.classRCQ(idade, sexo, cintura, quadril)
iac = calcParse.calcIAC(quadril, altura)
iacClas = calcParse.classIAC(sexo, quadril, altura)

print('---------------------------------------------')
print('')
print('--------------R E S U L T A D O--------------')
print(f'O seu IMC é {imc:.2f}, {imcClas}.') # print('O seu IMC é ' + str(round(imc, 2)) + ', ' + imcClas)
print(f'O seu RCQ é {rcq:.2f}, {rcqClas}.') # print('O seu RCQ é ' + str(round(rcq, 2)) + ', ' + rcqClas)
print(f'O seu IMC é {iac:.0f}, {iacClas}.') # print('O seu IAC é ' + str(round(iac, 0)) + ', ' + iacClas)
print('---------------------------------------------')
