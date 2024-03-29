import unittest
from notationPolonaiseInverse import NotationPolonaiseInverse


class Test(unittest.TestCase):
    def test_addition(self):
        # 2 2 +
        self.assertEqual(4, NotationPolonaiseInverse().addition(2, 2))

    def test_soustraction(self):
        # 5 3 -
        self.assertEqual(2, NotationPolonaiseInverse().soustraction(5, 3))

    def test_multiplication(self):
        # 6 6 *
        self.assertEqual(36, NotationPolonaiseInverse().multiplication(6, 6))

    def test_division(self):
        # 10 2 /
        self.assertEqual(5, NotationPolonaiseInverse().division(10, 2))

    def test_calcul_addition_npi(self):
        # 2 2 +
        self.assertEqual(4, NotationPolonaiseInverse().calcul(2, 2, "+"))

    def test_calcul_soustraction_npi(self):
        # 5 3 -
        self.assertEqual(2, NotationPolonaiseInverse().calcul(5, 3, "-"))

    def test_calcul_multiplication_npi(self):
        # 6 6 *
        self.assertEqual(36, NotationPolonaiseInverse().calcul(6, 6, "*"))

    def test_calcul_division_npi(self):
        # 10 2 /
        self.assertEqual(5, NotationPolonaiseInverse().calcul(10, 2, "/"))

    def test_calculatrice_1_npi(self):
        # 3 10 5 + *
        self.assertEqual(45, NotationPolonaiseInverse().calculatrice("3 10 5 + *"))

    def test_calculatrice_2_npi(self):
        # 10 4 3 + 2 * -
        self.assertEqual(-4, NotationPolonaiseInverse().calculatrice("10 4 3 + 2 * -"))

if __name__ == '__main__':
    unittest.main()
