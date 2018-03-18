from collections import defaultdict

class Supermarket:
    
    #Our price table and offers: 
    #+------+-------+----------------+
    #| Item | Price | Special offers |
    #+------+-------+----------------+
    #| A    | 50    | 3A for 130     |
    #| B    | 30    | 2B for 45      |
    #| C    | 20    |                |
    #| D    | 15    |                |
    #+------+-------+----------------+

    def __init__(self):
        self.prices = {
                "A" : 50,
                "B" : 30,
                "C" : 20,
                "D" : 15            
                }
        
        self.offers = {
                "A" : (3, 130),
                "B" : (2, 45)
                }

    
    def make_offer(self, item, count):
        offer_count, offer_price = self.offers.get(item, (1, self.prices[item]))
        
        return ((count / offer_count * offer_price) 
               + (count % offer_count * self.prices[item]))
        
            
    
    def checkout(self, basket):
        grouped = defaultdict(int)
        for item in basket:
            grouped[item] += 1
    
        price = 0
        for item, count in grouped.iteritems():                
            if item in self.offers:
                price += self.make_offer(item, count)
            elif item in self.prices:
                price += count * self.prices[item]
            else:
                return -1

        return price


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    basket = skus.split()
    shop = Supermarket()
    return shop.checkout(basket)
    
    
