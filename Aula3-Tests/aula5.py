
# class Escritor:

#     #Método Escritor
#     def __init__(self, nome, livros) -> None:
#         self.__nome = nome
#         self.__titulos = livros
    
#     #Getter
#     def get_nome(self):
#         return self.__nome
    
#     #Getter
#     def get__titulos(self):
#         for livro in self.__titulos:
#             print(livro)
#     #Setter
#     def set_nome(self, valor):
#         self.__nome = valor
    
# #Variavel Instancia da Classe Escritor - valores que estou passando paa dentro da classe
# escritor = Escritor("Shakspare", ["Livro1","Livro2","Livro3"])
# print(escritor.get_nome())
# escritor.set_nome("Machado de Assis")
# print(escritor.get_nome())


class Escritor:

    #Método Escritor
    def __init__(self, nome, livros) -> None:
        self.__nome = nome
        self.__titulos = livros

    @property
    def nome(self):
        return self.__nome
   
    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    @property
    def titulos(self):
        return self.__titulos
        
    @titulos.setter
    def titulos(self, valor):
        self.__titulos = valor


escritor = Escritor("Shakspare", ["Livro1","Livro2","Livro3"])
print(escritor.nome)
escritor.nome = "Machado de Assis"
print(escritor.nome)
print(escritor.titulos)
