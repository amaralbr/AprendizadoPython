# A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
# Faça um programa que gere a série até que o valor seja maior que 500.

x1 = 0
x2 = 1
x3 = 0
print(x1, end=', ')
print(x2, end=', ')
while x3 < 500:
    x3 = x1 + x2
    print(x3, end=', ')
    x1 = x2
    x2 = x3