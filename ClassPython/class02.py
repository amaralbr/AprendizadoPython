# Classe Quadrado: Crie uma classe que modele um quadrado:

# Atributos: Tamanho do lado
# Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área

class Quadrado:
    def __init__(self, lado):
        self.lado = lado
    
    def mudarLado(self, l):
        self.lado = l
    
    def printLado(self):
        print(self.lado)

    def area(self):
        print(self.lado**2)

quadrado_1 = Quadrado(10)
quadrado_1.printLado()
quadrado_1.area()
quadrado_1.mudarLado(20)
quadrado_1.printLado()
quadrado_1.area()