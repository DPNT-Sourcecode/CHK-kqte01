import unittest

from lib.solutions.checkout import checkout


class TestCheckout(unittest.TestCase):
    def test_checkout(self):
        self.assertEqual(checkout("A B C D"), 115)
        self.assertEqual(checkout("A B"), 80)
        self.assertEqual(checkout("A F D"), -1)


if __name__ == '__main__':
    unittest.main()