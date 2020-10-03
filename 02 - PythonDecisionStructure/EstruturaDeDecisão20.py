# Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
# A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
# A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# A mensagem "Aprovado com Distinção", se a média for igual a 10.

def media(x, y, z):
    m = (x + y + z) / 3
    return m

def result(x, y, z):
    if media(x, y, z) >= 7 and media(x, y, z) < 10:
        print(f'- Aprovado - Média: {media(x, y, z):.2f} pts.')
    elif media(x, y, z) < 7:
        print(f'- Reprovado - Média: {media(x, y, z):.2f} pts.')
    elif media(x, y, z) == 10:
        print(f'- Aprovado com Distinção - Média: {media(x, y, z):.2f} pts.')


x = int(input('Entre com a primeira nota: '))
y = int(input('Entre com a segunda nota: '))
z = int(input('Entre com a terceira nota: '))

result(x, y, z)