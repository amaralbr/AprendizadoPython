# Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

x = input('Entre com o sexo (M/F): ').upper()
if x == 'F':
    print('Feminino')
elif x == 'M':
    print('Masculino')
else:
    print('Sexo Inválido.')