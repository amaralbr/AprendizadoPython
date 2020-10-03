# Classe Retangulo: Crie uma classe que modele um retangulo:

# Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
# Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

class Retangulo:
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB
    
    def mudarLado(self, lA, lB):
        self.ladoA = lA
        self.ladoB = lB
    
    def returnLado(self):
        return self.ladoB
    
    def area(self):
        return self.ladoA * self.ladoB
    
    def perimetro(self):
        return (self.ladoA * 2) + (self.ladoB * 2)

def calcularMaterial(largura, comprimento, portasM):
    comodo = Retangulo(largura, comprimento)
    piso = Retangulo(0.20, 0.40)
    rodape = Retangulo(0.05, 0.20)

    quantidade_pisos = comodo.area() / piso.area()
    quantidade_rodapes = (comodo.perimetro() - portasM) / rodape.returnLado()

    print(f'Para o local são necessário {quantidade_pisos:.1f} pisos e {quantidade_rodapes:.2f} rodapés.')


########## P R O G R A M A ##########
try:
    print('----------')
    largura = float(input('Qual é largura do local em metros (0.00): '))
    comprimento = float(input('Qual é comprimento do local em metros (0.00): '))
    portasM = float(input('Qual o total de portas do local em metros (0.00): '))
    if largura > 0 and comprimento > 0 and portasM >= 0.01:
        print('... C A L C U L A N D O ...')
        calcularMaterial(largura, comprimento, portasM)
        print('----------')
except:
    print('<< Valor inválido! >>')