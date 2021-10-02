# Crie uma classe que escreva em um arquivo
# Crie uma classe que crie um produto para registrar dentro do arquivo
# Critérios:
# Os produtos devem conter:
# -id(integer)
# -nome(string)
# -preço(float)

# Cadastre ao menos 5 produtos e faça com que sejam impressos no terminal
# Exemplo de saída


class Escritora:

    def __init__(self, nome_do_arquivo) -> None:
        self.file_name = nome_do_arquivo
    
    def escrever(self, produtos):
        with open(f"{self.file_name}.txt", "a") as arquivo:
            arquivo.write(f"{produtos} \n")
    
    def ler(self):
        with open(f"{self.file_name}.txt", "r") as arquivo:
            conteudo = arquivo.readlines()
            print(conteudo)    

criador_de_arquivos = Escritora("proway")
criador_de_arquivos.escrever("Alunos Proway")
criador_de_arquivos.ler()



        


"""
{'id': 1, 'nome': 'coca-cola', 'preço': 5.79}

{'id': 2, 'nome': 'pepsi', 'preço': 5.79}

{'id': 3, 'nome': 'fanta', 'preço': 5.79}

{'id': 4, 'nome': 'guaraná', 'preço': 5.79}

{'id': 5, 'nome': 'Sprite', 'preço': 5.79}
"""


