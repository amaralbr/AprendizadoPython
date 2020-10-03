# O cardápio de uma lanchonete é o seguinte:
# Especificação   Código  Preço
# Cachorro Quente 100     R$ 1,20
# Bauru Simples   101     R$ 1,30
# Bauru com ovo   102     R$ 1,50
# Hambúrguer      103     R$ 1,20
# Cheeseburguer   104     R$ 1,30
# Refrigerante    105     R$ 1,00
# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.
# Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido.
# Considere que o cliente deve informar quando o pedido deve ser encerrado.


########## P R O G R A M A ##########
bdlanch = [['Cachorro Quente', 100, 5.20], ['Bauru Simples', 101, 8.30], ['Bauru com ovo', 102, 9.50], ['Hámburguer', 103, 9.20], ['Cheeseburguer', 104, 9.30], ['Refrigerante', 105, 5.00]]
pedidolist = []
while True:
    print('<<< >>>')
    try:
        pedido = int(input('Entre com o código do produto: '))
        for i in bdlanch:
            if pedido == i[1]:
                pedidolist.append(i[1])
        if pedido >= 100:
            continue
        elif pedido == 0:
            break
        elif pedido >= 0 and pedido < 100:
            print('Código inválido!')
    except:
        print('Entrada Inválida!')
total = []
print('--------------------------------------')
print('  Especificação   Preço   Qt   Valor  ')
for i in bdlanch:
    contador = 0
    for j in pedidolist:
        if i[1] == j:
            contador += 1
    if contador == 0:
        True
    else:
        valor = i[2] * contador
        total.append(valor)
        print(f'{i[0]:<17}{i[2]:^7.2f}{contador:^5.0f}{valor:^9.2f}')
valortotal = sum(total)
print('                    ------------------')
print(f'                      TOTAL: {valortotal:^7.2f}')
print('--------------------------------------')
