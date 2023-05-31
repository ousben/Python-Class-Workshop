import csv

class Item:
    pay_rate = 0.8 #The pay rate after a 20% discount
    all = []
    
    def __init__(self, name:str, price:float, quantity=0):
        #Run validations to the received arguments
        assert price >= 0
        assert quantity >= 0
        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        #Actions to execute
        Item.all.append(self)
        
    def stock_value(self):
        return self.price * self.quantity
    
    def discount_value(self):
        self.price = self.price * self.pay_rate
        return self.price
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        sentence = ("name = {}, price = {}, quantity = {}".format(self.name, self.price, self.quantity))
        return sentence