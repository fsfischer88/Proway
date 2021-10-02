"""
_ atributos:

_ protected
__ private

"""

_a = 'Alguma coisa'

class Produto:

        def __init__(self, nome, valor) -> None:
            self.__nome = nome
            self.__valor = valor

        def ler__nome(self):
            return self.__nome

        #Getter
        def ler__valor(self):
            return self.__valor

        #Setter
        def configurar_nome(self, nome):
            self.__nome = nome
        
        #Setter
        def configurar_nome(self, valor):
            self.__valor = valor

produto = Produto("Refrigerante", 5.80)

produto.__nome = "Produto de limpeza"
produto.__valor = 18.25
# produto.categoria = "Limpeza"

print(produto.__nome)
print(produto.__valor)
print(produto.ler__nome())
print(produto.ler__valor())
# print(produto._categoria)

produto.configurar_nome("Agua Tonica")
print(produto.ler__nome())
print(produto)
