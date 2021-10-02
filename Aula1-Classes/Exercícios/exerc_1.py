# Crie uma classe que represente uma calculadora
# A classe deve receber os valores a serem calculados pelo metodo inicializador
# Deve conter os 4 calculos básicos
# - Somar
# - Subtrair
# - Dividir
# - Multiplicar


class Calculadora:
  
    def __init__(self,x,y):
        self.um = x
        self.dois = y
    
    def somar(self):
        print(self.um + self.dois)

    def subtrair(self):
        print(self.um - self.dois)

    def dividir(self):
        print(self.um / self.dois)    
    
    def multiplicar(self):
        print(self.um * self.dois)

  
somar = Calculadora(10, 2)
somar.somar()
somar.subtrair()
somar.dividir()
somar.multiplicar()


