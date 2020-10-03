# Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
# "Qual o melhor Sistema Operacional para uso em servidores?"

# As possíveis respostas são:

# 1- Windows Server
# 2- Unix
# 3- Linux
# 4- Netware
# 5- Mac OS
# 6- Outro
# Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma.
# O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores
# além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor.
# Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o
# vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:
# Sistema Operacional     Votos   %
# -------------------     -----   ---
# Windows Server           1500   17%
# Unix                     3500   40%
# Linux                    3000   34%
# Netware                   500    5%
# Mac OS                    150    2%
# Outro                     150    2%
# -------------------     -----
# Total                    8800

# O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.


########## P R O G R A M A ##########
def percentual (soma, votos):
    operacao = (votos * 100) / soma
    return operacao

print('')
votacao = [0,0,0,0,0,0]
sistemas = ['Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro', 'Total']
while True:
    numero = int(input('Qual o melhor Sistema Operacional para uso em servidores? '))
    if numero > 0 and numero < 7:
        votacao[numero - 1] += 1
    elif numero == 0:
        break
    else:
        print('-- Entrada Inválida! --')
print('')
print('Sistema Operacional  Votos    %   ')
print('-------------------  ------  ------')
x=0
for i in votacao:
    print(f'{sistemas[x]:<20}{i:>6}{percentual(sum(votacao), i):>8.1f}%')
    x+=1
print('-------------------  ------')
print(f'{sistemas[6]:<20}{sum(votacao):>6}')
print('')
print(f'O Sistema Operacional mais votado foi o {sistemas[votacao.index(max(votacao))]}, com {max(votacao)} votos, correspondendo a {percentual(sum(votacao), max(votacao)):.1f}% dos votos.')