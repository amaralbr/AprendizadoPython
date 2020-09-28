# Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente.
# O jogador poderá errar 6 vezes antes de ser enforcado.

# Digite uma letra: A
# -> Você errou pela 1ª vez. Tente de novo!

# Digite uma letra: O
# A palavra é: _ _ _ _ O

# Digite uma letra: E
# A palavra é: _ E _ _ O

# Digite uma letra: S
# -> Você errou pela 2ª vez. Tente de novo!




## importação random para escolher uma palavra do arquivo txt
import random

## função para retornar letras da palavra
def validWord (palavra, letras):
    codificado = []
    for i in palavra:
        for letra in i:
            cont = 1
            for j in letras:
                if letra != j and cont < len(letras):
                    cont += 1
                    continue
                elif letra == j:
                    codificado.append(letra)
                    break
                elif letra != j and cont == len(letras):
                    codificado.append('_')
    separador = " "
    result = separador.join(codificado)
    return result

## função para sair do loop while do programa
def validResult (result):
    x = 0
    for i in result:
        if i == '_':
            x += 1
    if x == 0:
        return False
    elif x > 0:
        return True

########## P R O G R A M A ##########
palavrasList = []
arquivo = open('palavras_strings11.txt', 'r', encoding = 'utf8')
for i in arquivo:
    palavrasList.append(i.split())
palavra = palavrasList[random.randint(0, len(palavrasList)-1)]

letras = []
erros = 0

valid = True
while valid is True:
    print('')
    letra = input('Digite uma letra: ')
    for i in palavra:
        for j in i:
            if letra == j:
                letras.append(letra)
                print(f'A palavra é: {validWord(palavra, letras)}')
                valid = validResult(validWord(palavra, letras))
                break
    if letra == j:
        continue
    else:
        erros += 1
        if erros > 0 and erros < 6:
            print(f'-> Você erros pela {erros}ª vez. Tente de novo! <-')
            continue
        elif erros == 6:
            print(f'--- Você Perdeu! A palavra era: \"{palavra[0]}\" ---')
            break