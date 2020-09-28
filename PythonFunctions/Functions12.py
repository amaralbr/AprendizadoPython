# Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados.
# Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória.
# Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.


########## P R O G R A M A ##########
import random
def embaralha(p):
    letras = []
    while len(letras) != len(p):
        r = random.randint(0, len(p)-1)
        if r not in letras:
            letras.append(r)
            print(f'{p[r]}', end='')

embaralha(input('Entre com uma string: ').lower())