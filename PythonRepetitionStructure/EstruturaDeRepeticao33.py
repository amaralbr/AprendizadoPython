# Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a
# tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados
# também pelo usuário, conforme exemplo abaixo:
# Montar a tabuada de: 5
# Começar por: 4
# Terminar em: 7

# Vou montar a tabuada de 5 começando em 4 e terminando em 7:
# 5 X 4 = 20
# 5 X 5 = 25
# 5 X 6 = 30
# 5 X 7 = 35

########## P R O G R A M A ##########
try:
    tabuada = int(input('Montar tabuada de: '))
    inicio = int(input('Começar por: '))
    fim = int(input('Terminar em: '))
    if inicio < fim:
        print('')
        while inicio <= fim:
            print(f'{tabuada} X {inicio} = {tabuada * inicio}')
            inicio += 1
    else:
        print('-- Primeiro valor deve ser menor do que o segundo. --')
except:
    print('------ Inválido! ------')