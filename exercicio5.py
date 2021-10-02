# Crie uma classe de Produtos
# Que tenha seus atribuitos privados __
# Utilizando o getter e setter para poder alterar seus valores
# Sem property




class Produtos:
    def __init__(self, nome, desc, valor) -> None:
        self.__nome = nome
        self.__desc = desc
        self.__valor = valor

    def ler__nome(self):
        return self.__nome

    def ler__desc(self):
        return self.__desc
    
    def ler__valor(self):
        return self.__valor

    #Setter
    def configurar_nome(self, nome):
        self.__nome = nome

    def configurar_desc(self, desc):
        self.__desc = desc

    def configurar_valor(self, valor):
        self.__valor = valor
    
   
produto = Produtos(nome="Caneta",desc="Azul",valor=1.8)


produto.configurar_nome("Lapis")
produto.configurar_desc("Grafite")
produto.configurar_valor("1.5")

print(produto.ler__nome())
print(produto.ler__desc())
print(produto.ler__valor())


##############################

# Crie uma classe de Categoria
# Que tenha seus atributos privados __
# Utilizando o getter e setter para poder alterar seus valores
# Com property

class Categoria:

    def __init__(self, categoria) -> None:
        self.__categoria = categoria

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, valor):
        self.__categoria = valor

nome = Categoria("Bebidas")
print(nome.categoria)
nome.categoria = "Comida"
print(nome.categoria)

    
















