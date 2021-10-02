# Crie uma classe de produtos com classmethod
# Que valide se o valor do produto passado é um float
# A classe podera aceitar esse valor R$ 15.00
# Que devera ser transformado para um float

# Exemplo de aplicação
#
# nome = "CASCATA"
# print(nome.replace("A", "@"))
#
#
# produto = Produto.cria_classe("RS15.00")
# print(produto.valor)

"""
>>>>> 15.00

"""

class Produto:

    def __init__(self,nome, valor) -> None:
        self.nome = nome
        self.valor = valor

    def metodo_de_instance(self):
        print(f"Nome do produto é {self.nome}")
        
        
    @classmethod
    def metodo_de_classe(cls,nome,valor):
        if valor > 0:
            raise Exception ("15.00")
        return cls(nome,valor)

produto = Produto.metodo_de_classe(nome = "Acabaxi",valor ="RS15.00")
print(produto.valor)
        

