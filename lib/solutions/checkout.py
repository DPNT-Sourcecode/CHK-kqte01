from collections import defaultdict, namedtuple

class Supermarket:
    
    Price = namedtuple("Price", ["count", "price"])

    def __init__(self, offers_file):
        self.prices = defaultdict(list)
        self.giveAway = {}
        self.buy_any = []
        
        with open(offers_file) as file_in:
            for offer_line in file_in:
                offer = offer_line.split()
                
                if offer[0] == "price":
                    item, count, price = offer[1:]
                    self.prices[item].append(Supermarket.Price(int(count), int(price)))

                elif offer[0] == "give_away":
                    free, required_count, item = offer[1:]
                    self.giveAway[free] = (int(required_count), item)
                
                elif offer[0] == "buy_any":
                    count, price = offer[1:3]
                    items = offer[3:] # items in descending price order
                    self.buy_any.append((int(count), int(price), items))
                    
           
            
    def remove_give_aways(self, bought):
        for free, requirement in self.giveAway.iteritems():
            required_count, item = requirement
            if free in bought:
                item_count = bought.get(item, 0)
                free_count = item_count / required_count
                if bought[free] < free_count:
                    bought[free] = 0
                else:
                    bought[free] -= free_count

    
    def checkout(self, basket):
        bought = defaultdict(int)
        for item in basket:
            bought[item] += 1
    
        self.remove_give_aways(bought)
        
        total = 0
        
        # buy # any of        
        for count, price, items_on_offer in self.buy_any:
            
            any_of_group = []
            for item in items_on_offer:
                any_of_group += bought.pop(item, 0) * [item]
                                
            total += len(any_of_group) / count * price
            reminder = len(any_of_group) % count
            if reminder:
                # put not matched back on bought list
                not_matched = any_of_group[-reminder:]
                for item in not_matched:
                    bought[item] += 1
                            
    
        # prices and group buy
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


    
    
