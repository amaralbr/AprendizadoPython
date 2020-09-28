# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
# O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
# Tabuada de 5:
# 5 X 1 = 5
# 5 X 2 = 10
# ...
# 5 X 10 = 50

num = int(input('Você quer ver a tabuada de qual número (1-10)? '))
x = 1
print(f'Tabuada de {num}:')
while x <= 10:
    print(f'{num} x {x} = {num * x}')
    x += 1
