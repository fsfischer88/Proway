# Crie uma classe que represente uma pessoa
# A classe devera receber os valores pelo metodo inicializador
# Devera armazenar os valores e fazer a apresentação dessa pessoa 
# Devera conter um metodo para cada tarefa
# Exemplo de saida




class Pessoa:
 
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def apresentar(self):
        self.rodape()
        print(f"Olá, meu nome é {self.nome} tenho {self.idade} anos de idade e {self.altura} de altura","\n")
        self.cabecalho()

    def cabecalho(self):
        print('*'*15,'\n')

    def rodape(self):
        print('='*15,'\n')

felipe = Pessoa("Felipe",32,1.77)

# print(felipe.nome)
# print(felipe.idade)
# print(felipe.altura)

felipe.apresentar()
    

