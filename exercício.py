# Crie uma classe que contenha um classmethod
# Que devera criar pelo ano de nascimento
# e validar se a idade é maior que 18

# Crie uma classe de produtos com classmethod
# Que valide se o valor do produto passado é um float
# A classe podera aceita esse valor R$ 15.00
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


class Nascimento:

    def __init__(self,nome, ano) -> None:
        self.nome = nome
        self.ano = ano

    
    def metodo_de_instance(self):
        print(f"Meu nume é {self.nome}")
        
        
    @classmethod
    def metodo_de_classe(cls,nome,ano):
        if ano < 2003:
            raise Exception ("Você é maior de idade")
        print("Você é menor de idade")
        return cls(nome,ano)


minha_classe = Nascimento.metodo_de_classe(nome="Felipe", ano=2004)
print(minha_classe.nome)