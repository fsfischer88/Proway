
import unittest

class Test(unittest.TestCase):

    def test_aprendendo_testar(self):
        assert 1 == 1

    def test_strings(self):
        assert "1" == "1"
    
    def test_boleanos(self):
        assert True == False

    def test_boleano_dois(self):
        a = "teste"
        assert bool(a)

    def test_varios_testes(self):
        a = "Teste"
        b = "Teste"
        c = ""
        assert a == b or a == c
        # or == palavra 'OU'
        # a é igual a b ou a é igual a c?

    def test_com_and(self):
        a = "Teste"
        b = "Teste"
        c = ""
        assert a == b and a == c

    def test_valor_inteiro(self):
        assert isinstance(1, int)

if __name__ == "__main__":
    unittest.main()
