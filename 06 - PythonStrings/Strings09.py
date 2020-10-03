# Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e
# indique se é um número válido ou inválido através da validação dos dígitos verificadores edos caracteres de formatação.


########## P R O G R A M A ##########
cpf = input('CPF: ')
if cpf[3] == '.' and cpf[7] == '.' and cpf[11] == '-' and len(cpf) == 14:
    print('-- CPF Válido! --')
else:
    print('-- CPF Inválido! --')