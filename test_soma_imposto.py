import unittest
from soma_imposto import somaImposto

class TestSomaImposto(unittest.TestCase):

    def test_soma_imposto_valor_simples(self):
        """
        Testa o cálculo do imposto para um valor simples.
        """
        resultado = somaImposto(17.5, 200)
        self.assertEqual(resultado, 235.00, "O preço final com imposto está incorreto.")

    def test_soma_imposto_zero_imposto(self):
        """
        Testa o cálculo do imposto quando a taxa é 0%.
        """
        resultado = somaImposto(0, 100)
        self.assertEqual(resultado, 100.00, "Quando o imposto é 0%, o preço final deve ser igual ao custo.")

    def test_soma_imposto_imposto_100(self):
        """
        Testa o cálculo do imposto quando a taxa é 100%.
        """
        resultado = somaImposto(100, 100)
        self.assertEqual(resultado, 200.00, "Quando o imposto é 100%, o preço final deve ser o dobro do custo.")

    def test_soma_imposto_imposto_negativo(self):
        """
        Testa se a função lida corretamente com uma taxa negativa (não deve ser permitida).
        """
        with self.assertRaises(ValueError):
            somaImposto(-10, 100)

    def test_soma_imposto_imposto_grande(self):
        """
        Testa o cálculo do imposto com uma taxa muito alta (ex: 500%).
        """
        resultado = somaImposto(500, 100)
        self.assertEqual(resultado, 600.00, "Com uma taxa de 500%, o preço final deve ser 6 vezes o custo.")

if __name__ == '__main__':
    unittest.main()
