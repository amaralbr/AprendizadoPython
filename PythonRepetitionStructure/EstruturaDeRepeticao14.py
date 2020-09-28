# A série de Fibonacci é formada pela seqüência 0,1,2,3,5,8,13,21,34,55,...
# Faça um programa capaz de gerar a série até o n−ésimo termo.

num = int(input('Entre com um número: '))
x1 = 1
x2 = 1
valid = 1
print(x1, end=', ')
print(x2, end=', ')
while valid <= num:
    x3 = x1 + x2
    print(x3, end=', ')
    x1 = x2
    x2 = x3
    valid += 1