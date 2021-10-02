



class Animal:
    def __init__(self, patas, calda, som):
        self.patas = patas
        self.calda = calda
        self.som = som

    def emitir_som(self):
        print(self.som)

class Cachorro(Animal):

    def nadar(self):
        print("Sou um cachorro e estou nadando")

class Cobra(Animal):
    
    def subir_em_arvores(self):
        print("Sou uma cobra e estou subindo na arvore")

cachorro = Cachorro(patas=4, calda=True, som="Au au") 
cachorro.emitir_som()
cachorro.nadar() 

cobra = Cobra(patas=0, calda=True, som="ZzzZZZzzz")
cobra.emitir_som()
cobra.subir_em_arvores()
