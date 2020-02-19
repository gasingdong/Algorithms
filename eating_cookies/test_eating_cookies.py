import unittest
from eating_cookies import eating_cookies


class Test(unittest.TestCase):

    def test_eating_cookies_small_n(self):
        self.assertEqual(eating_cookies(0), 1)
        self.assertEqual(eating_cookies(1), 1)
        self.assertEqual(eating_cookies(2), 2)
        self.assertEqual(eating_cookies(5), 13)
        self.assertEqual(eating_cookies(10), 274)

    def test_eating_cookies_large_n(self):
        self.assertEqual(eating_cookies(
            50, [0 for i in range(51)]), 10562230626642)
        self.assertEqual(eating_cookies(
            100, [0 for i in range(101)]), 180396380815100901214157639)
        self.assertEqual(eating_cookies(500, [0 for i in range(
            501)]), int("130618656970218663498347545006237201871512019" +
                        "139119220715666434305161091397192795974451967" +
                        "6992404852130396504615663042713312314219527"))


if __name__ == '__main__':
    unittest.main()
