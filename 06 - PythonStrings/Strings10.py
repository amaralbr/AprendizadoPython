# Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso.


########## P R O G R A M A ##########
from num2words import num2words
num = int(input('Entre com um número inteiro: '))
print(num2words(num, lang = 'pt_BR'))