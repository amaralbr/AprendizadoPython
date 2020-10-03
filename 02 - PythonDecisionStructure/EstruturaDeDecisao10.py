# Faça um Programa que pergunte em que turno você estuda.
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

question = input('Você estuda em qual turno (M/V/N)? ').upper()
if question == 'M':
    print('Bom dia!')
elif question == 'V':
    print('Boa tarde!')
elif question == 'N':
    print('Boa noite!')
else:
    print('Valor Inválido!')