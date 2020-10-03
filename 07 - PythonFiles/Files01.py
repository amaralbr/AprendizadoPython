# Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, contendo um relatório dos
# endereços IP válidos e inválidos.
# O arquivo de entrada possui o seguinte formato:
# 200.135.80.9
# 192.168.1.1
# 8.35.67.74
# 257.32.4.5
# 85.345.1.2
# 1.2.3.4
# 9.8.234.5
# 192.168.0.256
# O arquivo de saída possui o seguinte formato:
# [Endereços válidos:]
# 200.135.80.9
# 192.168.1.1
# 8.35.67.74
# 1.2.3.4

# [Endereços inválidos:]
# 257.32.4.5
# 85.345.1.2
# 9.8.234.5
# 192.168.0.256


## importar função para validar ip
import ipaddress

########## P R O G R A M A ##########
ips = []
arquivo = open('textoentrada01.txt', 'r')
for linha in arquivo:
    ips.append(linha.replace('\n', ''))
arquivo.close()

numbValid = []
numbInvalid = []
for ip in ips:
    try:
        numb = ipaddress.ip_address(ip)
        numbValid.append(ip)
    except:
        numbInvalid.append(ip)

print('[Endereços Válidos:]')
for i in numbValid:
    print(i)
print('')
print('[Endereços Inválidos:]')
for i in numbInvalid:
    print(i)