# Altere o programa anterior para mostrar no final a soma dos números.

num1 = int(input('Entre com um número inteiro: '))
num2 = int(input('Entre com outro número inteiro:'))
x = min(num1, num2) + 1
list = []
while x < max(num1, num2):
    print(x)
    list.append(x)
    x += 1
print(sum(list))