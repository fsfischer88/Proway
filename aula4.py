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

        def ler__valor(self):
            return self.__valor

produto = Produto("Refrigerante", 5.80)

produto.__nome = "Produto de limpeza"
produto.__valor = 18.25
# produto.categoria = "Limpeza"

print(produto.__nome)
print(produto.__valor)
# print(produto._categoria)