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


if __name__ == '__main__':
    unittest.main()
