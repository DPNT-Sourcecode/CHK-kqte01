from collections import defaultdict, namedtuple

class Supermarket:
    
    Price = namedtuple("Price", ["count", "price"])

    def __init__(self, offers_file):
        self.prices = defaultdict(list)
        self.giveAway = {}
        self.buyAny = []
        
        with open(offers_file) as file_in:
            for offerLine in file_in:
                offer = offerLine.split()
                
                if offer[0] == "price":
                    item, count, price = offer[1:]
                    self.prices[item].append(Supermarket.Price(int(count), int(price)))

                elif offer[0] == "give_away":
                    free, requiredCount, item = offer[1:]
                    self.giveAway[free] = (int(requiredCount), item)
                
                elif offer[0] == "buy_any":
                    count, price = offer[1:3]
                    items = offer[3:] # items in descending price order
                    self.buyAny.append((int(count), int(price), items))
                    
           
            
    def remove_give_aways(self, bought):
        for free, requirement in self.giveAway.iteritems():
            requiredCount, item = requirement
            if free in bought:
                itemCount = bought.get(item, 0)
                freeCount = itemCount / requiredCount
                if bought[free] < freeCount:
                    bought[free] = 0
                else:
                    bought[free] -= freeCount

    
    def checkout(self, basket):
        bought = defaultdict(int)
        for item in basket:
            bought[item] += 1
    
        self.remove_give_aways(bought)
        
        total = 0
        
        # buy from any of group offer
        for count, price, itemsOnOffer in self.buyAny:
            
            anyOfGroup = []
            for item in itemsOnOffer:
                anyOfGroup += bought.pop(item, 0) * [item]
                                
            total += len(anyOfGroup) / count * price
            reminder = len(anyOfGroup) % count
            if reminder:
                # put not matched back on bought list
                notMatched = anyOfGroup[-reminder:]
                for item in notMatched:
                    bought[item] += 1
                            
    
        # prices and group buy
        for item, count in bought.iteritems():                
            if item not in self.prices:                
                return -1
            
            for offer in self.prices[item]:
                offersNum = count / offer.count
                price = offersNum * offer.price
                total += price
                
                # reduce count by what was added to total already
                count %= offer.count
                    
        return total


    
    
