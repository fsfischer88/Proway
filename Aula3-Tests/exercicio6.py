# Crie uma classe de Produtos
# Que tenha seus atributos privados __
# Utilizando o getter e setter para poder alterar seus valores
# Com property


class Produtos:
    def __init__(self, nome, desc, preco) -> None:
        self.__nome = nome
        self.__desc = desc
        self.__preco = preco

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    @property
    def desc(self):
        return self.__desc

    @desc.setter
    def desc(self, valor):
        self.__desc = valor
    
    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, preco):
        self.__preco = preco

produtos = Produtos("Caneta","Azul",1.8)
produtos.nome = "Lapis"
print(produtos.nome)
print(produtos.desc)
print(produtos.preco)


    


    
    

