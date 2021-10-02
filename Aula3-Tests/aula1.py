

class Pessoa:

    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
        self.valida_idade()

    def apresentar (self):
        print(f'Ola meu nome é {self.nome} e tenho {self.idade} anos')

    def valida_idade(self):
        if self.idade < 18:
            print("Sou menor de idade")
        else:
            print("Sou maior de idade")
    
pessoa = Pessoa(idade=32,nome="Felipe")
print(pessoa.nome)
print(pessoa.idade)