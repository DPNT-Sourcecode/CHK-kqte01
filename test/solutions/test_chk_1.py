import unittest

from lib.solutions.checkout import checkout


class TestCheckout(unittest.TestCase):
    
    #Our price table and offers: 
    #+------+-------+----------------+
    #| Item | Price | Special offers |
    #+------+-------+----------------+
    #| A    | 50    | 3A for 130     |
    #| B    | 30    | 2B for 45      |
    #| C    | 20    |                |
    #| D    | 15    |                |
    #+------+-------+----------------+
    
    #+------+-------+------------------------+
    #| Item | Price | Special offers         |
    #+------+-------+------------------------+
    #| A    | 50    | 3A for 130, 5A for 200 |
    #| B    | 30    | 2B for 45              |
    #| C    | 20    |                        |
    #| D    | 15    |                        |
    #| E    | 40    | 2E get one B free      |
    #+------+-------+------------------------+
    
    #+------+-------+------------------------+
    #| Item | Price | Special offers         |
    #+------+-------+------------------------+
    #| A    | 50    | 3A for 130, 5A for 200 |
    #| B    | 30    | 2B for 45              |
    #| C    | 20    |                        |
    #| D    | 15    |                        |
    #| E    | 40    | 2E get one B free      |
    #| F    | 10    | 2F get one F free      |
    #+------+-------+------------------------+
    
    def test_checkout(self):
        self.assertEqual(checkout("ABCD"), 115)
        self.assertEqual(checkout("AB"), 80)
        self.assertEqual(checkout("AXD"), -1)
        
        self.assertEqual(checkout("ABCACAAD"), 265)
        
        self.assertEqual(checkout("EEB"), 80)
        self.assertEqual(checkout("EEBEE"), 160)
        self.assertEqual(checkout("EEBEEB"), 160)
        self.assertEqual(checkout("EEBEEBB"), 190)
        self.assertEqual(checkout("EEBEEBBB"), 205)
        self.assertEqual(checkout("EEBEEBBBB"), 235)
        
        
        self.assertEqual(checkout("ABCACAADFF"), 285)
        self.assertEqual(checkout("ABCAFCFAADFFF"), 305)
        self.assertEqual(checkout("ABFCAFCFAADFFF"), 305)

        self.assertEqual(checkout("F"), 10)
        self.assertEqual(checkout("FF"), 20)
        self.assertEqual(checkout("FFF"), 20)
        self.assertEqual(checkout("FFFF"), 30)
        self.assertEqual(checkout("FFFFF"), 40)
        self.assertEqual(checkout("FFFFFF"), 40)
        self.assertEqual(checkout("FFFFFFF"), 50)


if __name__ == '__main__':
    unittest.main()