import unittest
import sys
import os

from lib.solutions.checkout import Supermarket


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
    
    def setUp(self):
        directory = os.path.dirname(sys.modules[__name__].__file__)
        self.shop = Supermarket(os.path.join(directory, "offers.txt"))
        
    
    def test_checkout(self):
        self.assertEqual(self.shop.checkout(list("ABCD")), 115)
        self.assertEqual(self.shop.checkout(list("AB")), 80)
        self.assertEqual(self.shop.checkout(list("A8D")), -1)
        
        self.assertEqual(self.shop.checkout(list("ABCACAAD")), 265)
        
        self.assertEqual(self.shop.checkout(list("EEB")), 80)
        self.assertEqual(self.shop.checkout(list("EEBEE")), 160)
        self.assertEqual(self.shop.checkout(list("EEBEEB")), 160)
        self.assertEqual(self.shop.checkout(list("EEBEEBB")), 190)
        self.assertEqual(self.shop.checkout(list("EEBEEBBB")), 205)
        self.assertEqual(self.shop.checkout(list("EEBEEBBBB")), 235)
        
        
        self.assertEqual(self.shop.checkout(list("ABCACAADFF")), 285)
        self.assertEqual(self.shop.checkout(list("ABCAFCFAADFFF")), 305)
        self.assertEqual(self.shop.checkout(list("ABFCAFCFAADFFF")), 305)

        self.assertEqual(self.shop.checkout(list("F")), 10)
        self.assertEqual(self.shop.checkout(list("FF")), 20)
        self.assertEqual(self.shop.checkout(list("FFF")), 20)
        self.assertEqual(self.shop.checkout(list("FFFF")), 30)
        self.assertEqual(self.shop.checkout(list("FFFFF")), 40)
        self.assertEqual(self.shop.checkout(list("FFFFFF")), 40)
        self.assertEqual(self.shop.checkout(list("FFFFFFF")), 50)


        self.assertEqual(self.shop.checkout(list("ABCACSTXAADFF")), 330)
        self.assertEqual(self.shop.checkout(list("ABCACSSSAADFF")), 330)
        self.assertEqual(self.shop.checkout(list("ABCACSSSSTXAADFF")), 375)
        self.assertEqual(self.shop.checkout(list("ABCACSSSSTXYZAADFF")), 412)
        self.assertEqual(self.shop.checkout(list("SSSZ")), 65)
        self.assertEqual(self.shop.checkout(list("STXZ")), 62)
        self.assertEqual(self.shop.checkout(list("ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ")), 1602)
        
        

if __name__ == '__main__':
    unittest.main()
