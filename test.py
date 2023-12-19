import unittest
from notationPolonaiseInverse import NotationPolonaiseInverse

class Test(unittest.TestCase):
    def test_addition(self):
        # 2 2 +
        self.assertEqual(4, NotationPolonaiseInverse().addition(2, 2))


if __name__ == '__main__':
    unittest.main()
