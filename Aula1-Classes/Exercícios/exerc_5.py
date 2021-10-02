# Crie uma classe de CadastroPessoa
# Crie uma classe de cliente que herde da classe CadastroPessoa
# a classe CadastroPessoa deve contar um metodo que informa se a pessoa cadastrada é um 
# cliente Vip ou não
#Exemplo de Saída:

class CadastroPessoa: 
    
    def __init__(self, cliente_vip):
        self.vip = cliente_vip #<--- Pode ser um valor booleano False ou True
       

class Cliente(CadastroPessoa):

    def tipo_de_cliente(self):
        if self.vip == True:
            self.rodape()
            print("Ana é um cliente vip \n")
            self.cabecalho()
        else:
            self.rodape()
            print("Ana é um cliente normal \n")
            self.cabecalho()

    def cabecalho(self):
        print('*'*15,'\n')
    def rodape(self):
        print('='*15,'\n')
        
Cliente(False).tipo_de_cliente()
