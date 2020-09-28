# Uma academia deseja fazer um senso entre seus clientes para descobrir
# o mais alto, o mais baixo, a mais gordo e o mais magro,
# para isto você deve fazer um programa que pergunte a cada um dos clientes da academia
# seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código.
# Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro,
# além da média das alturas e dos pesos dos clientes


########## P R O G R A M A ##########
codigo = []
altura = []
peso = []
while True:
    try:
        print('--------------------')
        cod = int(input('Código do aluno: '))
        if cod == 0:
            print('Calculando...')
            break
        alt = float(input('Altura (m): '))
        pes = float(input('Peso (kg): '))
        if cod > 0 and alt > 0 and pes > 0:
            codigo.append(cod)
            altura.append(alt)
            peso.append(pes)
    except:
        continue


maisAlto = altura.index(max(altura))
maisBaixo = altura.index(min(altura))
maisGordo = peso.index(max(peso))
maisMagro = peso.index(min(peso))

print(f'Aluno mais alto = Cód: {codigo[maisAlto]} Alt: {altura[maisAlto]:.2f} Peso: {peso[maisAlto]:.1f}')
print(f'Aluno mais baixo = Cód: {codigo[maisBaixo]} Alt: {altura[maisBaixo]:.2f} Peso: {peso[maisBaixo]:.1f}')
print(f'Alunos mais gordo = Cód: {codigo[maisGordo]} Alt: {altura[maisGordo]:.2f} Peso: {peso[maisGordo]:.1f}')
print(f'Aluno mais magro = Cód: {codigo[maisMagro]} Alt: {altura[maisMagro]:.2f} Peso: {peso[maisMagro]:.1f}')