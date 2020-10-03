# Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
# O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
# Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

try:
    numb = int(input('Entre com um número inteiro: '))
    if numb > 1:
        x = 1
        primos = []
        while x <= numb:
            n1 = 1
            n2 = x
            primo = []
            while n2 >= n1:
                result = x % n2
                if result == 0:
                    primo.append(n2)
                n2 -= 1    
            if len(primo) == 2 and (primo[0] == x and primo[1] == 1):
                primos.append(x)
            x += 1
        print(f'Os números primos entre 1 e {numb} são: {primos}')
    else:
        print('- Número negativo inválido! -')
except:
    print('---- Entrada Inválida! ----')