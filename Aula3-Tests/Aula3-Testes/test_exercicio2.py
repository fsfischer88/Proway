
from unittest import TestCase
import unittest

class ClasseDeTreino:

    def retornando_uma_lista(self):
        return[]

    def retornando_uma_tupla(self):
        return()

    def retornando_uma_dicionario(self):
        return{}

    def retornando_uma_string(self):
        return "String"

    def retornando_uma_integer(self):
        return 1

    def retornando_um_float(self):
        return 12.5

    def retornando_um_boolean(self):
        return True

class  TestClassDeTreino(TestCase):

    def test_retornando_uma_lista(self):
        a = ClasseDeTreino()

        self.assertIsInstance(a.retornando_uma_lista(), list)
        self.assertEqual(a.retornando_uma_lista(),[])

    

if __name__ == "__main__":
    unittest.main()






#Exemplo:
# self.assertIsInstance(ClasseDeTreino.retornando_um_boolean(), bool)
# self.assertEqual(ClasseDeTreino.retornando_um_boolean(), True)