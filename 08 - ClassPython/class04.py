# Classe Pessoa: Crie uma classe que modele uma pessoa:

# Atributos: nome, idade, peso e altura
# Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class Pessoa:
    def __init__ (self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    def envelhecer(self, idade):
        if self.idade < 21:
            self.altura += 0.5 * (idade)
            self.idade += idade
        else:
            self.idade += idade
    
    def engordar(self, peso):
        self.peso += peso
    
    def emagrecer(self, peso):
        self.peso -= peso
    
    def crescer(self, m):
        self.altura += m

    def printTest(self):
        print(f'{self.nome} {self.idade} {self.peso} {self.altura}')
    
pessoa_1 = Pessoa('Fabiano', 30, 98, 194)
pessoa_1.crescer(0.01)
pessoa_1.emagrecer(4)
pessoa_1.envelhecer(1)
pessoa_1.printTest()

pessoa_2 = Pessoa('Severino', 14, 70, 171)
pessoa_2.envelhecer(3)
pessoa_2.engordar(4)
pessoa_2.printTest()
