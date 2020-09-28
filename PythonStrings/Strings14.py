# Leet spek generator. Leet é uma forma de se escrever o alfabeto latino usando outros símbolos em lugar das letras, como números por
# exemplo. A própria palavra leet admite muitas variações, como l33t ou 1337. O uso do leet reflete uma subcultura relacionada ao mundo
# dos jogos de computador e internet, sendo muito usada para confundir os iniciantes e afirmar-se como parte de um grupo. Pesquise sobre
# as principais formas de traduzir as letras. Depois, faça um programa que peça uma texto e transforme-o para a grafia leet speak.

########## P R O G R A M A ##########
leet = {" ":" ",".":".",",":",","a":"@","b":"|3","c":"<","d":"[)","e":"&","f":"]=","g":"9","h":"#","i":"l","j":"_/","k":"|<","l":"7","m":"/\/\\","n":"/\/","o":"()","p":"|º","q":"(,)","r":"/2","s":"$","t":"+","u":"(_)","v":"√","w":"vv","x":"><","y":"`/","z":"≥","A":"4","B":"8","C":"(","D":"|)","E":"3","F":"|=","G":"6","H":"|-|","I":"!","J":"_|","K":"X","L":"1","M":"44","N":"|\|","O":"0","P":"|*","Q":"0_","R":"|2","S":"5","T":"7","U":"|_|","V":"\/","W":"\/\/","X":"%","Y":"j","Z":"2",
}

conversao = []
frase = input(':')
for i in range(len(frase)):
    conversao.append(leet[frase[i]])

print(''.join(conversao))