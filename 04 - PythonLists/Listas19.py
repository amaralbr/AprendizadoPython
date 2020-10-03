# A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos.
# Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar
# os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":
# alexandre       456123789
# anderson        1245698456
# antonio         123456456
# carlos          91257581
# cesar           987458
# rosemary        789456125
# Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere um relatório, chamado
# "relatório.txt", no seguinte formato:
# ACME Inc.               Uso do espaço em disco pelos usuários
# ------------------------------------------------------------------------
# Nr.  Usuário        Espaço utilizado     % do uso

# 1    alexandre       434,99 MB             16,85%
# 2    anderson       1187,99 MB             46,02%
# 3    antonio         117,73 MB              4,56%
# 4    carlos           87,03 MB              3,37%
# 5    cesar             0,94 MB              0,04%
# 6    rosemary        752,88 MB             29,16%

# Espaço total ocupado: 2581,57 MB
# Espaço médio ocupado: 430,26 MB
# O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma a agilizar a
# execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma função separada, que
# será chamada pelo programa principal. O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.


########## P R O G R A M A ##########
import babel.numbers
import decimal

arquivoEntrada = open('usuarios.txt', 'r')
linhas = arquivoEntrada.readlines()
arquivoEntrada.close()

usuarios = []
espacos = []
espacoTotal = 0
for i in linhas:
    campos = i.split()
    usuarios.append(campos[0])
    espacos.append(campos[1])
    espacoTotal += int(campos[1])

arquivoSaida = open('relatorio.txt', 'w')
arquivoSaida.write('ACME Inc.               Uso do espaço em disco pelos usuários\n')
arquivoSaida.write('------------------------------------------------------------------------\n')
arquivoSaida.write('Nr.  Usuário        Espaço utilizado     % do uso\n')
arquivoSaida.write('\n')
cont = 1
for i in espacos:
    arquivoSaida.write(f'{cont:<5} {usuarios[espacos.index(i)]:<15} {((int(i)*(9.537*(10**-7)))):>7.2f} MB {(int(i)*100)/espacoTotal:>17.2f}%\n'.replace('$-','-$'))
    cont += 1
arquivoSaida.write('\n')
arquivoSaida.write(f'Espaço total ocupado: {(espacoTotal*(9.537*(10**-7))):>7,.2f} MB\n')
arquivoSaida.write(f'Espaço médio ocupado: {(espacoTotal/len(espacos))*9.537*(10**-7):>7.2f} MB\n')
arquivoSaida.close()
