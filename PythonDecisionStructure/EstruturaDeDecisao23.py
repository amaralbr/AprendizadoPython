# Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.




valid = False
while valid is False:
    try:
        num = input('Entre com um número: ')
        try:
            num = int(num)
            print('Número inteiro!')
            valid = True
        except:
            num = float(num)
            print('Número decimal!')
            valid = True
    except:
        print('>>> Entrada inválida! <<<')
