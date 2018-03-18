from collections import defaultdict, namedtuple

class Supermarket:
    
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


    
    
