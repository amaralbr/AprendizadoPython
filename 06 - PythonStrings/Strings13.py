# Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com as letras
# embaralhadas. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador terá seis
# tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.

## importação random para escolher uma palavra do arquivo txt
import random

########## P R O G R A M A ##########
palavrasList = []
arquivo = open('palavras_strings11.txt', 'r', encoding = 'utf8')
for i in arquivo:
    palavrasList.append(i.split())
palavra = palavrasList[random.randint(0, len(palavrasList)-1)]
palavrastr = palavra[0]
embaralhada = []
numb = []
while True:
    if len(embaralhada) == len(palavrastr):
        if embaralhada == palavrastr:
            embaralhada.clear()
            numb.clear()
        else:
            break
    r = random.randint(0, len(palavrastr)-1)
    if r not in numb:
        numb.append(r)
        letra = palavrastr[r]
        embaralhada.append(letra)
palavraNaTela = ''.join(embaralhada)

erros = 0

while True:
    if erros < 6:
        print('')
        tentativa = input(f'A palavra embaralhada \'{palavraNaTela}\' é: ')
        if tentativa == palavrastr:
            print('')
            print(f'A palavra é {palavrastr}. >>> Você ganhou! <<<')
            break
        else:
            erros += 1
            print(f'Errou! Você ainda tem {6-erros} tentativas.')
            continue
    elif erros == 6:
        print('--')
        print(f'A palavra é {palavrastr}. --- Você perdeu! ---')
        break