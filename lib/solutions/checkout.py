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
    #    
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




    Price = namedtuple("Price", ["count", "price"])

    def __init__(self, offers_file):
        self.prices = defaultdict(list)
        self.give_away = {}
        
        with open(offers_file) as file_in:
            for offer_line in file_in:
                offer = offer_line.split()
                
                if offer[0] == "price":
                    item, count, price = offer[1:]
                    self.prices[item].append(Supermarket.Price(int(count), int(price)))

                elif offer[0] == "give_away":
                    free, required_count, item = offer[1:]
                    self.give_away[free] = (int(required_count), item)
        
            
#        self.prices = {
#                # Last price is always for a single item with no offers
#                "A" : [ 
#                        Supermarket.Price(5, 200),
#                        Supermarket.Price(3, 130),
#                        Supermarket.Price(1, 50)
#                      ],
#                "B" : [ 
#                        Supermarket.Price(2, 45),
#                        Supermarket.Price(1, 30)     
#                      ],
#                "C" : [
#                        Supermarket.Price(1, 20)
#                      ],
#                "D" : [
#                        Supermarket.Price(1, 15)
#                      ],
#                "E" : [
#                        Supermarket.Price(1, 40)
#                      ],
#                "F" : [
#                        Supermarket.Price(1, 10)
#                      ],
#                "G" : [
#                        Supermarket.Price(1, 20)
#                      ],
#                }
#        
#        self.give_away = {
#                "B" : (2, "E"),
#                "F" : (3, "F")
#                }
            
    
    def checkout(self, basket):
        bought = defaultdict(int)
        for item in basket:
            bought[item] += 1
    
        # deduct give aways        
        for give_away, requirement in self.give_away.iteritems():
            required_count, item = requirement
            if give_away in bought:
                item_count = bought.get(item, 0)
                free_count = item_count / required_count
                if bought[give_away] < free_count:
                    bought[give_away] = 0
                else:
                    bought[give_away] -= free_count
            
    
        total = 0
        for item, count in bought.iteritems():                
            if item not in self.prices:                
                return -1
            
            for offer in self.prices[item]:
                offers_num = count / offer.count
                price = offers_num * offer.price
                total += price
                
                # reduce count by what was added to total already
                count %= offer.count
                    
        return total

shop = Supermarket("offers.txt")

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    basket = list(skus)
    return shop.checkout(basket)
    
    