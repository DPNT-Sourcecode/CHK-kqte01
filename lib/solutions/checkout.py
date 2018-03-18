from collections import defaultdict, namedtuple

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

    #+------+-------+------------------------+
    #| Item | Price | Special offers         |
    #+------+-------+------------------------+
    #| A    | 50    | 3A for 130, 5A for 200 |
    #| B    | 30    | 2B for 45              |
    #| C    | 20    |                        |
    #| D    | 15    |                        |
    #| E    | 40    | 2E get one B free      |
    #+------+-------+------------------------+

    Price = namedtuple("Price", ["count", "price", "give_away"])

    def __init__(self):
        
        self.prices = {
                # Last price is always for a single item with no offers
                "A" : [ 
                        Supermarket.Price(5, 200, set()),
                        Supermarket.Price(3, 130, set()),
                        Supermarket.Price(1, 50, set())
                      ],
                "B" : [ 
                        Supermarket.Price(2, 45, set()),
                        Supermarket.Price(1, 30, set())     
                      ],
                "C" : [
                        Supermarket.Price(1, 20, set())
                      ],
                "D" : [
                        Supermarket.Price(1, 15, set())
                      ],
                "E" : [
                        Supermarket.Price(2, 80, set("B")),
                        Supermarket.Price(1, 40, set())
                      ],
                }
        
        

    
#    def make_offer(self, item, count):
#        offer_count, offer_price = self.offers.get(item, (1, self.prices[item]))
#        
#        return ((count / offer_count * offer_price) 
#               + (count % offer_count * self.prices[item]))
        
            
    
    def checkout(self, basket):
        grouped = defaultdict(int)
        for item in basket:
            grouped[item] += 1
    
        total = 0
        
        for item, count in grouped.iteritems():                
            if item not in self.prices:                
                return -1
            
            for offer in self.prices[item]:
                price = count / offer.count * offer.price
                count %= offer.count
                total += price
                
                if price > 0 and offer.give_away:
                    for free in offer.give_away:
                        if free in grouped:                            
                            total -= self.prices[free][-1] 
                                
        return total


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    basket = list(skus)
    shop = Supermarket()
    return shop.checkout(basket)
    
    
