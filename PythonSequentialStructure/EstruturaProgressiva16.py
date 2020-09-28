# Faça um programa para uma loja de tintas.
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e
# que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.


def calc(m2):
    if m2 % 3 != 0:
        l = (int(m2 / 3)) + 1
    elif m2 % 3 == 0:
        l = m2 / 3
    if l <= 18:
        q = 1
        return q
    elif l > 18:
        if l % 18 != 0:
            q = (int(l / 18)) + 1
            return q
        elif l % 18 == 0:
            q = l / 18
            return q

def valor(q):
    r = q * 80.00
    return r

x = float(input('Entre com os m2 a serem pintados: '))
q = calc(x)
v = valor(q)
print(f'Serão nessários {q} latas de tinta.')
print(f'Total: ${v:.2f}')