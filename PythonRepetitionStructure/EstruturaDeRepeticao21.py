# Altere o programa de cálculo dos números primos, informando,
# caso o número não seja primo, por quais número ele é divisível.

valid = True
while valid is True:
    try:
        primo = []
        print('---------------------------')
        numb = int(input('Entre com um número inteiro: '))
        x = numb
        while x > 0:
            result = numb % x
            if result == 0:
                primo.append(x)
            x -= 1    
            continue    
        if len(primo) > 2:
            print('<<< Este não é um número primo. >>>')
            print(f'Ele é divisível por: {primo}')
        elif len(primo) == 2 and (primo[0] == numb and primo[1] == 1):
            print('>>> Este é um número primo. <<<')
        else:
            print('--- Inválido! ---')
        print('---------------------------')
        while True:
            question = input('Deseja pesquisar outro número (S/N)? ').upper()
            if question == 'S':
                valid = True
                break
            elif question == 'N':
                valid = False
                break        
    except:
        print('----- Entrada Inválida! -----')