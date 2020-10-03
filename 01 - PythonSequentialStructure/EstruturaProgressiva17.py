# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho
# em metros quadrados da área a ser pintada. Considere que a cobertura da tinta
# é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o preço seja o menor.
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

def litros(m2):
    if m2 % 6 != 0:
        l = (int(m2 / 6)) + 1
        return l
    elif m2 % 6 == 0:
        l = m2 / 6
        return l

def latas(m2):
    if litros(m2) <= 18:
        q = 1
        return q
    elif litros(m2) > 18:
        if litros(m2) % 18 != 0:
            q = (int(litros(m2) / 18)) + 1
            return q
        elif litros(m2) % 18 == 0:
            q = litros(m2) / 18
            return q

def galoes(m2):
    if litros(m2) <= 3.6:
        q = 1
        return q
    elif litros(m2) > 3.6:
        if litros(m2) % 3.6 != 0:
            q = (int(litros(m2) / 3.6)) + 1
            return q
        elif litros(m2) % 3.6 == 0:
            q = litros(m2) / 3.6
            return q

def valorLatas(m2):
    r = latas(m2) * 80.00
    return r

def valorGaloes(m2):
    r = galoes(m2) * 25.00
    return r

def melhor(m2):
    l = (litros(m2) * 0.1) + litros(m2)
    ql = int(l / 18)
    lg = (((l / 18) - (int(l / 18))) * 18)
    qg = round(lg / 3.6 + 0.5)
    vl = ql * 80.00
    vg = qg * 25.00
    return print(f'A melhor opção é: {ql} latas e {qg} galões. Total: ${vl+vg:.2f}.')


x = int(input('Entre com os m2 a serem pintados: '))
litros(x)
print(f'Latas: {latas(x)} Total: ${valorLatas(x)}')
print(f'Galões: {galoes(x)} Total: ${valorGaloes(x)}')
melhor(x)