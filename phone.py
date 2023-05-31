from item import Item

class Phone(Item):
    def __init__(self, name:str, price:float, quantity=0, broken_phones=0):
        #Create the super function that allow access to all the attributes of Item class
        super().__init__(name, price, quantity)
        #Run validations to the received arguments
        assert broken_phones >= 0
        #Assign to self object
        self.broken_phones = broken_phones
    
    def __repr__(self):
        sentence = ("name = {}, price = {}, quantity = {}, broken phones = {}".format(self.name, self.price, self.quantity, self.broken_phones))
        return sentence