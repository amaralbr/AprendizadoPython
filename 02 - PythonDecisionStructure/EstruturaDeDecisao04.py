# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

x = input('Entre com uma letra do alfabeto: ').upper()
if x == 'A' or x == 'E' or x == 'I' or x == 'O' or x == 'U':
    print(f'\'{x}\' é uma vogal.')
else:
    print(f'\'{x}\' é uma consoante.')