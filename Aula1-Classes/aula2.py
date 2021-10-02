
def falar():
    print("EStou")

class Pessoa:

    def falar(self):
        print("Estou falando")
# Dentro dessa classe temos a função "falar"
# Para chamarmos essa função fazemos da seguinte forma

Pessoa().falar()

# Inicializador da classe

# Como nos metodos podemos passar argumentos para os parametros de uma função
# Em uma classe para passarmos argumento podemos fazer da seguinte forma

def falar_algo(assunto):
    print(f" estou falando sobre {assunto}")

class Pessoa:

    def _init_(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura
    
    def apresentar(self):
        print(f"Meu nome é {self.nome} tenho {self.idade} anos de idade e {self.altura} de altura")
        # sel.teste = "Testando o self"

# def printar(self):
#    print(self.teste)

pablo = Pessoa("Paulo", 17,1.68)


# pablo.apresentar()
print(pablo.nome)
print(pablo.idade)
print(pablo.altura)