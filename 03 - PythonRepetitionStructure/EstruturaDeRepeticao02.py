# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma
# mensagem de erro e voltando a pedir as informações.

valid = False
while valid is False:
    usuario = input('Entre com o nome de usuário: ')
    senha = input('Entre com a senha: ')
    if senha == usuario:
        print('Inválido! Usuário e senha não podem ser iguáis.')
        continue
    else:
        valid = True