# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd'

nome = ''
idade = 0
salario = 0
sexo = ''
estadoCivil = ''

while len(nome) <= 3:
    nome = input('Entre com o nome: ')
while idade <= 0 or idade > 150:
    idade = int(input('Entre com a idade: '))
while salario <= 0:
    salario = float(input('Entre com o salário: '))
while sexo != 'f' and sexo != 'm':
    sexo = input('Entre com o sexo (f/m): ').lower()
while estadoCivil != 's' and estadoCivil != 'c' and estadoCivil != 'v' and estadoCivil != 'd':
    estadoCivil = input('Entre com o estado civil (s/c/v/d): ')
