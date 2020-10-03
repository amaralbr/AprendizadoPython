# Classe Bola: Crie uma classe que modele uma bola:

# Atributos: Cor, circunferência, material
# Métodos: trocaCor e mostraCor

class Bola:
    def __init__(self, cor, circunf, material):
        self.cor = cor
        self.circunferencia = circunf
        self.material = material
    
    def trocaCor(self, cor):
        self.cor = cor
    
    def mostraCor(self):
        print(self.cor)

bola_1 = Bola('azul', 75, 'couro')
bola_1.mostraCor()
bola_1.trocaCor('branca')
bola_1.mostraCor()